#!/usr/bin/env python3
"""Offline contract tests for multilingual release QA. No network or form submits."""
import importlib.util
from pathlib import Path
from unittest import TestCase, main
from unittest.mock import patch
from urllib.parse import urlparse

SCRIPT = Path(__file__).with_name('verify-network-release.py')
spec = importlib.util.spec_from_file_location('release_qa', SCRIPT)
release_qa = importlib.util.module_from_spec(spec)
spec.loader.exec_module(release_qa)
SITE = 'https://ziontechgroup.com'


def page(route, bad_alternate=False):
    if route in release_qa.HOME:
        pos = release_qa.HOME.index(route)
        locale = [1, 0, 2, 3, 4][pos]
        links = [release_qa.FIELD[locale], release_qa.BATCH[locale]]
        return ('<html lang="%s"><head><link rel="stylesheet" href="/styles/app.css"></head>'
                '<body><h1>Home %d</h1><section data-batch113-promo="1"></section>%s</body></html>' %
                (release_qa.LANGS[locale], pos, ''.join('<a href="%s">Link</a>' % x for x in links)))
    group = 'field' if route in release_qa.FIELD else 'batch'
    family = release_qa.FIELD if group == 'field' else release_qa.BATCH
    i = family.index(route)
    alt = [(lang, SITE + target) for lang, target in zip(release_qa.LANGS, family)]
    if bad_alternate and group == 'field' and i == 2:
        alt[3] = ('fr', SITE + '/incorrect-fr')
    alternates = ''.join('<link rel="alternate" hreflang="%s" href="%s">' % (lang, target) for lang, target in alt)
    alternates += '<link rel="alternate" hreflang="x-default" href="%s">' % (SITE + family[0])
    discovery = '/discovery/' if i == 0 else '/' + ('pt' if i == 1 else release_qa.LANGS[i]) + '/discovery/'
    links = family + [discovery]
    if group == 'batch':
        links.append(release_qa.FIELD[i])
    return ('<html lang="%s"><head><link rel="canonical" href="%s">%s'
            '<link rel="stylesheet" href="/styles/app.css"></head><body><h1>%s %d</h1>'
            '<section data-field-evidence-gates="1"></section>%s</body></html>' %
            (release_qa.LANGS[i], SITE + route, alternates, group, i,
             ''.join('<a href="%s">Go</a>' % url for url in links)))


def fake_fetch(url, bad_alternate=False, outage=None):
    route = urlparse(url).path
    if route == '/styles/app.css':
        return 200, url, 'text/css', 'body { color: black; }'
    if outage == route:
        raise OSError('simulated outage')
    if route not in set(release_qa.HOME + release_qa.FIELD + release_qa.BATCH):
        raise AssertionError('Unexpected network request ' + url)
    return 200, url, 'text/html', page(route, bad_alternate=bad_alternate)


class OfflineReleaseQATests(TestCase):
    def test_all_15_pages_and_css_pass_valid_fixture(self):
        with patch.object(release_qa, 'get', side_effect=fake_fetch):
            report = release_qa.run(SITE)
        self.assertTrue(report['pass'], report['errors'])
        self.assertEqual(len(report['pages']), 15)
        self.assertEqual(len(report['assets']), 1)
        self.assertEqual(report['errors'], [])

    def test_mismatched_hreflang_fails_closed(self):
        with patch.object(release_qa, 'get', side_effect=lambda u: fake_fetch(u, bad_alternate=True)):
            report = release_qa.run(SITE)
        self.assertFalse(report['pass'])
        self.assertTrue(any('Wrong or duplicate hreflang: fr' in error for error in report['errors']))

    def test_http_failure_fails_closed_without_crashing(self):
        with patch.object(release_qa, 'get', side_effect=lambda u: fake_fetch(u, outage=release_qa.FIELD[4])):
            report = release_qa.run(SITE)
        self.assertFalse(report['pass'])
        self.assertTrue(any('simulated outage' in error for error in report['errors']))


if __name__ == '__main__':
    main()
