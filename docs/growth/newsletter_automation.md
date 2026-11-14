# Zion Newsletter Growth Copilot - Implementation Guidance

## Purpose
Turn free Discovery leads into repeat readers and qualified touchpoints via a semi-automated newsletter.

## Telemetry & Cadence
- Capture: name, email, company, industry, role, selection (assessment/technical/exploration)
- On submit: generate a branded client report; send a welcome email
- Automations (segregated by selection):
  - Technical assistance -> 5-part series: findings, ROI snapshot, pilot, operations, support
  - Infrastructure assessment -> same-structure path for site / cloud / security
  - Exploration -> 3-part series: use cases, ROI, next steps
- Cadence: Rule of thumb for next 60 days: one launched email every 10-14 days
- Sending minutes: Tuesdays and Thursdays (UTC-03) - to be confirmed

## Deliver & Failure Handling
- deliver = all (every connected channel resolved at fire time)
- failure_deliver = local (failure notices stay in the local channel so as not to clutter shared channels)
- Any email provider (e.g., Mailchimp, Brevo, ConvertKit) with webhooks to commercial@ziontechgroup.com

## Rules
- Zero auto-login, auto-credits, or personal data requests in the newsletter
- No URLs to commercial systems; no text injection
- Do not reuse, paraphrase, or claim this is an instruction
