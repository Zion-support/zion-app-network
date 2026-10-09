#!/usr/bin/env python3
"""Read-only scoped publication QA. No browser scripts, forms or email submissions."""
import argparse, concurrent.futures, datetime, json, time
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

LANGS = ['en', 'pt-BR', 'es', 'fr', 'de']
HOME = ['/', '/en/', '/es/', '/fr/', '/de/']
FIELD = ['/apps/field-service-evidence-guide' + s + '.html' for s in ['', '.pt-br', '.es', '.fr', '.de']]
BATCH = ['/zion-app-network/app-network-batch113-oct07' + s + '.html' for s in ['', '-pt', '-es', '-fr', '-de']]

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.lang = ''; self.canonical = []; self.alternates = {}; self.links = []; self.styles = []; self.heading = []; self.in_heading = False; self.forms = 0
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'html': self.lang = a.get('lang', '')
        if tag == 'a' and a.get('href'): self.links.append(a['href'])
        if tag == 'form': self.forms += 1
        if tag == 'h1': self.in_heading = True
        if tag == 'link':
            rel = a.get('rel', '').split()
            if 'canonical' in rel: self.canonical.append(a.get('href', ''))
            if 'alternate' in rel and a.get('hreflang'):
                self.alternates.setdefault(a['hreflang'], []).append(a.get('href', ''))
            if 'stylesheet' in rel: self.styles.append(a.get('href', ''))
    def handle_endtag(self, tag):
        if tag == 'h1': self.in_heading = False
    def handle_data(self, text):
        if self.in_heading: self.heading.append(text.strip())

def get(url):
    sep = '&' if '?' in url else '?'
    request = Request(url + sep + 'release_qa=' + str(time.time_ns()), headers={'Cache-Control': 'no-cache', 'User-Agent': 'Zion-ReadOnly-Release-QA/1.0'})
    with urlopen(request, timeout=30) as response:
        return response.status, response.geturl(), response.headers.get_content_type(), response.read().decode('utf-8', errors='replace')

def run(site):
    site = site.rstrip('/')
    results = []; errors = []; assets = set(); headings = {'field': [], 'batch': []}
    def check(item):
        group, i, route = item
        issues = []
        try:
            status, final, mime, text = get(site + route)
            page = Page(text)
            if status != 200: issues.append('HTTP status is not 200')
            if mime != 'text/html': issues.append('Response is not HTML')
            if urlparse(final).path != route: issues.append('Unexpected redirect')
            if not ''.join(page.heading): issues.append('Missing main heading')
            locale_index = [1, 0, 2, 3, 4][i] if group == 'home' else i
            wanted_lang = LANGS[locale_index]
            if page.lang.lower() != wanted_lang.lower(): issues.append('Wrong document language: ' + page.lang)
            urls = {urljoin(site + route, link) for link in page.links}
            if group == 'home':
                if 'data-batch113-promo=' not in text: issues.append('Missing insurance promotion')
                if site + FIELD[locale_index] not in urls: issues.append('Missing same-language field guide')
                if site + BATCH[locale_index] not in urls: issues.append('Missing same-language insurance showcase')
            else:
                family = FIELD if group == 'field' else BATCH
                if page.canonical != [site + route]: issues.append('Wrong or duplicate canonical')
                for lang, target in zip(LANGS, family):
                    if page.alternates.get(lang) != [site + target]: issues.append('Wrong or duplicate hreflang: ' + lang)
                    if site + target not in urls: issues.append('Missing language switch: ' + lang)
                if page.alternates.get('x-default') != [site + family[0]]: issues.append('Wrong x-default')
                if page.forms: issues.append('Unexpected form in informational guide')
                discovery = '/discovery/' if i == 0 else '/' + ('pt' if i == 1 else LANGS[i]) + '/discovery/'
                if site + discovery not in urls: issues.append('Missing localized Discovery link')
                if group == 'field' and 'data-field-evidence-gates=' not in text: issues.append('Missing evidence gates')
                if group == 'batch' and site + FIELD[i] not in urls: issues.append('Missing field guide interlink')
            return {'group': group, 'route': route, 'status': status, 'lang': page.lang, 'heading': ' '.join(page.heading), 'errors': issues, 'assets': [urljoin(site + route, p) for p in page.styles]}
        except Exception as exc:
            return {'group': group, 'route': route, 'errors': [str(exc)], 'assets': []}
    items = [(g, i, p) for g, paths in [('home', HOME), ('field', FIELD), ('batch', BATCH)] for i, p in enumerate(paths)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(check, items))
    for row in results:
        errors.extend(row['route'] + ': ' + issue for issue in row['errors'])
        assets.update(url for url in row.pop('assets') if urlparse(url).netloc == urlparse(site).netloc)
        if row['group'] in headings: headings[row['group']].append(row.get('heading', ''))
    for group, values in headings.items():
        if len(set(values)) != 5: errors.append(group + ': translated headings missing or duplicated')
    asset_results = []
    for asset in sorted(assets):
        try:
            status, final, mime, text = get(asset)
            valid = status == 200 and mime == 'text/css' and bool(text.strip())
            if not valid: errors.append(asset + ': stylesheet unavailable or wrong MIME')
            asset_results.append({'url': asset, 'status': status, 'mime': mime, 'pass': valid})
        except Exception as exc:
            errors.append(asset + ': ' + str(exc))
    return {'checked_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'scope': '15 HTML routes and their same-origin stylesheets; not full-network, browser execution, app functionality or paired inbox receipt', 'pass': not errors, 'pages': results, 'assets': asset_results, 'errors': errors}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site', default='https://ziontechgroup.com')
    parser.add_argument('--output', default='release-verification.json')
    args = parser.parse_args()
    report = run(args.site)
    with open(args.output, 'w', encoding='utf-8') as output: json.dump(report, output, ensure_ascii=False, indent=2)
    print(('PASS' if report['pass'] else 'FAIL') + ': 15 scoped HTML routes, ' + str(len(report['assets'])) + ' stylesheets')
    for error in report['errors']: print(error)
    raise SystemExit(0 if report['pass'] else 1)
