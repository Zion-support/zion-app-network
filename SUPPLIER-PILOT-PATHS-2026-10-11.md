# Supplier evidence → reversible pilot — 11 October 2026

Release: `supplier-pilot-paths-2026-10-11-v1`.

## Source snapshot — deployment not yet certified at this snapshot

[Website commit e90b7a8](https://github.com/Zion-support/zion-support.github.io/commit/e90b7a895a61e9f77798a1cc587a615241d3599b) adds two scripts and a narrow addition to the existing Simple Static Deploy pipeline. [Deployment run](https://github.com/Zion-support/zion-support.github.io/actions/runs/38168096690) was in progress at this snapshot. The immutable three committed files independently matched the locally tested bytes. Do not treat committed source as proof of live publication; final evidence is recorded separately in `SUPPLIER-PILOT-PATHS-VERIFIED-2026-10-11.md` when available.

## A useful, bounded route through the network

Try a fictional supplier example, review complete cost versus markup and client taxes, then define a reversible test with an owner, one measurable success criterion, human review and a stop rule. Retain the itemized written quote, its validity and each assumption. Local calculations do not authorize a purchase, reservation or dispatch; written client confirmation, applicable purchase order and separate Zion authorization are still required.

The new content is localized in English, Brazilian Portuguese, Spanish, French and German. It links the existing local calculators, review guides, field evidence guides, pilot guides, canonical homepages and [network hub](https://ziontechgroup.com/zion-app-network/). It extends the existing single supplier homepage promotion rather than duplicating it.

| Language | Local supplier calculator | Review guide | Pilot guide | Homepage |
|---|---|---|---|---|
| English | [Open](https://ziontechgroup.com/apps/supplier-quote-evidence-workbench.html#supplier-pilot-paths) | [Review](https://ziontechgroup.com/apps/supplier-quote-review-guide.html#supplier-pilot-paths) | [Pilot](https://ziontechgroup.com/apps/free-discovery-to-pilot-guide.html#supplier-pilot-paths) | [Home](https://ziontechgroup.com/en/#supplier-pilot-paths) |
| Português | [Abrir](https://ziontechgroup.com/apps/supplier-quote-evidence-workbench.pt-br.html#supplier-pilot-paths) | [Revisar](https://ziontechgroup.com/apps/supplier-quote-review-guide.pt-br.html#supplier-pilot-paths) | [Piloto](https://ziontechgroup.com/pt/apps/free-discovery-to-pilot-guide.html#supplier-pilot-paths) | [Início](https://ziontechgroup.com/#supplier-pilot-paths) |
| Español | [Abrir](https://ziontechgroup.com/apps/supplier-quote-evidence-workbench.es.html#supplier-pilot-paths) | [Revisar](https://ziontechgroup.com/apps/supplier-quote-review-guide.es.html#supplier-pilot-paths) | [Piloto](https://ziontechgroup.com/es/apps/free-discovery-to-pilot-guide.html#supplier-pilot-paths) | [Inicio](https://ziontechgroup.com/es/#supplier-pilot-paths) |
| Français | [Ouvrir](https://ziontechgroup.com/apps/supplier-quote-evidence-workbench.fr.html#supplier-pilot-paths) | [Revue](https://ziontechgroup.com/apps/supplier-quote-review-guide.fr.html#supplier-pilot-paths) | [Pilote](https://ziontechgroup.com/fr/apps/free-discovery-to-pilot-guide.html#supplier-pilot-paths) | [Accueil](https://ziontechgroup.com/fr/#supplier-pilot-paths) |
| Deutsch | [Öffnen](https://ziontechgroup.com/apps/supplier-quote-evidence-workbench.de.html#supplier-pilot-paths) | [Prüfen](https://ziontechgroup.com/apps/supplier-quote-review-guide.de.html#supplier-pilot-paths) | [Pilot](https://ziontechgroup.com/de/apps/free-discovery-to-pilot-guide.html#supplier-pilot-paths) | [Start](https://ziontechgroup.com/de/#supplier-pilot-paths) |

## Preservation and QA

Thirty fresh production fixtures were downloaded before editing. The new renderer passed twenty page fixtures, forty-three negative cases, repeated-render byte-idempotence, missing-route fail-before-write, unchanged forms/scripts and unchanged five pilot primary bodies. Original calculation-core tests: 8/8 passed. Existing twenty-one-route supplier guidance live checks passed before publication.

Calculator code, original supplier generation, reports, currency/tax policy, authorization gates, delivery recipients, pricing and checkout destinations are unchanged. The workflow addition retains all prior steps, permissions, concurrency and deployment settings; it adds only source-path triggers, a final render/test gate and GET-only live checks.

The browser exercised existing five-language calculators and examples at an actual 1512px desktop viewport. Detailed localized custom-error and download coverage is not fully established by the summary. Mobile viewport resizing was unavailable; do not claim mobile certification. Native editorial review, complete app-network translations, independently hosted app functionality and paired current inbox receipt remain unfinished.

[CEO execution board](https://app.notion.com/p/3f5b94b0eaf7818291d4fa512ae5d8a1) · [Single translation coverage authority](TRANSLATIONS-STATUS.md) · [Existing supplier catalog](CATALOG-SUPPLIER-EVIDENCE.md).
