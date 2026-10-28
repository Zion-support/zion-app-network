#!/usr/bin/env python3
"""Read-only scoped multilingual publication QA. No browser scripts, forms or email submissions."""
import argparse, concurrent.futures, datetime, json, time
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

LANGS = ['en', 'pt-BR', 'es', 'fr', 'de']
HOME = ['/', '/en/', '/es/', '/fr/', '/de/']
FIELD = ['/apps/field-service-evidence-guide' + s + '.html' for s in ['', '.pt-br', '.es', '.fr', '.de']]
BATCH = ['/zion-app-network/app-network-batch113-oct07' + s + '.html' for s in ['', '-pt', '-es', '-fr', '-de']]
OPS = ['/zion-app-network/app-network-operations-reliability-2026' + s + '.html' for s in ['', '-pt-br', '-es', '-fr', '-de']]
EVIDENCE = ['/zion-app-network/app-network-operations-evidence-checklist-2026' + s + '.html' for s in ['', '-pt-br', '-es', '-fr', '-de']]
SUFFIX = ['', '-pt-br', '-es', '-fr', '-de']
QUOTE = ['/zion-app-network/field-quote-readiness-2026' + s + '.html' for s in SUFFIX]
SHOW_SUFFIX = ['', '-pt', '-es', '-fr', '-de']
BATCH96 = ['/zion-app-network/app/network-batch96-showcase' + s + '.html' for s in SHOW_SUFFIX]
Q4 = ['/zion-app-network/app/network-q4-2026-showcase' + s + '.html' for s in SHOW_SUFFIX]
SUPPORT = ['/zion-app-network/app-network-sept26-support' + s + '.html' for s in SUFFIX]
FIELD_DIRECTORY = ['/zion-app-network/app-network-sept26-support-field' + s + '.html' for s in SUFFIX]
EQUIPMENT = ['/zion-app-network/equipment-lifecycle-decision-guide-2026' + s + '.html' for s in SUFFIX]
PILOT = ['/zion-app-network/app-to-pilot-paths-2026' + s + '.html' for s in SUFFIX]
DISCOVERY = ['/discovery/', '/pt/discovery/', '/es/discovery/', '/fr/discovery/', '/de/discovery/']
FREE_HEADINGS = [
    'Free AI & Automation Discovery',
    'Discovery gratuito de IA e automação',
    'Discovery gratuito de IA y automatización',
    'Discovery IA et automatisation gratuit',
    'Kostenlose KI- und Automatisierungs-Discovery',
]
FREE_STATEMENTS = [
    'No payment or meeting is required.',
    'Nenhum pagamento ou reunião é necessário.',
    'No se requiere pago ni reunión.',
    "Aucun paiement ni rendez-vous n'est requis.",
    'Keine Zahlung und kein Termin erforderlich.',
]
FAMILIES = {'field': FIELD, 'batch': BATCH, 'ops': OPS, 'evidence': EVIDENCE,
            'support': SUPPORT, 'fielddir': FIELD_DIRECTORY, 'equipment': EQUIPMENT, 'pilot': PILOT, 'quote': QUOTE, 'batch96': BATCH96, 'q4': Q4}

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.lang=''; self.canonical=[]; self.alternates={}; self.links=[]; self.styles=[]; self.heading=[]; self.in_heading=False; self.forms=0
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag=='html': self.lang=a.get('lang','')
        if tag=='a' and a.get('href'): self.links.append(a['href'])
        if tag=='form': self.forms += 1
        if tag=='h1': self.in_heading=True
        if tag=='link':
            rel=a.get('rel','').split()
            if 'canonical' in rel: self.canonical.append(a.get('href',''))
            if 'alternate' in rel and a.get('hreflang'): self.alternates.setdefault(a['hreflang'],[]).append(a.get('href',''))
            if 'stylesheet' in rel: self.styles.append(a.get('href',''))
    def handle_endtag(self, tag):
        if tag=='h1': self.in_heading=False
    def handle_data(self, text):
        if self.in_heading and text.strip(): self.heading.append(text.strip())

def get(url):
    sep='&' if '?' in url else '?'
    req=Request(url+sep+'release_qa='+str(time.time_ns()),headers={'Cache-Control':'no-cache','User-Agent':'Zion-ReadOnly-Release-QA/2.0'})
    with urlopen(req,timeout=30) as response:
        return response.status,response.geturl(),response.headers.get_content_type(),response.read().decode('utf-8',errors='replace')

def localized_discovery(i):
    return DISCOVERY[i]

def run(site, release_sha='', source_run_id=''):
    site=site.rstrip('/')
    errors=[]; assets=set(); headings={k:[] for k in FAMILIES}
    def check(item):
        group,i,route=item
        issues=[]
        try:
            status,final,mime,text=get(site+route)
            page=Page(text)
            if status!=200: issues.append('HTTP status is not 200')
            if mime!='text/html': issues.append('Response is not HTML')
            if urlparse(final).path!=route: issues.append('Unexpected redirect')
            if not ''.join(page.heading): issues.append('Missing main heading')
            locale_index=[1,0,2,3,4][i] if group=='home' else i
            wanted_lang=LANGS[locale_index]
            if page.lang.lower()!=wanted_lang.lower(): issues.append('Wrong document language: '+page.lang)
            urls={urljoin(site+route,link) for link in page.links}
            if group=='home':
                if 'data-batch113-promo=' not in text: issues.append('Missing insurance promotion')
                if site+FIELD[locale_index] not in urls: issues.append('Missing same-language field guide')
                if site+BATCH[locale_index] not in urls: issues.append('Missing same-language insurance showcase')
            elif group=='discovery':
                if page.canonical != [site+route]: issues.append('Wrong or duplicate free Discovery canonical')
                for lang,target in zip(LANGS,DISCOVERY):
                    if page.alternates.get(lang) != [site+target]: issues.append('Wrong or duplicate Discovery hreflang: '+lang)
                    if site+target not in urls: issues.append('Missing Discovery language switch: '+lang)
                if page.alternates.get('x-default') != [site+DISCOVERY[0]]: issues.append('Wrong Discovery x-default')
                if page.forms != 1: issues.append('Free Discovery must have exactly one questionnaire')
                if FREE_HEADINGS[i] not in ' '.join(page.heading): issues.append('Wrong free Discovery heading')
                if FREE_STATEMENTS[i] not in text: issues.append('Missing free/no-payment promise')
                if 'buy.stripe.com' in text.lower(): issues.append('Paid checkout found in free Discovery')
            else:
                family=FAMILIES[group]
                if page.canonical != [site+route]: issues.append('Wrong or duplicate canonical')
                for lang,target in zip(LANGS,family):
                    if page.alternates.get(lang) != [site+target]: issues.append('Wrong or duplicate hreflang: '+lang)
                    if target != route and site+target not in urls: issues.append('Missing language switch: '+lang)
                if page.alternates.get('x-default') != [site+family[0]]: issues.append('Wrong x-default')
                if page.forms: issues.append('Unexpected form in informational guide')
                if site+localized_discovery(i) not in urls: issues.append('Missing localized Discovery link')
                if group=='field' and 'data-field-evidence-gates=' not in text: issues.append('Missing evidence gates')
                if group=='batch' and site+FIELD[i] not in urls: issues.append('Missing field guide interlink')
                if group=='ops' and site+EVIDENCE[i] not in urls: issues.append('Missing Evidence checklist interlink')
                if group=='evidence' and site+OPS[i] not in urls: issues.append('Missing Operations hub interlink')
                if group=='support' and site+FIELD_DIRECTORY[i] not in urls: issues.append('Missing Field directory interlink')
                if group=='fielddir':
                    for name,target in [('Support',SUPPORT[i]),('Equipment',EQUIPMENT[i]),('Pilot',PILOT[i])]:
                        if site+target not in urls: issues.append('Missing '+name+' interlink from Field directory')
                if group=='equipment' and site+PILOT[i] not in urls: issues.append('Missing Pilot interlink from Equipment')
                if group=='pilot' and site+EQUIPMENT[i] not in urls: issues.append('Missing Equipment interlink from Pilot')
                if group=='batch96' and site+Q4[i] not in urls:
                    issues.append('Missing related Q4 showcase interlink')
                if group=='q4' and site+BATCH96[i] not in urls:
                    issues.append('Missing related Batch96 showcase interlink')
                if group=='quote':
                    if 'id="calculate"' not in text or 'id="brief"' not in text:
                        issues.append('Field quote calculation controls missing')
                    if 'total*1.4' not in text or 'Math.ceil(' not in text or 'minimum-total' not in text:
                        issues.append('Field quote 40% markup logic missing')
                    for name,target in [('Operations',OPS[i]),('Evidence',EVIDENCE[i]),('Pilot',PILOT[i])]:
                        if site+target not in urls:
                            issues.append('Missing '+name+' interlink from Field quote')
                    if 'fetch(' in text or 'XMLHttpRequest' in text or 'sendBeacon(' in text:
                        issues.append('Unexpected network capability in local-only Field quote')
            return {'group':group,'route':route,'status':status,'lang':page.lang,'heading':' '.join(page.heading),'errors':issues,'assets':[urljoin(site+route,p) for p in page.styles]}
        except Exception as exc:
            return {'group':group,'route':route,'errors':[str(exc)],'assets':[]}
    groups=[('home',HOME),('field',FIELD),('batch',BATCH),('ops',OPS),('evidence',EVIDENCE),
            ('support',SUPPORT),('fielddir',FIELD_DIRECTORY),('equipment',EQUIPMENT),('pilot',PILOT),('quote',QUOTE),('batch96',BATCH96),('q4',Q4),('discovery',DISCOVERY)]
    items=[(g,i,p) for g,paths in groups for i,p in enumerate(paths)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        results=list(pool.map(check,items))
    for row in results:
        errors.extend(row['route']+': '+issue for issue in row['errors'])
        assets.update(url for url in row.pop('assets') if urlparse(url).netloc==urlparse(site).netloc)
        if row['group'] in headings: headings[row['group']].append(row.get('heading',''))
    for group,values in headings.items():
        if len(values)!=5 or len(set(values))!=5: errors.append(group+': translated headings missing or duplicated')
    asset_results=[]
    for asset in sorted(assets):
        try:
            status,final,mime,text=get(asset)
            valid=status==200 and mime=='text/css' and bool(text.strip())
            if not valid: errors.append(asset+': stylesheet unavailable or wrong MIME')
            asset_results.append({'url':asset,'status':status,'mime':mime,'pass':valid})
        except Exception as exc:
            errors.append(asset+': '+str(exc))
    return {
        'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'scope':str(len(items))+' HTML routes and same-origin stylesheets; GET-only, no browser execution or form submissions; Discovery form structure is inspected',
        'release_sha':release_sha,
        'source_run_id':str(source_run_id or ''),
        'pass':not errors,
        'pages':results,
        'assets':asset_results,
        'errors':errors,
    }

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site',default='https://ziontechgroup.com')
    parser.add_argument('--output',default='release-verification.json')
    parser.add_argument('--release-sha',default='')
    parser.add_argument('--source-run-id',default='')
    args=parser.parse_args()
    report=run(args.site,args.release_sha,args.source_run_id)
    with open(args.output,'w',encoding='utf-8') as output: json.dump(report,output,ensure_ascii=False,indent=2)
    print(('PASS' if report['pass'] else 'FAIL')+': '+str(len(report['pages']))+' scoped HTML routes, '+str(len(report['assets']))+' stylesheets')
    for error in report['errors']: print(error)
    raise SystemExit(0 if report['pass'] else 1)
