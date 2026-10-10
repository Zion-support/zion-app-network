# Pilot tool paths — verified live 10 October 2026

Release: `pilot-tool-paths-2026-10-10-v1`. Scope: five homepage promotions and five pilot-guide language selectors, not the entire network.

## Evidence
- [Website commit 8221623](https://github.com/Zion-support/zion-support.github.io/commit/8221623cfba4b872eddb55ccbf96d0120d3aee51): exactly two files, new `scripts/render-pilot-tool-paths.cjs` and a narrow extension to the existing final `scripts/render-discovery-pilot-backlinks.cjs` hook. Workflow, forms, delivery recipients, prices and checkout destinations were not changed.
- [Simple Static Deploy 38055610601](https://github.com/Zion-support/zion-support.github.io/actions/runs/38055610601) completed SUCCESS; deploy job 114223326462 completed 10 October 2026 13:27:52 UTC. All rendering, offline checks, Pages publication and live regression steps passed.
- Immutable committed code matched local tested bytes: blobs `a0c069bc7fccdea2392188468b2047a22c2439ef` and `ec439c74d31d3301042b67b7281bc2d0d84e1c03`.
- 52 local assertions covered form/script/checkout preservation, idempotence, wrong-release rejection and missing-destination fail-before-write behavior across ten real-page fixtures. These are regression tests, not live form submissions.
- 27 independent fresh no-cache live routes passed: five homepages, five guides, ten pre-existing benefits/workflow backlinks, four tool destinations, one publication manifest and two actually referenced stylesheets. Initial guessed `/assets/css/apps.css` was 404 and is NOT a page dependency; actual stylesheets `/assets/css/site.css` and `/assets/css/discovery.css` returned 200.
- [Live publication manifest](https://ziontechgroup.com/apps/pilot-tool-paths-publication.json) declares the exact release and scope.

## Localized entry paths
| Language | Homepage promotion | Pilot guide |
|---|---|---|
| English | [Homepage](https://ziontechgroup.com/en/#pilot-tool-paths) | [Guide](https://ziontechgroup.com/apps/free-discovery-to-pilot-guide.html) |
| Português | [Início](https://ziontechgroup.com/#pilot-tool-paths) | [Guia](https://ziontechgroup.com/pt/apps/free-discovery-to-pilot-guide.html) |
| Español | [Inicio](https://ziontechgroup.com/es/#pilot-tool-paths) | [Guía](https://ziontechgroup.com/es/apps/free-discovery-to-pilot-guide.html) |
| Français | [Accueil](https://ziontechgroup.com/fr/#pilot-tool-paths) | [Guide](https://ziontechgroup.com/fr/apps/free-discovery-to-pilot-guide.html) |
| Deutsch | [Startseite](https://ziontechgroup.com/de/#pilot-tool-paths) | [Leitfaden](https://ziontechgroup.com/de/apps/free-discovery-to-pilot-guide.html) |

Every guide now has one consistent five-language selector, one current-language marker and six head alternates including x-default. Existing translated companion bodies remain preserved; this is not a claim of full semantic parity with the longer English guide.

## Interlinked planning tools
1. [Discovery Report Workbench](https://ziontechgroup.com/apps/discovery-report-workbench.html): organize the report and its assumptions.
2. [ROI Calculator](https://ziontechgroup.com/roi-calc/): compare modeled assumptions; do not confuse released capacity with measured cash savings.
3. [Automation Pilot Planner](https://ziontechgroup.com/automation-pilot-planner/): define one reversible pilot, owner and stop rule.
4. [AI Governance Checklist](https://ziontechgroup.com/ai-governance-checklist/): review permissions, human review and escalation before implementation.

These linked resources are disclosed as English-language planning tools. HTTP 200 does not certify every interaction, an integration, AI inference, compliance, savings or email delivery. The new cards and all homepage introductions/disclosures are localized in en, pt-BR, es, fr and de and use existing card/grid/button design classes.

## Continuation
Do not recreate this release or the already completed First Win, field-evidence or localized benefits/workflow releases. Next: bounded production-route inventory, body-level translation parity, same-language tool destinations and mobile/browser review. Preserve existing publication architecture and concurrent work. Full-network translation/functionality and paired Discovery inbox receipt remain incomplete. [Canonical translation authority](TRANSLATIONS-STATUS.md).
