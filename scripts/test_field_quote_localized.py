"""Offline, dependency-free contracts for the five localized field quote worksheets."""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://ziontechgroup.com/zion-app-network/"
CASES = (
    ("field-quote-readiness-2026.html", "en", "en", "Explore free planning resources"),
    ("field-quote-readiness-2026-pt-br.html", "pt-BR", "pt", "Explorar recursos gratuitos de planejamento"),
    ("field-quote-readiness-2026-es.html", "es", "es", "Explorar recursos gratuitos de planificación"),
    ("field-quote-readiness-2026-fr.html", "fr", "fr", "Explorer les ressources gratuites de planification"),
    ("field-quote-readiness-2026-de.html", "de", "de", "Kostenlose Planungsressourcen ansehen"),
)
ALL_FILES = {item[0] for item in CASES}
ALL_LANGS = {"en", "pt-BR", "es", "fr", "de", "x-default"}


class Tags(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.html_lang = None
        self.ids = []
        self.links = []
        self.alternates = []
        self.canonicals = []
        self.inputs = {}
        self.buttons = []

    def handle_starttag(self, tag, attrs):
        props = dict(attrs)
        if tag == "html":
            self.html_lang = props.get("lang")
        if props.get("id"):
            self.ids.append(props["id"])
        if tag == "a":
            self.links.append(props.get("href", ""))
        if tag == "link" and props.get("rel") == "alternate":
            self.alternates.append((props.get("hreflang"), props.get("href")))
        if tag == "link" and props.get("rel") == "canonical":
            self.canonicals.append(props.get("href"))
        if tag == "input":
            self.inputs[props.get("id")] = props
        if tag == "button":
            self.buttons.append(props)


class FieldQuoteReleaseTests(unittest.TestCase):
    def each_page(self):
        for filename, lang, directory_lang, label in CASES:
            source = (ROOT / filename).read_text(encoding="utf-8")
            tags = Tags()
            tags.feed(source)
            yield filename, lang, directory_lang, label, source, tags

    def test_five_localized_standalone_html_pages(self):
        for filename, lang, _, _, source, tags in self.each_page():
            with self.subTest(filename=filename):
                self.assertGreater(len(source), 6000)
                self.assertTrue(source.startswith("<!doctype html>"))
                self.assertEqual(tags.html_lang, lang)
                self.assertIn("<main", source)
                self.assertIn("</html>", source)
                self.assertEqual(tags.canonicals, [BASE + filename])

    def test_reciprocal_canonical_and_all_six_hreflang_links(self):
        for filename, _, _, _, _, tags in self.each_page():
            with self.subTest(filename=filename):
                pairs = dict(tags.alternates)
                self.assertEqual(len(tags.alternates), 6)
                self.assertEqual(set(pairs), ALL_LANGS)
                self.assertEqual(pairs["x-default"], BASE + CASES[0][0])
                for other, locale, _, _ in CASES:
                    self.assertEqual(pairs[locale], BASE + other)

    def test_five_localized_language_switcher_targets(self):
        for filename, _, _, _, _, tags in self.each_page():
            with self.subTest(filename=filename):
                self.assertTrue(ALL_FILES.issubset(set(tags.links)))

    def test_no_dead_or_misleading_paid_discovery_calls_to_action(self):
        for filename, _, directory_lang, label, source, tags in self.each_page():
            with self.subTest(filename=filename):
                self.assertIn(label, source)
                self.assertIn(BASE + f"directory-{directory_lang}.html", tags.links)
                self.assertNotIn("Start free Discovery", source)
                self.assertNotIn("Iniciar Discovery gratuito", source)
                self.assertNotIn("Commencer le Discovery gratuit", source)
                self.assertNotIn("Kostenloses Discovery starten", source)
                self.assertNotIn("https://ziontechgroup.com/discovery/", tags.links)
                for dead in ("es", "fr", "de"):
                    self.assertNotIn(f"https://ziontechgroup.com/{dead}/discovery/", tags.links)

    def test_all_in_cost_fields_and_nonbinding_floor(self):
        for filename, _, _, _, source, tags in self.each_page():
            with self.subTest(filename=filename):
                for field in ("labor", "travel", "parts", "tax", "other"):
                    self.assertIn(field, tags.inputs)
                    self.assertEqual(tags.inputs[field].get("type"), "number")
                    self.assertEqual(tags.inputs[field].get("min"), "0")
                    self.assertEqual(tags.inputs[field].get("step"), "0.01")
                self.assertIn('Math.ceil(total*1.4*100-1e-9)/100', source)
                self.assertIn("Number.isFinite", source)
                self.assertIn('id="result" hidden', source)
                self.assertIn('id="brief" readonly', source)

    def test_no_silent_network_or_automated_customer_commitments(self):
        for filename, _, _, _, source, tags in self.each_page():
            with self.subTest(filename=filename):
                self.assertNotRegex(source, r"\bfetch\s*\(|XMLHttpRequest|sendBeacon|new\s+WebSocket|localStorage|sessionStorage")
                self.assertNotRegex(source, r"<form\b|<iframe\b")
                self.assertIn("navigator.clipboard.writeText", source)
                self.assertIn('role="status"', source)
                self.assertIn('aria-live="polite"', source)
                self.assertTrue(all(button.get("type") == "button" for button in tags.buttons))
                self.assertTrue(len(tags.buttons) >= 2)

    def test_nav_ids_unique_and_accessible(self):
        for filename, _, _, _, source, tags in self.each_page():
            with self.subTest(filename=filename):
                self.assertEqual(len(tags.ids), len(set(tags.ids)))
                self.assertIn("main", tags.ids)
                self.assertIn('href="#main"', source)
                self.assertIn('aria-current="page"', source)
                self.assertIn('focus-visible', source)
                self.assertIn('@media', source)

    def test_hub_reciprocal_entry_points(self):
        hub = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertEqual(hub.count('{% capture fieldQuote2026 %}'), 1)
        self.assertEqual(hub.count("field-quote-readiness-2026\" aria-labelledby"), 1)
        self.assertIn("| replace: '</body>', fieldQuote2026", hub)
        # Buyer Journey may also link the worksheet; validate uniqueness inside its own hub section.
        field_section = hub.split("{% capture fieldQuote2026 %}", 1)[1].split("{% endcapture %}", 1)[0]
        for filename in ALL_FILES:
            with self.subTest(filename=filename):
                self.assertEqual(field_section.count("/zion-app-network/" + filename), 1)
        self.assertIn("minimum 40% markup", hub)
        self.assertIn("No booking, dispatch, purchase", hub)


if __name__ == "__main__":
    unittest.main()
