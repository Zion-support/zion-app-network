# Curated resource paths — 11 October 2026

Status: DRAFT BRANCH CONTENT, NOT LIVE VERIFIED. Do not present proposed routes as published.

The companion [five-language navigation page](../curated-resource-paths.html) uses one shared design, accessible keyboard focus, responsive layout and twenty same-language resource links. English, Portuguese (pt-BR), Spanish, French and German sections contain the same four resource categories and safety boundaries. No forms, trackers, payments, inferred app counts or production-AI promises are added.

## Evidence-led resource paths

1. Field-service evidence: scope, access, named responsibility and completion records.
2. Telecom concepts: six documented concepts, with implementation limits retained.
3. Logistics evidence: routing, forecasts and exception handling; validate data and human review.
4. Discovery to pilot: one workflow, baseline, owner, acceptance test and rollback plan.

The website companion branch `content/network-navigation-wide-20261011` creates five resource-path guides, five homepage promotions and twenty reciprocal guide links. Its generator checks target artifacts before writing and preserves existing form/script blocks. It runs after translation generation, not before it. Existing URLs remain unchanged.

## Route conventions

| Language | Website companion route (proposed) | Guide suffix | Pilot prefix |
|---|---|---|---|
| English | /apps/network-resource-paths.html | .html | /apps/ |
| Português | /pt/apps/network-resource-paths.html | .pt-br.html | /pt/apps/ |
| Español | /es/apps/network-resource-paths.html | .es.html | /es/apps/ |
| Français | /fr/apps/network-resource-paths.html | .fr.html | /fr/apps/ |
| Deutsch | /de/apps/network-resource-paths.html | .de.html | /de/apps/ |

Suffix conventions apply to the existing field-service, Telecom and Logistics guides. Pilot guides use path prefixes; never fabricate suffix variants. Portuguese homepage is `/`; English homepage is `/en/`.

## Release gates and scope

- Keep both PRs draft until current checks, route artifacts, accessibility and renderer order are reviewed.
- Approve merge/publication separately; no deployment was requested by this draft implementation batch.
- Fresh browser verification remains blocked until the Browserless connection is Active.
- After approved deployment, check canonical metadata, language selectors, twenty targets, reciprocal links and five homepage promotions against the release marker `network-resource-paths-2026-10-11`.
- HTTP availability is not app functionality certification or paired-inbox delivery evidence.
- Human language review and whole-network route/body inventory remain unfinished. [Coverage authority](../TRANSLATIONS-STATUS.md) remains authoritative; this draft does not overwrite historical evidence.
