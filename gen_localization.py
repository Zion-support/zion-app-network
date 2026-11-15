import os

WORK = '/Users/miami2/.hermes/profiles/agent-finops-ops/cache/apphub'
os.makedirs(WORK, exist_ok=True)

BASE = 'https://ziontechgroup.com/zion-app-network/app'
CANON = f'{BASE}/app-network-multilingual-localization-2026.html'
L = {
    'pt': f'{BASE}/app-network-multilingual-localization-2026-pt.html',
    'es': f'{BASE}/app-network-multilingual-localization-2026-es.html',
    'fr': f'{BASE}/app-network-multilingual-localization-2026-fr.html',
    'de': f'{BASE}/app-network-multilingual-localization-2026-de.html',
}
LANGS = [('en', CANON), ('pt-BR', L['pt']), ('es', L['es']), ('fr', L['fr']), ('de', L['de'])]

BODY = {
    'en': {
        'langbar': '<nav class="langbar">🌐 <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-multilingual-localization-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-multilingual-localization-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-multilingual-localization-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-multilingual-localization-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-multilingual-localization-2026-de.html">Deutsch</a></nav>',
        'title': 'Multilingual Localization Hub — Global Expansion & 5-Language Standard — Zion Tech Group',
        'description': 'Free Multilingual Localization Hub: hreflang standard, per-language content matrix, translation toolkit, and SEO-per-language playbook — the living standard for Zion\'s 5-language network (EN/PT-BR/ES/FR/DE).',
        'h1': '🌐 Multilingual Localization Hub',
        'pitch': 'The living standard for global expansion. Home of the 5-language network (EN/PT-BR/ES/FR/DE): hreflang best practice, per-language content matrix, translation toolkit, per-language SEO (meta tags, JSON-LD, sitemap), and a cultural-localization checklist. Feeds the homepage advertising, client-facing SEO/GEO services (Batch 120), and global expansion opportunities.',
        'cards': [
            ('🌐 hreflang Standard', 'Canonical URL convention, hreflang alternates (en, pt-BR, es, fr, de), x-default, per-language SEO meta tags — the Zion standard.', 'https://ziontechgroup.com/multilingual-localization/', 'https://github.com/Zion-support/zion-multilingual-localization'),
            ('📋 Per-Language Content Matrix', 'Which apps translate, which don\'t, and exactly how to translate them — the deployment map for every app in the network.', 'https://ziontechgroup.com/multilingual-localization/', 'https://github.com/Zion-support/zion-multilingual-localization'),
            ('🔧 Translation Toolkit', 'Open-source + paid paths (DeepL, Weglot, WordPress multilanguage, Smartling) with translation-memory and glossary guidance.', 'https://ziontechgroup.com/multilingual-localization/', 'https://github.com/Zion-support/zion-multilingual-localization'),
            ('📈 SEO per Language', 'Localised meta tags, JSON-LD, per-locale sitemap registration — so every language ranks in its own search engine.', 'https://ziontechgroup.com/multilingual-localization/', 'https://github.com/Zion-support/zion-multilingual-localization'),
            ('🌍 Localisation Checklist', 'Cultural adaptation, date/number formatting, legal disclaimers per market — so content feels local, not translated.', 'https://ziontechgroup.com/multilingual-localization/', 'https://github.com/Zion-support/zion-multilingual-localization'),
            ('🔁 Discovery Handoff', 'Localization plan → agent marketplace (Batch 117) + SEO/GEO sprint (Batch 120).', 'https://ziontechgroup.com/multilingual-localization/', 'https://github.com/Zion-support/zion-multilingual-localization'),
        ],
        'discovery_h2': '🧭 Free Discovery — always online, always free',
        'discovery_p': 'Give every city we serve our content — in their language, with their search terms, so they find us first. Your 5-language rollout plan is generated instantly and emailed to you and our commercial team (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Start Free Discovery',
        'discovery_cta2': 'Browse the App Network',
    },
    'pt': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-multilingual-localization-2026.html">English</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-multilingual-localization-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-multilingual-localization-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-multilingual-localization-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-multilingual-localization-2026-de.html">Deutsch</a></nav>',
        'title': 'Hub de Localização Multilíngue — Expansão Global e Padrão de 5 Idiomas — Zion Tech Group',
        'description': 'Hub gratuito de Localização Multilíngue: padrão hreflang, matriz de conteúdo por idioma, kit de tradução e playbook SEO por idioma — o padrão permanente para a rede 5-idioma da Zion (EN/PT-BR/ES/FR/DE).',
        'h1': '🌐 Hub de Localização Multilíngue',
        'pitch': 'O padrão permanente para expansão global. Casa da rede 5-idioma (EN/PT-BR/ES/FR/DE): melhor prática hreflang, matriz de conteúdo por idioma, kit de tradução, SEO por idioma (metadados, JSON-LD, sitemap), e um checklist de localização cultural. Alimenta a publicidade da homepage, os serviços SEO/GEO para clientes (Lote 120) e as oportunidades de expansão global.',
        'cards': [
            ('🌐 Padrão hreflang', 'Convenção de URL canônica, alternativas hreflang (en, pt-BR, es, fr, de), x-default, metadados SEO por idioma — o padrão Zion.', 'https://ziontechgroup.com/multilingual-localization/', 'https://github.com/Zion-support/zion-multilingual-localization'),
            ('📋 Matriz de Conteúdo por Idioma', 'Quais aplicativos traduzem, quais não, e como traduzi-los exatamente — o mapa de implantação para cada aplicativo na rede.', 'https://ziontechgroup.com/multilingual-localization/', 'https://github.com/Zion-support/zion-multilingual-localization'),
            ('🔧 Kit de Tradução', 'Caminhos open-source + pago (DeepL, Weglot, WordPress multilíngue, Smartling) com orientação de memória de tradução e glossário.', 'https://ziontechgroup.com/multilingual-localization/', 'https://github.com/Zion-support/zion-multilingual-localization'),
            ('📈 SEO por Idioma', 'Metadados localizados, JSON-LD, registro de sitemap por localidade — para que cada idioma classifique em seu próprio motor de busca.', 'https://ziontechgroup.com/multilingual-localization/', 'https://github.com/Zion-support/zion-multilingual-localization'),
            ('🌍 Checklist de Localização', 'Adaptação cultural, formatação de datas/números, avisos legais por mercado — para que o conteúdo pareça local, não traduzido.', 'https://ziontechgroup.com/multilingual-localization/', 'https://github.com/Zion-support/zion-multilingual-localization'),
            ('🔁 Mão de Obra de Descoberta', 'Plano de localização → marketplace de agentes (Lote 117) + sprint SEO/GEO (Lote 120).', 'https://ziontechgroup.com/multilingual-localization/', 'https://github.com/Zion-support/zion-multilingual-localization'),
        ],
        'discovery_h2': '🧭 Descoberta Gratuita — sempre online, sempre gratuita',
        'discovery_p': 'Dê a cada cidade que atendemos nosso conteúdo — no seu idioma, com seus termos de pesquisa, para que nos encontrem primeiro. Seu plano de implementação 5-idioma é gerado instantaneamente e enviado por e-mail para você e nossa equipe comercial (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Iniciar Descoberta Gratuita',
        'discovery_cta2': 'Navegar pela Rede de Aplicativos',
    },
    'es': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-multilingual-localization-2026.html">English</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-multilingual-localization-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-multilingual-localization-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-multilingual-localization-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-multilingual-localization-2026-de.html">Deutsch</a></nav>',
        'title': 'Hub de Localización Multilingüe — Expansión Global y Estándar de 5 Idiomas — Zion Tech Group',
        'description': 'Hub gratuito de Localización Multilingüe: estándar hreflang, matriz de contenido por idioma, kit de traducción y playbook SEO por idioma — el estándar permanente para la red 5-idioma de la Zion (EN/PT-BR/ES/FR/DE).',
        'h1': '🌐 Hub de Localización Multilingüe',
        'pitch': 'El estándar permanente para expansión global. Casa de la red 5-idioma (EN/PT-BR/ES/FR/DE): mejor práctica hreflang, matriz de contenido por idioma, kit de traducción, SEO por idioma (metadatos, JSON-LD, sitemap), y un checklist de localización cultural. Alimenta la publicidad de la homepage, los servicios SEO/GEO para clientes (Lote 120) y las oportunidades de expansión global.',
        'cards': [
            ('🌐 Estándar hreflang', 'Convención de URL canónica, alternativas hreflang (en, pt-BR, es, fr, de), x-default, metadatos SEO por idioma — el estándar Zion.', 'https://ziontechgroup.com/multilingual-localization/', 'https://github.com/Zion-support/zion-multilingual-localization'),
            ('📋 Matriz de Contenido por Idioma', 'Qué aplicaciones traducen, cuáles no, y cómo traducirlos exactamente — el mapa de implementación para cada aplicación en la red.', 'https://ziontechgroup.com/multilingual-localization/', 'https://github.com/Zion-support/zion-multilingual-localization'),
            ('🔧 Kit de Traducción', 'Caminos open-source + pago (DeepL, Weglot, WordPress multilingüe, Smartling) con orientación de memoria de traducción y glosario.', 'https://ziontechgroup.com/multilingual-localization/', 'https://github.com/Zion-support/zion-multilingual-localization'),
            ('📈 SEO por Idioma', 'Metadatos localizados, JSON-LD, registro de sitemap por localidad — para que cada idioma clasifique en su propio motor de búsqueda.', 'https://ziontechgroup.com/multilingual-localization/', 'https://github.com/Zion-support/zion-multilingual-localization'),
            ('🌍 Checklist de Localización', 'Adaptación cultural, formato de fechas/números, avisos legales por mercado — para que el contenido parezca local, no traducido.', 'https://ziontechgroup.com/multilingual-localization/', 'https://github.com/Zion-support/zion-multilingual-localization'),
            ('🔁 Mano de Obra de Descubrimiento', 'Plan de localización → marketplace de agentes (Lote 117) + sprint SEO/GEO (Lote 120).', 'https://ziontechgroup.com/multilingual-localization/', 'https://github.com/Zion-support/zion-multilingual-localization'),
        ],
        'discovery_h2': '🧭 Descubrimiento Gratuito — siempre en línea, siempre gratuito',
        'discovery_p': 'Dale a cada ciudad a la que atendemos nuestro contenido — en su idioma, con sus términos de búsqueda, para que nos encuentren primero. Su plan de implementación 5-idiomas se genera instantáneamente y se envía por correo a usted y a nuestro equipo comercial (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Comenzar Descubrimiento Gratuito',
        'discovery_cta2': 'Explorar la Red de Aplicaciones',
    },
    'fr': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-multilingual-localization-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-multilingual-localization-2026-fr.html">Français</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-multilingual-localization-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-multilingual-localization-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-multilingual-localization-2026-de.html">Deutsch</a></nav>',
        'title': 'Hub de Localisation Multilingue — Expansion Globale et Standard 5 Langues — Zion Tech Group',
        'description': 'Hub gratuit de Localisation Multilingue : standard hreflang, matrice de contenu par langue, kit de traduction et playbook SEO par langue — le standard vivant de la réseau 5 langues de la Zion (EN/PT-BR/ES/FR/DE).',
        'h1': '🌐 Hub de Localisation Multilingue',
        'pitch': 'Le standard vivant pour l\'expansion globale. Maison du réseau 5 langues (EN/PT-BR/ES/FR/DE) : meilleure pratique hreflang, matrice de contenu par langue, kit de traduction, SEO par langue (métadonnées, JSON-LD, sitemap), et une checklist de localisation culturelle. Alimente la publicité de la homepage, les services SEO/GEO pour clients (Lot 120) et les opportunités d\'expansion globale.',
        'cards': [
            ('🌐 Standard hreflang', 'Convention d\'URL canonique, alternatives hreflang (en, pt-BR, es, fr, de), x-default, métadonnées SEO par langue — le standard Zion.', 'https://ziontechgroup.com/multilingual-localization/', 'https://github.com/Zion-support/zion-multilingual-localization'),
            ('📋 Matrice de Contenu par Langue', 'Quelles applications traduisent, lesquelles non, et comment les traduire exactement — la carte de déploiement pour chaque application du réseau.', 'https://ziontechgroup.com/multilingual-localization/', 'https://github.com/Zion-support/zion-multilingual-localization'),
            ('🔧 Kit de Traduction', 'Pistes open-source + payantes (DeepL, Weglot, WordPress multilangue, Smartling) avec orientation mémoire de traduction et glossaire.', 'https://ziontechgroup.com/multilingual-localization/', 'https://github.com/Zion-support/zion-multilingual-localization'),
            ('📈 SEO par Langue', 'Métadonnées localisées, JSON-LD, enregistrement de sitemap par localité — pour que chaque langue figure dans son propre moteur de recherche.', 'https://ziontechgroup.com/multilingual-localization/', 'https://github.com/Zion-support/zion-multilingual-localization'),
            ('🌍 Checklist de Localisation', 'Adaptation culturelle, mise en forme des dates/nombres, mentions légales par marché — pour que le contenu paraisse local, pas traduit.', 'https://ziontechgroup.com/multilingual-localization/', 'https://github.com/Zion-support/zion-multilingual-localization'),
            ('🔁 Main d\'œuvre de Découverte', 'Plan de localisation → marketplace d\'agents (Lot 117) + sprint SEO/GEO (Lot 120).', 'https://ziontechgroup.com/multilingual-localization/', 'https://github.com/Zion-support/zion-multilingual-localization'),
        ],
        'discovery_h2': '🧭 Découverte Gratuite — toujours en ligne, toujours gratuite',
        'discovery_p': 'Donnez à chaque ville que nous desservons notre contenu — dans leur langue, avec leurs termes de recherche, pour qu\'ils nous trouvent en premier. Votre plan de déploiement 5 langues est généré instantanément et envoyé par e-mail à vous et à notre équipe commerciale (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Commencer la Découverte Gratuite',
        'discovery_cta2': 'Parcourir le Réseau d\'Applications',
    },
    'de': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-multilingual-localization-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-multilingual-localization-2026-de.html">Deutsch</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-multilingual-localization-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-multilingual-localization-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-multilingual-localization-2026-fr.html">Français</a></nav>',
        'title': 'Multiplattformlokalisierungs-HuB — Globale Expansion & 5-Sprach-Standard — Zion Tech Group',
        'description': 'Kostenloser Multiplattformlokalisierungs-HuB: hreflang-Standard, Inhaltsmatrix pro Sprache, Übersetzungstoolkit und SEO-Playbook pro Sprache — das lebendige Standard-Fenster für die 5-Sprach-Netzwerk der Zion (EN/PT-BR/ES/FR/DE).',
        'h1': '🌐 Multiplattformlokalisierungs-HuB',
        'pitch': 'Das lebendige Standardfenster für globale Expansion. Zuhause der 5-Sprach-Netzwerk (EN/PT-BR/ES/FR/DE): hreflang-Best Practice, Inhaltsmatrix pro Sprache, Übersetzungstoolkit, SEO pro Sprache (Meta-Tags, JSON-LD, Sitemap-Register), und eine kulturelle Lokalisierungs-Checkliste. Speist die Homepage-Werbung, die Kunden-SEO/GEO-Dienstleistungen (Zahl 120) und die globalen Expansions-Möglichkeiten.',
        'cards': [
            ('🌐 hreflang-Standard', 'Kanons-URL-Konvention, hreflang-Klappe (en, pt-BR, es, fr, de), x-default, SEO-Metadaten pro Sprache — das Zion-Standard.', 'https://ziontechgroup.com/multilingual-localization/', 'https://github.com/Zion-support/zion-multilingual-localization'),
            ('📋 Inhalts-Matrix pro Sprache', 'Welche Apps übersetzen, welche nicht, und wie genau man sie übersetzt — die Bereitstellungs-Karte für jede App im Netzwerk.', 'https://ziontechgroup.com/multilingual-localization/', 'https://github.com/Zion-support/zion-multilingual-localization'),
            ('🔧 Übersetzungstoolkit', 'Open-Source + kostenpflichtige Wege (DeepL, Weglot, WordPress Multiplattform, Smartling) mit Richtlinie von Übersetzungs-Durchsicht und Glossar.', 'https://ziontechgroup.com/multilingual-localization/', 'https://github.com/Zion-support/zion-multilingual-localization'),
            ('📈 SEO pro Sprache', 'Lokalisierte Meta-Tags, JSON-LD, Register des Sitemap pro Lokalität — damit jede Sprache in ihrer eigenen Suchmaschine sortiert wird.', 'https://ziontechgroup.com/multilingual-localization/', 'https://github.com/Zion-support/zion-multilingual-localization'),
            ('🌍 Lokalisierungs-Checkliste', 'Kulturelle Anpassung, Datums/Zahlen-Formatierung, rechtliche Stilmittel pro Markt — damit der Inhalt lokal, nicht übersetzt, wirkt.', 'https://ziontechgroup.com/multilingual-localization/', 'https://github.com/Zion-support/zion-multilingual-localization'),
            ('🔁 Entdeckungs-Handoff', 'Lokalisierungsplan → Agenten-Marktplatz (Zahl 117) + SEO/GEO-Sprint (Zahl 120).', 'https://ziontechgroup.com/multilingual-localization/', 'https://github.com/Zion-support/zion-multilingual-localization'),
        ],
        'discovery_h2': '🧭 Kostenloser Entdeckung — immer online, immer kostenlos',
        'discovery_p': 'Gewähren Sie jeder Stadt, die wir bedienen, unser Inhalt — in ihrer Sprache, mit ihren Suchbegriffen, damit sie uns zuerst finden. Ihr 5-Sprach-Rollout-Plan wird augenblicklich generiert und per E-Mail an Sie und unser Vertriebsteam (commercial@ziontechgroup.com) gesendet.',
        'discovery_cta1': 'Kostenlosen Entdeckung starten',
        'discovery_cta2': 'App-Netzwerk durchsuchen',
    },
}

def alternate_links():
    out = []
    for l2, u in LANGS:
        out.append(f'<link rel="alternate" hreflang="{l2}" href="{u}" />')
    return ''.join(out)

CSS = "body{font-family:system-ui,sans-serif;margin:0;color:#0f172a;background:#f8fafc}header,footer{background:#0b1220;color:#fff;padding:1rem}main{max-width:1100px;margin:0 auto;padding:1.5rem}.langbar{margin-bottom:1rem}.langbar a.active{color:#2563eb;font-weight:600}.cards{display:grid;gap:1rem}.card{background:#fff;border:1px solid #e2e8f0;border-radius:12px;padding:1rem;box-shadow:0 1px 3px rgba(15,23,42,.06)}.card h3{margin:.4rem 0 .3rem;color:#0f172a}.card p{color:#475569;font-size:.92rem}.card a{color:#2563eb;font-weight:600;text-decoration:none}.disc{background:#f1f5f9;border:1px solid #e2e8f0;border-radius:12px;padding:1.25rem;margin-top:1.25rem}.disc h2{margin-top:0}.disc .cta{display:inline-block;margin-top:.75rem;padding:.7rem 1.1rem;border-radius:8px;text-decoration:none;font-weight:650}.disc .cta.green{background:#059669;color:#fff}.disc .cta.alt{background:#0f1720;color:#fff}footer{background:#0b1220;color:#94a3b8;padding:1rem}footer a{color:#64748b}\n"

def assemble(lang):
    url_map = {'en': CANON, 'pt': L['pt'], 'es': L['es'], 'fr': L['fr'], 'de': L['de']}
    body = BODY[lang]
    urls = dict(LANGS); urls['en'] = CANON
    al = alternate_links()
    cards_groups = [g for g in (body['cards'][:3], body['cards'][3:6], body['cards'][6:9]) if g]
    labels = ['🌐 hreflang Standard + SEO', '📋 Per-Language Content Matrix', '🔧 Translation Toolkit', '🔁 Discovery Handoff']
    section_html = ''
    for grp, label in zip(cards_groups, labels):
        gh = ''.join(f'<div class="card"><h3>{h}</h3><p>{d}</p><a href="{live}">Live app →</a> · <a href="{repo}">Repo</a></div>' for h, d, live, repo in grp)
        section_html += f'<section><h2>{label}</h2><div class="cards">{gh}</div></section>'
    disc = f'<div class="disc"><h2>{body["discovery_h2"]}</h2><p>{body["discovery_p"]}</p><a class="cta green" href="https://ziontechgroup.com/discovery/">{body["discovery_cta1"]}</a><a class="cta alt" href="https://ziontechgroup.com/zion-app-network/">{body["discovery_cta2"]}</a></div>'
    closing = '<p style="margin-top:24px"><a href="https://ziontechgroup.com">← ziontechgroup.com</a> · <a href="https://github.com/Zion-support/zion-app-network/blob/main/SPOTLIGHT-multilingual-localization-2026.md">Spotlight doc</a> · <a href="https://github.com/Zion-support/zion-app-network/blob/main/APPS_INDEX-BATCH124-LOCALE.md">Batch rollup</a></p>'
    footer = '<footer>© 2026 Zion Tech Group — <a href="https://ziontechgroup.com">ziontechgroup.com</a> · Part of the Zion AI App Network</footer>'
    t = f'''<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{body['title']}</title>
  <meta name="description" content="[{body['description']}] — Zion Tech Group · Part of the Zion AI App Network" />
  <link rel="canonical" href="{url_map[lang]}" />
  <meta property="og:title" content="[{body['title']}]" />
  <meta property="og:description" content="[{body['description']}]" />
  <meta property="og:url" content="{url_map[lang]}" />
  {al}
  <style>__CSS__</style>
</head>
<body>
  {body['langbar']}
  <header>
    <h1>{body['h1']}</h1>
    <p>{body['pitch']}</p>
  </header>
  <main>
    {section_html}
    {disc}
    {closing}
  </main>
  {footer}
</body>
</html>'''
    return t.replace('__CSS__', CSS)

for lang, ext in [('en',''), ('pt','pt'), ('es','es'), ('fr','fr'), ('de','de')]:
    content = assemble(lang)
    path = os.path.join(WORK, f'app-network-multilingual-localization-2026{"-"+ext if ext else ""}.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("wrote", path, "len", len(content))
