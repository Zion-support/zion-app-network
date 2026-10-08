# Operational planning tools — local calculations, not AI claims

## Five equivalent guide editions

[English](https://ziontechgroup.com/apps/operational-planning-tools.html) · [Português](https://ziontechgroup.com/pt/apps/operational-planning-tools.html) · [Español](https://ziontechgroup.com/es/apps/operational-planning-tools.html) · [Français](https://ziontechgroup.com/fr/apps/operational-planning-tools.html) · [Deutsch](https://ziontechgroup.com/de/apps/operational-planning-tools.html)

| Tool or path | Status | English entry |
|---|---|---|
| ROI / manual-cost calculator | Local numeric calculation; manual hours × loaded hourly rate. No measured savings or ROI guarantee. | [Open](https://ziontechgroup.com/roi-calc/) |
| SLA downtime / credit calculator | Local linear scenario: allowed downtime, excess downtime, hourly credit and illustrative total. Contract caps and tiers are not applied. | [Open](https://ziontechgroup.com/sla-calculator/) |
| AI governance self-assessment | Ten self-reported controls; not an audit, certification or implementation approval. | [Open](https://ziontechgroup.com/ai-governance-checklist/) |
| FinOps Estimator | Existing redirect/advisory path, not a functioning calculator. | [FinOps consulting](https://ziontechgroup.com/finops-consulting/) |

Each of the three working local tools has equivalent EN/PT-BR/ES/FR/DE pages and reciprocal links through the operational guide. The controls, validation errors and result labels are translated. Inputs are not sent, uploaded or stored on a server; no model inference, payment or email occurs. JavaScript is required for interactive results.

## Reproducible scenario

- Manual workload: 40 hours/month × USD 45/hour = USD 1,800/month, USD 21,600/year.
- SLA: 99.9% over 30 days permits 0.72 hours. With 1 hour actual downtime, excess = 0.28 hours. A 5% credit per excess hour on a USD 1,000 period fee means USD 50/hour and USD 14 illustrative total, before contract-specific caps, tiers or exclusions.
- Governance: count only the ten controls in the checklist, not unrelated checkboxes elsewhere on a page.

## Publication and safety contract

[Renderer](https://github.com/Zion-support/zion-support.github.io/blob/main/scripts/render-operational-tools.cjs) · [Calculation/browser engine](https://github.com/Zion-support/zion-support.github.io/blob/main/public/assets/js/operational-tools.js) · [Regression tests](https://github.com/Zion-support/zion-support.github.io/blob/main/scripts/test-operational-tools.cjs)

Generated publication: 15 interactive tool pages, five guides and five localized homepage promotions. Tests cover formula invariants, invalid/empty/non-finite/negative inputs, period boundaries, scoped governance controls, translations, metadata, preserved homepage forms and idempotent rendering. Verify deployment using the [publication manifest](https://ziontechgroup.com/apps/operational-tools-publication.json); a source commit alone is not evidence of public availability.

[Free Discovery](https://ziontechgroup.com/discovery/) · [Finance & Insurance guide](https://ziontechgroup.com/apps/finance-insurance-paths.html) · [Network hub](https://ziontechgroup.com/zion-app-network/) · [Homepage](https://ziontechgroup.com/)

Discovery remains free. Its local report is instant; email submission is not proof of inbox receipt. This release does not send a Discovery email test.
