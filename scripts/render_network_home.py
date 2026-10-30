#!/usr/bin/env python3
"""Render the five network entrance pages from their shared content source."""

from __future__ import annotations

import argparse
import html
import json
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ORIGIN = "https://ziontechgroup.com"
DATA = ROOT / "_data" / "network-home.json"


def esc(value: str) -> str:
    return html.escape(value, quote=True)


class PageContract(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []
        self.fragments: list[str] = []
        self.h1_count = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if attributes.get("id"):
            self.ids.append(attributes["id"])
        if tag == "h1":
            self.h1_count += 1
        if tag == "a" and (attributes.get("href") or "").startswith("#"):
            self.fragments.append(attributes["href"][1:])


def render(data: dict, language: dict) -> str:
    code = language["code"]
    copy = data["locales"][code]
    routes = data["routes"][code]
    canonical = ORIGIN + language["path"]

    def link(route: str, label: str, css_class: str = "") -> str:
        class_attr = f' class="{esc(css_class)}"' if css_class else ""
        return f'<a{class_attr} href="{esc(routes[route])}">{esc(label)}</a>'

    def resource_card(item: dict) -> str:
        heading_id = item.get("heading_id", item["id"] + "-heading")
        return (
            f'<article class="card resource-card" id="{esc(item["id"])}" '
            f'aria-labelledby="{esc(heading_id)}">'
            f'<h3 id="{esc(heading_id)}">{esc(item["title"])}</h3>'
            f'<p>{esc(item["description"])}</p>'
            f'<div class="card-links">{link(item["route"], item["label"])}</div></article>'
        )

    alternates = "\n".join(
        f'<link rel="alternate" hreflang="{esc(item["lang"])}" '
        f'href="{ORIGIN}{esc(item["path"])}">'
        for item in data["languages"]
    )
    language_links = "".join(
        f'<a href="{esc(item["path"])}" lang="{esc(item["lang"])}" '
        f'hreflang="{esc(item["lang"])}"'
        + (' aria-current="page"' if item["code"] == code else "")
        + f'>{esc(item["name"])}</a>'
        for item in data["languages"]
    )
    # These visible guide links retain all five historical language fragments.
    starting_links = "".join(
        f'<a id="start-here-{esc(item["code"])}" '
        f'href="{esc(data["routes"][item["code"]]["start_here"])}" '
        f'lang="{esc(item["lang"])}" hreflang="{esc(item["lang"])}">'
        f'{esc(item["name"])}</a>'
        for item in data["languages"]
    )
    steps = "".join(
        f'<li><span class="step-number" aria-hidden="true">0{index}</span>'
        f'<div><h3>{esc(item["title"])}</h3><p>{esc(item["body"])}</p></div></li>'
        for index, item in enumerate(copy["hero_steps"], 1)
    )
    paths = "".join(
        '<article class="card path-card">'
        f'<span class="path-number" aria-hidden="true">0{index}</span>'
        f'<h3>{esc(item["title"])}</h3><p>{esc(item["description"])}</p>'
        '<div class="path-links">'
        + "".join(link(entry["route"], entry["label"]) for entry in item["links"])
        + "</div></article>"
        for index, item in enumerate(copy["paths"], 1)
    )
    resources = "\n".join(resource_card(item) for item in copy["resources"])
    collections = "\n".join(resource_card(item) for item in copy["collections"])
    structured_data = json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "CollectionPage",
            "name": copy["meta_title"],
            "description": copy["meta_description"],
            "url": canonical,
            "inLanguage": language["lang"],
        },
        ensure_ascii=False,
    ).replace("<", "\\u003c")
    return f'''<!doctype html>
<html lang="{esc(language['lang'])}">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(copy['meta_title'])}</title>
<meta name="description" content="{esc(copy['meta_description'])}"><meta name="robots" content="index,follow">
<link rel="canonical" href="{canonical}">
{alternates}
<link rel="alternate" hreflang="x-default" href="{ORIGIN}/zion-app-network/">
<meta property="og:title" content="{esc(copy['meta_title'])}"><meta property="og:description" content="{esc(copy['meta_description'])}">
<meta property="og:url" content="{canonical}"><meta property="og:type" content="website">
<link rel="stylesheet" href="/zion-app-network/assets/network-guides.css">
<link rel="stylesheet" href="/zion-app-network/assets/network-home.css">
<script type="application/ld+json">{structured_data}</script>
</head>
<body class="network-home" data-network-home="{esc(data['release'])}">
<a class="skip" href="#main">{esc(copy['skip'])}</a>
<header class="home-header">
<div class="wrap top"><a class="brand" href="{esc(routes['home'])}">Zion Tech Group<span>{esc(copy['network_label'])}</span></a>
<nav aria-label="{esc(copy['nav_label'])}">{link('home', copy['labels']['home'])}{link('catalog', copy['labels']['catalog'])}{link('guides', copy['labels']['guides'])}{link('discovery', copy['labels']['discovery'])}</nav></div>
<nav class="wrap languages" aria-label="{esc(copy['language_label'])}">{language_links}</nav>
</header>
<main class="wrap" id="main" tabindex="-1">
<section class="home-hero" id="network-start-here" aria-labelledby="network-start-title">
<div class="hero-copy"><p class="eyebrow">{esc(copy['eyebrow'])}</p><h1 id="network-start-title">{esc(copy['title'])}</h1>
<p class="lead">{esc(copy['intro'])}</p><div class="actions">{link('catalog', copy['primary'], 'button')}{link('discovery', copy['secondary'], 'secondary-button')}</div></div>
<aside class="hero-panel" aria-labelledby="hero-panel-title"><h2 id="hero-panel-title">{esc(copy['hero_panel_title'])}</h2><ol class="hero-steps">{steps}</ol></aside>
</section>
<nav class="section-nav" aria-label="{esc(copy['page_nav_label'])}"><a href="#app-network-start-here-2026">{esc(copy['paths_nav'])}</a><a href="#resources">{esc(copy['resources_nav'])}</a><a href="#showcases-2026">{esc(copy['collections_nav'])}</a><a href="#network-languages">{esc(copy['language_label'])}</a></nav>
<section class="section" id="app-network-start-here-2026" aria-labelledby="app-network-start-here-heading">
<div class="section-heading"><p class="eyebrow">{esc(copy['paths_eyebrow'])}</p><h2 id="app-network-start-here-heading">{esc(copy['paths_title'])}</h2><p class="section-intro">{esc(copy['paths_intro'])}</p></div>
<div class="path-grid">{paths}</div></section>
<section class="section" id="resources" aria-labelledby="resources-title"><div class="section-heading"><p class="eyebrow">{esc(copy['resources_eyebrow'])}</p><h2 id="resources-title">{esc(copy['resources_title'])}</h2><p class="section-intro">{esc(copy['resources_intro'])}</p></div>
<div class="resource-grid">{resources}</div></section>
<section class="section" id="showcases-2026" aria-labelledby="collections-title"><div class="section-heading"><p class="eyebrow">{esc(copy['collections_eyebrow'])}</p><h2 id="collections-title">{esc(copy['collections_title'])}</h2><p class="section-intro">{esc(copy['collections_intro'])}</p></div>
<div class="collection-grid">{collections}</div><div class="actions">{link('guides', copy['all_guides'], 'secondary-button')}{link('directory', copy['labels']['directory'])}</div></section>
<section class="section language-section" id="network-languages" aria-labelledby="network-languages-title"><div><h2 id="network-languages-title">{esc(copy['language_title'])}</h2><p>{esc(copy['language_intro'])}</p></div><nav class="directory-languages" aria-label="{esc(copy['start_languages_label'])}">{starting_links}</nav></section>
<section class="section discovery-banner" aria-labelledby="discovery-title"><div><p class="eyebrow">{esc(copy['labels']['discovery'])}</p><h2 id="discovery-title">{esc(copy['discovery_title'])}</h2><p>{esc(copy['discovery_intro'])}</p><p class="delivery-note">{esc(copy['discovery_note'])}</p></div><div class="actions">{link('discovery', copy['secondary'], 'button')}</div></section>
</main>
<footer><div class="wrap"><p>{esc(copy['footer_summary'])}</p><nav aria-label="{esc(copy['footer_nav_label'])}">{link('home', copy['labels']['home'])}{link('catalog', copy['labels']['catalog'])}{link('guides', copy['labels']['guides'])}{link('directory', copy['labels']['directory'])}</nav><div class="footer-bottom"><span>Zion Tech Group</span>{link('history', copy['history_label'])}</div></div></footer>
</body>
</html>
'''


def verify(page: str, data: dict, language: dict) -> None:
    contract = PageContract()
    contract.feed(page)
    duplicates = [item for item, count in Counter(contract.ids).items() if count > 1]
    missing = set(data["legacy_fragment_ids"]) - set(contract.ids)
    broken = set(contract.fragments) - set(contract.ids)
    if duplicates or missing or broken or contract.h1_count != 1:
        raise ValueError(
            f'{language["code"]}: duplicate IDs {duplicates}; missing legacy IDs '
            f'{sorted(missing)}; broken fragments {sorted(broken)}; h1 count {contract.h1_count}'
        )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check generated pages without writing them.")
    args = parser.parse_args()
    data = json.loads(DATA.read_text(encoding="utf-8"))
    expected = {"en", "pt", "es", "fr", "de"}
    if set(data["locales"]) != expected or set(data["routes"]) != expected:
        raise ValueError("Every published locale must have complete content and routes.")
    mismatches = []
    for language in data["languages"]:
        page = render(data, language)
        verify(page, data, language)
        target = ROOT / language["file"]
        if args.check:
            if not target.exists() or target.read_text(encoding="utf-8") != page:
                mismatches.append(language["file"])
        else:
            target.write_text(page, encoding="utf-8")
    if mismatches:
        print("Generated pages need updating: " + ", ".join(mismatches))
        return 1
    verb = "Checked" if args.check else "Rendered"
    print(f"{verb} {len(data['languages'])} network entrance pages; {len(data['legacy_fragment_ids'])} legacy fragments retained per page.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
