# Translation coverage — verified 9 October 2026

This file is the single coverage authority; TRANSLATIONS.md defines policy only. Older conflicting tables are superseded by scoped evidence. Not listed means unverified, not necessarily absent.

| Surface | en | pt-BR | es | fr | de | Evidence |
|---|---|---|---|---|---|---|
| Field Service Evidence Guide | 200 + QA | 200 + QA | 200 + QA | 200 + QA | 200 + QA | Fresh HTTPS GETs at 02:39 UTC on 9 Oct; canonical, reciprocal hreflang, language switcher, distinct headings, localized Discovery, evidence gates and stylesheet checks passed. |
| Batch 113 insurance concepts | 200 + QA | 200 + QA | 200 + QA | 200 + QA | 200 + QA | Fresh HTTPS GETs at 02:39 UTC on 9 Oct; canonical, reciprocal hreflang, language switcher, distinct headings, localized Discovery, field guide interlinks and stylesheet checks passed. |
| Homepage promotions | 200 + links | 200 + links | 200 + links | 200 + links | 200 + links | Five published homepages include same-language Batch 113 and Field Service guide links. Portuguese is /; English is /en/. |
| Other showcases and apps | unverified | unverified | unverified | unverified | unverified | Full paginated repository and production-route reconciliation remains pending. |

Evidence: [release record](RELEASE-VERIFICATION-2026-10-09.md), [machine-readable summary](release-verification-2026-10-09.json), [reusable read-only verifier](scripts/verify-network-release.py).

Field routes: `/apps/field-service-evidence-guide.html`, `.pt-br.html`, `.es.html`, `.fr.html`, `.de.html`.
Batch 113 routes: `/zion-app-network/app-network-batch113-oct07.html` plus `-pt`, `-es`, `-fr`, `-de` before `.html`.

Checks cover 15 HTML routes and 3 same-origin CSS assets. Distinct translated headings and navigation metadata were checked; this is not a full human translation review, browser interaction test, whole-network certification or paired email receipt proof. The six insurance repositories are presented as documented concepts, not verified deployed AI systems.

Next: reconcile full repository/production inventory, extend body-level translation and reciprocal-link checks, and backfill remaining suites in bounded releases. Do not duplicate existing renderers or renumber colliding batches.
