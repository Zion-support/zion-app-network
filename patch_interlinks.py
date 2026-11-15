import io

path = '/Users/miami2/.hermes/profiles/agent-finops-ops/cache/apphub/INTERLINKS-MASTER.md'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

anchor = '---\n© 2026 Zion Tech Group · https://ziontechgroup.com/'
print('anchor found:', anchor in content)

add = '''## 📣 Batch 123 — AI Sales & Lead-Gen Specialist (2026-11-14)

New concept app — free, always-online lead-engineering pipeline: scans all email labels (inbox + folders, oldest to
newest) for service requests & technician inquiries, enriches contacts (location, company, prior work, pricing),
drafts CRM + personalised outreach, and hands off to the agent marketplace and implementation vault — for FE's
& technicians.

- [zion-sales-leadgen](https://github.com/Zion-support/zion-sales-leadgen) ↔
  [app-network-sales-leadgen-2026.html](https://ziontechgroup.com/zion-app-network/app/app-network-sales-leadgen-2026.html)
Showcase (5 languages): https://ziontechgroup.com/zion-app-network/app/app-network-sales-leadgen-2026.html
(+ -pt/-es/-fr/-de). Interlinks: [INTERLINKS-sales-leadgen-2026.md](INTERLINKS-sales-leadgen-2026.md).

## 🌐 Batch 124 — Multilingual Localization Hub (2026-11-14)

New concept app — the living standard for the 5-language network (EN/PT-BR/ES/FR/DE): hreflang best practice,
per-language content matrix, translation toolkit, per-language SEO, and a cultural-localization checklist.

- [zion-multilingual-localization](https://github.com/Zion-support/zion-multilingual-localization) ↔
  [app-network-multilingual-localization-2026.html](https://ziontechgroup.com/zion-app-network/app/app-network-multilingual-localization-2026.html)
Showcase (5 languages): https://ziontechgroup.com/zion-app-network/app/app-network-multilingual-localization-2026.html
(+ -pt/-es/-fr/-de). Interlinks: [INTERLINKS-multilingual-localization-2026.md](INTERLINKS-multilingual-localization-2026.md).

---

© 2026 Zion Tech Group · https://ziontechgroup.com/'''

if anchor in content:
    content = content.replace(anchor, add, 1)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('patched OK')
else:
    print('anchor NOT found; aborting (no change)')
