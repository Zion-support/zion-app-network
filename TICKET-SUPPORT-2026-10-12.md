# Ticket support — five-language repair release

Release: `ticket-support-2026-10-12-v1`. [Multilingual hub catalog](https://ziontechgroup.com/zion-app-network/ticket-support.html).

[Website source](https://github.com/Zion-support/zion-support.github.io/commit/9ef42ce819cdca443e3c71cea52802ffc3c61607) changes exactly three files: the standalone artifact renderer, guarded entrypoint and narrow workflow integration. [Deployment status](https://github.com/Zion-support/zion-support.github.io/actions/runs/38187927176) was in progress when this source record was authored; source publication is not a live-verification claim. Final acceptance will be recorded separately after fresh checks.

## Intended publication matrix

| Locale | Ticket triage | SLA review | Homepage |
|---|---|---|---|
| en | [/ai-ticket-triage/](https://ziontechgroup.com/ai-ticket-triage/) | [/ai-ticket-sentinel/](https://ziontechgroup.com/ai-ticket-sentinel/) | [/en/#ticket-support](https://ziontechgroup.com/en/#ticket-support) |
| pt-BR | [/pt/ai-ticket-triage/](https://ziontechgroup.com/pt/ai-ticket-triage/) | [/pt/ai-ticket-sentinel/](https://ziontechgroup.com/pt/ai-ticket-sentinel/) | [/#ticket-support](https://ziontechgroup.com/#ticket-support) |
| es | [/es/ai-ticket-triage/](https://ziontechgroup.com/es/ai-ticket-triage/) | [/es/ai-ticket-sentinel/](https://ziontechgroup.com/es/ai-ticket-sentinel/) | [/es/#ticket-support](https://ziontechgroup.com/es/#ticket-support) |
| fr | [/fr/ai-ticket-triage/](https://ziontechgroup.com/fr/ai-ticket-triage/) | [/fr/ai-ticket-sentinel/](https://ziontechgroup.com/fr/ai-ticket-sentinel/) | [/fr/#ticket-support](https://ziontechgroup.com/fr/#ticket-support) |
| de | [/de/ai-ticket-triage/](https://ziontechgroup.com/de/ai-ticket-triage/) | [/de/ai-ticket-sentinel/](https://ziontechgroup.com/de/ai-ticket-sentinel/) | [/de/#ticket-support](https://ziontechgroup.com/de/#ticket-support) |

## Capabilities and migration

- Transparent local keyword rules, not semantic machine learning or incident verification.
- Manual elapsed-UTC SLA snapshot, not continuous monitoring or contractual determination.
- No network submission, persistence, model inference, email or ITSM update in either generated tool.
- Human review of impact, written source evidence, ownership and agreed service policy remains required.
- UTC timestamps now require `YYYY-MM-DDTHH:mm:ssZ` or ISO milliseconds with `Z`; ambiguous local timestamps are rejected. Business-hour calendars, pauses and contract exceptions are not modeled.
- SLA durations must be finite, greater than zero and at most 8760 hours. Priorities must be exactly P1–P4. Invalid rows and dates show localized errors instead of being silently discarded.
- Blank or changed input clears stale output. Fictional examples contain no customer data.

## Prepublication evidence

70 offline assertions passed: keyword cases, blank/size limits, strict priority/date validation, zero/negative/nonfinite SLA durations, breach/risk thresholds, all ten localized DOM examples/error states, idempotent rendering, outside-promotion homepage preservation and missing-destination fail-before-write. Fresh production fixtures rendered ten page editions with six alternates each and five homepage promotions. Wrapper pins the two original source blob hashes to prevent overwriting unnoticed source changes.

The source `public/ai-ticket-*` pages remain historical English inputs; production is the final artifact renderer. Do not infer production defects or missing translations solely from those raw source files. Generated coverage updates only the two corresponding groups in `/apps/network-publication-coverage.json`. Existing supplier, field, Discovery and other releases are retained. Historical `TRANSLATIONS-STATUS.md` is not rewritten by this source record.

Full-network translations, native editorial review, Safari/screen-reader certification and paired Discovery inbox receipt remain incomplete. No real tickets, customer messages, purchases or dispatch occurred.
