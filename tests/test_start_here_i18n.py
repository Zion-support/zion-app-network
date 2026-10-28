from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

PAGES = {
    "en": "app-network-start-here-2026.html",
    "pt-BR": "app-network-start-here-2026-pt-br.html",
    "es": "app-network-start-here-2026-es.html",
    "fr": "app-network-start-here-2026-fr.html",
    "de": "app-network-start-here-2026-de.html",
}

EXPECTED_ROUTES = [
    "/zion-app-network/app-selection-evidence-scorecard-2026",
    "/zion-app-network/field-quote-readiness-2026",
    "/zion-app-network/app-network-operations-evidence-checklist-2026",
]

class StartHereI18nTest(unittest.TestCase):
    def test_all_locales_exist_and_share_release_marker(self):
        for locale, filename in PAGES.items():
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertIn('data-start-here-release="buyer-journey-i18n-20261028"', text, filename)
            self.assertIn(f'<html lang="{locale}">', text, filename)
            self.assertIn("commercial@ziontechgroup.com", text, filename)

    def test_each_page_links_all_five_languages(self):
        expected = list(PAGES.values())
        for filename in PAGES.values():
            text = (ROOT / filename).read_text(encoding="utf-8")
            for target in expected:
                self.assertIn(target, text, f"{filename} missing {target}")
            for hreflang in ("en", "pt-BR", "es", "fr", "de", "x-default"):
                self.assertIn(f'hreflang="{hreflang}"', text, f"{filename} missing {hreflang}")

    def test_each_page_links_core_journey(self):
        for filename in PAGES.values():
            text = (ROOT / filename).read_text(encoding="utf-8")
            for route in EXPECTED_ROUTES:
                self.assertIn(route, text, f"{filename} missing {route}")
            self.assertIn("40%", text, filename)
            self.assertIn("PO", text, filename)

    def test_hub_interlinks_family(self):
        text = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn('id="app-network-start-here-2026"', text)
        for filename in PAGES.values():
            self.assertIn(f"/zion-app-network/{filename}", text)

if __name__ == "__main__":
    unittest.main()
