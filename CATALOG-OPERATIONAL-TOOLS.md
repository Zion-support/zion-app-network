# Operational planning tools — local calculations, not AI claims

## Five equivalent guide editions

[English](https://ziontechgroup.com/apps/operational-planning-tools.html) · [Português](https://ziontechgroup.com/pt/apps/operational-planning-tools.html) · [Español](https://ziontechgroup.com/es/apps/operational-planning-tools.html) · [Français](https://ziontechgroup.com/fr/apps/operational-planning-tools.html) · [Deutsch](https://ziontechgroup.com/de/apps/operational-planning-tools.html)

| Tool or path | Status | English entry |
|---|---|---|
| Manual workload cost calculator | Local numeric calculation; manual hours × loaded hourly rate, shown monthly and annually. It does not calculate investment returns. | [Open](https://ziontechgroup.com/roi-calc/) |
| SLA downtime / credit calculator | Local linear scenario: allowed downtime, excess downtime, hourly credit and illustrative total. Contract caps and tiers are not applied. | [Open](https://ziontechgroup.com/sla-calculator/) |
| AI governance self-assessment | Ten self-reported controls; not an audit, certification or implementation approval. | [Open](https://ziontechgroup.com/ai-governance-checklist/) |
| FinOps scenario estimator | Local cloud-cost scenario from your assumptions: gross reduction, net benefit and simple payback. No cloud account connection or measured-savings claim. | [Open](https://ziontechgroup.com/apps/finops-scenario-estimator.html) |

Each of the three working local tools has equivalent EN/PT-BR/ES/FR/DE pages and reciprocal links through the operational guide. The controls, validation errors and result labels are translated. Inputs are not sent, uploaded or stored on a server; no model inference, payment or email occurs. JavaScript is required for interactive results.

## Choose the tool in your language

| Language | Manual workload cost | SLA downtime and credits | Governance self-assessment | Operational guide |
|---|---|---|---|---|
| English | [Calculate workload cost](https://ziontechgroup.com/roi-calc/) | [Compare an SLA scenario](https://ziontechgroup.com/sla-calculator/) | [Review ten controls](https://ziontechgroup.com/ai-governance-checklist/) | [Read the guide](https://ziontechgroup.com/apps/operational-planning-tools.html) |
| Português (Brasil) | [Calcular o custo do trabalho](https://ziontechgroup.com/pt/roi-calc/) | [Comparar um cenário de SLA](https://ziontechgroup.com/pt/sla-calculator/) | [Revisar dez controles](https://ziontechgroup.com/pt/ai-governance-checklist/) | [Ler o guia](https://ziontechgroup.com/pt/apps/operational-planning-tools.html) |
| Español | [Calcular el coste del trabajo](https://ziontechgroup.com/es/roi-calc/) | [Comparar un escenario de SLA](https://ziontechgroup.com/es/sla-calculator/) | [Revisar diez controles](https://ziontechgroup.com/es/ai-governance-checklist/) | [Leer la guía](https://ziontechgroup.com/es/apps/operational-planning-tools.html) |
| Français | [Calculer le coût du travail](https://ziontechgroup.com/fr/roi-calc/) | [Comparer un scénario SLA](https://ziontechgroup.com/fr/sla-calculator/) | [Examiner dix contrôles](https://ziontechgroup.com/fr/ai-governance-checklist/) | [Lire le guide](https://ziontechgroup.com/fr/apps/operational-planning-tools.html) |
| Deutsch | [Arbeitskosten berechnen](https://ziontechgroup.com/de/roi-calc/) | [Ein SLA-Szenario vergleichen](https://ziontechgroup.com/de/sla-calculator/) | [Zehn Kontrollen prüfen](https://ziontechgroup.com/de/ai-governance-checklist/) | [Leitfaden lesen](https://ziontechgroup.com/de/apps/operational-planning-tools.html) |

## Reproducible scenario

- Manual workload: 40 hours/month × USD 45/hour = USD 1,800/month, USD 21,600/year.
- SLA: 99.9% over 30 days permits 0.72 hours. With 1 hour actual downtime, excess = 0.28 hours. A 5% credit per excess hour on a USD 1,000 period fee means USD 50/hour and USD 14 illustrative total, before contract-specific caps, tiers or exclusions.
- Governance: count only the ten controls in the checklist, not unrelated checkboxes elsewhere on a page.

## Publication and safety contract

[Renderer](https://github.com/Zion-support/zion-support.github.io/blob/main/scripts/render-operational-tools.cjs) · [Calculation/browser engine](https://github.com/Zion-support/zion-support.github.io/blob/main/public/assets/js/operational-tools.js) · [Regression tests](https://github.com/Zion-support/zion-support.github.io/blob/main/scripts/test-operational-tools.cjs)

Generated publication: 15 interactive tool pages, five guides and five localized homepage promotions. Tests cover formula invariants, invalid/empty/non-finite/negative inputs, period boundaries, scoped governance controls, translations, metadata, preserved homepage forms and idempotent rendering. Verify deployment using the [publication manifest](https://ziontechgroup.com/apps/operational-tools-publication.json); a source commit alone is not evidence of public availability.

[Free Discovery](https://ziontechgroup.com/discovery/) · [FinOps scenario estimator](https://ziontechgroup.com/apps/finops-scenario-estimator.html) · [Network hub](https://ziontechgroup.com/zion-app-network/) · [Homepage](https://ziontechgroup.com/)

Discovery remains free. Its local report is instant; email submission is not proof of inbox receipt. This release does not send a Discovery email test.

## SLA worked example — five calculator editions

Choose the same-language calculator and reproduce the synthetic scenario above:

| Language | Worked example | App verification guide |
|---|---|---|
| English | [Check the example](https://ziontechgroup.com/sla-calculator/) | [Choose and verify an app](https://ziontechgroup.com/apps/app-verification-guide.html) |
| Português (Brasil) | [Conferir o exemplo](https://ziontechgroup.com/pt/sla-calculator/) | [Escolher e verificar um app](https://ziontechgroup.com/pt/apps/app-verification-guide.html) |
| Español | [Comprobar el ejemplo](https://ziontechgroup.com/es/sla-calculator/) | [Elegir y verificar una app](https://ziontechgroup.com/es/apps/app-verification-guide.html) |
| Français | [Vérifier l’exemple](https://ziontechgroup.com/fr/sla-calculator/) | [Choisir et vérifier une application](https://ziontechgroup.com/fr/apps/app-verification-guide.html) |
| Deutsch | [Beispiel prüfen](https://ziontechgroup.com/de/sla-calculator/) | [Eine App auswählen und prüfen](https://ziontechgroup.com/de/apps/app-verification-guide.html) |

### Historical validation record — 11 October 2026

Release `sla-evidence-2026-10-11-v1` is published: [website commit](https://github.com/Zion-support/zion-support.github.io/commit/4f79edbff8917f280062355aacc7a6283e477505), [successful deployment](https://github.com/Zion-support/zion-support.github.io/actions/runs/38173388857), [live manifest](https://ziontechgroup.com/apps/sla-evidence-publication.json), [reproducible verifier](https://github.com/Zion-support/zion-support.github.io/blob/4f79edbff8917f280062355aacc7a6283e477505/scripts/render-sla-evidence.cjs).

Fresh read-only production verification passed five calculator/example pages, five verification guides and five homepage promotions, plus 71 unique internal destinations. Checks included the manifest marker, runtime SHA-256 integrity, localized calculation/error recovery, one owned example per calculator, canonical metadata, six alternate-language tags, language links and reciprocal navigation. Existing homepage promotions were extended rather than duplicated. The published calculator runtime was already correct; the release also reconciled the obsolete static fallback.

These checks do not certify native-language quality, real browser visual/keyboard accessibility, every network translation, every app implementation or Discovery inbox receipt. Remaining work: bounded source/build-generated localization and capability inventory, reciprocal-link matrix, and desktop/mobile/keyboard/native-speaker review. Preserve working canonical aliases and concurrent releases; do not recreate this release.
