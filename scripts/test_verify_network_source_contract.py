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
    return f'<html lang="{mod.LANGS[i]}"><head><link rel="canonical" href="{mod.SITE}{route}">{alts}</head><body><h1>{family} {mod.LANGS[i]}</h1>{links}</body></html>'

class SourceContractTests(TestCase):
    def fixture(self,mutate=None):
        td=tempfile.TemporaryDirectory(); root=Path(td.name)
        for family,entries in mod.FAMILIES.items():
            for i,(filename,_) in enumerate(entries):
                body=html(family,i)
                if mutate:
                    body=mutate(family,i,filename,body)
                (root/filename).write_text(body,encoding='utf-8')
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

if __name__=='__main__': main()
