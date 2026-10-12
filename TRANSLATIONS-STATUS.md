# Translation coverage — scoped verified releases

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

## Verified continuation — 11 October 2026 — consolidated homepage app paths

[Release record](HOME-APP-PATHS-2026-10-11.md) · [Final verification](HOME-APP-PATHS-VERIFIED-2026-10-11.md) · [Multilingual entry guide](https://ziontechgroup.com/zion-app-network/home-app-paths.html).

Website source e8ad62d added the scoped release. Its first run deployed successfully but failed a post-deploy alias-equality regression: canonical Field Service guides gained return links after aliases had been copied. The gate was preserved. Correction [bead76a9](https://github.com/Zion-support/zion-support.github.io/commit/bead76a9a5382864c27bff225440c54e468ce41f) reruns the existing alias finalizer after consolidation. [Deployment 38155089572](https://github.com/Zion-support/zion-support.github.io/actions/runs/38155089572) completed SUCCESS. Hub guide commit 2326b87e deployed via successful run 38154818663.

| Surface | en | pt-BR | es | fr | de | Evidence |
|---|---|---|---|---|---|---|
| New homepage app-path section | 200 + exact tested content | 200 + exact tested content | 200 + exact tested content | 200 + exact tested content | 200 + exact tested content | Six resource cards, capability labels, five language links and localized limitations/delivery wording per homepage. This new section is fully localized; historical archive entries are not recertified. |
| Same-site resource return links | 200 + five returns | 200 + five returns | 200 + five returns | 200 + five returns | 200 + five returns | 25 pages link to the corresponding homepage section; script/form blocks preserved. Standalone ROI calculator linked but not rewritten. |
| Field-guide canonical/alias pairs | Canonical checked | 200 + byte parity | 200 + byte parity | 200 + byte parity | 200 + byte parity | Four alias pairs are byte-identical and match final-integrity SHA256 values after the correction. |
| New network entry guide | 200 + section | 200 + section | 200 + section | 200 + section | 200 + section | One multilingual HTML page with five language sections and six destinations per section; not five separate localized URLs. |

Fresh no-cache acceptance at 2026-10-11 16:24:07 UTC passed 42 unique routes and 212 assertions. [Publication manifest](https://ziontechgroup.com/apps/home-app-paths-publication.json). Six English and eleven Portuguese repeated promotions, plus six in each other locale, remain unchanged in a native expandable archive. All original homepage hrefs and inspected forms/scripts are preserved.

Native browser verified archive expansion/collapse, capability-guide navigation and return, and all five headings. Observed viewport: innerWidth 1512px, document clientWidth 1497px, no section overflow at that width. Resizing unavailable: mobile and 1280px certification remain open. HTTP/fixture evidence is authoritative for exact card labels; the automated browser summary misstated two card names, so those names are not accepted as evidence.

Exact locale-prefix report-workbench routes returned 404 and are excluded from new cards. Investigate canonical route mappings before treating them as absent translations. Full-network translation/body/functionality/interlink audits and native editorial review remain incomplete. No email, form submission, purchase or dispatch was made.

## Verified continuation — 11 October 2026 — productivity and review catalog

Release: **catalog-productivity-review-2026-10-11-v1**. [Five-language catalog](https://ziontechgroup.com/zion-app-network/CATALOG-PRODUCTIVITY-REVIEW.html) · [Catalog navigation](https://ziontechgroup.com/zion-app-network/CATALOG-NAVIGATION.html). Historical snapshots above are preserved; this section adds scoped evidence for two already published website releases.

| Surface | en | pt-BR | es | fr | de | Capability boundary |
|---|---|---|---|---|---|---|
| Agent Brief | 200 + metadata | 200 + metadata | 200 + metadata | 200 + metadata | 200 + metadata | Local six-field composer; not autonomous agent execution. |
| Admissions Essay Reviewer | 200 + metadata | 200 + metadata | 200 + metadata | 200 + metadata | 200 + metadata | Manual-review rubric; no implemented essay processor or admission guarantee. |
| AI Access Reviewer | 200 + metadata | 200 + metadata | 200 + metadata | 200 + metadata | 200 + metadata | Human-approved planning resource; no account integration or automatic revocation. |
| AI Email Drafter | 200 + metadata | 200 + metadata | 200 + metadata | 200 + metadata | 200 + metadata | Local four-template browser tool; no model inference or email sending. |
| AI Meeting Notes Copilot | 200 + metadata | 200 + metadata | 200 + metadata | 200 + metadata | 200 + metadata | Local keyword rules; no audio transcription or semantic AI. |
| Incident Response | 200 + metadata | 200 + metadata | 200 + metadata | 200 + metadata | 200 + metadata | Service-planning guide; no live detection, monitoring or containment. |

Thirty existing page editions rechecked HTTP200 with expected declared languages, canonical URLs and six alternates. Fully translated page-body publication is documented by the prior artifact releases, not inferred from this route-only recheck: [legacy-three manifest](https://ziontechgroup.com/apps/legacy-three-locales-release.json), [source 2286a815](https://github.com/Zion-support/zion-support.github.io/commit/2286a81587b2f5ce17096677b6b9d219fd3b5338), [deployment 38175138922](https://github.com/Zion-support/zion-support.github.io/actions/runs/38175138922); [productivity/incident manifest](https://ziontechgroup.com/apps/productivity-incident-release.json), [source dc2065bb](https://github.com/Zion-support/zion-support.github.io/commit/dc2065bb56382a25446c68bcec52051ed8c4c0c6), [deployment 38180024602](https://github.com/Zion-support/zion-support.github.io/actions/runs/38180024602).

Real desktop browser audit exercised English/Portuguese email drafts, support acknowledgement and blank-input handling; Portuguese recap classification passed with actual newline characters and an Alex owner. A preceding delimiter ambiguity was resolved, not recorded as a runtime defect. Planning limits and reciprocal Portuguese verification-guide links were observed. Actual viewport1512×770, document client/scroll width1497; limited local-control focus checks, not complete keyboard/accessibility certification. Mobile resizing unavailable. [Browser and hub audit](https://backend.composio.dev/api/v3/sl/L2iv5Oy3nc).

Current [artifact coverage manifest](https://ziontechgroup.com/apps/network-publication-coverage.json) reports46five-language groups and15730gap groups after scoped reconciliation; previous aggregate file counts are historical. These are not implemented-AI-app totals or a fresh full-network census. The new catalog is one page with five translated sections and thirty localized page links, not five separate catalog URLs. No website runtime, form, delivery recipient, price, workflow or existing homepage promotion is changed by this hub-documentation consolidation. Full-network, native-speaker, mobile, assistive-technology, independently hosted repository and paired email-inbox receipt verification remain unfinished.

## Verified continuation — 12 October 2026 — supplier coverage reconciliation

The historical record above is unchanged. [Consolidated supplier verification](supplier-coverage.html) links all five workbenches, review guides, field guides, pilot guides and canonical homepages. This is a new multilingual coverage index, not another calculator or duplicated homepage promotion.

| Surface | en | pt-BR | es | fr | de | Evidence |
|---|---|---|---|---|---|---|
| Supplier-to-pilot reciprocal paths | 200 + exact blocks | 200 + exact blocks | 200 + exact blocks | 200 + exact blocks | 200 + exact blocks | Existing 20-page release rechecked; 31 routes/assets and 43 negative fixture cases passed. [Earlier release](SUPPLIER-PILOT-PATHS-2026-10-11.md) retained. |
| Supplier complete-cost worked comparison | 200 + exact blocks | 200 + exact blocks | 200 + exact blocks | 200 + exact blocks | 200 + exact blocks | Existing 15-page release and manifest independently rechecked at 2026-10-11 23:59:05 UTC; 31 negative cases passed. [Earlier release](SUPPLIER-COMPARISON-2026-10-11.md) retained. |
| Localized supplier runtime | 200 + synthetic DOM | 200 + synthetic DOM | 200 + synthetic DOM | 200 + synthetic DOM | 200 + synthetic DOM | Five freshly downloaded scripts passed 63 assertions: examples reset declarations, report/download equality, localized filenames and validation, two-supplier state, stale exports, owner-review state and unchanged arithmetic. Not visual browser certification. |

The worked-comparison website deployment [38169062825](https://github.com/Zion-support/zion-support.github.io/actions/runs/38169062825) was independently confirmed completed/success for d9946d0cab4ccf474e7faf7cf20e65584c1a6ea2. Current inspected website deployment [38180024602](https://github.com/Zion-support/zion-support.github.io/actions/runs/38180024602) also completed/success. No website source, renderer, runtime, workflow, forms or recipients changed in this reconciliation. Eight original arithmetic/privacy tests passed. GET-only verification and synthetic DOM tests made no real form submissions or supplier commitments.

Prior Notion evidence reports measured 390px/1280px supplier browser QA from the comparison release; that is prior scoped evidence, not a newly repeated browser test. Native editorial, screen-reader/Safari, whole-network body/interlink coverage and paired Discovery inbox delivery remain open. [Machine-readable reconciliation](supplier-coverage-2026-10-12.json).

## Verified continuation — 12 October 2026 — SLA evidence ledger reconciliation

The existing website release and operational catalog were preserved, not recreated. Release `sla-evidence-2026-10-11-v1`: [website source](https://github.com/Zion-support/zion-support.github.io/commit/4f79edbff8917f280062355aacc7a6283e477505), [successful deployment](https://github.com/Zion-support/zion-support.github.io/actions/runs/38173388857), [published manifest](https://ziontechgroup.com/apps/sla-evidence-publication.json), [localized operational catalog](CATALOG-OPERATIONAL-TOOLS.md). Website deploy job 114570552828 completed SUCCESS on 11 October at 20:46:30 UTC, including the new offline and live SLA checks. Hub catalog source 33b611e62ab1992dbfd0ed4592dc588b912092d3 deployed successfully through run 38174121466.

| Surface | en | pt-BR | es | fr | de | Evidence |
|---|---|---|---|---|---|---|
| Existing SLA calculator and new worked example | 200 + exact example | 200 + exact example | 200 + exact example | 200 + exact example | 200 + exact example | Runtime SHA-256 and immutable source-byte agreement; expected language, canonical, six alternates, five language switches and one example block. |
| Verification-guide SLA links | 200 + locale route | 200 + locale route | 200 + locale route | 200 + locale route | 200 + locale route | Five primary links point to the matching-language calculator; explicitly labelled English alternatives retained. |
| Existing homepage operational promotions | 200 + one CTA | 200 + one CTA | 200 + one CTA | 200 + one CTA | 200 + one CTA | One matching-language worked-example CTA per existing promotion; no duplicate tool section. |

Fresh GET-only re-verification on 12 October passed all 15 scoped pages and 71 unique internal destinations. The five-locale synthetic DOM suites passed calculations, localized invalid-input errors and recovery. Scenario: 30 days, 99.9% target, USD1,000 period fee, 5% credit per excess hour, 1 hour actual downtime yields 0.72 allowed hours, 0.28 excess hours, USD50 per excess hour and USD14 illustrative total. These are assumptions, not legal entitlement, supplier quotations or measured savings.

The production shared runtime and five interface translations already existed; the website release corrected the obsolete static fallback, added fully translated explanatory content and repaired guide navigation. Existing forms, scripts and SEO metadata were preserved. The published hub catalog was independently rechecked HTTP200 with the release marker and all ten localized example/guide links. This ledger-only continuation does not rewrite website code or repeat completed releases. Native-speaker review, real visual/mobile/keyboard/assistive-technology tests, whole-network translation/interlinks and paired Discovery inbox receipt remain unfinished.
