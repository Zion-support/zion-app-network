# 🎨 Zion App Network — Consolidated Design & Content Pattern (2026-10-06)

All new published pages (showcases, cross-showcases, homepage feature pages) MUST follow this single pattern so the whole network looks, reads and navigates the same.

## 1. Structure (in order)
1. `<nav class="langbar">` — language switcher: English · Português · Español, one link per published translation, `active` class on current language
2. `<header>` — gradient banner, H1 with emoji, one-paragraph pitch, 1–2 CTA buttons (Discovery CTA always present)
3. Suite/batch `<section>`s — H2 with emoji + `.cards` grid of `.card` items (title, 1-sentence description, Live app + Repo links)
4. **Discovery benefits `<section>`** — always present, always the 6 canonical benefits + the commercial banner (dual-delivery to client + commercial@ziontechgroup.com)
5. "Explore the Network" `<section>` — hub, homepage, GitHub hub, sibling showcases
6. `<footer>` — `© 2026 Zion Tech Group — ziontechgroup.com · Part of the Zion AI App Network`

## 2. Canonical URLs to interlink (every page)
- Hub: https://ziontechgroup.com/zion-app-network/
- GitHub hub: https://github.com/Zion-support/zion-app-network
- Discovery: https://ziontechgroup.com/discovery/ (+ https://ziontechgroup.com/app-network-discovery.html EN)
- Homepage: https://ziontechgroup.com/
- Latest cross-showcase: https://ziontechgroup.com/zion-app-network/app/network-october-2026-cross-showcase.html

## 3. Design tokens
- Font: system-ui stack; body color #0f172a on #f8fafc
- Header gradient: hub pages `#0ea5e9 → #6366f1`; homepage features `#1e3a8a → #0ea5e9`
- Cards: white, 1px #e2e8f0 border, 12px radius, subtle shadow
- CTAs: primary #1e3a8a (homepage) / #6366f1 (hub), `.green` #059669 for Discovery, `.sky`/`.alt` #0ea5e9
- H2 accent: 3px bottom border (#0ea5e9 homepage / #6366f1 hub)

## 4. Translations
- Languages: **en** (canonical), **pt-BR** (`-pt` suffix), **es** (`-es` suffix)
- Same file name with suffix, e.g. `app-network-october-2026.html` / `-pt.html` / `-es.html`
- Every translated page carries `<link rel="alternate" hreflang>` for all three + langbar nav
- Translate headings, descriptions, benefits and CTAs; keep app proper names and URLs unchanged

## 5. Discovery rules (non-negotiable)
- Discovery is **always online, always free** — never add pricing to Discovery pages
- Every page advertises the 6 benefits and the instant dual-delivery: results emailed to the client AND commercial@ziontechgroup.com on submit (FormSubmit + mailto fallback)

## 6. Deployment
- Public web content only goes in repos that serve on the custom domain: `zion-support.github.io` (public/) and `zion-app-network` (served at /zion-app-network/)
- Repo-root .md files in zion-support.github.io are NOT publicly served — publish HTML under public/
- After committing, verify 200 with curl; Pages deploys can take several minutes

© 2026 Zion Tech Group