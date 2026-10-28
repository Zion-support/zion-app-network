#!/usr/bin/env python3
"""Offline source contract for the current multilingual Operations release.

Reads repository HTML only. No network, browser, forms, secrets or external actions.
"""
import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin

SITE='https://ziontechgroup.com'
LANGS=['en','pt-BR','es','fr','de']

FAMILIES={
    'ops':[
        ('app-network-operations-reliability-2026.html','/zion-app-network/app-network-operations-reliability-2026.html'),
        ('app-network-operations-reliability-2026-pt-br.html','/zion-app-network/app-network-operations-reliability-2026-pt-br.html'),
        ('app-network-operations-reliability-2026-es.html','/zion-app-network/app-network-operations-reliability-2026-es.html'),
        ('app-network-operations-reliability-2026-fr.html','/zion-app-network/app-network-operations-reliability-2026-fr.html'),
        ('app-network-operations-reliability-2026-de.html','/zion-app-network/app-network-operations-reliability-2026-de.html'),
    ],
    'evidence':[
        ('app-network-operations-evidence-checklist-2026.html','/zion-app-network/app-network-operations-evidence-checklist-2026.html'),
        ('app-network-operations-evidence-checklist-2026-pt-br.html','/zion-app-network/app-network-operations-evidence-checklist-2026-pt-br.html'),
        ('app-network-operations-evidence-checklist-2026-es.html','/zion-app-network/app-network-operations-evidence-checklist-2026-es.html'),
        ('app-network-operations-evidence-checklist-2026-fr.html','/zion-app-network/app-network-operations-evidence-checklist-2026-fr.html'),
        ('app-network-operations-evidence-checklist-2026-de.html','/zion-app-network/app-network-operations-evidence-checklist-2026-de.html'),
    ],
    'quote':[
        ('field-quote-readiness-2026.html','/zion-app-network/field-quote-readiness-2026.html'),
        ('field-quote-readiness-2026-pt-br.html','/zion-app-network/field-quote-readiness-2026-pt-br.html'),
        ('field-quote-readiness-2026-es.html','/zion-app-network/field-quote-readiness-2026-es.html'),
        ('field-quote-readiness-2026-fr.html','/zion-app-network/field-quote-readiness-2026-fr.html'),
        ('field-quote-readiness-2026-de.html','/zion-app-network/field-quote-readiness-2026-de.html'),
    ],
    'batch96':[
        ('app/network-batch96-showcase.html','/zion-app-network/app/network-batch96-showcase.html'),
        ('app/network-batch96-showcase-pt.html','/zion-app-network/app/network-batch96-showcase-pt.html'),
        ('app/network-batch96-showcase-es.html','/zion-app-network/app/network-batch96-showcase-es.html'),
        ('app/network-batch96-showcase-fr.html','/zion-app-network/app/network-batch96-showcase-fr.html'),
        ('app/network-batch96-showcase-de.html','/zion-app-network/app/network-batch96-showcase-de.html'),
    ],
    'q4':[
        ('app/network-q4-2026-showcase.html','/zion-app-network/app/network-q4-2026-showcase.html'),
        ('app/network-q4-2026-showcase-pt.html','/zion-app-network/app/network-q4-2026-showcase-pt.html'),
        ('app/network-q4-2026-showcase-es.html','/zion-app-network/app/network-q4-2026-showcase-es.html'),
        ('app/network-q4-2026-showcase-fr.html','/zion-app-network/app/network-q4-2026-showcase-fr.html'),
        ('app/network-q4-2026-showcase-de.html','/zion-app-network/app/network-q4-2026-showcase-de.html'),
    ],
}

class Page(HTMLParser):
    def __init__(self,text):
        super().__init__()
        self.lang=''
        self.canonical=[]
        self.alternates={}
        self.links=[]
        self.ids=set()
        self.external_scripts=[]
        self.forms=0
        self.h1=[]
        self.in_h1=False
        self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if a.get('id'):
            self.ids.add(a['id'])
        if tag=='form':
            self.forms += 1
        if tag=='script' and a.get('src'):
            self.external_scripts.append(a['src'])
        if tag=='html':
            self.lang=a.get('lang','')
        elif tag=='a' and a.get('href'):
            self.links.append(a['href'])
        elif tag=='h1':
            self.in_h1=True
        elif tag=='link':
            rel=(a.get('rel') or '').split()
            if 'canonical' in rel:
                self.canonical.append(a.get('href',''))
            if 'alternate' in rel and a.get('hreflang'):
                self.alternates.setdefault(a['hreflang'],[]).append(a.get('href',''))
    def handle_endtag(self,tag):
        if tag=='h1':
            self.in_h1=False
    def handle_data(self,data):
        if self.in_h1 and data.strip():
            self.h1.append(data.strip())

def localized_discovery(i):
    return '/discovery/' if i==0 else '/' + ('pt' if i==1 else LANGS[i]) + '/discovery/'

def verify(root:Path):
    errors=[]
    headings={name:[] for name in FAMILIES}
    parsed={}
    for family,entries in FAMILIES.items():
        routes=[route for _,route in entries]
        for i,(filename,route) in enumerate(entries):
            path=root/filename
            if not path.is_file():
                errors.append(f'{family}: missing source file {filename}')
                continue
            page=Page(path.read_text(encoding='utf-8'))
            parsed[(family,i)]=page
            heading=' '.join(page.h1)
            headings[family].append(heading)
            if not heading:
                errors.append(f'{filename}: missing h1')
            if page.lang.lower()!=LANGS[i].lower():
                errors.append(f'{filename}: wrong lang {page.lang!r}, expected {LANGS[i]!r}')
            expected=SITE+route
            if page.canonical != [expected]:
                errors.append(f'{filename}: canonical must be exactly {expected}')
            for lang,target in zip(LANGS,routes):
                wanted=SITE+target
                if page.alternates.get(lang) != [wanted]:
                    errors.append(f'{filename}: hreflang {lang} must be exactly {wanted}')
            if page.alternates.get('x-default') != [SITE+routes[0]]:
                errors.append(f'{filename}: wrong or missing x-default')
            absolute={urljoin(expected,href) for href in page.links}
            for target in routes:
                if target != route and SITE+target not in absolute:
                    errors.append(f'{filename}: missing language switch to {target}')
            if SITE+localized_discovery(i) not in absolute:
                errors.append(f'{filename}: missing localized Discovery link')
            if family=='quote':
                required={'calculate','copy','brief','total','floor','add','currency',
                          'labor','travel','parts','tax','other','country','asset','service','window'}
                absent=required-page.ids
                if absent:
                    errors.append(f'{filename}: missing calculator element IDs: {sorted(absent)}')
                if page.forms or page.external_scripts:
                    errors.append(f'{filename}: quote worksheet must not include forms or external scripts')
                raw=path.read_text(encoding='utf-8')
                if ('total*1.4' not in raw or 'Math.ceil(' not in raw or
                        'minimum-total' not in raw):
                    errors.append(f'{filename}: safe minimum 40% markup calculation is missing')
                for blocked in ('fetch(', 'XMLHttpRequest', 'sendBeacon(', 'WebSocket('):
                    if blocked in path.read_text(encoding='utf-8'):
                        errors.append(f'{filename}: network operation {blocked} is not allowed')
                for route_name,route_target in (
                    ('Operations',FAMILIES['ops'][i][1]),
                    ('Evidence',FAMILIES['evidence'][i][1]),
                    ('Pilot','/zion-app-network/app-to-pilot-paths-2026'+(['','-pt-br','-es','-fr','-de'][i])+'.html')):
                    if SITE+route_target not in absolute:
                        errors.append(f'{filename}: missing {route_name} interlink')

    for family,values in headings.items():
        if len(values)==5 and len(set(values))!=5:
            errors.append(f'{family}: translated h1 values are duplicated')

    for i in range(5):
        ops=parsed.get(('ops',i))
        evidence=parsed.get(('evidence',i))
        if ops and evidence:
            ops_url=SITE+FAMILIES['ops'][i][1]
            evidence_url=SITE+FAMILIES['evidence'][i][1]
            ops_links={urljoin(ops_url,x) for x in ops.links}
            evidence_links={urljoin(evidence_url,x) for x in evidence.links}
            if evidence_url not in ops_links:
                errors.append(f'{FAMILIES["ops"][i][0]}: missing matching Evidence checklist interlink')
            if ops_url not in evidence_links:
                errors.append(f'{FAMILIES["evidence"][i][0]}: missing matching Operations interlink')
    catalog=root/'CATALOG-NAVIGATION.html'
    if not catalog.is_file():
        errors.append('CATALOG-NAVIGATION.html: missing five-language catalog landing page')
    else:
        nav=Page(catalog.read_text(encoding='utf-8'))
        url=SITE+'/zion-app-network/CATALOG-NAVIGATION.html'
        if nav.canonical!=[url]:
            errors.append('CATALOG-NAVIGATION.html: canonical mismatch')
        for i,(lang,slug) in enumerate(zip(LANGS,['en','pt','es','fr','de'])):
            if 'start-here-'+slug not in nav.ids:
                errors.append('CATALOG-NAVIGATION.html: missing language anchor '+slug)
            dest=SITE+'/zion-app-network/directory-'+slug+'.html'
            hrefs={urljoin(url,h) for h in nav.links}
            if dest not in hrefs:
                errors.append('CATALOG-NAVIGATION.html: missing directory entry '+slug)
            quote=SITE+FAMILIES['quote'][i][1]
            if quote not in hrefs:
                errors.append('CATALOG-NAVIGATION.html: missing field quote entry '+slug)
            if SITE+localized_discovery(i) not in hrefs:
                errors.append('CATALOG-NAVIGATION.html: missing Discovery entry '+slug)

    paths=root/'task-paths.html'
    if not paths.is_file():
        errors.append('task-paths.html: missing source')
    else:
        body=paths.read_text(encoding='utf-8')
        task=Page(body)
        target='/zion-app-network/supplier-evidence.html'
        if task.links.count(target)<5:
            errors.append('task-paths.html: multilingual supplier evidence interlinks incomplete')
        if '/zion-app-network/CATALOG-SUPPLIER-EVIDENCE.html' in task.links:
            errors.append('task-paths.html: legacy unresolved supplier catalog link remains')
    for i in range(5):
        batch=parsed.get(('batch96',i))
        q4=parsed.get(('q4',i))
        if batch and q4:
            batch_url=SITE+FAMILIES['batch96'][i][1]
            q4_url=SITE+FAMILIES['q4'][i][1]
            if q4_url not in {urljoin(batch_url,x) for x in batch.links}:
                errors.append(f'{FAMILIES["batch96"][i][0]}: missing matching Q4 showcase interlink')
            if batch_url not in {urljoin(q4_url,x) for x in q4.links}:
                errors.append(f'{FAMILIES["q4"][i][0]}: missing matching Batch96 showcase interlink')
    return errors

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',default='.')
    args=parser.parse_args()
    errors=verify(Path(args.root))
    if errors:
        for error in errors:
            print('ERROR:',error)
        raise SystemExit(1)
    print('PASS: 25 locale files plus Catalog Navigation and Supplier Task Paths')
