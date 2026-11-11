#!/usr/bin/env python3
"""Offline integration fixtures for the additive communications catalog writer."""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("consolidate-communications.py").resolve()
PIPELINE = "{{ corrected | replace: '</body>', promotion | replace: '</body>', showcases2026 | replace: '</body>', ops2026 | replace: '</body>', opsEvidence2026 }}"


class ConsolidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.catalogs = ("CATALOG.md", "APPS_INDEX.md", "index.html")
        for name in self.catalogs[:2]:
            (self.root / name).write_text(
                "# Preserve existing entries\n\n[Legacy](https://github.com/Zion-support/legacy-resource)\n",
                encoding="utf-8")

    def run_writer(self):
        return subprocess.run([sys.executable, str(SCRIPT)], cwd=self.root,
                              capture_output=True, text=True, timeout=10)

    def snapshots(self):
        return {p: (self.root / p).read_bytes() for p in self.catalogs}

    def test_legacy_html_footer_idempotent(self):
        (self.root / "index.html").write_text(
            '<html><body><a href="/legacy/">Keep</a><footer>Existing footer</footer></body></html>',
            encoding="utf-8")
        first = self.run_writer()
        self.assertEqual(first.returncode, 0, first.stderr)
        saved = self.snapshots()
        second = self.run_writer()
        self.assertEqual(second.returncode, 0, second.stderr)
        self.assertEqual(saved, self.snapshots())
        html = saved["index.html"].decode("utf-8")
        self.assertEqual(html.count('id="communications-suite"'), 1)
        self.assertIn('<a href="/legacy/">', html)
        self.assertIn("<footer>Existing footer</footer>", html)
        for master in self.catalogs[:2]:
            self.assertIn("legacy-resource", saved[master].decode())

    def test_liquid_capture_pipeline_is_preserved_and_idempotent(self):
        html = (
            "---\nlayout: null\n---\n"
            "{% capture original %}{% include hub_legacy.html %}{% endcapture %}\n"
            "{% capture opsEvidence2026 %}<section><h2>Keep existing hub cards</h2></section></body>{% endcapture %}\n"
            + PIPELINE + "\n"
        )
        (self.root / "index.html").write_text(html, encoding="utf-8")
        first = self.run_writer()
        self.assertEqual(first.returncode, 0, first.stderr)
        saved = self.snapshots()
        second = self.run_writer()
        self.assertEqual(second.returncode, 0, second.stderr)
        self.assertEqual(saved, self.snapshots())
        updated = saved["index.html"].decode("utf-8")
        self.assertIn("{% include hub_legacy.html %}", updated)
        self.assertIn("{% capture opsEvidence2026 %}", updated)
        self.assertIn("{% capture communicationsSuite %}", updated)
        self.assertIn("opsEvidence2026 | replace: '</body>', communicationsSuite }}", updated)
        self.assertEqual(updated.count('id="communications-suite"'), 1)
        self.assertEqual(updated.count("{% endcapture %}"), 3)

    def test_unknown_hub_template_fails_closed(self):
        (self.root / "index.html").write_text(
            "<html><body><div>Unsupported structure</div></body></html>",
            encoding="utf-8")
        result = self.run_writer()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unsupported hub template", result.stderr)
        # A failing preflight must never write a new homepage version.
        self.assertNotIn('id="communications-suite"',
                         (self.root / "index.html").read_text())


if __name__ == "__main__":
    unittest.main()
