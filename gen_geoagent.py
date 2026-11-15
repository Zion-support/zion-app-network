import os

WORK = '/Users/miami2/.hermes/profiles/agent-finops-ops/cache/apphub'
os.makedirs(WORK, exist_ok=True)

BASE = 'https://ziontechgroup.com/zion-app-network/app'
CANON = f'{BASE}/app-network-content-intelligence-geo-agent-2026.html'
L = {
    'pt': f'{BASE}/app-network-content-intelligence-geo-agent-2026-pt.html',
    'es': f'{BASE}/app-network-content-intelligence-geo-agent-2026-es.html',
    'fr': f'{BASE}/app-network-content-intelligence-geo-agent-2026-fr.html',
    'de': f'{BASE}/app-network-content-intelligence-geo-agent-2026-de.html',
}
LANGS = [('en', CANON), ('pt-BR', L['pt']), ('es', L['es']), ('fr', L['fr']), ('de', L['de'])]

BODY = {
    'en': {
        'langbar': '<nav class="langbar">🌐 <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-content-intelligence-geo-agent-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-content-intelligence-geo-agent-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-content-intelligence-geo-agent-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-content-intelligence-geo-agent-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-content-intelligence-geo-agent-2026-de.html">Deutsch</a></nav>',
        'title': 'Content Intelligence & GEO Agent — AI Visibility & Content Strategy — Zion Tech Group',
        'description': 'Free Content Intelligence & GEO Agent hub: content-intelligence scanner, GEO visibility monitor across ChatGPT/Google/Claude, competitor benchmarking, and content-gap briefs — the AI visibility layer for EN/PT-BR/ES/FR/DE.',
        'h1': '🌐 Content Intelligence & GEO Agent',
        'pitch': 'The AI visibility layer for content strategy and GEO: scan your content vs competitors, monitor brand presence across ChatGPT, Google AI Overviews, Claude, Gemini, Copilot, Perplexity, and package every finding into a scoped content brief for each of the 5 languages. Feeds the agent marketplace and implementation vault.',
        'cards': [
            ('🔍 Content-Intelligence Scanner', 'Reviews published content vs competitors: keyword coverage, topic clusters, AI-citation gaps, content gaps.', 'https://ziontechgroup.com/content-intelligence-geo-agent/', 'https://github.com/Zion-support/zion-content-intelligence-geo-agent'),
            ('📡 GEO Visibility Monitor', 'Monitors brand presence and AI citations across ChatGPT, Google AI Overviews, Claude, Gemini, Copilot, Perplexity.', 'https://ziontechgroup.com/content-intelligence-geo-agent/', 'https://github.com/Zion-support/zion-content-intelligence-geo-agent'),
            ('📊 Competitor Benchmarking', 'Share of voice, brand position, sentiment vs named competitors.', 'https://ziontechgroup.com/content-intelligence-geo-agent/', 'https://github.com/Zion-support/zion-content-intelligence-geo-agent'),
            ('📝 Content-Gap Brief Generator', 'Turns each finding into a scoped, briefed content play with keyword targets, driving/trigger questions, FAQ blocks, comparison scorecards.', 'https://ziontechgroup.com/content-intelligence-geo-agent/', 'https://github.com/Zion-support/zion-content-intelligence-geo-agent'),
            ('🌍 Localization & Geotargeting', 'Adapts briefs to each of the 5 languages (EN/PT-BR/ES/FR/DE).', 'https://ziontechgroup.com/content-intelligence-geo-agent/', 'https://github.com/Zion-support/zion-content-intelligence-geo-agent'),
            ('🔁 Discovery Handoff', 'Content play → agent marketplace (Batch 117) + implementation vault (Batch 121) + vertical trust (Batch 122).', 'https://ziontechgroup.com/content-intelligence-geo-agent/', 'https://github.com/Zion-support/zion-content-intelligence-geo-agent'),
        ],
        'discovery_h2': '🧭 Free Discovery — always online, always free',
        'discovery_p': 'Find what we\'re missing in every language, fix it, and get cited in AI answers across ChatGPT, Google, and Claude — so every city we serve finds us first. Your content-gap + GEO playbook is generated instantly and emailed to you and our commercial team (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Start Free Discovery',
        'discovery_cta2': 'Browse the App Network',
    },
    'pt': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-content-intelligence-geo-agent-2026.html">English</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-content-intelligence-geo-agent-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-content-intelligence-geo-agent-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-content-intelligence-geo-agent-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-content-intelligence-geo-agent-2026-de.html">Deutsch</a></nav>',
        'title': 'Hub de Inteligência de Conteúdo e Agente GEO — estratégia de conteúdo e visibilidade AI — Zion Tech Group',
        'description': 'Hub gratuito de Inteligência de Conteúdo e Agente GEO: scanner de inteligência de conteúdo, monitor de visibilidade GEO em ChatGPT/Google/Claude, benchmarking de concorrentes e briefings de gap de conteúdo — a camada de visibilidade AI para EN/PT-BR/ES/FR/DE.',
        'h1': '🌐 Hub de Inteligência de Conteúdo e Agente GEO',
        'pitch': 'A camada de visibilidade AI para estratégia de conteúdo e GEO: varra seu conteúdo vs concorrentes, monitore a presença da marca em ChatGPT, Google AI Overviews, Claude, Gemini, Copilot, Perplexity e embale cada achado em uma briefings de conteúdo para cada um dos 5 idiomas. Alimenta o marketplace de agentes e o vault de implementação.',
        'cards': [
            ('🔍 Scanner de Inteligência de Conteúdo', 'Revela o conteúdo publicado vs concorrentes: cobertura de palavras-chave, clusters temáticos, gaps de citação AI, gaps de conteúdo.', 'https://ziontechgroup.com/content-intelligence-geo-agent/', 'https://github.com/Zion-support/zion-content-intelligence-geo-agent'),
            ('📡 Monitor de Visibilidade GEO', 'Monitorea a presença da marca e citações AI em ChatGPT, Google AI Overviews, Claude, Gemini, Copilot, Perplexity.', 'https://ziontechgroup.com/content-intelligence-geo-agent/', 'https://github.com/Zion-support/zion-content-intelligence-geo-agent'),
            ('📊 Benchmarking de Concorrentes', 'Compartilhamento de voz, posicionamento da marca, tom de voz vs concorrentes nomeados.', 'https://ziontechgroup.com/content-intelligence-geo-agent/', 'https://github.com/Zion-support/zion-content-intelligence-geo-agent'),
            ('📝 Gerador de Briefings de Gap de Conteúdo', 'Transforma cada achado em um play de conteúdo escopo e briefado com alvos de palavras-chave, perguntas-driver/trigger, blocs FAQ, scorecards de comparação.', 'https://ziontechgroup.com/content-intelligence-geo-agent/', 'https://github.com/Zion-support/zion-content-intelligence-geo-agent'),
            ('🌍 Localização & Geotargeting', 'Adapta briefings a cada um dos 5 idiomas (EN/PT-BR/ES/FR/DE).', 'https://ziontechgroup.com/content-intelligence-geo-agent/', 'https://github.com/Zion-support/zion-content-intelligence-geo-agent'),
            ('🔁 Mão de Obra de Descoberta', 'Play de conteúdo → marketplace de agentes (Lote 117) + vault de implementação (Lote 121) + confiança vertical (Lote 122).', 'https://ziontechgroup.com/content-intelligence-geo-agent/', 'https://github.com/Zion-support/zion-content-intelligence-geo-agent'),
        ],
        'discovery_h2': '🧭 Descoberta Gratuita — sempre online, sempre gratuita',
        'discovery_p': 'Encontre o que estamos perdendo em cada idioma, corrija e seja citado em respostas AI em ChatGPT, Google e Claude — para que cada cidade que atendemos nos encontre primeiro. Seu playbook de gap de conteúdo + GEO é gerado instantaneamente e enviado por e-mail para você e nossa equipe comercial (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Iniciar Descoberta Gratuita',
        'discovery_cta2': 'Navegar pela Rede de Aplicativos',
    },
    'es': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-content-intelligence-geo-agent-2026.html">English</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-content-intelligence-geo-agent-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-content-intelligence-geo-agent-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-content-intelligence-geo-agent-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-content-intelligence-geo-agent-2026-de.html">Deutsch</a></nav>',
        'title': 'Inteligencia de Contenido y Agente GEO — visibilidad AI y estrategia de contenido — Zion Tech Group',
        'description': 'Hub gratuito de Inteligencia de Contenido y Agente GEO: escáner de inteligencia de contenido, monitor de visibilidad GEO en ChatGPT/Google/Claude, benchmarking de concursantes, briefs de gap de contenido — la capa de visibilidad AI para EN/PT-BR/ES/FR/DE.',
        'h1': '🌐 Inteligencia de Contenido y Agente GEO',
        'pitch': 'La capa de visibilidad AI para estrategia de contenido y GEO: varra su contenido vs concursos, monitore la presencia de la marca en ChatGPT, Google AI Overviews, Claude, Gemini, Copilot, Perplexity y empaque cada hallazgo en un briefing de contenido para cada uno de los 5 idiomas. Alimenta el marketplace de agentes y el vault de implementación.',
        'cards': [
            ('🔍 Escáner de Inteligencia de Contenido', 'Revela el contenido publicado vs concursos: cobertura de palabras clave, clusters temáticos, gaps de cita AI, gaps de contenido.', 'https://ziontechgroup.com/content-intelligence-geo-agent/', 'https://github.com/Zion-support/zion-content-intelligence-geo-agent'),
            ('📡 Monitor de Visibilidad GEO', 'Monitorea la presencia de la marca y citas AI en ChatGPT, Google AI Overviews, Claude, Gemini, Copilot, Perplexity.', 'https://ziontechgroup.com/content-intelligence-geo-agent/', 'https://github.com/Zion-support/zion-content-intelligence-geo-agent'),
            ('📊 Benchmarking de Concurrentes', 'Voz compartida, posicionamiento de la marca, tono vs concursantes mencionados.', 'https://ziontechgroup.com/content-intelligence-geo-agent/', 'https://github.com/Zion-support/zion-content-intelligence-geo-agent'),
            ('📝 Generador de Briefings de Gap de Contenido', 'Convierte cada hallazgo en un play de contenido con objetivos de palabras clave, preguntas-driver/trigger, bloques FAQ, scorecards de comparación.', 'https://ziontechgroup.com/content-intelligence-geo-agent/', 'https://github.com/Zion-support/zion-content-intelligence-geo-agent'),
            ('🌍 Localización & Geotargeting', 'Adaptar briefings a cada uno de los 5 idiomas (EN/PT-BR/ES/FR/DE).', 'https://ziontechgroup.com/content-intelligence-geo-agent/', 'https://github.com/Zion-support/zion-content-intelligence-geo-agent'),
            ('🔁 Mano de Obra de Descubrimiento', 'Play de contenido → marketplace de agentes (Lote 117) + vault de implementación (Lote 121) + confianza vertical (Lote 122).', 'https://ziontechgroup.com/content-intelligence-geo-agent/', 'https://github.com/Zion-support/zion-content-intelligence-geo-agent'),
        ],
        'discovery_h2': '🧭 Descubrimiento Gratuito — siempre en línea, siempre gratuito',
        'discovery_p': 'Encuentre lo que estamos perdiendo en cada idioma, corríjamelo y sea citado en respuestas AI en ChatGPT, Google y Claude — para que cada ciudad que atendemos nos encuentre primero. Su playbook de gap de contenido + GEO se genera instantáneamente y se envía por correo a usted y a nuestro equipo comercial (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Comenzar Descubrimiento Gratuito',
        'discovery_cta2': 'Explorar la Red de Aplicaciones',
    },
    'fr': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-content-intelligence-geo-agent-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-content-intelligence-geo-agent-2026-fr.html">Français</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-content-intelligence-geo-agent-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-content-intelligence-geo-agent-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-content-intelligence-geo-agent-2026-de.html">Deutsch</a></nav>',
        'title': 'Intelligence de Contenu et Agent GEO — visibilité IA et stratégie de contenu — Zion Tech Group',
        'description': 'Hub gratuit de Intelligence de Contenu et Agent GEO : scanner d\'intelligence de contenu, monitor de visibilité GEO sur ChatGPT/Google/Claude, benchmarking de concurrents, briefs de gap de contenu — la couche de visibilité IA pour EN/PT-BR/ES/FR/DE.',
        'h1': '🌐 Intelligence de Contenu et Agent GEO',
        'pitch': 'La couche de visibilité IA pour la stratégie de contenu et le GEO : analysez votre contenu vs concurrents, surveillez la présence de la marque sur ChatGPT, Google AI Overviews, Claude, Gemini, Copilot, Perplexity, et emballer chaque résultat dans un briefing de contenu pour chacune des 5 langues. Alimente le marketplace d\'agents et le vault d\'implémentation.',
        'cards': [
            ('🔍 Scanner d\'Intelligence de Contenu', 'Analysez le contenu publié vs concurrents : couverture de mots-clés, clusters thématiques, gaps de citation IA, gaps de contenu.', 'https://ziontechgroup.com/content-intelligence-geo-agent/', 'https://github.com/Zion-support/zion-content-intelligence-geo-agent'),
            ('📡 Monitor de Visibilité GEO', 'Surveiller la présence de la marque et les citations IA sur ChatGPT, Google AI Overviews, Claude, Gemini, Copilot, Perplexity.', 'https://ziontechgroup.com/content-intelligence-geo-agent/', 'https://github.com/Zion-support/zion-content-intelligence-geo-agent'),
            ('📊 Benchmarking des Concurrents', 'Part de voix, positionnement de la marque, ton vs concurrents nommés.', 'https://ziontechgroup.com/content-intelligence-geo-agent/', 'https://github.com/Zion-support/zion-content-intelligence-geo-agent'),
            ('📝 Générateur de Briefings de Gap de Contenu', 'Transforme chaque résultat en une offre de contenu avec cibles de mots-clés, questions-driver/trigger, blocs FAQ, scorecards de comparaison.', 'https://ziontechgroup.com/content-intelligence-geo-agent/', 'https://github.com/Zion-support/zion-content-intelligence-geo-agent'),
            ('🌍 Localisation & Geotargeting', 'Adapter les briefings à chacune des 5 langues (EN/PT-BR/ES/FR/DE).', 'https://ziontechgroup.com/content-intelligence-geo-agent/', 'https://github.com/Zion-support/zion-content-intelligence-geo-agent'),
            ('🔁 Main d\'œuvre de Découverte', 'Play de contenu → marketplace d\'agents (Lot 117) + vault d\'implémentation (Lot 121) + confiance verticale (Lot 122).', 'https://ziontechgroup.com/content-intelligence-geo-agent/', 'https://github.com/Zion-support/zion-content-intelligence-geo-agent'),
        ],
        'discovery_h2': '🧭 Découverte Gratuite — toujours en ligne, toujours gratuite',
        'discovery_p': 'Trouvez ce que nous manquons dans chaque langue, corrigez-le et soyez cité dans les réponses IA sur ChatGPT, Google et Claude — pour que chaque ville que nous desservons nos trouve en premier. Votre playbook de gap de contenu + GEO est généré instantanément et envoyé par e-mail à vous et à notre équipe commerciale (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Commencer la Découverte Gratuite',
        'discovery_cta2': 'Parcourir le Réseau d\'Applications',
    },
    'de': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-content-intelligence-geo-agent-2026.html">English</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-content-intelligence-geo-agent-2026-de.html">Deutsch</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-content-intelligence-geo-agent-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-content-intelligence-geo-agent-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-content-intelligence-geo-agent-2026-fr.html">Français</a></nav>',
        'title': 'Inhalts-Intelligenz & GEO-Agent — KI-Sichtbarkeit & Inhaltsstrategie — Zion Tech Group',
        'description': 'Kostenloser Inhalts-Intelligenz & GEO-Agent-HuB: Inhalts-Intelligenz-Scanner, GEO-Sichtbarkeits-Monitor auf ChatGPT/Google/Claude, Wettbewerbs-Benchmarking und Inhalts-Lücken-Briefings — die KI-Sichtbarkeits-Schicht für EN/PT-BR/ES/FR/DE.',
        'h1': '🌐 Inhalts-Intelligenz & GEO-Agent',
        'pitch': 'Die KI-Sichtbarkeits-Schicht für Inhaltsstrategie und GEO: scannen Sie Ihren Inhalt im Vergleich zu Wettbewerbern, überwachen Sie die Markenpräsenz auf ChatGPT, Google AI Overviews, Claude, Gemini, Copilot, Perplexity und verpacken Sie jedes Ergebnis in ein kuratiertes Inhalts-Briefing für jede der 5 Sprachen. Speist den Agentenmarktplatz und den Implementierungshaller.',
        'cards': [
            ('🔍 Inhalts-Intelligenz-Scanner', 'Überprüfen Sie Ihren veröffentlichten Inhalt im Vergleich zu Wettbewerbern: Stichwortabdeckung, Themen-Cluster, KI-Zitations-Lücken, Inhalts-Lücken.', 'https://ziontechgroup.com/content-intelligence-geo-agent/', 'https://github.com/Zion-support/zion-content-intelligence-geo-agent'),
            ('📡 GEO-Sichtbarkeits-Monitor', 'Überwacht Markenpräsenz und KI-Zitationen auf ChatGPT, Google AI Overviews, Claude, Gemini, Copilot, Perplexity.', 'https://ziontechgroup.com/content-intelligence-geo-agent/', 'https://github.com/Zion-support/zion-content-intelligence-geo-agent'),
            ('📊 Wettbewerbs-Benchmarking', 'Markenpräsenz, Markenposition, Ton vs benannten Wettbewerbern.', 'https://ziontechgroup.com/content-intelligence-geo-agent/', 'https://github.com/Zion-support/zion-content-intelligence-geo-agent'),
            ('📝 Inhalts-Lücken-Briefing-Generator', 'Verpackt jedes Ergebnis in ein kuratiertes Inhalts-Briefing mit Stichwort-Zielen, driving/trigger-Fragen, FAQ-Blöcken, Vergleichs-Scorecards.', 'https://ziontechgroup.com/content-intelligence-geo-agent/', 'https://github.com/Zion-support/zion-content-intelligence-geo-agent'),
            ('🌍 Lokalisierung & Geotargeting', 'Passt Briefings an jede der 5 Sprachen (EN/PT-BR/ES/FR/DE) an.', 'https://ziontechgroup.com/content-intelligence-geo-agent/', 'https://github.com/Zion-support/zion-content-intelligence-geo-agent'),
            ('🔁 Entdeckungs-Handoff', 'Inhalts-Play → Agenten-Marktplatz (Zahl 117) + Implementierungshaller (Zahl 121) + vertikale Anweisung (Zahl 122).', 'https://ziontechgroup.com/content-intelligence-geo-agent/', 'https://github.com/Zion-support/zion-content-intelligence-geo-agent'),
        ],
        'discovery_h2': '🧭 Kostenloser Entdeckung — immer online, immer kostenlos',
        'discovery_p': '-Finden Sie, was wir in jeder Sprache fehlt, reparieren Sie es und werden Sie in KI-Antworten zitiert auf ChatGPT, Google und Claude — damit jede Stadt, die wir bedienen, uns zuerst findet. Ihr Inhalts-Lücken + GEO-Playbook wird augenblicklich generiert und per E-Mail an Sie und unser Vertriebsteam (commercial@ziontechgroup.com) gesendet.',
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
    labels = ['🔍 Content-Intelligence Scanner', '📡 GEO Visibility Monitor', '📊 Competitor Benchmarking', '📝 Content-Gap Brief Generator', '🔁 Discovery Handoff']
    section_html = ''
    for grp, label in zip(cards_groups, labels):
        gh = ''.join(f'<div class="card"><h3>{h}</h3><p>{d}</p><a href="{live}">Live app →</a> · <a href="{repo}">Repo</a></div>' for h, d, live, repo in grp)
        section_html += f'<section><h2>{label}</h2><div class="cards">{gh}</div></section>'
    disc = f'<div class="disc"><h2>{body["discovery_h2"]}</h2><p>{body["discovery_p"]}</p><a class="cta green" href="https://ziontechgroup.com/discovery/">{body["discovery_cta1"]}</a><a class="cta alt" href="https://ziontechgroup.com/zion-app-network/">{body["discovery_cta2"]}</a></div>'
    closing = '<p style="margin-top:24px"><a href="https://ziontechgroup.com">← ziontechgroup.com</a> · <a href="https://github.com/Zion-support/zion-app-network/blob/main/SPOTLIGHT-content-intelligence-geo-agent-2026.md">Spotlight doc</a> · <a href="https://github.com/Zion-support/zion-app-network/blob/main/APPS_INDEX-BATCH126-GEOAGENT.md">Batch rollup</a></p>'
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
    path = os.path.join(WORK, f'app-network-content-intelligence-geo-agent-2026{"-"+ext if ext else ""}.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("wrote", path, "len", len(content))
