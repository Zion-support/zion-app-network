# Field guide alias integrity — verified 10 October 2026

## Release result
The four translated prefix aliases now contain the same six-record evidence checklist as the corresponding canonical guides. The order fix was already shipped in [9d434d7](https://github.com/Zion-support/zion-support.github.io/commit/9d434d79dff773028a741a3847c1073bc96d92e3); this continuation preserved that work instead of duplicating it.

New regression hardening in [2274991](https://github.com/Zion-support/zion-support.github.io/commit/2274991ce0bd14ea552bc4113f98e26e263dec02) checks exactly one canonical URL, the correct six alternate language targets, unique hreflang labels, all five language-switch destinations, the six checklist records and alias/canonical checklist equality. It is also invoked by the regular field evidence publication test. No guide text, homepages, forms, recipients or paid-service links were rewritten by this test-only patch.

[Deployment 38020428184](https://github.com/Zion-support/zion-support.github.io/actions/runs/38020428184) completed SUCCESS at 03:27:16 UTC. [Live guard manifest](https://ziontechgroup.com/apps/field-evidence-alias-integrity.json) contains release field-alias-integrity-2026-10-10-v2. Fresh read-only HTTPS tests passed all nine guide routes. Negative local fixtures correctly reject wrong canonical URLs, duplicate locales, incorrect alternate targets and wrong language buttons.

## Verification links
- [English guide](https://ziontechgroup.com/apps/field-service-evidence-guide.html#evidence-pack)
- [Português alias](https://ziontechgroup.com/pt/apps/field-service-evidence-guide.html#evidence-pack) · [canonical](https://ziontechgroup.com/apps/field-service-evidence-guide.pt-br.html#evidence-pack)
- [Español alias](https://ziontechgroup.com/es/apps/field-service-evidence-guide.html#evidence-pack) · [canonical](https://ziontechgroup.com/apps/field-service-evidence-guide.es.html#evidence-pack)
- [Français alias](https://ziontechgroup.com/fr/apps/field-service-evidence-guide.html#evidence-pack) · [canonical](https://ziontechgroup.com/apps/field-service-evidence-guide.fr.html#evidence-pack)
- [Deutsch alias](https://ziontechgroup.com/de/apps/field-service-evidence-guide.html#evidence-pack) · [canonical](https://ziontechgroup.com/apps/field-service-evidence-guide.de.html#evidence-pack)

Continue via [homepage](https://ziontechgroup.com/), [network map](https://ziontechgroup.com/apps/network.html), [free Discovery](https://ziontechgroup.com/discovery/), [supplier quote evidence](https://ziontechgroup.com/apps/supplier-quote-evidence-workbench.html), [SLA](https://ziontechgroup.com/sla-calculator/), [ROI](https://ziontechgroup.com/roi-calc/) and [pilot planning](https://ziontechgroup.com/automation-pilot-planner/). Linked tools retain their published language and capability; this note does not certify integrations or production readiness.

## Bounded production audit
[Download CSV and JSON results](https://backend.composio.dev/api/v3/sl/k8yhgKbISx).

Scope: all 167 HTML files listed directly in public/apps at commit 2274991; generated language-prefix pages, other routes and the separate hub are excluded. All 167 requested addresses returned HTTP 200. Declared HTML languages: en 147, pt-BR 8, es 4, fr 4, de 4. These declarations do not prove translated-body quality.

127 sampled pages declare a canonical; 30 declare at least one language alternate; 12 declare all five languages plus x-default. Missing metadata in this scope is not proof that translations are absent at another route. The sampled graph has 1,048 directed in-scope interlinks, of which 378 have reverse edges. This is a graph observation, not a requirement to make every edge reciprocal or proof that out-of-scope destinations work.

Use [TRANSLATIONS-STATUS.md](TRANSLATIONS-STATUS.md) as the single translation coverage authority and [TRANSLATIONS.md](TRANSLATIONS.md) for policy. Next: merge generated/prefix routes into inventory; inspect translated bodies and real capability; prioritize canonical/hreflang gaps; expand purposeful reciprocal navigation without adding duplicate homepage cards or colliding batch numbers.

Publication and metadata checks are not full browser interaction tests, supplier readiness, whole-network translation certification or email receipt proof. No forms submitted, emails sent, bookings, payments, purchases, dispatches or deletions in this release.
