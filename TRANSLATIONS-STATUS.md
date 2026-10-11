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

## Verified continuation — 11 October 2026 — supplier review guidance

[Release evidence](SUPPLIER-GUIDANCE-VERIFIED-2026-10-11.md) · [Canonical route catalog](CATALOG-SUPPLIER-EVIDENCE.md). The prior supplier calculator release was recovered from memory and preserved, not recreated. Website commit [ffb4a174](https://github.com/Zion-support/zion-support.github.io/commit/ffb4a174619fcd9345e8db8ddd5dfa5275ac688e) published successfully via [run 38152437270](https://github.com/Zion-support/zion-support.github.io/actions/runs/38152437270); deploy job 114508472209 completed 15:46:02 UTC. Hub interlinks published via [run 38152511638](https://github.com/Zion-support/zion-app-network/actions/runs/38152511638).

| Surface | en | pt-BR | es | fr | de | Evidence |
|---|---|---|---|---|---|---|
| Supplier quote review guide | 200 + body parity | 200 + body parity | 200 + body parity | 200 + body parity | 200 + body parity | Five full translated sections; fictional costs, markup versus margin, tax separation, authorization and privacy. Each deployed page byte-identical to the tested artifact, with canonical, six alternates and five-language navigation. |
| Existing supplier workbench | 200 + regression | 200 + regression | 200 + regression | 200 + regression | 200 + regression | Five calculation scripts byte-identical before/after this increment. Existing pricing/gate/privacy tests passed. Native report samples observed in all five languages; detailed download/stale-export/two-supplier/owner-review/native validation tested in English. |
| Homepage and workbench guidance links | 200 + reciprocal links | 200 + reciprocal links | 200 + reciprocal links | 200 + reciprocal links | 200 + reciprocal links | Ten pages each contain exactly one matching-language guide link; previous homepage promotions and all 25 workbench-to-field-guide returns retained. |
| Multilingual supplier hub | 200 + section link | 200 + section link | 200 + section link | 200 + section link | 200 + section link | One multilingual hub page with five language sections; not five separate localized hub routes. Each section links its guide, workbench and field guide. |

27 unique fresh HTTP routes/assets passed: five guides, five workbenches, five canonical homepages, five scripts, five field guides, one manifest and one hub. [Publication manifest](https://ziontechgroup.com/apps/supplier-guidance-publication.json). Guide render is idempotent and asserts form/script preservation. No calculator core, tax/pricing policy, approval gate, recipient, payment or workflow definition changed.

Native browser viewport was actually 1512px (document client width 1497px); resizing is unsupported. Do not claim new 390px/1280px viewport or assistive-technology certification. Native-speaker review and full-network route/body/capability/interlink coverage remain unfinished. The historical snapshots above are preserved; this continuation is scoped supplier evidence, not whole-network certification.
