# App Network — New Concept App: AI Voice & Missed-Call Automation (Field Services)

**Cluster:** Operations / Field Services · **Batch:** 115 (2026-11-14) · **Status:** Published (5-language HTML) + repo in GitHub  
**Owner:** Zion Tech Group · **Lead:** Commercial + SalesOps

## 1. Purpose

Turn every missed and unanswered phone call from field-service, trades and local businesses into a booked job.
A wake-on-call voice agent answers the phone, captures the site address, describes the job, and books it into
the dispatcher queue — 24/7, in the client's own language, with no raising of hands.

## 2. Why now (market signal)

- 79% of consumers still call for emergency / quoted service (source: Yelp, 2026 industry data) and the average
  local-service business misses 38% of after-hours calls (source: industry surveys).
- The MVP build is a voice-agent + telephony integration — ~1–2 weeks, cheap to demo, high perceived value.
- This is the single highest-intent, highest-frequency touch a local service business has with a lead.

## 3. Target clients (FE's & technicians — top priority)

- Electricians, plumbers, HVAC, locksmiths, landscapers, general contractors, tow services.
- Small/micro local businesses with 1–5 field staff, little CRM use, phones on the shop floor + call-out.
- Already validated with H&F Support Requirement threads (SolidTech, Dublin/Tech Domain, Datech) — call answering
  and dispatch are exactly the friction they asked us to fix.

## 4. Core features

1. **Wake-on-call** — answers the phone, asks for the site address and job summary, asks for best callback time.
2. **Language auto-detect** — English / Português / Español / Français / Deutsch (matches the 5-language network standard).
3. **Book-in** — writes the job into a dispatcher queue / CRM (Zion CRM / HubSpot) with site count, postcode and SLA.
4. **Handoff** — notifies the on-duty technician, flags the job as "unassigned after 60s".
5. **Live status** — callers get a one-touch "how am I doing" and booking confirmation (SMS or WhatsApp for field techs).
6. **Analytics** — missed-call rate, conversion per call, average answer time, booked vs quoted by operator.

## 5. Pricing & markup (Zion)

- This is a **service-led** offer with a **minimum 40% markup over all-in cost** for Zion (CEO rule).
- Suggested commercial: 30-day pilot = 4 hrs/week voice agent @ rate (confirmed with provider) + 15% runoff.
- Final quote is shared only after client confirms need and we have a confirmed provider rate.

## 6. Discovery & pitch

- Free Discovery questionnaire (same as the governance cluster) → personalized AI-discovery report emailed to the
  client and commercial@ziontechgroup.com.
- Pitch: "Every missed call is a booked job you didn't get. Coin the campaign, set up the agent, we handle the rest."
- Discovery results + RFQ body + Stripe links for self-serve pilots.

## 7. Repo & links

- Repo: `zion-voice-field-automation` (GitHub, `Zion-support` org).
- Live app: `https://ziontechgroup.com/voice-field-automation/` (awaiting sites enable).
- App-network hub page: generated 5-language HTML in `zion-app-network/app/`.

## 8. Related apps in the network

- AI readiness assessment / AI governance dashboard (use voice AI as the delivery channel)
- Compliance evidence collector (call logs and consent records are evidence)
- Prompt shield (runtime firewall for the voice agent edge)

---

**Interlinks:** link `app-network-voice-field-2026` ↔ `app-network-governance-trust-2026` (via discovery CTA),
↔ `app-network-implementation-vault-2026` (deployment steps), ↔ `app-network-geotopics-2026` (SEO/geotargeting).
