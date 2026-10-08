# Operations Baseline Worksheet

A free, browser-only calculator for explicit workload and automation assumptions. It estimates potential capacity, not measured savings, cash savings, ROI, a quotation or permission to implement.

## Five equivalent worksheet languages

- [English](https://ziontechgroup.com/apps/operations-baseline.html)
- [Português](https://ziontechgroup.com/pt/apps/operations-baseline.html)
- [Español](https://ziontechgroup.com/es/apps/operations-baseline.html)
- [Français](https://ziontechgroup.com/fr/apps/operations-baseline.html)
- [Deutsch](https://ziontechgroup.com/de/apps/operations-baseline.html)

## Calculation and limits

Potential monthly capacity hours = team-hours × assumed automatable share / 100.

Illustrative monthly capacity value (USD) = capacity hours × hourly capacity value.

Default example: 100 team-hours, USD45/hour, 40% share → 40 capacity hours and USD1,800 illustrative capacity value. Values are assumptions, not evidence. Implementation costs and adoption are excluded. Accept finite hours 0–100,000, hourly value 0–10,000 and share 0–100. Blank/invalid inputs do not silently become zero.

No account, card, upload, storage or automatic email. Calculation happens locally; reloading resets inputs. JavaScript is required for interactive results. Formula and navigation remain available without JavaScript.

## Interlinked existing tools

| Tool | Public route | Source |
|---|---|---|
| ROI Calculator | [Open](https://ziontechgroup.com/roi-calc/) | [Website source](https://github.com/Zion-support/zion-support.github.io/blob/main/public/roi-calc/index.html) |
| FinOps Estimator | [Open](https://ziontechgroup.com/finops-estimator/) | [Website source](https://github.com/Zion-support/zion-support.github.io/blob/main/public/finops-estimator/index.html) |
| AI Governance Checklist | [Open](https://ziontechgroup.com/ai-governance-checklist/) | [Website source](https://github.com/Zion-support/zion-support.github.io/blob/main/public/ai-governance-checklist/index.html) |
| SLA Calculator | [Open](https://ziontechgroup.com/sla-calculator/) | [Website source](https://github.com/Zion-support/zion-support.github.io/blob/main/public/sla-calculator/index.html) |

Existing calculators retain their original interface language and executable scripts. The new worksheet is fully translated; legacy tool translation is not claimed complete. Each existing tool links back to the worksheet in its native language.

## Publication contract

- Renderer: `scripts/render-operations-baseline.cjs` in the website repository.
- Engine: [operations-baseline.js](https://github.com/Zion-support/zion-support.github.io/blob/main/public/assets/js/operations-baseline.js).
- Gate: `scripts/test-operations-baseline.cjs`; calculations, boundaries, invalid/blank input, five-language browser results and nine promotions.
- Preserve existing form and script markup exactly; re-rendering must not duplicate advertisements.
- Six language alternate links per worksheet; labels, keyboard focus, live outputs and no-JavaScript explanation.
- Five homepage advertisements, four reciprocal tool links; publication manifest `/apps/operations-baseline-publication.json`.
- Reconcile the worksheet and previous finance guide into the overall coverage inventory.
- Verify the actual public deployment before marking this source release live.

[Homepage](https://ziontechgroup.com/) · [App Network](https://ziontechgroup.com/zion-app-network/) · [Free Discovery](https://ziontechgroup.com/discovery/) · [Finance paths](https://ziontechgroup.com/apps/finance-insurance-paths.html)
