# Marketing Automation Architecture for Zion

## Purpose
Architecture for marketing automation: lead scoring, nurture sequences, churn prevention, upsell sequences, and attribution.

## Architecture Layers
1. **CRM + Marketing Automation**: HubSpot, Salesforce, or open-source equivalent
2. **Product Analytics + In-App Messaging**: Mixpanel, Amplitude, Customer.io, Braze
3. **Email Automation**: Built-in CRM or Customer.io/Braze for complex flows
4. **Attribution & Funnel Analytics**: Tools that show which channels drive pipeline

## Core Workflows
### A. Trial Activation Automation
- Trigger: signup event
- Action: immediate activation email
- Follow-up: feature-adoption nudges triggered by product usage
- Stop: contact replies, books meeting, or enters sales process

### B. Churn Risk Alert
- Trigger: usage decline or support ticket spike
- Action: CS task creation + renewal prep sequence
- Owner: account owner notified

### C. Expansion Trigger
- Condition: seat limit 80% utilised or enterprise feature on standard plan
- Action: upgrade recommendation from account owner
- Flow: targeted upgrade email, not generic upsell

### D. Dunning Sequence
- Trigger: payment failure
- Action: automated recovery emails
- Priority: highest ROI automation, commonly skipped

## Metrics to Track
- Cost per verified contact
- Qualified replies per seat
- Meeting acceptance rate
- Meeting show rate
- Pipeline sourced or influenced
- Conversion rate by lifecycle stage and cohort
- Revenue per sequence

## Priority Order for Launch
1. If trial-to-paid is the problem: start with activation automation
2. If churn is the problem: start with churn-risk alert
3. If acquisition is the bottleneck: start with MQL routing
4. Build one workflow at a time; measure 4-6 weeks; add next

