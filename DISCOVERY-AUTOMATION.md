# Discovery Automation Spec — Questionnaire → Instant Results Email

Goal: every https://ziontechgroup.com/discovery/ submission instantly emails results to the client AND commercial@ziontechgroup.com.

## Flow
1. Client submits discovery questionnaire (12 questions, ~5 min)
2. Backend webhook scores answers and renders the personalized report (HTML + PDF)
3. Email 1 → client address: report + links to matched apps (ziontechgroup.com/<app>/)
4. Email 2 → commercial@ziontechgroup.com: full answers, lead score, matched apps, report link
5. Lead row created in Notion pipeline (status: New Discovery)
6. Retries on failure with 60s SLA; ops alert after 3 failed retries

## Requirements
- Transactional email provider with template: discovery-results-v2
- Idempotency key = submission UUID (no duplicate emails)
- LGPD/GDPR consent checkbox captured and stored with the submission

## Status
Spec published 2026-10-04 in zion-app-network hub. Implementation tracked in Notion CEO Ops.
