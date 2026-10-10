# Field evidence aliases — verified 10 October 2026

Status: LIVE VERIFIED. The four translated language-prefix aliases now contain the newest six-record evidence checklist, matching the corresponding canonical guide sections. English remains the fifth canonical checklist language.

## Five languages, nine working guide routes

| Language | Canonical guide | Additional entry point |
|---|---|---|
| English | [Build a reviewable evidence pack](https://ziontechgroup.com/apps/field-service-evidence-guide.html#evidence-pack) | Same canonical entry |
| Português | [Monte um pacote de evidências para revisão](https://ziontechgroup.com/apps/field-service-evidence-guide.pt-br.html#evidence-pack) | [Português — alias](https://ziontechgroup.com/pt/apps/field-service-evidence-guide.html#evidence-pack) |
| Español | [Prepare un paquete de evidencias revisable](https://ziontechgroup.com/apps/field-service-evidence-guide.es.html#evidence-pack) | [Español — alias](https://ziontechgroup.com/es/apps/field-service-evidence-guide.html#evidence-pack) |
| Français | [Constituez un dossier de preuves vérifiable](https://ziontechgroup.com/apps/field-service-evidence-guide.fr.html#evidence-pack) | [Français — alias](https://ziontechgroup.com/fr/apps/field-service-evidence-guide.html#evidence-pack) |
| Deutsch | [Erstellen Sie ein prüfbares Nachweispaket](https://ziontechgroup.com/apps/field-service-evidence-guide.de.html#evidence-pack) | [Deutsch — alias](https://ziontechgroup.com/de/apps/field-service-evidence-guide.html#evidence-pack) |

The guides connect [supplier quote evidence](https://ziontechgroup.com/apps/supplier-quote-evidence-workbench.html), [SLA](https://ziontechgroup.com/sla-calculator/), [ROI](https://ziontechgroup.com/roi-calc/), [pilot planning](https://ziontechgroup.com/automation-pilot-planner/), [Smart Hands planning](https://ziontechgroup.com/apps/field-services-smart-hands-playbook.html), [free Discovery](https://ziontechgroup.com/discovery/) and the [network map](https://ziontechgroup.com/apps/network.html). Tools retain their published language and limitations. No booking, purchase or dispatch is authorized by a checklist.

## Implementation and release evidence

The order-only repair and regression gate were already committed by another session in [9d434d7](https://github.com/Zion-support/zion-support.github.io/commit/9d434d79dff773028a741a3847c1073bc96d92e3). The current [regression checker](https://github.com/Zion-support/zion-support.github.io/blob/2274991ce0bd14ea552bc4113f98e26e263dec02/scripts/test-field-evidence-alias-integrity.cjs) also validates exact canonical, hreflang and language-switch targets. This continuation reviewed and retained that work; no duplicate website code commit, manual deployment or rerun was made.

[Simple Static Deploy 38020428184](https://github.com/Zion-support/zion-support.github.io/actions/runs/38020428184) completed SUCCESS at 03:27 UTC on 10 October 2026. After deployment, fresh no-cache HTTPS checks passed all nine guide routes: correct document language, canonical target, six alternates, switcher destinations, one six-item checklist, tools anchor and read-only HTML. The four alias/canonical checklist sections matched exactly. [Deployed manifest](https://ziontechgroup.com/apps/field-evidence-alias-integrity.json) contains release `field-alias-integrity-2026-10-10-v2`.

Offline aliases are byte-equal to canonical guides at the alias-generation stage. Later additive renderers can modify canonical pages, so live checks compare the translated checklist sections and metadata rather than claiming whole-document byte equality after all rendering.

## Bounded route audit, not whole-network certification

167 immediate `public/apps` HTML source routes at SHA `2274991ce0bd14ea552bc4113f98e26e263dec02` were fetched read-only. All returned final HTTP 200 after redirects. Declared languages: en 147, pt-BR 8, es 4, fr 4, de 4. These declarations do not prove body translation quality.

12 routes had the exact policy metadata keys en/pt-BR/es/fr/de/x-default; 155 lacked the full exact set. This does NOT prove translated variants are absent. Forty lacked a canonical tag; one lacked an H1. All had internal navigation. The graph contained 1,193 links to other destinations in the same scanned set, including self-links. Every other outgoing destination was not requested.

[Machine-readable bounded summary](PUBLIC-APPS-AUDIT-2026-10-10.json) · [Download the full CSV and link graph](https://backend.composio.dev/api/v3/sl/Ba4fUxbflx).

[TRANSLATIONS-STATUS.md](TRANSLATIONS-STATUS.md) remains the single coverage authority; [TRANSLATIONS.md](TRANSLATIONS.md) defines policy. Generated/prefix-language routes, other directories, subdomains and per-repository apps are excluded from this source-route count. Interactive functionality and human translation review remain separate gates.

Next: inspect the actual translated bodies and navigation of the content hub and selected Discovery journey pages, then repair canonicals only against verified real production URLs. Preserve forms, delivery recipients, paid-plan links, approval gates and concurrent work.
