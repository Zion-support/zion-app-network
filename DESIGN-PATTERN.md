# 🎨 Zion App Network — Consolidated Design & Content Pattern (2026-10-08, v2)

All published pages (showcases, cross-showcases, homepage feature pages) MUST follow this single pattern so the whole network looks, reads and navigates the same.

## 1. Structure (in order)
1. `<nav class="langbar">` — language switcher with ALL FIVE languages: English · Português · Español · Français · Deutsch, one link per published translation, `active` class on current language
2. `<header>` — gradient banner, H1 with emoji, one-paragraph pitch, 1–2 CTA buttons (Discovery CTA always present)
3. Suite/batch `<section>`s — H2 with emoji + `.cards` grid of `.card` items (title, 1-sentence description, Live app + Repo links)
4. **Discovery benefits `<section>`** — always present, always the 6 canonical benefits + the commercial banner (dual-delivery to client + commercial@ziontechgroup.com)
5. "Explore the Network" `<section>` — hub, homepage, GitHub hub, sibling showcases
6. `<footer>` — `© 2026 Zion Tech Group — ziontechgroup.com · Part of the Zion AI App Network`

## 2. Canonical URLs to interlink (every page)
- Hub: https://ziontechgroup.com/zion-app-network/
- GitHub hub: https://github.com/Zion-support/zion-app-network
- Discovery: https://ziontechgroup.com/discovery/ (+ https://ziontechgroup.com/app-network-discovery.html EN)
- Discovery guides: /apps/discovery-showcase.html (EN) · -pt.html · -es.html · -fr.html · -de.html
- Homepage: https://ziontechgroup.com/
- Latest cross-showcase: https://ziontechgroup.com/zion-app-network/app/network-october-2026-cross-showcase.html

## 3. Design tokens
- Font: system-ui stack; body color #0f172a on #f8fafc
- Header gradient: hub pages `#0ea5e9 → #6366f1`; homepage features `#1e3a8a → #0ea5e9`
- Cards: white, 1px #e2e8f0 border, 12px radius, subtle shadow
- CTAs: primary #1e3a8a (homepage) / #6366f1 (hub), `.green` #059669 for Discovery, `.sky`/`.alt` #0ea5e9
- H2 accent: 3px bottom border (#0ea5e9 homepage / #6366f1 hub)

## 4. Translations — FIVE-language standard
- Languages: **en** (canonical, no suffix), **pt-BR** (`-pt`), **es** (`-es`), **fr** (`-fr`), **de** (`-de`)
- Same file name with suffix, e.g. `app-network-october-2026.html` / `-pt.html` / `-es.html` / `-fr.html` / `-de.html`
- Every translated page carries `<link rel="alternate" hreflang>` for all five + full 5-language langbar nav
- Translate headings, descriptions, benefits and CTAs; keep app proper names and URLs unchanged
- Where possible link the same-language Discovery guide (/apps/discovery-showcase-XX.html)
- Reference implementation (5 languages, verified): October 2026 cross-showcase + homepage feature; batch 98 showcase (app-network-batch98-oct06[-pt|-es|-fr|-de].html)

## 5. Discovery rules (non-negotiable)
- Discovery is **always online, always free** — never add pricing to Discovery pages
- Every page advertises the 6 benefits and the instant dual-delivery: results emailed to the client AND commercial@ziontechgroup.com on submit (FormSubmit + mailto fallback)

## 6. Deployment
- Public web content only goes in repos that serve on the custom domain: `zion-support.github.io` (public/) and `zion-app-network` (served at /zion-app-network/)
- Repo-root .md files in zion-support.github.io are NOT publicly served — publish HTML under public/
- Pages deploys take ~5–8 minutes after commit — always verify 200 with curl after waiting
- CATALOG.md (~52KB) and APPS_INDEX.md (~45KB) are too large to rewrite via API each session — consolidate via rollup files (e.g. APPS_INDEX-BATCHES-92-113.md)

## 7. Backfill status (2026-10-08)
- 5-language complete: October 2026 cross-showcase, October 2026 homepage feature, batch 98 showcase, Discovery guides
- Pending backfill: batch showcases 70–97 and 99–113 (FR/DE + 5-lang nav)

© 2026 Zion Tech Group