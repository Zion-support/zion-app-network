# 🌍 Translations Policy & Status (Oct 8, 2026)

## Supported languages (match ziontechgroup.com hreflang set)
`en` (default), `pt-BR`, `es`, `fr`, `de` (+ `x-default` → en)

## Rules
1. Every public showcase/spotlight page ships in all 5 languages at release time.
2. Naming: hub `app-network-batchNN-<date>[-pt|-es|-fr|-de].html`; live site `public/apps/october-2026-batchNN[.pt-br|.es|.fr|.de].html` (site convention).
3. Each variant sets `<html lang="…">` and carries hreflang alternates to all 5 variants.
4. App product names stay in English; value props, CTAs, Discovery block and navigation are translated.
5. Language switcher nav on top of every page: 🌐 EN · PT · ES · FR · DE.
6. **Deploy rule:** ziontechgroup.com publishes ONLY from `public/**` (Simple Static Deploy workflow, push trigger + cron */5min). Root-level commits never go live.

## Status
| Content | en | pt-BR | es | fr | de |
|---|---|---|---|---|---|
| Batch 98 Sports showcase (hub + live /apps/october-2026-batch128-sports-venue*) | ✅ | ✅ | ✅ | ✅ | ✅ |
| Batch 100 Manufacturing showcase (/apps/october-2026-batch100*) | ✅ | ✅ | ✅ | ✅ | ✅ |
| Batches 70–97, 99, 101+ showcases | ✅ | ⏳ backlog | ⏳ backlog | ⏳ backlog | ⏳ backlog |

Backlog: translate remaining batch showcases using [DESIGN_PATTERN.md](DESIGN_PATTERN.md) as the canonical layout; add language switcher to EN originals when touched.

© 2026 Zion Tech Group