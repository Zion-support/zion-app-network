#!/usr/bin/env python3
"""Offline contract tests for multilingual release QA. No network or form submits."""
import importlib.util
from pathlib import Path
from unittest import TestCase, main
from unittest.mock import patch
from urllib.parse import urlparse

SCRIPT=Path(__file__).with_name('verify-network-release.py')
spec=importlib.util.spec_from_file_location('release_qa',SCRIPT)
release_qa=importlib.util.module_from_spec(spec); spec.loader.exec_module(release_qa)
SITE='https://ziontechgroup.com'

def family_for(route):
    for name,family in release_qa.FAMILIES.items():
        if route in family: return name,family
    raise AssertionError('Unknown route '+route)

def page(route,bad_alternate=False,missing_interlink=False,missing_support_link=False,paid_discovery=False):
    if route in release_qa.HOME:
        pos=release_qa.HOME.index(route); locale=[1,0,2,3,4][pos]
        links=[release_qa.FIELD[locale],release_qa.BATCH[locale]]
        return ('<html lang="%s"><head><link rel="stylesheet" href="/styles/app.css"></head>'
                '<body><h1>Home %d</h1><section data-batch113-promo="1"></section>%s</body></html>' %
                (release_qa.LANGS[locale],pos,''.join('<a href="%s">Link</a>'%x for x in links)))
    if route in release_qa.DISCOVERY:
        i=release_qa.DISCOVERY.index(route)
        alts=''.join('<link rel="alternate" hreflang="%s" href="%s">'%(lang,SITE+target)
                     for lang,target in zip(release_qa.LANGS,release_qa.DISCOVERY))
        alts+='<link rel="alternate" hreflang="x-default" href="%s">'%(SITE+release_qa.DISCOVERY[0])
        statement='Pay $99 before continuing.' if paid_discovery else release_qa.FREE_STATEMENTS[i]
        return ('<html lang="%s"><head><link rel="canonical" href="%s">%s'
                '<link rel="stylesheet" href="/styles/app.css"></head><body><h1>%s</h1>'
                '<p>%s</p><form><input name="process"></form>%s</body></html>' %
                (release_qa.LANGS[i],SITE+route,alts,release_qa.FREE_HEADINGS[i],
                 statement,''.join('<a href="%s">Language</a>'%u for u in release_qa.DISCOVERY)))
    group,family=family_for(route); i=family.index(route)
    alt=[(lang,SITE+target) for lang,target in zip(release_qa.LANGS,family)]
    if bad_alternate and group=='ops' and i==2: alt[3]=('fr',SITE+'/incorrect-fr')
    alternates=''.join('<link rel="alternate" hreflang="%s" href="%s">'%(lang,target) for lang,target in alt)
    alternates+='<link rel="alternate" hreflang="x-default" href="%s">'%(SITE+family[0])
    links=[target for target in family if target != route]+[release_qa.localized_discovery(i)]
    if group=='batch': links.append(release_qa.FIELD[i])
    if group=='ops' and not missing_interlink: links.append(release_qa.EVIDENCE[i])
    if group=='evidence': links.append(release_qa.OPS[i])
    if group=='support' and not missing_support_link: links.append(release_qa.FIELD_DIRECTORY[i])
    if group=='fielddir': links.extend([release_qa.SUPPORT[i],release_qa.EQUIPMENT[i],release_qa.PILOT[i]])
    if group=='equipment': links.append(release_qa.PILOT[i])
    if group=='pilot': links.append(release_qa.EQUIPMENT[i])
    marker='<section data-field-evidence-gates="1"></section>' if group=='field' else ''
    return ('<html lang="%s"><head><link rel="canonical" href="%s">%s<link rel="stylesheet" href="/styles/app.css"></head>'
            '<body><h1>%s %d</h1>%s%s</body></html>' %
            (release_qa.LANGS[i],SITE+route,alternates,group,i,marker,''.join('<a href="%s">Go</a>'%u for u in links)))

def fake_fetch(url,bad_alternate=False,outage=None,missing_interlink=False,missing_support_link=False,paid_discovery=False):
    route=urlparse(url).path
    if route=='/styles/app.css': return 200,url,'text/css','body { color: black; }'
    if outage==route: raise OSError('simulated outage')
    known=set(release_qa.HOME+release_qa.DISCOVERY)
    for family in release_qa.FAMILIES.values(): known.update(family)
    if route not in known: raise AssertionError('Unexpected network request '+url)
    return 200,url,'text/html',page(route,bad_alternate,missing_interlink,missing_support_link,paid_discovery)

class OfflineReleaseQATests(TestCase):
    def test_all_50_pages_and_css_pass_valid_fixture(self):
        with patch.object(release_qa,'get',side_effect=fake_fetch): report=release_qa.run(SITE)
        self.assertTrue(report['pass'],report['errors']); self.assertEqual(len(report['pages']),50); self.assertEqual(len(report['assets']),1)
    def test_mismatched_hreflang_fails_closed(self):
        with patch.object(release_qa,'get',side_effect=lambda u: fake_fetch(u,bad_alternate=True)): report=release_qa.run(SITE)
        self.assertFalse(report['pass']); self.assertTrue(any('Wrong or duplicate hreflang: fr' in e for e in report['errors']))
    def test_http_failure_fails_closed(self):
        with patch.object(release_qa,'get',side_effect=lambda u: fake_fetch(u,outage=release_qa.EVIDENCE[4])): report=release_qa.run(SITE)
        self.assertFalse(report['pass']); self.assertTrue(any('simulated outage' in e for e in report['errors']))
    def test_missing_support_field_interlink_fails_closed(self):
        with patch.object(release_qa,'get',side_effect=lambda u: fake_fetch(u,missing_support_link=True)): report=release_qa.run(SITE)
        self.assertFalse(report['pass'])
        self.assertTrue(any('Missing Field directory interlink' in e for e in report['errors']))

    def test_discovery_payment_gate_fails_closed(self):
        with patch.object(release_qa,'get',side_effect=lambda u: fake_fetch(u,paid_discovery=True)): report=release_qa.run(SITE)
        self.assertFalse(report['pass'])
        self.assertTrue(any('Missing free/no-payment promise' in e for e in report['errors']))

    def test_missing_foreign_language_fails_closed(self):
        def broken(u):
            result=fake_fetch(u)
            if urlparse(u).path==release_qa.OPS[0]:
                s,final,mime,body=result
                body=body.replace('<a href="%s">Go</a>'%release_qa.OPS[4],'')
                return s,final,mime,body
            return result
        with patch.object(release_qa,'get',side_effect=broken): report=release_qa.run(SITE)
        self.assertFalse(report['pass'])
        self.assertTrue(any('Missing language switch: de' in e for e in report['errors']))

    def test_missing_ops_evidence_interlink_fails_closed(self):
        with patch.object(release_qa,'get',side_effect=lambda u: fake_fetch(u,missing_interlink=True)): report=release_qa.run(SITE)
        self.assertFalse(report['pass']); self.assertTrue(any('Missing Evidence checklist interlink' in e for e in report['errors']))

if __name__=='__main__': main()
