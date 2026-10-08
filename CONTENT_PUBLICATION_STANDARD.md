# Zion App Network — content, navigation and translation standard

Adopted for the 2026-10-08 scoped consolidation. Apply incrementally after inspecting each repository; do not bulk-overwrite working app interfaces.

## One reader journey

Homepage → free Discovery → process-specific guide → app or concept → source and related apps → small human-reviewed pilot.

Each app/content page should provide:

1. One clear title and a plain-language problem statement.
2. Current capability status: **functional local tool**, **prototype**, **documented concept**, or **verified production integration**.
3. Inputs, outputs, limitations and evidence for implemented features.
4. A free Discovery link and an explicit statement that implementation services are optional.
5. Related apps, the network map, source repository and a route back to the homepage.
6. Privacy/data-handling notes, human-review requirements and any relevant stop rules.

A successful HTTP response proves publication, not functionality, security compliance, regulatory suitability or production readiness. Do not claim SSO, RBAC, encryption, APIs or integrations solely because a README lists them.

## Shared presentation

Use the accessible Discovery stylesheet where appropriate: `/assets/css/discovery.css`. Keep a skip link, `main` landmark, semantic headings, visible keyboard focus, readable contrast, responsive cards and descriptive link text. Preserve established product names. Avoid unrelated pricing ladders or newly invented commercial SKUs.

New static guide pages in the homepage repository are rendered into the Pages artifact by approved scripts, without rewriting unrelated source homepages. Add one stable section marker; test repeated rendering does not duplicate content.

## Language coverage

Current supported guide locales: English (en), Brazilian Portuguese (pt-BR), Spanish (es), French (fr), German (de).

- Translate visible navigation, copy, action labels, validation/status text and report output where implemented.
- Keep stable canonical form values while translating display labels.
- Publish a canonical URL for each actual translated route.
- Include reciprocal language alternatives plus `x-default`.
- Language switching must land on the equivalent page, not an unrelated homepage.
- If an app remains English, disclose it. A translated guide does not imply a translated app interface.
- Track coverage per page and locale. Never label the entire network translated without a complete route inventory.

Recommended coverage ledger fields: repository; route; content type; capability status; locale; translation status; owner role; source commit; publication timestamp; HTTP status; functional test evidence; last review; blocker.

## Discovery contract

Discovery remains free and online, with no credit-card, paid meeting or purchase gate. Generate the result locally before email finishes. Provide copy/download/manual fallback. Submit the same report to the validated client address and commercial@ziontechgroup.com; distinguish provider acceptance from verified inbox delivery. Do not add unrelated recipients.

Current P0: an earlier approved provider test on 2026-10-08 returned FormSubmit HTTP 500. Mail administrator must confirm activation/service health or provision a verified transactional delivery service. Test recipient approval and designated client address are required for the round trip. Static copy changes cannot repair the external mail service.

## Release gates

- Source and public claims agree with inspected implementation.
- New pages, assets and linked app routes return HTTP 200 with expected content, not a fallback page.
- Correct `lang`, canonical URL, reciprocal language links and source references.
- No duplicate homepage sections; existing navigation and commercial links preserved.
- Test normal input, invalid input, no-JavaScript fallback and email failure states where relevant.
- Recheck the current branch/file state before editing; preserve concurrent work.
- Update the Notion CEO acceptance register and memory checkpoint with commits, tests, actual blockers and exact next steps.

## Current reference release

[Publication matrix](DISCOVERY_CONSOLIDATION_2026-10-08.md) · [Benefits](https://ziontechgroup.com/apps/discovery-benefits.html) · [Workflow guide](https://ziontechgroup.com/apps/discovery-workflow-paths.html) · [Network](https://ziontechgroup.com/apps/network.html).

Read-only publication check in the homepage repository: `node scripts/test-network-benefits.cjs --live`. The check never submits a form or sends email.
