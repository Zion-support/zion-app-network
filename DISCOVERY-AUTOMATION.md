# Discovery Automation — source-grounded delivery runbook

Reviewed: 7 October 2026. Discovery remains free, online and self-service.

## Canonical source and route
- Public questionnaire: https://ziontechgroup.com/discovery/
- Repository: https://github.com/Zion-support/zion-support.github.io
- Source: `discovery/index.html`; deployment copy: `public/discovery/index.html`.
- Both copies had blob SHA `614a6d264ba30d87734ad3402f517490b707dc5d` at review. Keep them synchronized; verify the actual deployment source before changing either.

## Captured fields
Name, email, company, industry, process, hours band, systems, 90-day goal and timeline. There is no `interest` multi-select in this reviewed questionnaire. UTM attribution is bounded; only the page origin/path and referrer origin are forwarded, not private query strings/fragments.

## Report generation
The report is generated in the browser before email acceptance is awaited. It includes an indicative readiness score, selected process, recommended app links, baseline/owner/stop-rule guidance and an illustrative capacity-value scenario. Hour bands map to 15/50/140/260 hours; the scenario uses US$45/hour and 40% potentially automatable. These are assumptions, not measured savings, an audit, a quote or implementation approval. This 40% automation assumption is separate from Zion's commercial 40% COST markup.

## Email delivery
The browser POSTs JSON to `https://formsubmit.co/ajax/commercial@ziontechgroup.com`. Commercial is the primary destination; `_cc` includes the submitted client email and `carlos@ziontechgroup.com`, deduplicated against Commercial; `_replyto` is the submitted client email. The payload includes the same full report, bounded answers and attribution, `event: discovery_submit`, and the report version.

A successful HTTP response AND provider `success: true` means accepted for processing, NOT confirmed inbox delivery. Provider activation, availability, deliverability and recipient inbox rules can prevent delivery. No end-to-end receipt was verified by this audit; do not claim a guaranteed immediate email or zero lead loss.

## Recovery and duplicate controls
- Immediate on-screen report plus copy/download (.txt) remain available even when email fails.
- Manual mailto fallback opens a prefilled draft; it does NOT send automatically or guarantee a copy.
- Pending-submit guard disables concurrent submissions.
- Identical accepted answers are suppressed only within the current page session; this is not cross-session/server idempotency.
- Timeout: 15 seconds. A timed-out request may already have been accepted. No automatic retry; check receipts before resubmitting.
- Form validation, textContent rendering and bounded input reduce injection risk; do not submit credentials or confidential client/site data.

## Commercial and operational gates
Free Discovery creates no purchase, paid engagement, supplier reservation, dispatch or client PO. Paid work requires confirmed all-in cost, minimum 40% COST markup, separately explained applicable taxes/import charges, client written confirmation and a PO before commitment. Optional existing paid offers are separate from Discovery.

## Verification and monitoring
1. Check public route, source/deployed copies, report generation, navigation, timeout/error UI and duplicate guards without sending mail.
2. Obtain specific approval for an end-to-end test, including approved test identity and every To/CC recipient. A real submission sends email to Commercial, the test email and Carlos.
3. Verify actual receipts in both client and Commercial inboxes; record timestamp/message evidence. Provider acceptance alone is insufficient.
4. Review failures and duplicates in the existing monitoring lane before adding an automation. Never promise continuous monitoring without a configured verified job.

## Known evidence limits
This review read source and cached public page extraction. It did not verify HTTP uptime, dynamic live execution, provider activation or inbox receipt. Offline tests are separate from live delivery tests.
