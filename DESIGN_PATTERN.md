# 🎨 Zion App Network — Canonical Content & Design Pattern (Oct 6, 2026)

All published app-network content (showcases, spotlights, interlinks) MUST follow this single pattern for consistency.

## 1. Showcase HTML pages (per batch)
- **File naming:** `app-network-batchNN-<mondd>.html` (hub) and `apps/<month>-<year>-batchNN.html` (homepage repo)
- **Head:** `<meta charset=utf-8>`, viewport meta, `<title>Batch NN — <Theme> | Zion …</title>`, meta description, hreflang alternates (en, pt-BR, es, fr, de)
- **Layout (canonical):**
  1. Language switcher nav (🌐 EN · PT · ES · FR · DE)
  2. H1 with theme emoji + batch title
  3. Release line linking to the GitHub hub
  4. Responsive card grid — one card per app: live link (H3), one-line value prop, GitHub link
  5. Discovery block (`.disc`): 5 benefits + 2 CTAs (Start Free Discovery → /discovery/, Browse the App Network → /zion-app-network/)
  6. Footer: back link to homepage + spotlight doc link
- **CSS:** shared inline block — system-ui, max-width 960px, `#0b5fff` primary, `.grid`/`.card`/`.cta`/`.disc` classes. No external assets.

## 2. Spotlight Markdown (hub)
- `SPOTLIGHT-YYYY-MM-DD-BATCHNN.md`: emoji title, app table (repo + live URL), "Why this batch", interlinks section, Discovery footer.

## 3. Interlinks
- `INTERLINKS-batchNN-<theme>.md` in hub + `ZION_APP_NETWORK.md` in every app repo: full mesh of the batch + 2–3 related cross-batch repos + hub/homepage/Discovery links.

## 4. Indexes (always updated on release)
- Hub `APP_NETWORK_LATEST.md` (prepend) · Homepage `SPOTLIGHTS_INDEX.md` (prepend)

## 5. Translations (i18n)
- Every public showcase ships in **en, pt-BR, es, fr, de** — same file name + `-pt`, `-es`, `-fr`, `-de` suffix; `<html lang>` set; hreflang alternates on all variants. See [TRANSLATIONS.md](TRANSLATIONS.md).

© 2026 Zion Tech Group — https://ziontechgroup.com