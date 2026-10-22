#!/usr/bin/env python3
"""Fail-closed PR diff guard for obvious private links, secret tokens and confidential rate labels.

This checks only ADDED lines, not entire repository history or semantic supplier pricing.
It never prints matching text, authenticates externally, or modifies public content.
"""
import argparse
import html
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

CONTENT_SUFFIXES = {".html", ".htm", ".md", ".markdown", ".json", ".txt",
                    ".xml", ".js", ".jsx", ".ts", ".tsx", ".css", ".yaml", ".yml"}
FIXTURE_PATH = "scripts/test_public_content_privacy_guard.py"
COMMIT_SHA = re.compile(r"[a-fA-F0-9]{40}\Z")
HUNK = re.compile(r"^@@ -\d+(?:,\d+)? \+(\d+)(?:,\d+)? @@")

# High-confidence private-system links and credentials. Avoid generic "cost" keywords:
# public ROI calculators and price-comparison documentation legitimately mention cost.
RULES = (
    ("private-gmail-deeplink", re.compile(r"https?://mail\.google\.com/mail(?:/|#)", re.I)),
    ("private-notion-page", re.compile(r"https?://app\.notion\.com/p/", re.I)),
    ("private-hubspot-record", re.compile(r"https?://app\.hubspot\.com/(?:contacts|tasks|sales)/", re.I)),
    ("private-composio-artifact", re.compile(r"https?://backend\.composio\.dev/api/v3/sl/", re.I)),
    ("github-token-like", re.compile(r"(?<![\w])(?:github_pat_[A-Za-z0-9_]{20,}|gh[pousr]_[A-Za-z0-9]{20,})")),
    ("openai-token-like", re.compile(r"(?<![\w])sk-(?:proj-|svcacct-)?[A-Za-z0-9_-]{28,}")),
    ("google-api-key-like", re.compile(r"(?<![\w])AIza[A-Za-z0-9_-]{30,}")),
    ("private-key-header", re.compile(r"-----BEGIN (?:[A-Z]+ )?PRIVATE KEY-----")),
    ("explicit-confidential-supplier-rates", re.compile(
        r"\b(?:CONFIDENTIAL\s+(?:SUPPLIER|VENDOR)\s+(?:RATE|PRICE|COST)|"
        r"(?:SUPPLIER|VENDOR)\s+PRIVATE\s+(?:RATE|PRICE|COST))\b", re.I)),
)


def eligible(path):
    return bool(path and path != FIXTURE_PATH and Path(path).suffix.lower() in CONTENT_SUFFIXES)


def scan_patch(patch):
    path = None
    lineno = 0
    scanned = 0
    findings = []
    for line in patch.splitlines():
        if line.startswith("+++ "):
            path = line[6:] if line.startswith("+++ b/") else None
            lineno = 0
            continue
        if line.startswith("@@ "):
            found = HUNK.match(line)
            if found:
                lineno = int(found.group(1))
            continue
        if line.startswith("+") and not line.startswith("+++ "):
            if eligible(path):
                scanned += 1
                content = html.unescape(unquote(line[1:]))
                for rule, regex in RULES:
                    if regex.search(content):
                        # Never output source text, matching values, tokens or excerpts.
                        findings.append({"path": path, "line": lineno, "rule": rule})
            lineno += 1
        elif line.startswith(" "):
            lineno += 1
    return {"status": "blocked" if findings else "pass",
            "scanned_added_lines": scanned, "finding_count": len(findings),
            "findings": findings,
            "scope": "New lines in public text/code files; known patterns only. Not full secret scanning or supplier-cost inference."}


def get_patch(repo, base, head):
    if not COMMIT_SHA.fullmatch(base) or not COMMIT_SHA.fullmatch(head):
        raise ValueError("base and head must each be an exact 40-character commit SHA")
    proc = subprocess.run(
        ["git", "-C", str(repo), "-c", "core.quotePath=false", "diff",
         "--no-ext-diff", "--no-color", "--unified=0", "--diff-filter=ACMR",
         base, head, "--"],
        check=True, capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    return proc.stdout


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True, help="PR base commit SHA")
    parser.add_argument("--head", required=True, help="PR head commit SHA")
    parser.add_argument("--repo", default=".", help="checked-out repository root")
    parser.add_argument("--output", default="privacy-guard-report.json")
    args = parser.parse_args(argv)
    try:
        result = scan_patch(get_patch(args.repo, args.base, args.head))
    except (OSError, subprocess.CalledProcessError, ValueError) as exc:
        # Error type only; subprocess stderr could inadvertently echo sensitive content.
        print(f"PR privacy guard could not verify diff ({type(exc).__name__}); blocking.")
        return 2
    with open(args.output, "w", encoding="utf-8") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(f"PR privacy guard: {result['status']}, {result['scanned_added_lines']} new lines checked, {result['finding_count']} high-confidence findings.")
    for f in result["findings"][:30]:
        print(f"::error file={f['path']},line={f['line']}::{f['rule']} — private material candidate; review source privately.")
    if result["finding_count"] > 30:
        print(f"{result['finding_count'] - 30} additional findings omitted from log.")
    return 1 if result["findings"] else 0


if __name__ == "__main__":
    sys.exit(main())
