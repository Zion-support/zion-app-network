import os

WORK = '/Users/miami2/.hermes/profiles/agent-finops-ops/cache/apphub'
os.makedirs(WORK, exist_ok=True)

BASE = 'https://ziontechgroup.com/zion-app-network/app'
CANON = f'{BASE}/app-network-ai-marketing-campaign-2026.html'
L = {
    'pt': f'{BASE}/app-network-ai-marketing-campaign-2026-pt.html',
    'es': f'{BASE}/app-network-ai-marketing-campaign-2026-es.html',
    'fr': f'{BASE}/app-network-ai-marketing-campaign-2026-fr.html',
    'de': f'{BASE}/app-network-ai-marketing-campaign-2026-de.html',
}
LANGS = [('en', CANON), ('pt-BR', L['pt']), ('es', L['es']), ('fr', L['fr']), ('de', L['de'])]

BODY = {
    'en': {
        'langbar': '<nav class="langbar">🌐 <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-marketing-campaign-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-marketing-campaign-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-marketing-campaign-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-marketing-campaign-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-marketing-campaign-2026-de.html">Deutsch</a></nav>',
        'title': 'AI Marketing Campaign Agent — Content, Social & Campaign Automation — Zion Tech Group',
        'description': 'Free AI Marketing Campaign Agent hub: content generation, social media, SEO, ad copy, and multi-channel distribution — cutting content time 60-80% and software costs 50-70%, in all five languages.',
        'h1': '🤖 AI Marketing Campaign Agent',
        'pitch': 'We plan, draft, translate, and schedule your next campaign in your brand voice — across all channels, in all five languages, in days not weeks. Multi-agent team: campaign lead + content + social + SEO + repurposing agents, with a human approval gate. Content time down 60-80%, software costs down 50-70%.',
        'cards': [
            ('📋 Campaign Lead Agent', 'Takes a goal (product launch, lead gen, brand awareness) and plans the campaign across channels with a human approval gate.', 'https://ziontechgroup.com/ai-marketing-campaign/', 'https://github.com/Zion-support/zion-ai-marketing-campaign'),
            ('✍️ Content Generation Agent', 'Drafts blog posts, landing pages, social posts, and email copy in Zion\'s brand voice across the 5-language network.', 'https://ziontechgroup.com/ai-marketing-campaign/', 'https://github.com/Zion-support/zion-ai-marketing-campaign'),
            ('🔄 Repurposing Agent', 'Turns one asset into 8+ channel formats — blog → social post, email, LinkedIn, ad variants.', 'https://ziontechgroup.com/ai-marketing-campaign/', 'https://github.com/Zion-support/zion-ai-marketing-campaign'),
            ('🔍 SEO & Metadata Agent', 'Keyword research, briefs, optimisation for Google and AI search (GEO), metadata suggestions.', 'https://ziontechgroup.com/ai-marketing-campaign/', 'https://github.com/Zion-support/zion-ai-marketing-campaign'),
            ('📱 Social Media Agent', 'Planning, copy generation, scheduling across LinkedIn, X, Instagram, with performance monitoring.', 'https://ziontechgroup.com/ai-marketing-campaign/', 'https://github.com/Zion-support/zion-ai-marketing-campaign'),
            ('📊 Competitive Monitoring Agent', 'Tracks rival launches, pricing, content; flags patterns in a weekly brief.', 'https://ziontechgroup.com/ai-marketing-campaign/', 'https://github.com/Zion-support/zion-ai-marketing-campaign'),
        ],
        'discovery_h2': '🧭 Free Discovery — always online, always free',
        'discovery_p': 'Tell us your campaign goal, and we\'ll plan, draft, translate, schedule, and publish it in your brand voice across all channels — in days not weeks. Your plan is emailed to you and our commercial team (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Start Free Discovery',
        'discovery_cta2': 'Browse the App Network',
    },
    'pt': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-marketing-campaign-2026.html">English</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-marketing-campaign-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-marketing-campaign-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-marketing-campaign-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-marketing-campaign-2026-de.html">Deutsch</a></nav>',
        'title': 'Agente Multi-Agente de Marketing com IA — conteúdo, redes sociais e campanhas — Zion Tech Group',
        'description': 'Hub gratuito de Agente Multi-Agente de Marketing com IA: geração de conteúdo, redes sociais, SEO, anúncios e distribuição multi-canais — reduzindo o tempo de conteúdo em 60-80% e os custos de software em 50-70%, em todos os cinco idiomas.',
        'h1': '🤖 Agente Multi-Agente de Marketing com IA',
        'pitch': 'Nós planejamos, redigimos, traduzimos, agendamos e publicamos a sua próxima campanha na sua voz de marca — em todos os canais, em todos os cinco idiomas, em dias e não em semanas. Equipe multi-agente: líder de campanha + agentes de conteúdo, redes sociais, SEO e repaginação, com uma porta de aprovação humana. Tempo de conteúdo -60-80%, custos de software -50-70%.',
        'cards': [
            ('📋 Agente Líder de Campanha', 'Toma um objetivo (lançamento de produto, geração de leads, consciência de marca) e planifica a campanha por canais com uma porta de aprovação humana.', 'https://ziontechgroup.com/ai-marketing-campaign/', 'https://github.com/Zion-support/zion-ai-marketing-campaign'),
            ('✍️ Agente de Geração de Conteúdo', 'Redige artigos de blog, páginas de aterrissagem, posts de redes sociais e e-mails em voz de marca da Zion em todos os 5 idiomas.', 'https://ziontechgroup.com/ai-marketing-campaign/', 'https://github.com/Zion-support/zion-ai-marketing-campaign'),
            ('🔄 Agente de Repaginação', 'Transforma um ativo em 8+ formatos de canal — blog → post de rede social, e-mail, LinkedIn, variantes de anúncio.', 'https://ziontechgroup.com/ai-marketing-campaign/', 'https://github.com/Zion-support/zion-ai-marketing-campaign'),
            ('🔍 Agente SEO & Metadados', 'Pesquisa de palavras-chave, briefings, otimização para Google e busca AI (GEO), sugestões de metadados.', 'https://ziontechgroup.com/ai-marketing-campaign/', 'https://github.com/Zion-support/zion-ai-marketing-campaign'),
            ('📱 Agente de Redes Sociais', 'Planejamento, geração de cópia, agendamento em LinkedIn, X, Instagram, com monitoramento de desempenho.', 'https://ziontechgroup.com/ai-marketing-campaign/', 'https://github.com/Zion-support/zion-ai-marketing-campaign'),
            ('📊 Agente de Monitoramento de Concorrência', 'Rastreia lançamentos, preços e conteúdo de concorrentes; sinaliza padrões em um briefing semanal.', 'https://ziontechgroup.com/ai-marketing-campaign/', 'https://github.com/Zion-support/zion-ai-marketing-campaign'),
        ],
        'discovery_h2': '🧭 Descoberta Gratuita — sempre online, sempre gratuita',
        'discovery_p': 'Diga-nos o seu objetivo de campanha e nós planejamos, redigimos, traduzimos, agendamos e publicamos em sua voz de marca em todos os canais — em dias e não em semanas. O seu plano é enviado por e-mail para você e nossa equipa comercial (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Iniciar Descoberta Gratuita',
        'discovery_cta2': 'Navegar pela Rede de Aplicativos',
    },
    'es': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-marketing-campaign-2026.html">English</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-marketing-campaign-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-marketing-campaign-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-marketing-campaign-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-marketing-campaign-2026-de.html">Deutsch</a></nav>',
        'title': 'Agente Multi-Agence de Marketing con IA — contenido, redes sociales y campañas — Zion Tech Group',
        'description': 'Hub gratuito de Agente Multi-Agence de Marketing con IA: generación de contenido, redes sociales, SEO, anuncios y distribución multi-canal — reduciendo el tiempo de contenido en 60-80% y los costos de software en 50-70%, en los cinco idiomas.',
        'h1': '🤖 Agente Multi-Agence de Marketing con IA',
        'pitch': 'Nosotros planificamos, redactamos, traducimos, programamos y publicamos su próxima campaña en su voz de marca — en todos los canales, en los cinco idiomas, en días y no en semanas. Equipo multi-agente: líder de campaña + agentes de contenido, redes sociales, SEO y repaginación, con una puerta de aprobación humana. Tiempo de contenido -60-80%, costos de software -50-70%.',
        'cards': [
            ('📋 Agente Líder de Campaña', 'Toma un objetivo (lanzamiento de producto, generación de Leads, notoriedad de marca) y planifica la campaña por canales con una puerta de aprobación humana.', 'https://ziontechgroup.com/ai-marketing-campaign/', 'https://github.com/Zion-support/zion-ai-marketing-campaign'),
            ('✍️ Agente de Generación de Contenido', 'Redacta artículos de blog, páginas de aterrizaje, publicaciones de redes sociales y correos en la voz de marca de Zion en los 5 idiomas.', 'https://ziontechgroup.com/ai-marketing-campaign/', 'https://github.com/Zion-support/zion-ai-marketing-campaign'),
            ('🔄 Agente de Repaginación', 'Convierte un activo en 8+ formatos de canal — blog → publicación de redes sociales, correo, LinkedIn, variantes de anuncio.', 'https://ziontechgroup.com/ai-marketing-campaign/', 'https://github.com/Zion-support/zion-ai-marketing-campaign'),
            ('🔍 Agente SEO & Metadatos', 'Investigación de palabras clave, briefings, optimización para Google y búsqueda AI (GEO), sugerencias de metadatos.', 'https://ziontechgroup.com/ai-marketing-campaign/', 'https://github.com/Zion-support/zion-ai-marketing-campaign'),
            ('📱 Agente de Redes Sociales', 'Planificación, generación de copia, programación en LinkedIn, X, Instagram, con monitoreo de desempeño.', 'https://ziontechgroup.com/ai-marketing-campaign/', 'https://github.com/Zion-support/zion-ai-marketing-campaign'),
            ('📊 Agente de Monitoreo de Competidores', 'Rastrea lanzamientos, precios y contenido de concursantes; señala patrones en un briefing semanal.', 'https://ziontechgroup.com/ai-marketing-campaign/', 'https://github.com/Zion-support/zion-ai-marketing-campaign'),
        ],
        'discovery_h2': '🧭 Descubrimiento Gratuito — siempre en línea, siempre gratuito',
        'discovery_p': 'Díganos su objetivo de campaña y nosotros planeamos, redactamos, traducimos, programamos y publicamos en su voz de marca en todos los canales — en días y no en semanas. Su plan se envía por correo a usted y nuestro equipo comercial (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Comenzar Descubrimiento Gratuito',
        'discovery_cta2': 'Explorar la Red de Aplicaciones',
    },
    'fr': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-marketing-campaign-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-marketing-campaign-2026-fr.html">Français</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-marketing-campaign-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-marketing-campaign-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-marketing-campaign-2026-de.html">Deutsch</a></nav>',
        'title': 'Agent Multi-Agents de Marketing IA — contenu, réseaux sociaux et campagnes — Zion Tech Group',
        'description': 'Hub gratuit de Agent Multi-Agents de Marketing IA : génération de contenu, réseaux sociaux, SEO, pubs et distribution multi-canaux — réduisant le temps de contenu de 60-80% et les coûts de logiciels de 50-70%, dans les cinq langues.',
        'h1': '🤖 Agent Multi-Agents de Marketing IA',
        'pitch': 'Nous planifions, rédigeons, traduisons, programmons et publions votre prochaine campagne dans votre voix de marque — sur tous les canaux, dans les cinq langues, en jours et non en semaines. Équipe multi-agents : chef de campagne + agents contenu, réseaux sociaux, SEO, reprise, avec une porte d\'approbation humaine. Temps de contenu -60-80%, coûts logiciels -50-70%.',
        'cards': [
            ('📋 Chef de Campagne', 'Prend un objectif (lancement produit, génération de Leads, visibilité de marque) et planifie la campagne par canaux avec une porte d\'approbation humaine.', 'https://ziontechgroup.com/ai-marketing-campaign/', 'https://github.com/Zion-support/zion-ai-marketing-campaign'),
            ('✍️ Agent de Génération de Contenu', 'Rédige articles de blog, pages de destination, publications de réseaux sociaux et e-mails dans la voix de marque de Zion dans les 5 langues.', 'https://ziontechgroup.com/ai-marketing-campaign/', 'https://github.com/Zion-support/zion-ai-marketing-campaign'),
            ('🔄 Agent de Reprise', 'Transforme un seul actif en 8+ formats de canaux — blog → publication réseau, e-mail, LinkedIn, variantes publicitaires.', 'https://ziontechgroup.com/ai-marketing-campaign/', 'https://github.com/Zion-support/zion-ai-marketing-campaign'),
            ('🔍 Agent SEO & Méta-données', 'Recherche de mots-clés, briefings, optimisation pour Google et recherche IA (GEO), suggestions de métadonnées.', 'https://ziontechgroup.com/ai-marketing-campaign/', 'https://github.com/Zion-support/zion-ai-marketing-campaign'),
            ('📱 Agent Réseaux Sociaux', 'Planification, génération de copie, programmation sur LinkedIn, X, Instagram, avec surveillance de performance.', 'https://ziontechgroup.com/ai-marketing-campaign/', 'https://github.com/Zion-support/zion-ai-marketing-campaign'),
            ('📊 Agent de Surveillance Concurrent', 'Suit les lancements, prix et contenus des concurrents ; signale des tendances dans un briefing hebdomadaire.', 'https://ziontechgroup.com/ai-marketing-campaign/', 'https://github.com/Zion-support/zion-ai-marketing-campaign'),
        ],
        'discovery_h2': '🧭 Découverte Gratuite — toujours en ligne, toujours gratuite',
        'discovery_p': 'Dites-nous votre objectif de campagne et nous planifions, rédigeons, traduisons, programmons et publions dans votre voix de marque sur tous les canaux — en jours et non en semaines. Votre plan est envoyé par e-mail à vous et à notre équipe commerciale (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Commencer la Découverte Gratuite',
        'discovery_cta2': 'Parcourir le Réseau d\'Applications',
    },
    'de': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-marketing-campaign-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-marketing-campaign-2026-de.html">Deutsch</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-marketing-campaign-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-marketing-campaign-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-marketing-campaign-2026-fr.html">Français</a></nav>',
        'title': 'KI-Marketing-Kampagne-Agent & Multi-Agenten — Inhalt, Social Media & Kampagne-Automatisierung — Zion Tech Group',
        'description': 'Kostenloser KI-Marketing-Kampagne-Agent & Multi-Agenten-HuB: Inhaltsgenerierung, Social Media, SEO, Werbecopy und Multi-Kanal-Verteilung — Reduzierung der Inhaltszeit um 60-80% und der Softwarekosten um 50-70%, in allen fünf Sprachen.',
        'h1': '🤖 KI-Marketing-Kampagne-Agent & Multi-Agenten',
        'pitch': 'Wir planen, verfassen, übersetzen, planen und veröffentlichen Ihre nächste Kampagne in Ihrer Markenstimme — auf allen Kanälen, in allen fünf Sprachen, in Tagen statt Wochen. Multi-Agenten-Team: Kampagnenleiter + Inhalts-, Social-Media-, SEO- und Repurposing-Agenten mit menschlicher Freigabeportal. Inhaltszeit -60-80%, Softwarekosten -50-70%.',
        'cards': [
            ('📋 Kampagnenleiter-Agent', 'Nimmt ein Ziel (Produktlaunch, Leadgenerierung, Markenbekanntheit) und plant die Kampagne auf Kanälen mit einem menschlichen Freigabeportal.', 'https://ziontechgroup.com/ai-marketing-campaign/', 'https://github.com/Zion-support/zion-ai-marketing-campaign'),
            ('✍️ Inhaltsgenerierungs-Agent', 'Verfasst Blogposts, Landingpages, Social-Media-Posts und E-Mail-Sätze in Zion\'s Markenstimme in den 5 Sprachen.', 'https://ziontechgroup.com/ai-marketing-campaign/', 'https://github.com/Zion-support/zion-ai-marketing-campaign'),
            ('🔄 Repurposing-Agent', 'Verwandelt ein Asset in 8+ Kanalformate — Blog → Social-Media-Post, E-Mail, LinkedIn, Werbeanzeigen.', 'https://ziontechgroup.com/ai-marketing-campaign/', 'https://github.com/Zion-support/zion-ai-marketing-campaign'),
            ('🔍 SEO & Metadaten-Agent', 'Stichwortrecherche, Briefings, Optimierung für Google und KI-Suche (GEO), Metadaten-Vorschläge.', 'https://ziontechgroup.com/ai-marketing-campaign/', 'https://github.com/Zion-support/zion-ai-marketing-campaign'),
            ('📱 Social-Media-Agent', 'Planung, Copy-Generierung, Terminierung auf LinkedIn, X, Instagram mit Leistungsmonitoring.', 'https://ziontechgroup.com/ai-marketing-campaign/', 'https://github.com/Zion-support/zion-ai-marketing-campaign'),
            ('📊 Wettbewerbsüberwachungs-Agent', 'Verfolgt Konkurrenten-Lancer, Preise, Inhalte; signalisiert Muster in einem wöchentlichen Briefing.', 'https://ziontechgroup.com/ai-marketing-campaign/', 'https://github.com/Zion-support/zion-ai-marketing-campaign'),
        ],
        'discovery_h2': '🧭 Kostenloser Entdeckung — immer online, immer kostenlos',
        'discovery_p': 'Erzählen Sie uns Ihr Kampagnenziel, und wir planen, verfassen, übersetzen, planen und veröffentlichen es in Ihrer Markenstimme auf allen Kanälen — in Tagen statt Wochen. Ihr Plan wird per E-Mail an Sie und unser Vertriebsteam (commercial@ziontechgroup.com) gesendet.',
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
    labels = ['📋 Campaign Lead', '✍️ Content Generation', '🔄 Repurposing', '🔍 SEO & Metadata', '📱 Social Media', '📊 Competitive Monitor']
    section_html = ''
    for grp, label in zip(cards_groups, labels):
        gh = ''.join(f'<div class="card"><h3>{h}</h3><p>{d}</p><a href="{live}">Live app →</a> · <a href="{repo}">Repo</a></div>' for h, d, live, repo in grp)
        section_html += f'<section><h2>{label}</h2><div class="cards">{gh}</div></section>'
    disc = f'<div class="disc"><h2>{body["discovery_h2"]}</h2><p>{body["discovery_p"]}</p><a class="cta green" href="https://ziontechgroup.com/discovery/">{body["discovery_cta1"]}</a><a class="cta alt" href="https://ziontechgroup.com/zion-app-network/">{body["discovery_cta2"]}</a></div>'
    closing = '<p style="margin-top:24px"><a href="https://ziontechgroup.com">← ziontechgroup.com</a> · <a href="https://github.com/Zion-support/zion-app-network/blob/main/SPOTLIGHT-ai-marketing-campaign-2026.md">Spotlight doc</a> · <a href="https://github.com/Zion-support/zion-app-network/blob/main/APPS_INDEX-BATCH129-MARKETING.md">Batch rollup</a></p>'
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
    path = os.path.join(WORK, f'app-network-ai-marketing-campaign-2026{"-"+ext if ext else ""}.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("wrote", path, "len", len(content))
