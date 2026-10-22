import importlib.util
from pathlib import Path
from unittest import TestCase, main
from unittest.mock import patch
spec = importlib.util.spec_from_file_location("guard", Path(__file__).with_name("public_content_privacy_guard.py"))
guard = importlib.util.module_from_spec(spec)
spec.loader.exec_module(guard)
class GuardTests(TestCase):
    def test_safe_public_content(self):
        diff="+++ b/docs/guide.md\n@@ -0,0 +1,2 @@\n+Pricing calculators compare cost estimates.\n+Our public site https://ziontechgroup.com/apps/ is free.\n"
        report=guard.scan_patch(diff)
        self.assertEqual(report["status"],"pass")
        self.assertEqual(report["scanned_added_lines"],2)
    def test_private_links_and_tokens_redacted(self):
        diff=("+++ b/docs/new.md\n@@ -0,0 +1,3 @@\n"
             "+https://mail.google.com/mail/u/0/#all/example\n"
             "+https://app.notion.com/p/private\n"
             "+github_pat_"+"a"*32+"\n")
        report=guard.scan_patch(diff)
        self.assertEqual(report["finding_count"],3)
        self.assertNotIn("github_pat_",str(report))
        self.assertEqual(set(x["rule"] for x in report["findings"]),{"private-gmail-deeplink","private-notion-page","github-token-like"})
    def test_removed_lines_not_scanned(self):
        diff="+++ b/docs/guide.md\n@@ -1 +1 @@\n-https://app.notion.com/p/old\n+Public content only.\n"
        self.assertEqual(guard.scan_patch(diff)["finding_count"],0)
    def test_encoded_html_and_nonpublic_fixtures(self):
        diff="+++ b/public/sample.html\n@@ -0,0 +1 @@\n+https%3A%2F%2Fapp.hubspot.com%2Fcontacts%2F123\n+++ b/scripts/test_public_content_privacy_guard.py\n@@ -0,0 +1 @@\n+https://mail.google.com/mail/u/0/#all/private\n"
        report=guard.scan_patch(diff)
        self.assertEqual(report["finding_count"],1)
        self.assertEqual(report["findings"][0]["rule"],"private-hubspot-record")
    def test_workflow_triggers_cover_every_scanned_extension(self):
        workflow = Path(__file__).parents[1] / ".github/workflows/public-content-privacy-guard.yml"
        text = workflow.read_text(encoding="utf-8")
        for suffix in guard.CONTENT_SUFFIXES:
            self.assertIn("'**/*" + suffix + "'", text, "Missing trigger for " + suffix)
    def test_invalid_commit_sha_rejected(self):
        with self.assertRaises(ValueError):
            guard.get_patch(".", "main", "HEAD")
if __name__ == "__main__":
    main()
