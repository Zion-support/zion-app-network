#!/usr/bin/env python3
"""Deterministic, offline, read-only audit of up to 1000 HTML hyperlinks.

This is a source audit, NOT an HTTP health check and NOT a deployment certificate.
It reads HTML files from the checked-out repository without executing JavaScript,
fetching URLs, submitting forms or accessing secrets. Legacy findings are advisory;
new release contracts are validated separately by verify_network_source_contract.py.
"""
import argparse
import collections
import datetime
import json
import os
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse

SITE = "https://ziontechgroup.com"
PREFIX = "/zion-app-network/"
IGNORE = {".git", "_site", "node_modules", ".next", "dist", "build", "__pycache__"}

class SourceHTML(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.lang = ""
        self.viewport = False
        self.h1_count = 0
        self.canonical = []
        self.alternates = []
        self.anchors = []
        self.ids = set()
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.add(a["id"])
        if tag == "html":
            self.lang = a.get("lang", "")
        if tag == "h1":
            self.h1_count += 1
        if tag == "meta" and a.get("name", "").lower() == "viewport":
            self.viewport = True
        if tag == "a":
            self.anchors.append(a.get("href", ""))
        if tag == "link":
            rel = (a.get("rel") or "").split()
            if "canonical" in rel:
                self.canonical.append(a.get("href", ""))
            if "alternate" in rel and a.get("hreflang"):
                self.alternates.append((a.get("hreflang"), a.get("href", "")))


def eligible_files(root):
    return sorted(p for p in root.rglob("*.html")
                  if not any(part in IGNORE for part in p.relative_to(root).parts)
                  and p.is_file())


def source_route(root, file):
    rel = file.relative_to(root).as_posix()
    if rel == "index.html":
        return PREFIX
    return PREFIX + rel


def scrub_href(href):
    """Keep diagnostic paths while removing credentials, query strings and fragments."""
    if href.startswith("#"):
        return href[:80]
    try:
        parsed = urlparse(href)
        if parsed.scheme in ("mailto", "tel", "javascript", "data"):
            return parsed.scheme + ":<redacted>"
        if parsed.netloc:
            return parsed.scheme + "://" + (parsed.hostname or "invalid-host") + parsed.path[:120]
    except ValueError:
        return "<malformed-url>"
    return href.split("?", 1)[0].split("#", 1)[0][:180]


def resolve_link(root, file, href, ids):
    """Return category and optional advisory finding for one local hyperlink."""
    if not href or not href.strip():
        return "placeholder", "Empty href"
    href = href.strip()
    if href.startswith("#"):
        target = unquote(href[1:])
        if target and target not in ids:
            return "fragment", "Fragment anchor not found in static source"
        return "fragment", None
    try:
        parsed = urlparse(href)
    except ValueError:
        return "malformed_url", "Malformed URL"
    if parsed.scheme in ("mailto", "tel"):
        return "contact", None
    if parsed.scheme not in ("", "https", "http"):
        return "unsafe_or_unsupported_scheme", "Non-HTTP or unsupported URL scheme"
    if parsed.scheme == "http":
        return "http_link", "Plain HTTP link; review TLS and redirects"
    try:
        absolute = urljoin(SITE + source_route(root, file), href)
        dest = urlparse(absolute)
    except ValueError:
        return "malformed_url", "Malformed URL"
    if dest.hostname != "ziontechgroup.com":
        return "external_not_fetched", None
    if not dest.path.startswith(PREFIX):
        return "main_site_cross_repository", None
    relative = unquote(dest.path[len(PREFIX):]).lstrip("/")
    if not relative or relative.endswith("/"):
        relative += "index.html"
    if any(segment in (".", "..") for segment in Path(relative).parts):
        return "unsafe_path", "Unexpected path traversal component"
    candidate = root / relative
    if candidate.is_file():
        return "network_source_present", None
    return "network_source_unresolved", "Same-repository URL has no matching source file"


def round_robin_edges(pages):
    queues = {path: collections.deque(dict.fromkeys(page.anchors))
              for path, page in pages.items()}
    pending = sorted(queues)
    while pending:
        remaining = []
        for path in pending:
            queue = queues[path]
            if queue:
                yield path, queue.popleft()
            if queue:
                remaining.append(path)
        pending = remaining


def run(root, max_checks=1000, offset=0):
    root = Path(root).resolve()
    if not 1 <= max_checks <= 1000:
        raise ValueError("max_checks must be between 1 and 1000")
    if offset < 0:
        raise ValueError("offset must be nonnegative")
    pages = {}
    diagnostics = collections.Counter()
    for file in eligible_files(root):
        raw = file.read_text(encoding="utf-8", errors="replace")
        parsed = SourceHTML(raw)
        rel = file.relative_to(root).as_posix()
        pages[rel] = parsed
        templated = raw.lstrip().startswith("---") or "{% " in raw
        if not templated:
            if not parsed.lang:
                diagnostics["missing_html_lang"] += 1
            if not parsed.viewport:
                diagnostics["missing_viewport"] += 1
            if parsed.h1_count != 1:
                diagnostics["h1_count_not_one"] += 1
            if len(parsed.canonical) != 1:
                diagnostics["missing_or_multiple_canonical"] += 1
    ordered = list(round_robin_edges(pages))
    checked = ordered[offset:offset + max_checks]
    categories = collections.Counter()
    warnings = collections.Counter()
    examples = []
    covered = set()
    for relative, href in checked:
        covered.add(relative)
        category, advisory = resolve_link(root, root / relative, href, pages[relative].ids)
        categories[category] += 1
        if advisory:
            warnings[category] += 1
            if len(examples) < 60:
                examples.append({"source": relative, "href": scrub_href(href),
                                 "category": category, "advisory": advisory})
    return {
        "audited_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "method": "offline deterministic round-robin link references; no HTTP requests, browser execution, forms or dispatch",
        "source_commit": os.getenv("GITHUB_SHA", ""),
        "html_files_scanned": len(pages),
        "html_files_covered_by_link_checks": len(covered),
        "eligible_unique_per_page_links": len(ordered),
        "offset": offset,
        "max_checks": max_checks,
        "link_checks_completed": len(checked),
        "link_checks_remaining_after_window": max(0, len(ordered) - offset - len(checked)),
        "classification_counts": dict(categories),
        "advisory_counts": dict(warnings),
        "structural_advisory_counts": dict(diagnostics),
        "advisory_examples": examples,
        "verified_live_urls": 0,
        "production_deployment_verified": False,
        "limitations": "Unresolved local source links can be built by other repositories. External/main-site URLs are not fetched. Structural diagnostics on legacy source are advisory, not release blockers."
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default=".")
    ap.add_argument("--output", default="network-source-audit.json")
    ap.add_argument("--max-checks", type=int, default=1000)
    ap.add_argument("--offset", type=int, default=0)
    args = ap.parse_args()
    report = run(args.root, max_checks=args.max_checks, offset=args.offset)
    Path(args.output).write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("Offline audit: %d/%d unique link references checked across %d/%d HTML pages" %
          (report["link_checks_completed"], report["eligible_unique_per_page_links"],
           report["html_files_covered_by_link_checks"], report["html_files_scanned"]))
    print("Classifications: " + json.dumps(report["classification_counts"], sort_keys=True))
    print("Advisories: " + json.dumps(report["advisory_counts"], sort_keys=True))
    print("Report: " + args.output + " (not a production verification)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
