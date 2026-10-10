# Translation coverage — verified 9 October 2026

This is the single coverage authority; TRANSLATIONS.md defines policy only. Not listed means unverified, not necessarily absent. Source naming, HTTP publication, translated body and actual functionality are separate evidence levels.

| Surface | en | pt-BR | es | fr | de | Evidence |
|---|---|---|---|---|---|---|
| Field Service Evidence Guide | 200 + QA | 200 + QA | 200 + QA | 200 + QA | 200 + QA | Canonical/alternate/switcher/heading and asset checks passed originally 02:39 UTC; regression and Telecom reciprocal links rechecked in this continuation. |
| Batch 113 insurance concepts | 200 + QA | 200 + QA | 200 + QA | 200 + QA | 200 + QA | Prior five-language publication regression passed after Telecom release; not implementation certification. |
| Batch 112 Telecom hub showcases | 200 + QA | 200 + QA | 200 + QA | 200 + QA | 200 + QA | Fresh no-cache HTTPS QA at 03:05:21 UTC: canonical, reciprocal hreflang, language switches, distinct headings, six repository links, localized Discovery, insurance/field and mirror links. |
| Batch 112 website mirrors | 200 + QA | 200 + QA | 200 + QA | 200 + QA | 200 + QA | Same verified checks as hub. Generated from one pinned, Git-blob-integrity-checked translation source. |
| Homepage Telecom promotions | 200 + links | 200 + links | 200 + links | 200 + links | 200 + links | One localized promotion per homepage, same-language Telecom mirror plus existing guides; form/script preservation asserted in renderer. Portuguese /; English /en/. |
| Field guide and insurance workbench Telecom return links | 200 + links | 200 + links | 200 + links | 200 + links | 200 + links | All ten existing related pages contain exactly one new promotion with same-language Telecom guide link. Workbench locales use /pt/apps/, /es/apps/, /fr/apps/, /de/apps/, not suffix variants. |
| Other showcases and apps | unverified | unverified | unverified | unverified | unverified | Full production-route/body coverage remains unfinished. Repository enumeration alone does not certify these pages. |

Evidence: [Batch 112 release record](BATCH112-RELEASE-2026-10-09.md), [machine-readable summary](batch112-live-verification-2026-10-09.json), [prior release record](RELEASE-VERIFICATION-2026-10-09.md), [prior read-only verifier](scripts/verify-network-release.py).

## Routes
Hub Telecom: `/zion-app-network/app-network-batch112-oct07.html` plus `-pt`, `-es`, `-fr`, `-de` before `.html`.
Website Telecom: `/apps/october-2026-batch112-telecom.html` plus `.pt-br`, `.es`, `.fr`, `.de` before `.html`.
Field guide: `/apps/field-service-evidence-guide.html` and the same website suffix convention.
Insurance workbench: `/apps/insurance-evidence-workbench.html` and `/pt/apps/insurance-evidence-workbench.html`, `/es/apps/insurance-evidence-workbench.html`, `/fr/apps/insurance-evidence-workbench.html`, `/de/apps/insurance-evidence-workbench.html`.

## Inventory boundaries
Accessible GitHub repository enumeration is complete at this audit snapshot: 1,245 distinct owner repositories, page 13 short (45), pages 14–15 empty. This is NOT a count of implemented apps. Private repository identifiers are not published here.
Full production route inventory remains partial. Before Telecom release, hub source naming heuristics counted 160 HTML files and 12 complete five-language families; public/apps source subtree contained 167 HTML files, excluding artifact renderers and other routes. These historic source counts must not be confused with current live coverage.

The Telecom release QA covered 25 HTML routes, 3 CSS assets and one publication manifest. Distinct translated headings and body-source integrity were checked; not a full human translation review, browser interaction test, whole-network certification or paired inbox receipt proof. The six Telecom repositories contain documentation/interlink/license files but no implementation code at audit. Next: complete bounded production route inventory, extend body-level coverage and reciprocal-link matrices, then backfill remaining suites without duplicating verified releases.

## Verified continuation — 10 October 2026 — pilot tool paths

The historical 9 October snapshot above is preserved. [Pilot tool-path release](PILOT-TOOL-PATHS-2026-10-10.md) deployed successfully via [run 38055610601](https://github.com/Zion-support/zion-support.github.io/actions/runs/38055610601); deploy job completed 13:27:52 UTC.

| Surface | en | pt-BR | es | fr | de | Evidence |
|---|---|---|---|---|---|---|
| Homepage pilot tool-path content | 200 + localized cards | 200 + localized cards | 200 + localized cards | 200 + localized cards | 200 + localized cards | One owned promotion, four cards and matching locale-guide CTA per page. Linked tool destinations are explicitly English-language resources. |
| Discovery-to-Pilot guide language navigation | 200 + navigation QA | 200 + navigation QA | 200 + navigation QA | 200 + navigation QA | 200 + navigation QA | One five-language selector, one current-language marker and six alternates per guide. Original/companion body content preserved, not full semantic parity certification. |
| Existing benefits/workflow pilot backlinks | 200 + links | 200 + links | 200 + links | 200 + links | 200 + links | Ten existing pages retain one same-language guide backlink each. |

27 independent no-cache route checks and 52 local safety/idempotence/negative assertions passed. [Exact production manifest](https://ziontechgroup.com/apps/pilot-tool-paths-publication.json). Forms, scripts, checkout links, delivery recipients and workflow definitions were preserved. No real form submission or mail was sent. Full-network body translation, human language review, browser interactions and paired inbox delivery remain incomplete.

## Verified continuation — 10 October 2026 — four pilot guide primary bodies

[Body translation release](PILOT-GUIDE-BODY-PARITY-2026-10-10.md) is LIVE via [deployment 38061365804](https://github.com/Zion-support/zion-support.github.io/actions/runs/38061365804), completed SUCCESS, deploy job 114240234178 finished 14:56:26 UTC. Supersedes the earlier short-companion primary-body coverage gap only; prior snapshots remain historical evidence.

| Surface | en | pt-BR | es | fr | de | Evidence |
|---|---|---|---|---|---|---|
| Discovery-to-Pilot primary body | Original unchanged | 200 + complete section coverage | 200 + complete section coverage | 200 + complete section coverage | 200 + complete section coverage | Four benefit cards, four tool paths, nine h2 headings and fourteen checklist items per localized guide; production bodies exactly match immutable tested translations. Not native-language editorial certification. |
| Previous homepage promotions and guide selectors | Preserved | Preserved | Preserved | Preserved | Preserved | Five homepages retain one promotion each; five guides retain one selector/five language links/six alternates. Ten existing benefits/workflow backlinks rechecked. |

49 portable regressions and 46 unique fresh no-cache live-route checks passed. [Exact body publication manifest](https://ziontechgroup.com/apps/pilot-guide-body-parity-publication.json). Same-language First Win/benefits/questionnaire/plans destinations are linked; English-only planning/catalog resources remain explicitly EN. No forms, recipients, pricing, checkout links, app logic or workflow definitions changed. Native-language review, mobile/browser interactions, complete production-route inventory, independently hosted app coverage and paired inbox receipt remain unfinished.
