import os

WORK = '/Users/miami2/.hermes/profiles/agent-finops-ops/cache/apphub'
os.makedirs(WORK, exist_ok=True)

BASE = 'https://ziontechgroup.com/zion-app-network/app'
CANON = f'{BASE}/app-network-geotopics-2026.html'
L = {
    'pt': f'{BASE}/app-network-geotopics-2026-pt.html',
    'es': f'{BASE}/app-network-geotopics-2026-es.html',
    'fr': f'{BASE}/app-network-geotopics-2026-fr.html',
    'de': f'{BASE}/app-network-geotopics-2026-de.html',
}
LANGS = [('en', CANON), ('pt-BR', L['pt']), ('es', L['es']), ('fr', L['fr']), ('de', L['de'])]

BODY = {
    'en': {
        'langbar': '<nav class="langbar">🌐 <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-geotopics-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-geotopics-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-geotopics-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-geotopics-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-geotopics-2026-de.html">Deutsch</a></nav>',
        'title': 'GEO Topic Clusters & AI Search Visibility — Zion Tech Group',
        'description': 'Free GEO Topic Clusters hub: pillar pages, subquestions, FAQ blocks and comparison scorecards — optimized for Google AI Overviews, ChatGPT, Perplexity and Gemini.',
        'h1': '🌐 GEO Topic Clusters & AI Search Visibility',
        'pitch': 'Free GEO hub: turn Zion into a semantic topic-cluster authority — pillar pages, subquestions, FAQ blocks, comparison scorecards — optimized for ChatGPT, Perplexity and Google AI Overviews. Feeds the homepage advertising and client SEO/GEO services.',
        'cards': [
            ('📘 Pillar Content Engine', 'Comprehensive guide per core service + subpages on every related question.', 'https://ziontechgroup.com/geo-topics/', 'https://github.com/Zion-support/zion-geo-topics'),
            ('❓ FAQ + Direct-Answer Blocks', 'AI-extracted first lines; prompt-aligned FAQ sections — the highest-citation levers.', 'https://ziontechgroup.com/geo-topics/', 'https://github.com/Zion-support/zion-geo-topics'),
            ('⚖️ Comparison Scorecards', 'Structured comparisons (e.g., SaaS vs open-source) that AI engines can cite directly.', 'https://ziontechgroup.com/geo-topics/', 'https://github.com/Zion-support/zion-geo-topics'),
            ('🔍 GEO Audit Tool', 'Free check of any page\'s AI-readability: structured data, E-E-A-T, citation readiness.', 'https://ziontechgroup.com/geo-topics/', 'https://github.com/Zion-support/zion-geo-topics'),
            ('🎯 BOFU Content Templates', 'Conversion-oriented page → pillar → supporting posts, linked intentionally.', 'https://ziontechgroup.com/geo-topics/', 'https://github.com/Zion-support/zion-geo-topics'),
            ('🧭 Discovery Handoff', 'GEO report → free discovery questionnaire (Batch 116) → SEO/GEO sprint.', 'https://ziontechgroup.com/geo-topics/', 'https://github.com/Zion-support/zion-geo-topics'),
        ],
        'discovery_h2': '🧭 Free Discovery — always online, always free',
        'discovery_p': 'Make Zion the source AI citations trust. Your AI-search-visibility report is generated instantly and emailed to you and our commercial team (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Start Free Discovery',
        'discovery_cta2': 'Browse the App Network',
    },
    'pt': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-geotopics-2026.html">English</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-geotopics-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-geotopics-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-geotopics-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-geotopics-2026-de.html">Deutsch</a></nav>',
        'title': 'Clusters de Tópicos GEO e Visibilidade na Busca AI — Zion Tech Group',
        'description': 'Hub gratuito de Clusters de Tópicos GEO: páginas-pilão, subperguntas, blocos FAQ e placas de comparação — otimizado para Google AI Overviews, ChatGPT, Perplexity e Gemini.',
        'h1': '🌐 Clusters de Tópicos GEO e Visibilidade na Busca AI',
        'pitch': 'Hub GEO gratuito: transforme a Zion em uma autoridade de cluster semântico — páginas-pilão, subperguntas, blocos FAQ, placas de comparação — otimizado para ChatGPT, Perplexity e Google AI Overviews. Alimenta a publicidade da homepage e os serviços de SEO/GEO do cliente.',
        'cards': [
            ('📘 Motor de Conteúdo Pilão', 'Guia abrangente por serviço principal + subpáginas em cada pergunta relacionada.', 'https://ziontechgroup.com/geo-topics/', 'https://github.com/Zion-support/zion-geo-topics'),
            ('❓ Blocos FAQ + Resposta Direta', 'Primeiras linhas extraídas por IA; seções FAQ alinhadas a prompts — os bigodes de citação mais altos.', 'https://ziontechgroup.com/geo-topics/', 'https://github.com/Zion-support/zion-geo-topics'),
            ('⚖️ Placas de Comparação', 'Comparações estruturadas (ex.: SaaS vs código aberto) que os motores de busca podem citar diretamente.', 'https://ziontechgroup.com/geo-topics/', 'https://github.com/Zion-support/zion-geo-topics'),
            ('🔍 Ferramenta de Auditoria GEO', 'Verificação gratuita do perfil de inteligência artificial de qualquer página: dados estruturados, E-E-A-T, prontidão para citação.', 'https://ziontechgroup.com/geo-topics/', 'https://github.com/Zion-support/zion-geo-topics'),
            ('🎯 Modelos de Conteúdo BOFU', 'Página orientada à conversão → pilão → posts subsidiários, vinculados intencionalmente.', 'https://ziontechgroup.com/geo-topics/', 'https://github.com/Zion-support/zion-geo-topics'),
            ('🧭 Mão de Obra de Descoberta', 'Relatório GEO → questionário de descoberta gratuito (Lote 116) → sprint SEO/GEO.', 'https://ziontechgroup.com/geo-topics/', 'https://github.com/Zion-support/zion-geo-topics'),
        ],
        'discovery_h2': '🧭 Descoberta Gratuita — sempre online, sempre gratuita',
        'discovery_p': 'Torne a Zion a fonte em que a IA confia nas citações. Seu relatório de visibilidade na busca AI é gerado instantaneamente e enviado por e-mail para você e nossa equipe comercial (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Iniciar Descoberta Gratuita',
        'discovery_cta2': 'Navegar pela Rede de Aplicativos',
    },
    'es': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-geotopics-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-geotopics-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-geotopics-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-geotopics-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-geotopics-2026-de.html">Deutsch</a></nav>',
        'title': 'Clusters de Temas GEO y Visibilidad en la Búsqueda IA — Zion Tech Group',
        'description': 'Hub gratuito de Clusters de Temas GEO: páginas pilares, subpreguntas, bloques FAQ y placas de comparación — optimizado para Google AI Overviews, ChatGPT, Perplexity y Gemini.',
        'h1': '🌐 Clusters de Temas GEO y Visibilidad en la Búsqueda IA',
        'pitch': 'Hub GEO gratuito: convierta a Zion en una autoridad de cluster temático — páginas pilares, subpreguntas, bloques FAQ, placas de comparación — optimizado para ChatGPT, Perplexity y Google AI Overviews. Alimenta la publicidad de la homepage y los servicios de SEO/GEO del cliente.',
        'cards': [
            ('📘 Motor de Contenido Pilár', 'Guía abarcativa por servicio principal + subpáginas en cada pregunta relacionada.', 'https://ziontechgroup.com/geo-topics/', 'https://github.com/Zion-support/zion-geo-topics'),
            ('❓ Bloques FAQ + Respuesta Directa', 'Primeras líneas extraídas por IA; secciones FAQ alineadas a prompts — los bigodes de cita más altos.', 'https://ziontechgroup.com/geo-topics/', 'https://github.com/Zion-support/zion-geo-topics'),
            ('⚖️ Placas de Comparación', 'Comparaciones estructuradas (p. ej., SaaS vs código abierto) que los motores de búsqueda pueden citar directamente.', 'https://ziontechgroup.com/geo-topics/', 'https://github.com/Zion-support/zion-geo-topics'),
            ('🔍 Herramienta de Auditoría GEO', 'Verificación gratuita del perfil de inteligencia artificial de cualquier página: datos estructurados, E-E-A-T, prontitud para cita.', 'https://ziontechgroup.com/geo-topics/', 'https://github.com/Zion-support/zion-geo-topics'),
            ('🎯 Plantillas de Contenido BOFU', 'Página orientada a la conversión → pilár → posts subsidiarios, vinculados intencionalmente.', 'https://ziontechgroup.com/geo-topics/', 'https://github.com/Zion-support/zion-geo-topics'),
            ('🧭 Mano de Obra de Descubrimiento', 'Informe GEO → cuestionario de descubrimiento gratuito (Lote 116) → sprint SEO/GEO.', 'https://ziontechgroup.com/geo-topics/', 'https://github.com/Zion-support/zion-geo-topics'),
        ],
        'discovery_h2': '🧭 Descubrimiento Gratuito — siempre en línea, siempre gratuito',
        'discovery_p': 'Haga que Zion sea la fuente en la que la IA confía en las citas. Su informe de visibilidad en la búsqueda AI se genera instantáneamente y se envía por correo a usted y a nuestro equipo comercial (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Comenzar Descubrimiento Gratuito',
        'discovery_cta2': 'Explorar la Red de Aplicaciones',
    },
    'fr': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-geotopics-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-geotopics-2026-fr.html">Français</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-geotopics-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-geotopics-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-geotopics-2026-de.html">Deutsch</a></nav>',
        'title': 'Clusters de Sujets GEO et Visibilité en Recherche IA — Zion Tech Group',
        'description': 'Hub gratuit de Clusters de Sujets GEO : pages-pilotes, sous-questions, blocs FAQ et fiches de comparaison — optimisé pour Google AI Overviews, ChatGPT, Perplexity et Gemini.',
        'h1': '🌐 Clusters de Sujets GEO et Visibilité en Recherche IA',
        'pitch': 'Hub GEO gratuit : transformez la Zion en autorité de cluster sémantique — pages-pilotes, sous-questions, blocs FAQ, fiches de comparaison — optimisé pour ChatGPT, Perplexity et Google AI Overviews. Alimente la publicité de la homepage et les services SEO/GEO du client.',
        'cards': [
            ('📘 Moteur de Contenu Pilote', 'Guide complet par service principal + sous-pages sur chaque question liée.', 'https://ziontechgroup.com/geo-topics/', 'https://github.com/Zion-support/zion-geo-topics'),
            ('❓ Blocs FAQ + Réponse Directe', 'Premières lignes extraites par IA ; sections FAQ alignées sur les requêtes — les gros gagnants de citation.', 'https://ziontechgroup.com/geo-topics/', 'https://github.com/Zion-support/zion-geo-topics'),
            ('⚖️ Fiches de Comparaison', 'Comparaisons structurées (ex. SaaS vs open-source) que les moteurs de recherche peuvent citer directement.', 'https://ziontechgroup.com/geo-topics/', 'https://github.com/Zion-support/zion-geo-topics'),
            ('🔍 Outil d\'Audit GEO', 'Vérification gratuite du profil IA de chaque page : données structurées, E-E-A-T, prêt pour citation.', 'https://ziontechgroup.com/geo-topics/', 'https://github.com/Zion-support/zion-geo-topics'),
            ('🎯 Modèles de Contenu BOFU', 'Page orientée conversion → pilote → articles subsidiaires, liés intentionnellement.', 'https://ziontechgroup.com/geo-topics/', 'https://github.com/Zion-support/zion-geo-topics'),
            ('🧭 Main d\'œuvre de Découverte', 'Rapport GEO → questionnaire de découverte gratuit (Lot 116) → sprint SEO/GEO.', 'https://ziontechgroup.com/geo-topics/', 'https://github.com/Zion-support/zion-geo-topics'),
        ],
        'discovery_h2': '🧭 Découverte Gratuite — toujours en ligne, toujours gratuite',
        'discovery_p': 'Rendez Zion la source en laquelle l\'IA fait confiance. Votre rapport de visibilité en recherche IA est généré instantanément et envoyé par e-mail à vous et à notre équipe commerciale (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Commencer la Découverte Gratuite',
        'discovery_cta2': 'Parcourir le Réseau d\'Applications',
    },
    'de': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-geotopics-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-geotopics-2026-de.html">Deutsch</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-geotopics-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-geotopics-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-geotopics-2026-fr.html">Français</a></nav>',
        'title': 'GEO-Themen-Cluster & KI-Browse-Sichtbarkeit — Zion Tech Group',
        'description': 'Kostenloser GEO-Themen-Cluster-Hub: Pilypages, Unterfragen, FAQ-Blöcke und Vergleichstabellen — optimiert für Google AI Overviews, ChatGPT, Perplexity und Gemini.',
        'h1': '🌐 GEO-Themen-Cluster & KI-Browse-Sichtbarkeit',
        'pitch': 'Kostenloser GEO-Adapter: machen Sie Zion zu einer semantischen Themen-Clustherautorität — Pilypages, Unterfragen, FAQ-Blöcke, Vergleichstabellen — optimiert für ChatGPT, Perplexity und Google AI Overviews. Speist die Homepage-Werbung und die Kunden-SEO/GEO-Dienstleistungen.',
        'cards': [
            ('📘 Pilarpfad-Inhalt', 'Umfassende Anleitung pro Kern-Dienstleistung + Unterseiten zu jeder verwandten Frage.', 'https://ziontechgroup.com/geo-topics/', 'https://github.com/Zion-support/zion-geo-topics'),
            ('❓ FAQ- und Direktantwort-Blocke', 'KI-extrahierte ersten Zeilen; prompt-angepasste FAQ-Bereiche — die hochwertigsten Zitier-Bigoden.', 'https://ziontechgroup.com/geo-topics/', 'https://github.com/Zion-support/zion-geo-topics'),
            ('⚖️ Vergleichstabellen', 'Strukturierte Vergleiche (z. B. SaaS vs Open-Source), die KI-Motoren direkt zitieren können.', 'https://ziontechgroup.com/geo-topics/', 'https://github.com/Zion-support/zion-geo-topics'),
            ('🔍 GEO-Prüfwerk', 'Kostenlose Überprüfung der KI-Lesbarkeit jeder Seite: strukturierte Daten, E-E-A-T, Zitierfähigkeit.', 'https://ziontechgroup.com/geo-topics/', 'https://github.com/Zion-support/zion-geo-topics'),
            ('🎯 BOFU-Inhalts-Vorlagen', 'Umsetzungsgerichtete Seite → Pilarpfad → unterstützende Beiträge, bewusst verlinkt.', 'https://ziontechgroup.com/geo-topics/', 'https://github.com/Zion-support/zion-geo-topics'),
            ('🧭 Entdeckungs-Handoff', 'GEO-Bericht → kostenloses Entdeckungsfragebogen (Nummer 116) → SEO/GEO-Sprint.', 'https://ziontechgroup.com/geo-topics/', 'https://github.com/Zion-support/zion-geo-topics'),
        ],
        'discovery_h2': '🧭 Kostenloser Entdeckung — immer online, immer kostenlos',
        'discovery_p': 'Machen Sie Zion zur Quelle, die künstliche Intelligenz bei Zitaten vertraut. Ihr Bericht zur Sichtbarkeit in der Suchmaschine wird augenblicklich generiert und per E-Mail an Sie und unser Vertriebsteam (commercial@ziontechgroup.com) gesendet.',
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
    labels = ['📘 Pillar Content Engine', '❓ FAQ + Direct-Answer Blocks', '⚖️ Comparison Scorecards', '🆕 Open-Source Engine']
    section_html = ''
    for grp, label in zip(cards_groups, labels):
        gh = ''.join(f'<div class="card"><h3>{h}</h3><p>{d}</p><a href="{live}">Live app →</a> · <a href="{repo}">Repo</a></div>' for h, d, live, repo in grp)
        section_html += f'<section><h2>{label}</h2><div class="cards">{gh}</div></section>'
    disc = f'<div class="disc"><h2>{body["discovery_h2"]}</h2><p>{body["discovery_p"]}</p><a class="cta green" href="https://ziontechgroup.com/discovery/">{body["discovery_cta1"]}</a><a class="cta alt" href="https://ziontechgroup.com/zion-app-network/">{body["discovery_cta2"]}</a></div>'
    closing = '<p style="margin-top:24px"><a href="https://ziontechgroup.com">← ziontechgroup.com</a> · <a href="https://github.com/Zion-support/zion-app-network/blob/main/SPOTLIGHT-geotopics-2026.md">Spotlight doc</a> · <a href="https://github.com/Zion-support/zion-app-network/blob/main/APPS_INDEX-BATCH120-GEO.md">Batch rollup</a></p>'
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
    path = os.path.join(WORK, f'app-network-geotopics-2026{"-"+ext if ext else ""}.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("wrote", path, "len", len(content))
