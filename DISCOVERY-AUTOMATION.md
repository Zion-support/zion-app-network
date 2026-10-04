# Discovery Automation — How results reach the client and commercial@ziontechgroup.com

Goal: **the moment a client submits the questionnaire, both the client and our commercial department receive the discovery results.**

## Architecture (always online, zero backend)
1. **Questionnaire page**: `zion-network/discovery/index.html` → served at https://ziontechgroup.com/discovery/
2. **Primary delivery**: on submit, the page POSTs JSON to `https://formsubmit.co/ajax/commercial@ziontechgroup.com` with:
   - `_subject`: "New AI Discovery submission — <company>"
   - `_cc`: the client's work email (so the client receives the same results instantly)
   - all answers: name, email, company, industry, size, challenge, interest(s), timeline, plus the generated app recommendations
3. **On-page instant report**: the page immediately renders the personalized recommendations client-side (no network dependency), so the user sees results even before the email arrives.
4. **Fallback**: a `mailto:commercial@ziontechgroup.com?cc=<client>` link pre-filled with the full report is shown after submission — guarantees a copy even if the fetch is blocked by a corporate firewall/ad-blocker.

## Guarantees
- **Always online**: static hosting (GitHub Pages), no server, no database.
- **Always free**: FormSubmit free tier; no paid dependency.
- **No lead loss**: dual-channel delivery (FormSubmit email + mailto fallback + on-page report).

## Multi-select fix (Oct 4, 2026)
The interest field is a multi-select; the script now uses `FormData.getAll('interest')` so **all** selected interests are emailed and used for recommendations (previously only the first was captured).

## Monitoring
- Submissions land in the commercial@ziontechgroup.com inbox with subject "New AI Discovery submission".
- Weekly: confirm a test submission round-trips to both inboxes.

© 2026 Zion Tech Group