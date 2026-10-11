# Hub landing-page source correction

Approved scope: remove unsupported headline/category/footer app totals and add equivalent Sales & Revenue guide links without replacing unrelated content.

The original index blob `76dfb0e8238739c23a03750718b3fe51bfadad64` is preserved byte-for-byte as `_includes/hub_legacy.html`. The new index is a minimal Jekyll wrapper with explicit text replacements. This avoids reconstructing or losing the historical directory, navigation, sections and links. Existing Git history and unrelated files remain intact. The Git tree extends the fresh parent tree; reference update is fast-forward only, never forced.

This source repair supersedes the earlier release-note warning that the independent hub index had not yet been corrected. Build and live verification are still required; a source commit alone is not publication proof. No inventory or app-functionality total is certified. Remaining historical batch descriptions and independently hosted app interfaces require separate audits.
