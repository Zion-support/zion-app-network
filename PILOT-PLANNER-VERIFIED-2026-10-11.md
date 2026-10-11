# Pilot Planner — verified live publication

Release: `2026-10-11-pilot-planner-v1`.

**Live / Online / En línea / En ligne / Online.** Scope: this planner and its tested navigation, not the entire apps network.

## Publication evidence
- [Repair and additive release ac84dba](https://github.com/Zion-support/zion-support.github.io/commit/ac84dbaa856d88b201cb4c34ff9205b215dbb541).
- [Simple Static Deploy 38150741405](https://github.com/Zion-support/zion-support.github.io/actions/runs/38150741405): deploy job 114503500575 SUCCESS; deployment completed 2026-10-11 15:21:39 UTC. All existing live regression stages also passed, final job completed 15:21:46 UTC.
- Independent repository GET-only test completed 2026-10-11 15:21:54 UTC: **41/41** checks passed: five canonical planners with declared language/canonical/six alternates/usage/guide contracts; twenty same-language homepage/Discovery/Field Guide/learning-path promotions; ten related ROI/SLA language pages; four redirect aliases; publication manifest and shared stylesheet.
- [Durable GET-only test](https://github.com/Zion-support/zion-support.github.io/blob/main/scripts/test-pilot-planner-live.cjs).
- [Canonical route register](CATALOG-PILOT-PLANNER.md).

## Native browser outcome
Task `6bc02b53-cf3b-43f5-b57d-2973a6246647` completed. English retained the synthetic process, 100 hours/month baseline, QA owner, Test system, 20% less manual time metric and 5% error stop rule. All five time stages were generated in English and in default-input PT-BR/ES/FR/DE drafts. Translated usage/privacy instructions and language links were observed. English .txt download was generated and its contents read back. Clipboard access was blocked/timed out in this environment: do not claim native clipboard success. Missing/denied/success handlers passed the offline runtime suite.

[English interaction screenshot](https://cdn.browser-use.com/screenshots/6bc02b53-cf3b-43f5-b57d-2973a6246647/3.png) · [Portuguese draft](https://cdn.browser-use.com/screenshots/6bc02b53-cf3b-43f5-b57d-2973a6246647/9.png) · [Spanish draft](https://cdn.browser-use.com/screenshots/6bc02b53-cf3b-43f5-b57d-2973a6246647/11.png) · [French draft](https://cdn.browser-use.com/screenshots/6bc02b53-cf3b-43f5-b57d-2973a6246647/13.png) · [German draft](https://cdn.browser-use.com/screenshots/6bc02b53-cf3b-43f5-b57d-2973a6246647/15.png).

**Viewport correction:** the browser agent assigned `window.innerWidth` rather than changing the real viewport; document clientWidth remained 1497px. Neither 390px nor 1280px is a valid completed viewport test. Treat both requested real-width checks as OPEN, regardless of the agent's summarized 1280px-success claim. Screenshots prove rendering at the actual available desktop viewport only.

## Correction history
Initial replacement renderer collided with an existing API; activation 38150233568 failed before artifact upload. Original renderer blob 4f29af692043251af0c30dfdb8b5670714229ccc was restored exactly. The issue was introduced in this session and repaired, not a pre-existing defect. No partial failed-build release was published. Preserve the original /automation-pilot-planner/{en,es,fr,de}/ canonical routes and Portuguese root.

## QA boundaries and next session
Original five-language runtime QA, all-guide returns and translated usage/accessibility suites passed. Two clean fixtures preserved forms/runtime and consolidated promotions idempotently. Source restoration and new final compatibility gate passed the production pipeline. No network form submission, email, purchase, booking or implementation approval. Local drafts/downloads are not execution, measured savings or production certification.

Next: genuine 390px/1280px browser viewport QA; bounded source-aware route/language/capability/interlink reconciliation; separately inspect supplier-workbench cost logic before proposing its complete localization. Full-network translation/interlinks remain incomplete. Recover memory and refresh current HEAD before editing; raw public planner source is not the final artifact renderer output.
