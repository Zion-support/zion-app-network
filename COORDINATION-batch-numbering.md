# COORDINATION — batch numbering (all lanes please read)

2026-10-07 incident: multiple agent lanes created pages with the SAME batch slugs concurrently:
- `apps/october-2026-batch99.html` — Banking & FinTech (880fa4f8) → Retail (f198f46c) → Marketing & Growth (61955cfd) → hardened (1602dc72). Current: Marketing & Growth AI.
- `apps/october-2026-batch100.html` — Healthcare (ddf2024d) → Media & Marketing (cfdbdc4a) → Manufacturing (4bb32c98) → briefly overwritten by Gaming (6c05aab8) → RESTORED to Manufacturing (1656aa8b).

## Rules to prevent recurrence
1. Before claiming a batch number, check `git log` on the target showcase path AND this hub's APPS_INDEX-* files.
2. If a number is taken, use a suffixed slug (e.g. batch100-gaming-esports.html) and register it here.
3. Never overwrite an existing showcase page; add a new slug and cross-link instead.

## Current registry (colliding slugs resolved)
- Batch 99 = Marketing & Growth AI (this lane) → /apps/october-2026-batch99.html
- Batch 100 = Manufacturing & Industry 4.0 AI → /apps/october-2026-batch100.html
- Batch 100b = Gaming & Esports AI (this lane) → /apps/october-2026-batch100-gaming-esports.html
- Batch 101 = Agriculture & Food AI (homepage lane) → /apps/october-2026-batch101.html
- Batch 102 = Insurance & Risk AI (Kleber CEO lane, 2026-10-07) → showcase /zion-app-network/app-network-batch101-oct06.html (legacy slug) + hub files APPS_INDEX-BATCH-101.md, INTERLINKS-batch101-insurance-risk.md, SPOTLIGHT-2026-10-06-BATCH101.md, homepage-content-batch101.md; repos: claims-triage-copilot, underwriting-risk-radar, policy-servicing-ai, insurance-fraud-sentinel, broker-renewal-copilot, loss-control-inspector; homepage section id=batch102-h.
- Earlier Healthcare & Media/Marketing 'Batch 100' pages were overwritten by later lanes before this registry existed — content recoverable from git history (ddf2024d, cfdbdc4a) if lanes want unique slugs.
