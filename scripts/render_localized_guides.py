#!/usr/bin/env python3
"""Render maintained five-language guides without runtime dependencies."""
from __future__ import annotations
import argparse
import html
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://ziontechgroup.com'
LOCALES = ('en', 'pt', 'es', 'fr', 'de')
RELEASE = 'network-guides-2026-10-30-v1'
UI = json.loads((ROOT / '_data/guide-ui.json').read_text())

def esc(value):
    return html.escape(str(value), quote=True)

def route(guide, locale):
    suffix = '' if locale == 'en' else '-pt-br' if locale == 'pt' else '-' + locale
    return '/zion-app-network/' + guide['basePath'] + suffix + '.html'

def local_path(guide, locale):
    return route(guide, locale).removeprefix('/zion-app-network/')

def valid_href(value):
    parsed = urlparse(value)
    if value.startswith('/') and not value.startswith('//'):
        return value
    if parsed.scheme == 'https' and parsed.netloc in {'ziontechgroup.com', 'github.com'}:
        return value
    raise ValueError('Unapproved guide URL: ' + value)

def link(href, label, attrs=''):
    return f'<a href="{esc(valid_href(href))}"{attrs}>{esc(label)}</a>'

def load_guides():
    files = sorted((ROOT / '_data').glob('guide-*.json'))
    guides = [json.loads(f.read_text()) for f in files if f.name != 'guide-ui.json']
    for guide in guides:
        if set(guide['locales']) != set(LOCALES):
            raise ValueError('Incomplete locales: ' + guide['id'])
    return guides

def render(guide, locale, guides):
    c, u = guide['locales'][locale], UI[locale]
    prefix = '/' if locale == 'en' else '/' + locale + '/'
    home = '/' if locale == 'pt' else '/' + locale + '/'
    canonical = ORIGIN + route(guide, locale)
    alternates = '\n'.join(f'<link rel="alternate" hreflang="{UI[l]["lang"]}" href="{ORIGIN + route(guide,l)}">' for l in LOCALES)
    languages = ''.join(link(route(guide,l), UI[l]['name'], f' lang="{UI[l]["lang"]}" hreflang="{UI[l]["lang"]}"' + (' aria-current="page"' if l == locale else '')) for l in LOCALES)
    navigation = link(home,u['home']) + link(prefix+'apps/',u['catalog']) + link('/zion-app-network/directory-'+locale+'.html',u['directory']) + link(prefix+'discovery/',u['discovery'])
    toc = ''.join(f'<a href="#{esc(s["id"])}">{esc(s["title"])}</a>' for s in c['sections'])
    sections = []
    for section in c['sections']:
        cards = []
        for resource in section['resources']:
            source = link(resource['source'],u['source']) if resource.get('source') else ''
            lang = resource.get('language', locale)
            language_note = f'<span class="language-note">{esc(u["english"])}</span>' if lang == 'en' and locale != 'en' else ''
            attrs = f' hreflang="{esc(UI.get(lang,{"lang":lang})["lang"])}"'
            cards.append(f'<article class="card"><h3>{esc(resource["name"])}</h3><p>{esc(resource["description"])}</p><div class="card-links">{link(resource["href"],u["open"],attrs)}{source}</div>{language_note}</article>')
        sections.append(f'<section class="section" id="{esc(section["id"])}" aria-labelledby="{esc(section["id"])}-title"><h2 id="{esc(section["id"])}-title">{esc(section["title"])}</h2><p class="section-intro">{esc(section["intro"])}</p><div class="grid">{"".join(cards)}</div></section>')
    steps = ''.join(f'<li><h3>{esc(s["title"])}</h3><p>{esc(s["body"])}</p></li>' for s in c['steps'])
    related = ''.join(link(route(g,locale),g['locales'][locale]['title']) for g in guides if g['id'] != guide['id'])
    legacy = ''
    if guide.get('legacyLinks'):
        legacy_links = ''.join(link(item['href'],u['collection']+' '+str(item['number']),' hreflang="en"') for item in guide['legacyLinks'])
        legacy = f'<p>{esc(u["legacy"])}</p><nav aria-label="{esc(u["legacy"])}">{legacy_links}</nav>'
    structured = json.dumps({'@context':'https://schema.org','@type':'CollectionPage','name':c['title'],'description':c['description'],'url':canonical,'inLanguage':u['lang']},ensure_ascii=False).replace('<','\\u003c')
    return f'''<!doctype html>
<html lang="{u['lang']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(c['title'])} | Zion Tech Group</title><meta name="description" content="{esc(c['description'])}"><meta name="robots" content="index,follow">
<link rel="canonical" href="{canonical}">
{alternates}
<link rel="alternate" hreflang="x-default" href="{ORIGIN+route(guide,'en')}">
<meta property="og:title" content="{esc(c['title'])}"><meta property="og:description" content="{esc(c['description'])}"><meta property="og:url" content="{canonical}"><meta property="og:type" content="website">
<link rel="stylesheet" href="/zion-app-network/assets/network-guides.css"><script type="application/ld+json">{structured}</script></head>
<body data-guide-release="{RELEASE}" data-guide="{esc(guide['id'])}">
<a class="skip" href="#main">{esc(u['skip'])}</a>
<header><div class="wrap top"><a class="brand" href="{home}">Zion Tech Group<span>Apps Network</span></a><nav aria-label="{esc(u['catalog'])}">{navigation}</nav></div><nav class="wrap languages" aria-label="{esc(u['languages'])}">{languages}</nav></header>
<main class="wrap" id="main" tabindex="-1"><section class="hero" aria-labelledby="page-title"><p class="eyebrow">{esc(u['guide'])}</p><h1 id="page-title">{esc(c['title'])}</h1><p class="lead">{esc(c['intro'])}</p></section>
<div class="guide-contents"><p>{esc(u['contents'])}</p><nav aria-label="{esc(u['contents'])}">{toc}<a href="#practice">{esc(u['steps'])}</a></nav></div>
{''.join(sections)}
<section class="section" id="practice" aria-labelledby="practice-title"><h2 id="practice-title">{esc(u['steps'])}</h2><ol class="steps">{steps}</ol><div class="example"><p class="eyebrow">{esc(u['example'])}</p><h3>{esc(c['example']['title'])}</h3><p>{esc(c['example']['body'])}</p></div><aside class="scope" aria-labelledby="scope-title"><h2 id="scope-title">{esc(u['scope'])}</h2><p>{esc(c['scope'])}</p></aside></section>
<section class="section" aria-labelledby="related-title"><h2 id="related-title">{esc(u['related'])}</h2><nav class="related" aria-label="{esc(u['related'])}">{related}</nav>{legacy}</section>
<section class="section discovery" aria-labelledby="discovery-title"><h2 id="discovery-title">{esc(u['discovery'])}</h2><p>{esc(u['discoveryText'])}</p><div class="actions">{link(prefix+'discovery/',u['discovery'],' class="button"')}{link(prefix+'apps/',u['catalog'])}</div></section>
</main><footer><div class="wrap"><p>{esc(u['footer'])}</p><nav aria-label="{esc(u['catalog'])}">{navigation}{link('https://github.com/Zion-support/zion-app-network',u['source'])}</nav><p>Zion Tech Group</p></div></footer></body></html>
'''

def run(check=False):
    guides = load_guides()
    mismatches = []
    for guide in guides:
        for locale in LOCALES:
            target = ROOT / local_path(guide,locale)
            output = render(guide,locale,guides)
            if check:
                if not target.exists() or target.read_text() != output:
                    mismatches.append(str(target.relative_to(ROOT)))
            else:
                target.parent.mkdir(parents=True,exist_ok=True)
                target.write_text(output)
    if mismatches:
        raise SystemExit('Run render_localized_guides.py; stale output: ' + ', '.join(mismatches))
    print(f'{"Verified" if check else "Rendered"} {len(guides)*len(LOCALES)} pages from {len(guides)} guide families.')

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--check',action='store_true')
    run(parser.parse_args().check)
