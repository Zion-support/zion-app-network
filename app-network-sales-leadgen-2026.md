# App Network — New Concept App: AI Sales & Lead-Gen Specialist

**Cluster:** Sales & Lead Generation · **Batch:** 123 (2026-11-14) · **Status:** Published (5-language HTML) + repo in GitHub  
**Owner:** Zion Tech Group · **Lead:** Apollo specialist + SalesOps

## 1. Purpose

A free, always-online **AI Sales & Lead-Gen Specialist** hub: the content and discovery layer for B2B lead
enrichment, prospecting, and outreach. It scans the company's own email history and external sources to surface
qualified leads by location, enriches them (contact + buying signals), and packages them for the agent marketplace
(Batch 117) and the implementation vault (Batch 121). This is the "search emails for leads, contact them offering
services, extract contacts to CRM/HubSpot" workflow, made searchable and actionable.

## 2. Why now (market signal)

- Enterprise teams use AI agents for B2B sales: lead scoring, email personalization, sequence optimization, outreach,
  contact enrichment (Apollo, Clay, ZoomInfo, Outreach, Lamyarket, HubSpot Breeze, Regie.ai).
- The highest-value data is the company's own email thread history (prior work in a location, prior contacts, prior
  pricing). Combining that with external prospecting data multiplies qualified opportunities.
- This cluster is the lead-engineering pipeline: intake (email search + enrichment) → scoring → CRM write-back
  (HubSpot) → outreach → implementation (Batch 121).

## 3. Core features

1. **Email-thread lead scanner** — free intake that scans all labels (inbox + label folders, oldest to newest) for
   service requests, FE/technician inquiries, and mentions of location, then ranks them by commercial value.
2. **Lead enrichment** — adds contact + buying signals: location, company, prior-work history, pricing range.
3. **CRM write-back** — drafts a HubSpot contact record (name, email, lead source, score), so the Commercial team
   can review and push to the CRM.
4. **Quoted-price teaser** — hides markup; surfaces only the "client-facing" price range for outreach.
5. **Outreach draft** — writes a personalised cold-email draft (with commercial@ziontechgroup.com c/c) + a follow-up
   reminder schedule.
6. **Discovery handoff** → agent marketplace (Batch 117) + implementation vault (Batch 121).

## 4. Pricing & markup (Zion)

- **Lead-gen specialist hub:** free, always online (scan + enrichment + CRM draft).
- **CRM write-back / outreach send:** priced per engagement, **minimum 40% markup over all-in cost for Zion**.
- No order or send begins without client written confirmation + PO + Zion release.

## 5. Discovery & pitch

- Free Discovery questionnaire → lead-gen specialist hub → your ranked lead list + enriched contacts + outreach draft → paid implementation.
- Pitch: "Find every lead we've already worked with — in your area — and turn them into booked work, without a single cold call."

## 6. Repo & links

- Repo: `zion-sales-leadgen` (GitHub, `Zion-support` org).
- Live app: `https://ziontechgroup.com/sales-leadgen/` (awaiting sites enable).
- App-network hub page: generated 5-language HTML in `zion-app-network/app/`.

---

**Interlinks:** link `app-network-sales-leadgen-2026` ↔ `app-network-agent-marketplace-2026` (enriched leads),
↔ `app-network-implementation-vault-2026` (CRM + outreach implementation).
