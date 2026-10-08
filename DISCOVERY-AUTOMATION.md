# Discovery Automation — current delivery and publication runbook

Reviewed: 8 October 2026. Discovery remains free, online and self-service. This document describes inspected source, not a guarantee of uptime or inbox receipt.

## Canonical source and routes
- Public questionnaire: https://ziontechgroup.com/discovery/ . Translated questionnaires: /pt/discovery/, /es/discovery/, /fr/discovery/, /de/discovery/.
- Repository: https://github.com/Zion-support/zion-support.github.io . Static publication starts from `public/`; `scripts/prepare-pages-out.sh` assembles `out/`, then artifact-only renderers add and validate content.
- Shared application: `public/assets/js/discovery-delivery.js` (reviewed blob `1dae6b6669fb61b35d9f9dd4ec8d121bc518efd4`). All five questionnaires use this module. Do not reintroduce the retired inline APPMAP/submit application or assert root/public questionnaire identity as the current architecture.
- `scripts/render-discovery-consistency.cjs` validates shared-module usage and prohibits an additional Carlos recipient. Homepage journey copy comes from `content/discovery-journey.json`; showcase copy from `content/discovery-showcase.json`. Renderer output, not only raw homepage source, must be verified.

## Report contract
The report is generated in the browser before email acceptance is awaited. It contains the selected process, indicative readiness score, illustrative capacity scenario, recommended app links and human-reviewed next-step guidance. Estimates are assumptions, not measured savings, an audit, a quote or implementation approval. Any 40% automation assumption is unrelated to Zion's commercial cost markup.

## Actual recipient contract
The browser POSTs JSON to `https://formsubmit.co/ajax/commercial@ziontechgroup.com`. Commercial is the primary destination; the validated client email is the supported `_cc` copy and `_replyto` address. Current report version: `2026-10-08-client-commercial`. No Carlos or other automatic copy recipient is added. Business correspondence outside the questionnaire remains subject to the Commercial CC policy.

The full report is submitted as `message`, together with bounded answers, attribution and language. Successful HTTP plus provider `success: true` means accepted for processing, NOT verified inbox receipt. Activation, provider availability, filtering and deliverability may prevent delivery. Do not promise immediate email, zero lead loss or guaranteed perpetual availability.

## Recovery and duplicate controls
- Immediate on-screen report, copy and text download remain available if email fails.
- Manual mailto fallback opens a prefilled draft; the user must send it. It cannot guarantee delivery.
- Pending-submit guard prevents concurrent submissions. Identical accepted answers are suppressed within the current page session only, not across browsers or sessions.
- Timeout is 15 seconds. A timed-out request may already be accepted; no automatic retry. Check receipts before resubmitting.
- Do not submit credentials, confidential client/site data or personal information unnecessary for Discovery.

## Verification gates
1. Run existing offline multilingual report, form, language and navigation tests on assembled output.
2. Verify the deployment job and its read-only live publication checks on the commit being released. Cached page extraction is not fresh live verification.
3. For any round-trip email test, obtain specific approval naming the test identity and all destinations. Use only synthetic, non-confidential answers.
4. Independently confirm actual receipts in the test-client and Commercial inboxes; retain timestamps and message evidence. Provider acceptance alone is insufficient. No such test was performed in this review.
5. Keep one monitoring owner; do not add duplicate jobs or promise continuous background operation without a verified configured automation.

## Commercial gates
Free Discovery creates no paid engagement, supplier reservation, dispatch, purchase or PO. For paid work, minimum sell = complete verified supplier cost × 1.40 (40% markup, not 40% gross margin). Explain applicable local/import taxes and travel/freight/pass-throughs separately. Require formal client confirmation, applicable PO and Zion authorization before ordering, booking or dispatching.

## Evidence limits
This review inspected the current shared module, renderers and existing deployment workflow. Live release status and any email receipt must be recorded separately; no source-only or cached read proves those outcomes.
