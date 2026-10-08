#!/usr/bin/env python3
"""Idempotent, additive catalog synchronization for the approved communications suite."""
from pathlib import Path

APPS = [('Smart Call Routing AI', 'smart-call-routing-ai'), ('Call Intelligence Hub', 'call-intelligence-hub'), ('Voicemail Triage AI', 'voicemail-triage-ai'), ('Meeting Intelligence AI', 'meeting-intelligence-ai')]
GUIDE = 'https://ziontechgroup.com/apps/discovery-showcase.html'
for name in ['CATALOG.md', 'APPS_INDEX.md']:
    path = Path(name)
    original = path.read_text(encoding='utf-8')
    missing = [(title, slug) for title, slug in APPS if f'https://github.com/Zion-support/{slug}' not in original]
    if missing:
        section = '\n## Communications suite — consolidated 2026-10-08\n\n'
        section += 'Free [Discovery](https://ziontechgroup.com/discovery/) provides an instant on-screen report and submits it for email delivery to the client and commercial@ziontechgroup.com. Inbox delivery remains unverified.\n\n'
        section += '| App | Live page | Source |\n|---|---|---|\n'
        for title, slug in missing:
            section += f'| {title} | [Explore](https://ziontechgroup.com/{slug}/) | [GitHub](https://github.com/Zion-support/{slug}) |\n'
        section += '\nDiscovery guides: [EN]('+GUIDE+') · [PT-BR](https://ziontechgroup.com/apps/discovery-showcase-pt.html) · [ES](https://ziontechgroup.com/apps/discovery-showcase-es.html) · [FR](https://ziontechgroup.com/apps/discovery-showcase-fr.html) · [DE](https://ziontechgroup.com/apps/discovery-showcase-de.html).\n\n'
        section += 'Related repositories link back through NETWORK.md. This additive update does not establish a verified network-wide app count.\n'
        path.write_text(original.rstrip()+'\n'+section, encoding='utf-8')
        final = path.read_text(encoding='utf-8')
        assert all(f'https://github.com/Zion-support/{slug}' in final for _,slug in APPS)

path = Path('index.html')
original = path.read_text(encoding='utf-8')
replacements = {
 'Answer 12 questions': 'Answer 8 questions',
 '<strong>instantly by email</strong>': '<strong>instantly on-screen</strong>',
 '<li><strong>Instant report</strong> — results emailed to you the moment you finish</li>': '<li><strong>Instant report</strong> — see your result on-screen immediately; copy or download it for your records</li>',
 '<li><strong>Same-day expert follow-up</strong> — our commercial team receives your results simultaneously and reaches out with a tailored plan</li>': '<li><strong>Email submission</strong> — the same report is submitted for email delivery to you and Commercial; provider acceptance does not confirm inbox delivery</li>',
 '<li><strong>Matched to 800+ apps</strong> — your answers are mapped to the exact Zion AI apps that pay for themselves fastest</li>': '<li><strong>Relevant app suggestions</strong> — explore apps for your selected process; validate suitability, permissions and expected value before implementation</li>',
 'https://ziontechgroup.com/zion-app-network/app/discovery-showcase.html': GUIDE,
}
updated = original
for before, after in replacements.items():
    updated = updated.replace(before, after)
if 'id="communications-suite"' not in updated:
    section = '<section id="communications-suite"><h2>Voice and communications: choose a practical workflow</h2><p>Start with the free Discovery report, choose one workflow, confirm data permissions, and define a human reviewer and a baseline before implementation.</p><ul>'
    for title, slug in APPS:
        section += f'<li><a href="https://ziontechgroup.com/{slug}/">{title}</a> · <a href="https://github.com/Zion-support/{slug}">Source</a></li>'
    section += '</ul><p><a href="'+GUIDE+'">Read the five-language Discovery guide</a> · <a href="https://github.com/Zion-support/zion-app-network/blob/main/CATALOG.md">Master catalog</a> · <a href="https://github.com/Zion-support/zion-app-network/blob/main/APPS_INDEX.md">Master index</a></p></section>\n'
    assert '<footer>' in updated, 'Stop: expected hub footer not found'
    updated = updated.replace('<footer>', section+'<footer>', 1)
assert 'Answer 12 questions' not in updated
assert '<strong>instantly by email</strong>' not in updated
assert 'Same-day expert follow-up' not in updated
assert 'pay for themselves fastest' not in updated
path.write_text(updated, encoding='utf-8')
print('Communications catalog and hub checks passed; existing entries preserved.')
