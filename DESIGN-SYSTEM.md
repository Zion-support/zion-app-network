# Zion App Network — Content Design System (consolidated pattern)

Standard pattern for ALL published showcase/landing content (hub pages, batch spotlights, discovery, blog).

## Theme
- Dark: bg `#080b16`, panel `#0e1528`, border `#26324d`, muted `#aab6d0`
- Gradient brand text: `linear-gradient(90deg,#c4b5fd,#f5d0fe 50%,#93c5fd)`
- CTA button `#7c3aed` (radius 11px), alt button `#151e35` + border `#384766`
- Cards: `linear-gradient(145deg,#101a31,#0c1222)`, radius 16px, 2-col grid → 1-col ≤720px

## Layout (all pages)
1. Header nav: brand → App Network · Plans · Book a call
2. Hero: eyebrow · H1 with gradient span · sub-paragraph · 2 CTAs
3. Benefits grid (cards)
4. Questionnaire / content section
5. "Explore the network" interlink grid (hub · APPS_INDEX · CATALOG · INTERLINKS · Plans)
6. Footer: © 2026 Zion Tech Group · ziontechgroup.com · commercial@ziontechgroup.com · Plans · App Network

## Interlinks (mandatory on every page)
- https://ziontechgroup.com/zion-app-network/
- https://ziontechgroup.com/discovery/
- https://ziontechgroup.com/en/plans/
- https://github.com/Zion-support/zion-app-network

## i18n
- Current standard for new app/showcase routes: **en, pt-BR, es, fr, de**. Older pages are not presumed translated until audited.
- Every localized page needs a unique translated title, H1, substantive copy, `<html lang>`, self-canonical, reciprocal `hreflang` siblings, and `x-default` pointing to English.
- Provide visible keyboard-accessible language switching and a locally translated navigation, content and CTA.
- Free Discovery routes: `/discovery/`, `/pt/discovery/`, `/es/discovery/`, `/fr/discovery/`, `/de/discovery/`.
- Release QA is source-only until verified against actual deployed URLs; do not confuse a GitHub commit, green CI, or an HTTP 200 with a proven usable customer journey.

## Content and service integrity
- Discovery self-assessment is **free**; optional paid consulting, implementation and subscriptions must be separately described and must not block the free journey.
- App cards and network listings are evidence of published resources, not proof that listed AI engines are functional or production-ready.
- For field-service planning, show verified supplier all-in cost and at least a **40% markup** (minimum sale = verified cost x 1.40, not 40% gross margin).
- Never book, purchase, reserve or dispatch without written client confirmation, PO number and Zion internal release.
- Public tools must not request client secrets, exact site details, serial numbers, private procurement references or personal data unnecessary to the use case.
- Before a production merge: run targeted source-contract tests, privacy diff guard and exact-head CI; after deployment verify localized routes and links without assuming email delivery or payment activation.

## Publishing rules
- Custom domain serves ONLY from zion-support.github.io; publish /discovery/* and /blog/* there (standalone repos deploy their own Pages but the domain does not route to them).
- Durable showcase pages go in zion-app-network repo (Pages serve in ~1 min).
- Never hand-edit homepage index.html (auto-managed system overwrites).

© 2026 Zion Tech Group
