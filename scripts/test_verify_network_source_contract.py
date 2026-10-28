#!/usr/bin/env python3
import importlib.util
import tempfile
from pathlib import Path
from unittest import TestCase, main

SCRIPT=Path(__file__).with_name('verify_network_source_contract.py')
spec=importlib.util.spec_from_file_location('source_contract',SCRIPT)
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)

def html(family,i):
    entries=mod.FAMILIES[family]
    routes=[r for _,r in entries]
    route=routes[i]
    other='evidence' if family=='ops' else 'ops'
    other_route=mod.FAMILIES[other][i][1]
    alts=''.join(f'<link rel="alternate" hreflang="{lang}" href="{mod.SITE}{target}">' for lang,target in zip(mod.LANGS,routes))
    alts+=f'<link rel="alternate" hreflang="x-default" href="{mod.SITE}{routes[0]}">'
    links=''.join(f'<a href="{target}">{lang}</a>' for lang,target in zip(mod.LANGS,routes))
    links+=f'<a href="{mod.localized_discovery(i)}">Discovery</a><a href="{other_route}">Sibling</a>'
    if family in ('batch96','q4'):
        sibling='q4' if family=='batch96' else 'batch96'
        sibling_route=mod.FAMILIES[sibling][i][1]
        links+=f'<a href="{sibling_route}">Related showcase</a>'
    extra=''
    if family=='quote':
        evidence=mod.FAMILIES['evidence'][i][1]
        pilot='/zion-app-network/app-to-pilot-paths-2026'+(['','-pt-br','-es','-fr','-de'][i])+'.html'
        links+=f'<a href="{evidence}">Evidence</a><a href="{pilot}">Pilot</a>'
        ids=['calculate','copy','brief','total','floor','add','currency','labor',
             'travel','parts','tax','other','country','asset','service','window']
        extra=''.join(f'<span id="{element}"></span>' for element in ids)
        extra+='<script>const minimum=Math.ceil(total*1.4*100)/100; const increment=minimum-total;</script>'
    return f'<html lang="{mod.LANGS[i]}"><head><link rel="canonical" href="{mod.SITE}{route}">{alts}</head><body><h1>{family} {mod.LANGS[i]}</h1>{links}{extra}</body></html>'

class SourceContractTests(TestCase):
    def fixture(self,mutate=None):
        td=tempfile.TemporaryDirectory(); root=Path(td.name)
        for family,entries in mod.FAMILIES.items():
            for i,(filename,_) in enumerate(entries):
                body=html(family,i)
                if mutate:
                    body=mutate(family,i,filename,body)
                path=root/filename
                path.parent.mkdir(parents=True,exist_ok=True)
                path.write_text(body,encoding='utf-8')
        routes=['en','pt','es','fr','de']
        blocks=[]
        for i,slug in enumerate(routes):
            quote_name=mod.FAMILIES['quote'][i][0]
            blocks.append(f'<a id="start-here-{slug}"></a>\n## Locale {slug}\n'
                          f'- [Quote worksheet]({quote_name})\n')
        catalog=('# Zion App Network — catalog navigation\n\n'
                 +''.join(blocks)+'\n**Public-route discrepancy:** public Discovery paths must be verified before release.\n')
        (root/'CATALOG-NAVIGATION.md').write_text(catalog,encoding='utf-8')
        task='<html lang="en"><body><h1>Tasks</h1>'+(
            '<a href="/zion-app-network/supplier-evidence.html">Evidence</a>'*5
        )+'</body></html>'
        (root/'task-paths.html').write_text(task,encoding='utf-8')
        return td,root
    def test_valid_family_passes(self):
        td,root=self.fixture()
        try: self.assertEqual(mod.verify(root),[])
        finally: td.cleanup()
    def test_missing_locale_file_fails(self):
        td,root=self.fixture()
        try:
            (root/mod.FAMILIES['ops'][4][0]).unlink()
            self.assertTrue(any('missing source file' in e for e in mod.verify(root)))
        finally: td.cleanup()
    def test_wrong_canonical_fails(self):
        def mutate(family,i,filename,body):
            if family=='evidence' and i==2:
                return body.replace('rel="canonical" href="','rel="canonical" href="https://invalid.example/')
            return body
        td,root=self.fixture(mutate)
        try: self.assertTrue(any('canonical must be exactly' in e for e in mod.verify(root)))
        finally: td.cleanup()
    def test_current_language_label_without_self_link_is_valid(self):
        def mutate(family,i,filename,body):
            _,route=mod.FAMILIES[family][i]
            return body.replace(f'<a href="{route}">{mod.LANGS[i]}</a>',
                                f'<span aria-current="page">{mod.LANGS[i]}</span>')
        td,root=self.fixture(mutate)
        try: self.assertEqual(mod.verify(root),[])
        finally: td.cleanup()

    def test_missing_foreign_language_switch_fails(self):
        def mutate(family,i,filename,body):
            if family=='ops' and i==0:
                target=mod.FAMILIES[family][4][1]
                return body.replace(f'<a href="{target}">{mod.LANGS[4]}</a>','')
            return body
        td,root=self.fixture(mutate)
        try: self.assertTrue(any('missing language switch to' in e for e in mod.verify(root)))
        finally: td.cleanup()

    def test_missing_interlink_fails(self):
        def mutate(family,i,filename,body):
            if family=='ops' and i==1:
                target=mod.FAMILIES['evidence'][i][1]
                return body.replace(f'<a href="{target}">Sibling</a>','')
            return body
        td,root=self.fixture(mutate)
        try: self.assertTrue(any('missing matching Evidence' in e for e in mod.verify(root)))
        finally: td.cleanup()

    def test_quote_rejects_broken_40_percent_markup(self):
        def mutate(family,i,filename,body):
            if family=='quote' and i==3:
                return body.replace('total*1.4','total*1.3')
            return body
        td,root=self.fixture(mutate)
        try: self.assertTrue(any('minimum 40% markup' in e for e in mod.verify(root)))
        finally: td.cleanup()

    def test_quote_fails_when_markup_is_rounded_down(self):
        def mutate(family,i,filename,body):
            if family=='quote' and i==0:
                return body.replace('Math.ceil(', 'Math.round(')
            return body
        td,root=self.fixture(mutate)
        try:
            self.assertTrue(any('safe minimum 40% markup' in e for e in mod.verify(root)))
        finally: td.cleanup()

    def test_quote_requires_localized_free_discovery(self):
        def mutate(family,i,filename,body):
            if family=='quote' and i==1:
                return body.replace('href="/pt/discovery/"','href="/discovery/"')
            return body
        td,root=self.fixture(mutate)
        try: self.assertTrue(any('missing localized Discovery' in e for e in mod.verify(root)))
        finally: td.cleanup()

    def test_quote_blocks_network_operations(self):
        def mutate(family,i,filename,body):
            if family=='quote' and i==4:
                return body.replace('</script>','fetch("https://example.com")</script>')
            return body
        td,root=self.fixture(mutate)
        try: self.assertTrue(any('network operation' in e for e in mod.verify(root)))
        finally: td.cleanup()

    def test_catalog_requires_all_language_anchors(self):
        td,root=self.fixture()
        try:
            file=root/'CATALOG-NAVIGATION.md'
            file.write_text(file.read_text().replace('id="start-here-de"','id="missing-de"'))
            self.assertTrue(any('missing existing language anchor de' in e for e in mod.verify(root)))
        finally: td.cleanup()

    def test_duplicate_catalog_html_source_is_rejected(self):
        td,root=self.fixture()
        try:
            (root/'CATALOG-NAVIGATION.html').write_text('<html>Duplicate</html>',encoding='utf-8')
            self.assertTrue(any('duplicate HTML source' in e for e in mod.verify(root)))
        finally: td.cleanup()

    def test_supplier_links_must_target_real_hub(self):
        td,root=self.fixture()
        try:
            file=root/'task-paths.html'
            file.write_text(file.read_text().replace(
                '/zion-app-network/supplier-evidence.html',
                '/zion-app-network/CATALOG-SUPPLIER-EVIDENCE.html'))
            self.assertTrue(any('legacy unresolved supplier catalog' in e for e in mod.verify(root)))
        finally: td.cleanup()

    def test_showcase_requires_reciprocal_links(self):
        def mutate(family,i,filename,body):
            if family=='batch96' and i==2:
                path=mod.FAMILIES['q4'][i][1]
                return body.replace(f'<a href="{path}">Related showcase</a>','')
            return body
        td,root=self.fixture(mutate)
        try:
            self.assertTrue(any('missing matching Q4 showcase' in e for e in mod.verify(root)))
        finally: td.cleanup()

if __name__=='__main__': main()
