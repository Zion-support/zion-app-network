#!/usr/bin/env python3
"""Check new PR HTML/Markdown links pointing into this GitHub Pages repository.

Read-only, offline, stdlib-only, diff-scoped. External sites and paths owned by
ziontechgroup.com outside /zion-app-network/ are intentionally not certified.
Existing unchanged legacy links are not re-audited.
"""
import argparse
from collections import defaultdict
from html.parser import HTMLParser
import html
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

SITE_PATH = "/zion-app-network"
SITE_HOSTS = {"ziontechgroup.com", "www.ziontechgroup.com"}
SUFFIXES = {".html", ".htm", ".md", ".markdown"}
SHA = re.compile(r"[a-fA-F0-9]{40}\Z")
HUNK = re.compile(r"^@@ -\d+(?:,\d+)? \+(\d+)(?:,\d+)? @@")
MARKDOWN_LINK = re.compile(r"!?\[[^\]\n]*\]\(\s*<?([^\s)>]+)>?", re.I)
MARKDOWN_REF = re.compile(r"^\s{0,3}\[[^\]]+\]:\s*<?([^\s>]+)>?", re.I)
MAX_FILE_BYTES = 2_000_000
# Parse complete raw HTML attribute lexemes, excluding fake href= strings
# embedded in unrelated quoted attribute values.
ATTR_LEXEME = re.compile(r'''([^\s=/>]+)(?:\s*=\s*(?:"[^"]*"|'[^']*'|[^\s>]+))?''', re.S)


def added_line_numbers(patch):
    """Map PR changed paths to their *added* final-file line numbers."""
    found = defaultdict(set)
    source = None
    lineno = 0
    for line in patch.splitlines():
        if line.startswith("+++ "):
            source = line[6:] if line.startswith("+++ b/") else None
            lineno = 0
        elif line.startswith("@@ "):
            match = HUNK.match(line)
            if match:
                lineno = int(match.group(1))
        elif line.startswith("+") and not line.startswith("+++ "):
            if source and Path(source).suffix.lower() in SUFFIXES:
                found[source].add(lineno)
            lineno += 1
        elif line.startswith(" "):
            lineno += 1
    return dict(found)


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.anchors = set()

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if values.get("id"):
            self.anchors.add(values["id"])
        if tag == "a" and values.get("name"):
            self.anchors.add(values["name"])
        if tag not in {"a", "area", "link", "img", "script", "source", "iframe"}:
            return

        # HTMLParser reports only the beginning of a multiline start tag.
        # Identify the exact href/src attribute span to check changed lines.
        raw = self.get_starttag_text() or ""
        first_line = self.getpos()[0]
        locations = {}
        for token in ATTR_LEXEME.finditer(raw):
            name = token.group(1).lower()
            if name not in {"href", "src"}:
                continue
            first = first_line + raw.count("\n", 0, token.start())
            last = first_line + raw.count("\n", 0, token.end())
            locations.setdefault(name, []).append((first, last))
        for name in ("href", "src"):
            if values.get(name):
                first, last = locations.get(
                    name, [(first_line, first_line + raw.count("\n"))]
                )[0]
                self.links.append((first, last, values[name]))


def markdown_links(body, changed):
    in_fence = False
    fence_char = ""
    fence_length = 0
    for line_number, line in enumerate(body.splitlines(), start=1):
        marker = re.match(r"^\s{0,3}(" + chr(96) + r"{3,}|~{3,})", line)
        if marker:
            run = marker.group(1)
            if not in_fence:
                in_fence = True
                fence_char, fence_length = run[0], len(run)
            elif run[0] == fence_char and len(run) >= fence_length:
                in_fence = False
            continue
        if in_fence or line_number not in changed:
            continue
        for match in MARKDOWN_LINK.finditer(line):
            yield line_number, match.group(1)
        reference = MARKDOWN_REF.match(line)
        if reference:
            yield line_number, reference.group(1)


def read_bounded(path):
    if path.stat().st_size > MAX_FILE_BYTES:
        raise ValueError("file-too-large")
    return path.read_text(encoding="utf-8")


def available_target(candidate):
    if candidate.is_file():
        return candidate
    if candidate.is_dir():
        for name in ("index.html", "index.md"):
            possible = candidate / name
            if possible.is_file():
                return possible
    if not candidate.suffix:
        for possible in (candidate.with_suffix(".html"), candidate / "index.html"):
            if possible.is_file():
                return possible
    return None


def resolve_local(root, source, link):
    """Return (target, fragment, rule), or (None, None, None) when out of scope."""
    raw = html.unescape(link.strip())
    url = urlsplit(raw)
    scheme = url.scheme.lower()
    if scheme in {"javascript", "vbscript"}:
        return None, None, "unsafe-link-scheme"
    if scheme and scheme not in {"http", "https"}:
        return None, None, None
    if scheme in {"http", "https"} and (url.hostname or "").lower() not in SITE_HOSTS:
        return None, None, None
    if url.netloc and not scheme:
        return None, None, None  # Protocol-relative links are not local-owned evidence.

    path = unquote(url.path)
    if scheme in {"http", "https"} or path.startswith("/"):
        if path == SITE_PATH:
            path = SITE_PATH + "/"
        if not path.startswith(SITE_PATH + "/"):
            return None, None, None
        relative = path[len(SITE_PATH) + 1:]
        candidate = root / relative
        explicit_site_path = True
    else:
        candidate = root / source.parent / path if path else root / source
        explicit_site_path = False

    try:
        relative_candidate = candidate.resolve().relative_to(root.resolve())
    except ValueError:
        if explicit_site_path:
            return None, None, "unsafe-link-path"
        return None, None, None  # Relative off-repo navigation may be intentional.
    found = available_target(root / relative_candidate)
    if not found:
        return root / relative_candidate, url.fragment, "missing-local-target"
    return found, url.fragment, None


def check_patch(repo, patch):
    root = Path(repo).resolve()
    changed_files = added_line_numbers(patch)
    findings = []
    checked = 0
    skipped = 0
    anchors_cache = {}

    for relpath, changed in sorted(changed_files.items()):
        source = Path(relpath)
        original = (root / source).resolve()
        if not original.is_relative_to(root) or not original.is_file():
            findings.append({"path": relpath, "line": 1, "rule": "source-unavailable"})
            continue
        try:
            body = read_bounded(original)
        except (OSError, UnicodeError, ValueError):
            findings.append({"path": relpath, "line": 1, "rule": "source-unreadable"})
            continue
        if source.suffix.lower() in {".html", ".htm"}:
            parser = LinkParser()
            parser.feed(body)
            links = []
            for first, last, url in parser.links:
                touched = [line for line in range(first, last + 1) if line in changed]
                if touched:
                    links.append((touched[0], url))
        else:
            links = list(markdown_links(body, changed))

        for line, url in links:
            try:
                target, fragment, error = resolve_local(root, source, url)
            except ValueError:
                target, fragment, error = None, None, "malformed-url"
            if error:
                findings.append({"path": relpath, "line": line, "rule": error})
                continue
            if target is None:
                skipped += 1
                continue
            checked += 1
            if not fragment or target.suffix.lower() not in {".html", ".htm"}:
                continue
            if fragment.startswith(":~:text="):
                continue  # Browser text fragments are not DOM IDs.
            try:
                if target not in anchors_cache:
                    document = LinkParser()
                    document.feed(read_bounded(target))
                    anchors_cache[target] = document.anchors
            except (OSError, UnicodeError, ValueError):
                findings.append({"path": relpath, "line": line, "rule": "target-unreadable"})
                continue
            if unquote(fragment) not in anchors_cache[target]:
                findings.append({"path": relpath, "line": line, "rule": "missing-local-anchor"})
    return {
        "status": "blocked" if findings else "pass",
        "changed_content_files": len(changed_files),
        "local_links_checked": checked,
        "off_scope_links_skipped": skipped,
        "findings": findings,
        "scope": "New HTML and Markdown PR lines; local Zion App Network files and HTML anchors only. External/live sites not certified."
    }


def get_patch(repo, base, head):
    if not SHA.fullmatch(base) or not SHA.fullmatch(head):
        raise ValueError("Commit identifiers must each be 40-character SHA values")
    result = subprocess.run(
        ["git", "-C", str(repo), "-c", "core.quotePath=false", "diff", "--no-ext-diff",
         "--no-color", "--unified=0", "--diff-filter=ACMR", base, head, "--"],
        text=True, capture_output=True, check=True, encoding="utf-8", errors="replace")
    return result.stdout


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True)
    parser.add_argument("--head", required=True)
    parser.add_argument("--repo", default=".")
    parser.add_argument("--output", default="link-guard-report.json")
    args = parser.parse_args(argv)
    try:
        report = check_patch(args.repo, get_patch(args.repo, args.base, args.head))
    except (OSError, subprocess.CalledProcessError, ValueError) as exc:
        print(f"Local link guard could not verify diff ({type(exc).__name__}); blocking.")
        return 2
    Path(args.output).write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"App Network link guard: {report['status']}; {report['local_links_checked']} new local links checked; {len(report['findings'])} findings.")
    for problem in report["findings"][:30]:
        clean = re.sub(r"[^A-Za-z0-9_./-]", "_", problem["path"])
        print(f"::error file={clean},line={problem['line']}::{problem['rule']}")
    return 1 if report["findings"] else 0


if __name__ == "__main__":
    sys.exit(main())
