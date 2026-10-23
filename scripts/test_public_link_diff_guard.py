"""Offline fixtures for incremental App Network local link validation."""
import importlib.util
from pathlib import Path
import tempfile
from unittest import TestCase, main

spec = importlib.util.spec_from_file_location(
    "link_guard", Path(__file__).with_name("public_link_diff_guard.py"))
guard = importlib.util.module_from_spec(spec)
spec.loader.exec_module(guard)


class LinkGuardTests(TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "docs").mkdir()
        (self.root / "index.html").write_text('<html><body><div id="start"></div></body></html>')
        (self.root / "docs" / "guide.md").write_text('# Local guide\n')
        (self.root / "asset.js").write_text('console.log("ok");\n')

    def write(self, name, body):
        destination = self.root / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(body, encoding="utf-8")

    def changes(self, name, body, first=1):
        self.write(name, body)
        count = len(body.splitlines()) - first + 1
        return (f"diff --git a/{name} b/{name}\n+++ b/{name}\n"
                f"@@ -0,0 +{first},{count} @@\n"
                + "".join("+" + ln + "\n" for ln in body.splitlines()[first - 1:]))

    def test_valid_same_site_links_and_anchors(self):
        self.write("other.html", '<div id="spot">Destination</div>')
        body = ('<html><body><div id="en">English</div>\n'
                '<a href="#en">EN</a>\n'
                '<a href="https://ziontechgroup.com/zion-app-network/other.html?track=1#spot">Local</a>\n'
                '<a href="/zion-app-network/">Home</a>\n'
                '<script src="asset.js"></script>\n'
                '<a href="https://ziontechgroup.com/apps/">External main site</a>\n'
                '</body></html>\n')
        result = guard.check_patch(self.root, self.changes("new.html", body))
        self.assertEqual(result["status"], "pass")
        self.assertEqual(result["local_links_checked"], 4)
        self.assertEqual(result["off_scope_links_skipped"], 1)

    def test_missing_local_file_fails(self):
        body = '<a href="/zion-app-network/not-published.html">Soon</a>\n'
        report = guard.check_patch(self.root, self.changes("new.html", body))
        self.assertEqual(report["status"], "blocked")
        self.assertEqual(report["findings"][0]["rule"], "missing-local-target")
        self.assertNotIn("not-published", str(report))

    def test_missing_html_anchor_fails(self):
        body = '<a href="#missing">Bad anchor</a>\n'
        report = guard.check_patch(self.root, self.changes("page.html", body))
        self.assertEqual(report["findings"][0]["rule"], "missing-local-anchor")

    def test_removed_and_unchanged_lines_not_scanned(self):
        body = '<a href="missing-legacy.html">Legacy</a>\n<a href="index.html">New</a>\n'
        self.write("example.html", body)
        patch = ('+++ b/example.html\n@@ -1,2 +1,2 @@\n'
                 ' <a href="missing-legacy.html">Legacy</a>\n'
                 '+<a href="index.html">New</a>\n')
        result = guard.check_patch(self.root, patch)
        self.assertEqual(result["status"], "pass")
        self.assertEqual(result["local_links_checked"], 1)

    def test_markdown_links_and_fences(self):
        body = ('# New resource\n'
                '[Guide](../docs/guide.md#ignored-github-heading)\n'
                '[Home](https://ziontechgroup.com/zion-app-network/#start)\n'
                '[Other product](https://ziontechgroup.com/apps/)\n'
                '~~~md\n[Example](missing-example.md)\n~~~\n')
        report = guard.check_patch(self.root, self.changes("docs/new.md", body))
        self.assertEqual(report["status"], "pass")
        self.assertEqual(report["local_links_checked"], 2)

    def test_unsafe_scheme_and_explicit_traversal(self):
        body = ('<a href="javascript:alert(1)">Bad</a>\n'
                '<a href="/zion-app-network/../../outside.html">Bad traversal</a>\n')
        report = guard.check_patch(self.root, self.changes("new.html", body))
        self.assertEqual({item["rule"] for item in report["findings"]},
                         {"unsafe-link-scheme", "unsafe-link-path"})

    def test_extensionless_page_and_reference_definition(self):
        self.write("news/index.html", '<h1>News</h1>')
        body = '[News]: /zion-app-network/news/\n[Source](./index.html)\n'
        report = guard.check_patch(self.root, self.changes("docs.md", body))
        self.assertEqual(report["status"], "pass")
        self.assertEqual(report["local_links_checked"], 2)

    def test_multiline_href_added_below_unchanged_opening_tag(self):
        self.write("multi.html", '<a\n  href="missing-target.html">New</a>\n')
        patch = """+++ b/multi.html
@@ -1,2 +1,2 @@
 <a
+  href="missing-target.html">New</a>
"""
        result = guard.check_patch(self.root, patch)
        self.assertEqual(result["status"], "blocked")
        self.assertEqual(result["findings"][0],
                         {"path": "multi.html", "line": 2, "rule": "missing-local-target"})

    def test_multiline_attribute_value_only_is_checked(self):
        self.write("continued.html", '<a href=\n "absent.html">New</a>\n')
        patch = """+++ b/continued.html
@@ -1,2 +1,2 @@
 <a href=
+ "absent.html">New</a>
"""
        result = guard.check_patch(self.root, patch)
        self.assertEqual(result["status"], "blocked")
        self.assertEqual(result["findings"][0]["line"], 2)

    def test_unchanged_multiline_href_ignores_changed_text(self):
        self.write("legacy.html", '<a\n href="old-missing.html">\nUpdated text\n</a>\n')
        patch = """+++ b/legacy.html
@@ -1,4 +1,4 @@
 <a
 href="old-missing.html">
+Updated text
 </a>
"""
        result = guard.check_patch(self.root, patch)
        self.assertEqual(result["status"], "pass")
        self.assertEqual(result["local_links_checked"], 0)

    def test_data_note_cannot_spoof_href_location(self):
        self.write("safe.html", """<a data-note='href="false.html"'
 href='index.html'>OK</a>
""")
        patch = """+++ b/safe.html
@@ -1,2 +1,2 @@
 <a data-note='href="false.html"'
+ href='index.html'>OK</a>
"""
        result = guard.check_patch(self.root, patch)
        self.assertEqual(result["status"], "pass")
        self.assertEqual(result["local_links_checked"], 1)

    def test_changing_data_href_does_not_reaudit_legacy_href(self):
        self.write("custom.html", '<a href="old-missing.html"\n data-href="new-text">OK</a>\n')
        patch = """+++ b/custom.html
@@ -1,2 +1,2 @@
 <a href="old-missing.html"
+ data-href="new-text">OK</a>
"""
        result = guard.check_patch(self.root, patch)
        self.assertEqual(result["status"], "pass")
        self.assertEqual(result["local_links_checked"], 0)

    def test_invalid_commits_fail_closed(self):
        with self.assertRaises(ValueError):
            guard.get_patch(self.root, "main", "HEAD")

    def test_workflow_is_single_existing_pr_trigger(self):
        workflow = Path(__file__).parents[1] / ".github/workflows/public-content-privacy-guard.yml"
        if workflow.exists():
            text = workflow.read_text(encoding="utf-8")
            self.assertIn("public_link_diff_guard.py", text)
            self.assertIn("test_public_link_diff_guard.py", text)
            self.assertNotIn("schedule:", text)
            self.assertIn("cancel-in-progress: ${{ github.event_name == 'pull_request' }}", text)
            self.assertIn("github.event.pull_request.number || github.ref", text)

    def test_supply_chain_checks_never_cancel_main_or_scheduled_runs(self):
        workflow = Path(__file__).parents[1] / ".github/workflows/workflow-supply-chain-guard.yml"
        if workflow.exists():
            text = workflow.read_text(encoding="utf-8")
            self.assertIn("schedule:", text)
            self.assertIn("branches: [main]", text)
            self.assertIn("cancel-in-progress: ${{ github.event_name == 'pull_request' }}", text)
            self.assertIn("workflow-supply-chain-guard-${{ github.event_name }}", text)


if __name__ == "__main__":
    main()
