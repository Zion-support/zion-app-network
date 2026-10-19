# Hub v17 — Merged Release 2026 (draft, not live)

Status: DRAFT branch/PR only on 2026-10-19. Not merged, not deployed, not live-verified. Publication is not proof of AI functionality.

## What this adds
- Five-language showcase (EN, pt-BR, ES, FR, DE) following DESIGN-PATTERN.md: language bar with all five languages, hub header gradient, cards, responsible-pilot/Discovery section, Explore the Network section, standard footer.
- Interlinks from every locale to: Agent Trace Evidence Lab, Field SLA Acceptance Matrix, AI Dependency Blast Radius (all live HTTP 200 on 2026-10-19), localized Discovery, localized homepage, localized directory, Restored A-E showcase, and this GitHub hub.
- APPS_INDEX-ADDENDUM-MERGED-RELEASE-2026.md: first index tranche for repositories missing from APPS_INDEX.md + CATALOG.md.

## Inventory basis (2026-10-19 audit)
- Zion-support repositories: 1,245.
- APPS_INDEX.md unique repo links: 193. CATALOG.md: 484. Combined indexed: 560. Missing from both: 685.
- Per DESIGN-PATTERN.md section 6, the large masters are consolidated via rollup/addendum files rather than rewritten wholesale via API. Further tranches should continue alphabetically and verify each live route before promotion.

## Release gates before merge/deploy
1. Review this draft PR and the five HTML files for language, links and claims.
2. Merge only with separate named approval; do not merge PR71543 in zion-support.github.io (open/draft, dirty, modifies static-deploy.yml).
3. After merge, wait for Pages and verify all five showcase URLs return HTTP 200 with the correct lang, canonical and hreflang set.
4. Add this showcase to the hub legacy index/promotion only in a reviewed follow-up if the include structure is confirmed; this draft does not rewrite index.html or hub_legacy.html.
5. Update APP_NETWORK_LATEST.md and the Notion CEO register after live verification, not before.

## Live links referenced (verified 2026-10-19)
- https://ziontechgroup.com/agent-trace-evidence-lab/
- https://ziontechgroup.com/field-sla-acceptance-matrix/
- https://ziontechgroup.com/ai-dependency-blast-radius/
- https://ziontechgroup.com/zion-app-network/
- https://ziontechgroup.com/discovery/
