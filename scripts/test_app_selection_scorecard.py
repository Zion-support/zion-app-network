#!/usr/bin/env python3
"""Offline source, localization and safety contract for the five scorecard pages."""
from html.parser import HTMLParser
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://ziontechgroup.com/zion-app-network/"
LOCALES = [("en", ""), ("pt-BR", "-pt-br"), ("es", "-es"), ("fr", "-fr"), ("de", "-de")]
NAME = "app-selection-evidence-scorecard-2026"

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.lang = ""
        self.canonical = []
        self.alternates = {}
        self.ids = set()
        self.links = set()
        self.selects = []
        self.in_h1 = False
        self.h1 = ""
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html": self.lang = a.get("lang", "")
        if a.get("id"): self.ids.add(a["id"])
        if tag == "select": self.selects.append(a.get("id"))
        if tag == "a" and a.get("href"): self.links.add(a["href"])
        if tag == "script" and a.get("src"): self.links.add(a["src"])
        if tag == "link":
            if a.get("rel") == "canonical": self.canonical.append(a.get("href"))
            if a.get("rel") == "alternate": self.alternates.setdefault(a.get("hreflang"), []).append(a.get("href"))
        if tag == "h1": self.in_h1 = True
    def handle_data(self, data):
        if self.in_h1: self.h1 += data.strip()
    def handle_endtag(self, tag):
        if tag == "h1": self.in_h1 = False

class ScorecardContract(unittest.TestCase):
    def test_five_full_language_routes_and_human_gates(self):
        headings = []
        slugs = [NAME + suffix + ".html" for _, suffix in LOCALES]
        for lang, suffix in LOCALES:
            with self.subTest(locale=lang):
                src = ROOT / (NAME + suffix + ".html")
                self.assertTrue(src.is_file(), str(src))
                content = src.read_text(encoding="utf-8")
                page = Page(content)
                self.assertEqual(page.lang, lang)
                self.assertEqual(page.canonical, [BASE + src.name])
                self.assertEqual(page.alternates.get("x-default"), [BASE + slugs[0]])
                for (other, _), other_slug in zip(LOCALES, slugs):
                    self.assertEqual(page.alternates.get(other), [BASE + other_slug])
                    self.assertIn(BASE + other_slug, page.links)
                headings.append(page.h1)
                self.assertTrue(page.h1)
                self.assertEqual(page.selects, ["criterion-" + str(i) for i in range(5)])
                for required in ("main", "scorecard-form", "report", "score", "advice",
                                 "brief", "copy", "copy-message", "privacy-note",
                                 "score-label", "brief-heading", "copy-ok", "copy-fail",
                                 "state-0", "state-1", "state-2", "next-0", "next-1", "next-2"):
                    self.assertIn(required, page.ids)
                self.assertIn("/zion-app-network/" + NAME + ".js", page.links)
                self.assertIn(BASE + "field-quote-readiness-2026" + suffix + ".html", page.links)
                self.assertIn(BASE + "app-network-operations-evidence-checklist-2026" + suffix + ".html", page.links)
                self.assertIn("https://ziontechgroup.com/zion-app-network/", page.links)
                self.assertNotIn("fetch(", content)
                self.assertNotIn("XMLHttpRequest", content)
                self.assertNotIn("action=", content)
        self.assertEqual(len(set(headings)), 5)
    def test_client_script_is_local_only(self):
        code = (ROOT / (NAME + ".js")).read_text(encoding="utf-8")
        for forbidden in ("fetch(", "XMLHttpRequest", "sendBeacon", "localStorage", "sessionStorage", "eval("):
            self.assertNotIn(forbidden, code)
        self.assertIn('event.preventDefault()', code)
        self.assertIn("total<=7?0:total<=14?1:2", code)
        self.assertIn('values.every(v=>Number.isInteger(v)&&v>=0&&v<=4)', code)
    def test_hub_has_all_language_links(self):
        hub = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("evidenceScorecard2026 }}", hub)
        for lang, suffix in LOCALES:
            self.assertIn("/zion-app-network/" + NAME + suffix + ".html", hub)
        self.assertEqual(hub.count("{% capture evidenceScorecard2026 %}"), 1)
    def test_existing_sibling_paths(self):
        for _, suffix in LOCALES:
            for prefix in ("field-quote-readiness-2026", "app-network-operations-evidence-checklist-2026"):
                self.assertTrue((ROOT / (prefix + suffix + ".html")).is_file(), prefix + suffix)
if __name__ == "__main__": unittest.main()
