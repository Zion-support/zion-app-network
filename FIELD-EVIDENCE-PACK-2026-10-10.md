# Field evidence pack — 10 October 2026

A focused content increment for the existing field-service guides. It adds six reviewable records: process/baseline, site/scope, supplier evidence, complete costs, client approval and closeout. Missing facts remain unknown. The checklist is not a quote, audit, certification, reservation or authorization to dispatch.

## Five-language entry points

| Language | Guide and evidence checklist |
|---|---|
| English | [Build a reviewable evidence pack](https://ziontechgroup.com/apps/field-service-evidence-guide.html#evidence-pack) |
| Português | [Monte um pacote de evidências para revisão](https://ziontechgroup.com/apps/field-service-evidence-guide.pt-br.html#evidence-pack) |
| Español | [Prepare un paquete de evidencias revisable](https://ziontechgroup.com/apps/field-service-evidence-guide.es.html#evidence-pack) |
| Français | [Constituez un dossier de preuves vérifiable](https://ziontechgroup.com/apps/field-service-evidence-guide.fr.html#evidence-pack) |
| Deutsch | [Erstellen Sie ein prüfbares Nachweispaket](https://ziontechgroup.com/apps/field-service-evidence-guide.de.html#evidence-pack) |

## Follow the connected tools

- [Supplier Quote Evidence Workbench](https://ziontechgroup.com/apps/supplier-quote-evidence-workbench.html): compare written quote evidence and missing facts; no supplier order or dispatch.
- [SLA Calculator](https://ziontechgroup.com/sla-calculator/): examine contractual assumptions, service windows and exclusions.
- [ROI Calculator](https://ziontechgroup.com/roi-calc/): illustrative capacity estimates, not audited savings or a client quote.
- [Automation Pilot Planner](https://ziontechgroup.com/automation-pilot-planner/): owner, baseline, human review and a stop rule for a reversible pilot.
- [Smart Hands playbook](https://ziontechgroup.com/apps/field-services-smart-hands-playbook.html), [network map](https://ziontechgroup.com/apps/network.html), [free Discovery](https://ziontechgroup.com/discovery/) and [homepage](https://ziontechgroup.com/).

Tool destinations retain their published language and capability. A working page is not production-readiness certification. The guide language switcher preserves all five variants; homepage CTA text is translated.

## Release evidence and boundaries

[Website commit 4e9f23b](https://github.com/Zion-support/zion-support.github.io/commit/4e9f23ba11212d0a7433c97056573782ef775ae7) contains a new artifact-only renderer and one integration hook. Existing root guide source is not replaced because production publishes public/** plus renderers.

Local checks: 10 HTML fixtures; five six-record checklists; reciprocal hreflang retained; one scoped homepage CTA; form/script bytes preserved; second rendering byte-identical. Committed bytes match tested bytes. No forms submitted, emails sent, bookings or purchases made.

[Deployment run](https://github.com/Zion-support/zion-support.github.io/actions/runs/38017054045) completed SUCCESS. Fresh no-cache HTTPS verification on 10 October 2026 confirmed all five guides and all five homepage CTAs contain the new release marker. All four linked tools, network/content hubs, five Discovery routes and shared stylesheet returned 200. The [publication manifest](https://ziontechgroup.com/apps/field-evidence-pack-publication.json) contains the exact release ID. This is content/link publication evidence, not complete interactive or whole-network QA.

[Translation coverage authority](TRANSLATIONS-STATUS.md) and [translation policy](TRANSLATIONS.md) were already reconciled by the 9 October release; that prior progress is preserved, not duplicated. This increment does not certify translation or interlinks for every app. Next work: bounded production-route inventory, translated body/capability checks and reciprocal links for unverified suites.
