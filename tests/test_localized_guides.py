"""Publication contracts for the maintained guides and their original resources."""
import copy
import importlib.util
import json
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('guides',ROOT/'scripts/render_localized_guides.py')
guides=importlib.util.module_from_spec(spec)
spec.loader.exec_module(guides)

class Page(HTMLParser):
    def __init__(self,text):
        super().__init__(convert_charrefs=True)
        self.tags=[]
        self.feed(text)
    def handle_starttag(self,tag,attrs):
        self.tags.append((tag,dict(attrs)))
    def find(self,tag):
        return [attrs for t,attrs in self.tags if t==tag]

class LocalizedGuideTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.models=guides.load_guides()
        cls.original=json.loads((ROOT/'tests/fixtures/guide-original-destinations.json').read_text())

    def test_all_five_families_have_complete_distinct_translations(self):
        self.assertEqual({g['id'] for g in self.models},{'catalog-navigation','green-education','infrastructure','govtech','legal-ops'})
        for model in self.models:
            for locale in guides.LOCALES:
                c=model['locales'][locale]
                for field in ('title','description','intro','scope'):
                    self.assertGreater(len(c[field]),15)
                    if locale!='en':
                        self.assertNotEqual(c[field],model['locales']['en'][field])
                self.assertGreaterEqual(len(c['steps']),3)
                self.assertGreater(len(c['example']['body']),70)
                self.assertEqual(len({s['id'] for s in c['sections']}),len(c['sections']))
                self.assertEqual(set(guides.UI[locale]),set(guides.UI['en']))

    def test_original_app_destinations_survive_in_every_language(self):
        for model in self.models:
            if model['id'] not in self.original:
                continue
            for locale in guides.LOCALES:
                hrefs={r['href'] for s in model['locales'][locale]['sections'] for r in s['resources']}
                self.assertTrue(set(self.original[model['id']])<=hrefs,(model['id'],locale))

    def test_published_files_have_reciprocal_metadata_and_accessible_structure(self):
        for model in self.models:
            for locale in guides.LOCALES:
                text=(ROOT/guides.local_path(model,locale)).read_text()
                self.assertEqual(text,guides.render(model,locale,self.models),'Generated file differs from its model')
                p=Page(text)
                self.assertEqual(p.find('html')[0]['lang'],guides.UI[locale]['lang'])
                self.assertEqual(len(p.find('h1')),1)
                self.assertEqual(len(p.find('main')),1)
                self.assertEqual(p.find('main')[0]['id'],'main')
                ids=[a['id'] for _,a in p.tags if 'id' in a]
                self.assertEqual(len(ids),len(set(ids)))
                self.assertEqual([a['href'] for a in p.find('link') if a.get('rel')=='canonical'],[guides.ORIGIN+guides.route(model,locale)])
                alt={a['hreflang']:a['href'] for a in p.find('link') if a.get('rel')=='alternate'}
                self.assertEqual(len(alt),6)
                for target in guides.LOCALES:
                    self.assertEqual(alt[guides.UI[target]['lang']],guides.ORIGIN+guides.route(model,target))
                    self.assertTrue((ROOT/guides.local_path(model,target)).is_file())
                for anchor in p.find('a'):
                    if anchor['href'].startswith('#'):
                        self.assertIn(anchor['href'][1:],ids)
                self.assertFalse(p.find('form') or p.find('iframe'))
                self.assertTrue(all(s.get('type')=='application/ld+json' for s in p.find('script')))

    def test_shared_navigation_and_crosslinks_keep_the_selected_language(self):
        for model in self.models:
            for locale in guides.LOCALES:
                p=Page(guides.render(model,locale,self.models))
                hrefs={a['href'] for a in p.find('a')}
                prefix='/' if locale=='en' else '/'+locale+'/'
                self.assertIn(prefix+'apps/',hrefs)
                self.assertIn(prefix+'discovery/',hrefs)
                self.assertIn('/zion-app-network/directory-'+locale+'.html',hrefs)
                for sibling in self.models:
                    if sibling['id']!=model['id']:
                        self.assertIn(guides.route(sibling,locale),hrefs)

    def test_every_internal_network_destination_exists(self):
        for model in self.models:
            for locale in guides.LOCALES:
                for anchor in Page(guides.render(model,locale,self.models)).find('a'):
                    url=urlsplit(anchor['href'])
                    if url.netloc not in ('','ziontechgroup.com') or not url.path.startswith('/zion-app-network/'):
                        continue
                    path=ROOT/url.path.removeprefix('/zion-app-network/')
                    if url.path.endswith('/'):
                        path=path/'index.html'
                    if not path.is_file() and path.suffix=='.html':
                        path=path.with_suffix('.md')
                    self.assertTrue(path.is_file(),(model['id'],locale,anchor['href']))

    def test_text_is_escaped_and_unsafe_urls_are_rejected(self):
        original=self.models[0]
        model=copy.deepcopy(original)
        model['locales']['en']['intro']='<img src=x onerror=alert(1)> & "test"'
        text=guides.render(model,'en',self.models)
        self.assertIn('&lt;img src=x onerror=alert(1)&gt;',text)
        self.assertNotIn('<img src=x',text)
        for url in ('javascript:alert(1)','//example.com/','https://example.com/unverified'):
            with self.assertRaises(ValueError):
                guides.valid_href(url)

    def test_discovery_copy_does_not_reintroduce_price_or_delivery_guarantees(self):
        for model in self.models:
            for locale in guides.LOCALES:
                text=guides.render(model,locale,self.models).lower()
                for claim in ('$99','830+','890+','instant dual','same-day follow-up'):
                    self.assertNotIn(claim,text)

if __name__=='__main__':
    unittest.main()
