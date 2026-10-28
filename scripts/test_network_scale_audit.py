#!/usr/bin/env python3
"""Offline regression tests for the read-only, 1000-link audit."""
import importlib.util
import tempfile
from pathlib import Path
from unittest import TestCase, main

FILE = Path(__file__).with_name("network_scale_audit.py")
spec = importlib.util.spec_from_file_location("network_scale_audit", FILE)
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)

def fixture(root):
    (root / "a.html").write_text(
        '<html lang="en"><head><meta name="viewport" content="width=device-width">'
        '<link rel="canonical" href="https://ziontechgroup.com/zion-app-network/a.html"></head>'
        '<body><h1>A</h1><a href="b.html">B</a>'
        '<a href="https://ziontechgroup.com/discovery/">Discovery</a>'
        '<a href="#local">Local</a><div id="local"></div></body></html>',
        encoding="utf-8"
    )
    (root / "b.html").write_text(
        '<html lang="pt-BR"><head><meta name="viewport" content="width=device-width">'
        '<link rel="canonical" href="https://ziontechgroup.com/zion-app-network/b.html"></head>'
        '<body><h1>B</h1><a href="missing.html">Missing</a>'
        '<a href="https://example.com/external">External</a>'
        '<a href="javascript:alert(1)">Unsafe</a></body></html>',
        encoding="utf-8"
    )

class NetworkScaleAuditTests(TestCase):
    def test_all_five_links_are_categorized_without_network(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture(root)
            report = audit.run(root)
            self.assertEqual(report["html_files_scanned"], 2)
            self.assertEqual(report["link_checks_completed"], 6)
            self.assertEqual(report["verified_live_urls"], 0)
            self.assertFalse(report["production_deployment_verified"])
            self.assertEqual(report["classification_counts"]["network_source_present"], 1)
            self.assertEqual(report["classification_counts"]["network_source_unresolved"], 1)
            self.assertEqual(report["classification_counts"]["external_not_fetched"], 1)
            self.assertEqual(report["classification_counts"]["unsafe_or_unsupported_scheme"], 1)
            self.assertEqual(report["classification_counts"]["main_site_cross_repository"], 1)
            self.assertEqual(report["classification_counts"]["fragment"], 1)

    def test_bounded_round_robin_window_does_not_repeat_first_page(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture(root)
            first = audit.run(root, max_checks=2)
            second = audit.run(root, max_checks=2, offset=2)
            self.assertEqual(first["link_checks_completed"], 2)
            self.assertEqual(first["html_files_covered_by_link_checks"], 2)
            self.assertEqual(second["link_checks_completed"], 2)
            self.assertEqual(second["html_files_covered_by_link_checks"], 2)
            self.assertNotEqual(first["classification_counts"], second["classification_counts"])

    def test_local_fragment_detection(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "index.html").write_text(
                '<html lang="en"><h1>Home</h1><a href="#not-found">Broken</a></html>',
                encoding="utf-8"
            )
            report = audit.run(root)
            self.assertEqual(report["advisory_counts"]["fragment"], 1)

    def test_invalid_window_does_not_scan(self):
        with tempfile.TemporaryDirectory() as tmp:
            for max_checks, offset in ((0, 0), (1001, 0), (1, -1)):
                with self.subTest(max_checks=max_checks, offset=offset):
                    with self.assertRaises(ValueError):
                        audit.run(Path(tmp), max_checks=max_checks, offset=offset)

    def test_source_files_are_read_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture(root)
            before = {p.name: p.read_bytes() for p in root.glob("*.html")}
            audit.run(root)
            after = {p.name: p.read_bytes() for p in root.glob("*.html")}
            self.assertEqual(before, after)

if __name__ == "__main__":
    main()
