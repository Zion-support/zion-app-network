import unittest
from pathlib import Path
from html.parser import HTMLParser
import yaml
from liquid import Environment

ROOT = Path(__file__).resolve().parents[1]
class Document(HTMLParser):
    def __init__(self, text):
        super().__init__(); self.tags=[]; self.feed(text)
    def handle_starttag(self, tag, attrs):
        self.tags.append((tag,dict(attrs)))
    def attrs(self, tag):
        return [a for t,a in self.tags if t==tag]

class DirectoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.layout=(ROOT/'_layouts/network_directory.html').read_text()
        cls.template=Environment().from_string(cls.layout)
        cls.pages={loc:yaml.safe_load((ROOT/f'directory-{loc}.html').read_text().split('---',2)[1]) for loc in ['en','pt','es','fr','de']}
    def render(self,page): return self.template.render(page=page)
    def test_all_locales_render_without_liquid_tokens(self):
        for loc,page in self.pages.items():
            with self.subTest(locale=loc):
                html=self.render(page);self.assertNotIn('{{',html);self.assertNotIn('{%',html)
    def test_one_main_and_h1_per_locale(self):
        for page in self.pages.values():
            d=Document(self.render(page)); self.assertEqual(len(d.attrs('main')),1);self.assertEqual(len(d.attrs('h1')),1)
    def test_language_links_and_current_marker(self):
        for page in self.pages.values():
            d=Document(self.render(page));links=[a for a in d.attrs('a') if 'hreflang' in a]
            self.assertEqual({a['lang'] for a in links},{'en','pt-BR','es','fr','de'})
            self.assertTrue(all(a['lang']==a['hreflang'] for a in links))
            current=[a for a in links if a.get('aria-current')=='page'];self.assertEqual(len(current),1);self.assertEqual(current[0]['lang'],page['lang'])
    def test_canonical_and_alternates_preserved(self):
        for page in self.pages.values():
            links=Document(self.render(page)).attrs('link')
            self.assertEqual([a['href'] for a in links if a.get('rel')=='canonical'],['https://ziontechgroup.com/zion-app-network/directory-'+page['locale']+'.html'])
            self.assertEqual(len([a for a in links if a.get('rel')=='alternate']),6)
    def test_every_nav_has_a_localized_label(self):
        for page in self.pages.values():
            navs=Document(self.render(page)).attrs('nav');self.assertEqual(len(navs),4)
            self.assertTrue(all(a.get('aria-label') for a in navs))
    def test_four_existing_cards_and_three_service_cards(self):
        for page in self.pages.values():
            self.assertEqual(len(Document(self.render(page)).attrs('article')),7)
    def test_scoped_service_content_and_distinct_translations(self):
        self.assertEqual(len({p['services']['heading'] for p in self.pages.values()}),5)
        for page in self.pages.values():
            self.assertEqual(len(page['services']['cards']),3);self.assertTrue(page['services']['note'])
    def test_evidence_route_matches_localized_checklist(self):
        for loc,page in self.pages.items():
            suffix='' if loc=='en' else '-'+('pt-br' if loc=='pt' else loc)
            self.assertEqual(page['routes'][3],'/zion-app-network/app-network-operations-evidence-checklist-2026'+suffix+'.html')
    def test_discovery_link_is_localized(self):
        for page in self.pages.values():
            links=Document(self.render(page)).attrs('a');self.assertIn(page['prefix']+'discovery/',[a.get('href') for a in links])
    def test_no_forms_scripts_or_checkout_added(self):
        for page in self.pages.values():
            d=Document(self.render(page));self.assertEqual(d.attrs('form'),[]);self.assertEqual(d.attrs('script'),[])
            self.assertFalse(any('stripe' in a.get('href','').lower() for a in d.attrs('a')))
    def test_malicious_content_is_escaped(self):
        import copy
        page=copy.deepcopy(self.pages['en']);page['services']['heading']='<script>alert(1)</script>'
        html=self.render(page);self.assertIn('&lt;script&gt;',html);self.assertEqual(Document(html).attrs('script'),[])
    def test_missing_optional_services_does_not_add_empty_section(self):
        import copy
        page=copy.deepcopy(self.pages['en']);del page['services']
        html=self.render(page);self.assertNotIn('id="service-planning-title"',html);self.assertEqual(len(Document(html).attrs('main')),1)
if __name__=='__main__': unittest.main(verbosity=2)
