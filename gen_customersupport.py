import os

WORK = '/Users/miami2/.hermes/profiles/agent-finops-ops/cache/apphub'
os.makedirs(WORK, exist_ok=True)

BASE = 'https://ziontechgroup.com/zion-app-network/app'
CANON = f'{BASE}/app-network-ai-customer-support-2026.html'
L = {
    'pt': f'{BASE}/app-network-ai-customer-support-2026-pt.html',
    'es': f'{BASE}/app-network-ai-customer-support-2026-es.html',
    'fr': f'{BASE}/app-network-ai-customer-support-2026-fr.html',
    'de': f'{BASE}/app-network-ai-customer-support-2026-de.html',
}
LANGS = [('en', CANON), ('pt-BR', L['pt']), ('es', L['es']), ('fr', L['fr']), ('de', L['de'])]

BODY = {
    'en': {
        'langbar': '<nav class="langbar">🌐 <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-customer-support-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-customer-support-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-customer-support-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-customer-support-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-customer-support-2026-de.html">Deutsch</a></nav>',
        'title': 'AI Customer Support Agent — Helpdesk Automation & Knowledge Base — Zion Tech Group',
        'description': 'Free AI Customer Support Agent hub: knowledge-grounded answers, ticket triage & routing, resolution, multilingual support, and human handoff — with full conversation context preserved.',
        'h1': '🤖 AI Customer Support Agent',
        'pitch': 'Your customers get instant answers, in their own language, 24/7 — and complex issues go to your team with full context, never lost. Grounded in your knowledge base, resolves routine requests end-to-end, routes tickets, triggers actions, and escalates with complete context to human agents.',
        'cards': [
            ('📚 Knowledge-Grounded Agent', 'Answers from approved sources: knowledge base, help center, policies, product catalog, ticket history.', 'https://ziontechgroup.com/ai-customer-support/', 'https://github.com/Zion-support/zion-ai-customer-support'),
            ('🧭 Ticket Triage & Routing', 'Classifies incoming requests by intent/sentiment and routes to the right queue, team, or escalation path.', 'https://ziontechgroup.com/ai-customer-support/', 'https://github.com/Zion-support/zion-ai-customer-support'),
            ('✅ Resolution Agent', 'Takes actions: query records, update tickets, trigger workflows, and hand off complex cases with full context.', 'https://ziontechgroup.com/ai-customer-support/', 'https://github.com/Zion-support/zion-ai-customer-support'),
            ('🌐 Multilingual Support (5 langs)', 'EN/PT-BR/ES/FR/DE support, consistent with the 5-language network.', 'https://ziontechgroup.com/ai-customer-support/', 'https://github.com/Zion-support/zion-ai-customer-support'),
            ('🙋 Human Handoff', 'Escalates complex cases to human agents with full conversation context preserved.', 'https://ziontechgroup.com/ai-customer-support/', 'https://github.com/Zion-support/zion-ai-customer-support'),
            ('📈 Support Analytics', 'Resolution rate, deflection rate, avg. handle time, CSAT by topic and language.', 'https://ziontechgroup.com/ai-customer-support/', 'https://github.com/Zion-support/zion-ai-customer-support'),
        ],
        'discovery_h2': '🧭 Free Discovery — always online, always free',
        'discovery_p': 'Your customers get instant answers, in their own language, 24/7 — and complex issues go to your team with full context, never lost. Your support system is generated instantly and emailed to you and our commercial team (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Start Free Discovery',
        'discovery_cta2': 'Browse the App Network',
    },
    'pt': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-customer-support-2026.html">English</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-customer-support-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-customer-support-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-customer-support-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-customer-support-2026-de.html">Deutsch</a></nav>',
        'title': 'Agente de Suporte ao Cliente com IA — automatização de helpdesk e base de conhecimento — Zion Tech Group',
        'description': 'Hub gratuito de Agente de Suporte ao Cliente com IA: respostas fundamentadas em conhecimento, triagem de tickets e roteamento, resolução, suporte multilíngue e mão de mão humano — com contexto completo das conversas preservado.',
        'h1': '🤖 Agente de Suporte ao Cliente com IA',
        'pitch': 'Seus clientes ganham respostas instantâneas, no seu próprio idioma, 24/7 — e questões complexas vão para a sua equipe com contexto completo, nunca perdido. Fundamentado na sua base de conhecimento, resolve solicitações rotineiras em última instância, roteia tickets, dispara ações e escala com contexto completo para agentes humanos.',
        'cards': [
            ('📚 Agente com Conhecimento', 'Responde de fontes aprovadas: base de conhecimento, helpdesk, políticas, catálogo de produtos, histórico de tickets.', 'https://ziontechgroup.com/ai-customer-support/', 'https://github.com/Zion-support/zion-ai-customer-support'),
            ('🧭 Triagem de Tickets', 'Classifica solicitações de entrada por intenção/tom de voz e roteia para a fila, equipe ou caminho de escalada corretos.', 'https://ziontechgroup.com/ai-customer-support/', 'https://github.com/Zion-support/zion-ai-customer-support'),
            ('✅ Agente de Resolução', 'Executa ações: consultar registros, atualizar tickets, disparar fluxos, e entregar casos complexos com contexto completo.', 'https://ziontechgroup.com/ai-customer-support/', 'https://github.com/Zion-support/zion-ai-customer-support'),
            ('🌐 Suporte Multilíngue (5 idiomas)', 'Suporte EN/PT-BR/ES/FR/DE, consistente com a rede 5-idioma.', 'https://ziontechgroup.com/ai-customer-support/', 'https://github.com/Zion-support/zion-ai-customer-support'),
            ('🙋 Mão de Mão Humano', 'Escala casos complexos para agentes humanos com contexto completo da conversa preservado.', 'https://ziontechgroup.com/ai-customer-support/', 'https://github.com/Zion-support/zion-ai-customer-support'),
            ('📈 Análise de Suporte', 'Taxa de resolução, taxa de deflexão, tempo médio de resolução, CSAT por tópico e idioma.', 'https://ziontechgroup.com/ai-customer-support/', 'https://github.com/Zion-support/zion-ai-customer-support'),
        ],
        'discovery_h2': '🧭 Descoberta Gratuita — sempre online, sempre gratuita',
        'discovery_p': 'Seus clientes ganham respostas instantâneas, no seu próprio idioma, 24/7 — e questões complexas vão para a sua equipe com contexto completo, nunca perdido. Seu sistema de suporte é gerado instantaneamente e enviado por e-mail para você e nossa equipe comercial (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Iniciar Descoberta Gratuita',
        'discovery_cta2': 'Navegar pela Rede de Aplicativos',
    },
    'es': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-customer-support-2026.html">English</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-customer-support-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-customer-support-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-customer-support-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-customer-support-2026-de.html">Deutsch</a></nav>',
        'title': 'Agente de Soporte al Cliente con IA — automatización de helpdesk y base de conocimiento — Zion Tech Group',
        'description': 'Hub gratuito de Agente de Soporte al Cliente con IA: respuestas fundamentadas en conocimiento, triaje y enrutamiento de tickets, resolución, soporte multilíngue y mano de mano humano — con contexto completo de las conversaciones preservado.',
        'h1': '🤖 Agente de Soporte al Cliente con IA',
        'pitch': 'Tus clientes reciben respuestas instantáneas, en su propio idioma, 24/7 — y los temas complejos van al equipo con contexto completo, nunca perdido. Fundamentado en tu base de conocimiento, resuelve solicitudes rutinarias en última instancia, enruta tickets, desencadena acciones y escala con contexto completo a agentes humanos.',
        'cards': [
            ('📚 Agente con Conocimiento', 'Responde de fuentes aprobadas: base de conocimiento, helpdesk, políticas, catálogo de productos, historial de tickets.', 'https://ziontechgroup.com/ai-customer-support/', 'https://github.com/Zion-support/zion-ai-customer-support'),
            ('🧭 Triaje de Tickets', 'Clasifica solicitudes de entrada por intención/tono de voz y enruta al equipo o ruta de escalamiento correctos.', 'https://ziontechgroup.com/ai-customer-support/', 'https://github.com/Zion-support/zion-ai-customer-support'),
            ('✅ Agente de Resolución', 'Ejecuta acciones: consultar registros, actualizar tickets, disparar flujos y entregar casos complejos con contexto completo.', 'https://ziontechgroup.com/ai-customer-support/', 'https://github.com/Zion-support/zion-ai-customer-support'),
            ('🌐 Soporte Multilingüe (5 idiomas)', 'Soporte EN/PT-BR/ES/FR/DE, consistente con la red 5-idioma.', 'https://ziontechgroup.com/ai-customer-support/', 'https://github.com/Zion-support/zion-ai-customer-support'),
            ('🙋 Mano de Mano Humano', 'Escala casos complejos a agentes humanos con contexto completo de la conversación preservado.', 'https://ziontechgroup.com/ai-customer-support/', 'https://github.com/Zion-support/zion-ai-customer-support'),
            ('📈 Análisis de Soporte', 'Tasa de resolución, tasa de deflexión, tiempo promedio de resolución, CSAT por tema e idioma.', 'https://ziontechgroup.com/ai-customer-support/', 'https://github.com/Zion-support/zion-ai-customer-support'),
        ],
        'discovery_h2': '🧭 Descubrimiento Gratuito — siempre en línea, siempre gratuito',
        'discovery_p': 'Tus clientes reciben respuestas instantáneas, en su propio idioma, 24/7 — y los temas complejos van al equipo con contexto completo, nunca perdido. Tu sistema de soporte se genera instantáneamente y se envía por correo a usted y nuestro equipo comercial (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Comenzar Descubrimiento Gratuito',
        'discovery_cta2': 'Explorar la Red de Aplicaciones',
    },
    'fr': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-customer-support-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-customer-support-2026-fr.html">Français</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-customer-support-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-customer-support-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-customer-support-2026-de.html">Deutsch</a></nav>',
        'title': 'Agent de Support Client IA — automatisation de helpdesk et base de connaissances — Zion Tech Group',
        'description': 'Hub gratuit de Agent de Support Client IA : réponses fondées sur les connaissances, tri et acheminement de tickets, résolution, support multilingue, et main d\'ouvrière humaine — avec contexte complet des conversations préservé.',
        'h1': '🤖 Agent de Support Client IA',
        'pitch': 'Vos clients obtiennent des réponses instantanées, dans leur propre langue, 24/7 — et les problèmes complexes vont vers votre équipe avec contexte complet, jamais perdu. Fondé sur votre base de connaissances, résout les demandes courantes en bout en bout, achemine les tickets, déclenche des actions et escalade avec contexte complet vers les agents humains.',
        'cards': [
            ('📚 Agent à Base de Connaissances', 'Répond à partir de sources approuvées : base de connaissances, helpdesk, politiques, catalogue produits, historique de tickets.', 'https://ziontechgroup.com/ai-customer-support/', 'https://github.com/Zion-support/zion-ai-customer-support'),
            ('🧭 Tri et Acheminement de Tickets', 'Classe les demandes entrantes par intention/sentiment et achemine vers la bonne file, équipe ou voie d\'escalade.', 'https://ziontechgroup.com/ai-customer-support/', 'https://github.com/Zion-support/zion-ai-customer-support'),
            ('✅ Agent de Résolution', 'Prend des actions : interroger des enregistrements, mettre à jour les tickets, déclencher des flux et escalader des cas complexes avec contexte complet.', 'https://ziontechgroup.com/ai-customer-support/', 'https://github.com/Zion-support/zion-ai-customer-support'),
            ('🌐 Support Multilingue (5 langues)', 'Support EN/PT-BR/ES/FR/DE, cohérent avec le réseau 5 langues.', 'https://ziontechgroup.com/ai-customer-support/', 'https://github.com/Zion-support/zion-ai-customer-support'),
            ('🙋 Main d\'ouvrière Humaine', 'Escalade les cas complexes aux agents humains avec contexte complet de la conversation préservé.', 'https://ziontechgroup.com/ai-customer-support/', 'https://github.com/Zion-support/zion-ai-customer-support'),
            ('📈 Analyses de Support', 'Taux de résolution, taux de déviation, temps moyen de résolution, CSAT par sujet et langue.', 'https://ziontechgroup.com/ai-customer-support/', 'https://github.com/Zion-support/zion-ai-customer-support'),
        ],
        'discovery_h2': '🧭 Découverte Gratuite — toujours en ligne, toujours gratuite',
        'discovery_p': 'Vos clients obtiennent des réponses instantanées, dans leur propre langue, 24/7 — et les problèmes complexes vont vers votre équipe avec contexte complet, jamais perdu. Votre système de support est généré instantanément et envoyé par e-mail à vous et à notre équipe commerciale (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Commencer la Découverte Gratuite',
        'discovery_cta2': 'Parcourir le Réseau d\'Applications',
    },
    'de': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-customer-support-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-customer-support-2026-de.html">Deutsch</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-customer-support-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-customer-support-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-customer-support-2026-fr.html">Français</a></nav>',
        'title': 'KI-Kundenbetreuungs-Agent & Helpdesk-Automatisierung — Zion Tech Group',
        'description': 'Kostenloser KI-Kundenbetreuungs-Agent & Helpdesk-Automatisierungs-HuB: wissensbasierte Antworten, Ticket-Klassifizierung & Routing, Auflösung, mehrsprachiger Support und menschliche Handoff-Übergabe — mit vollständigem Kontext der Gespräche gepflegt.',
        'h1': '🤖 KI-Kundenbetreuungs-Agent & Helpdesk-Automatisierung',
        'pitch': 'Ihre Kunden erhalten sofortige Antworten, in ihrer eigenen Sprache, 24/7 — und komplexe Themen gehen an Ihr Team mit vollständigem Kontext, niemals verloren. Auf Ihrer Wissensbasis fundiert, lösen Sie Routineaufgaben endlos, leiten Tickets weiter, lösen Maßnahmen aus und eskalieren mit vollständigem Kontext an menschliche Agenten.',
        'cards': [
            ('📚 Wissensbasiert-Agent', 'Antworten aus genehmigten Quellen: Wissensbasis, Helpdesk, Richtlinien, Produkt-Katalog, Ticket-Geschichte.', 'https://ziontechgroup.com/ai-customer-support/', 'https://github.com/Zion-support/zion-ai-customer-support'),
            ('🧭 Ticket-Klassifizierung & Routing', 'Klassifiziert eingehende Anfragen nach Intent/Sentiment und leitet an die richtige Warteschlange, Abteilung oder Eskalationsroute.', 'https://ziontechgroup.com/ai-customer-support/', 'https://github.com/Zion-support/zion-ai-customer-support'),
            ('✅ Lösung-Agent', 'Führt Maßnahmen aus: Datensätze abfragen, Tickets aktualisieren, Workflows auslösen und komplexe Fälle mit vollem Kontext eskalieren.', 'https://ziontechgroup.com/ai-customer-support/', 'https://github.com/Zion-support/zion-ai-customer-support'),
            ('🌐 Mehrsprachiger Support (5 Sprachen)', 'EN/PT-BR/ES/FR/DE-Support, konsistent mit dem 5-Sprach-Netzwerk.', 'https://ziontechgroup.com/ai-customer-support/', 'https://github.com/Zion-support/zion-ai-customer-support'),
            ('🙋 Menschliche Handoff-Übergabe', 'Eskaliert komplexe Fälle an menschliche Agenten mit vollständigem Kontext der Gespräche gepflegt.', 'https://ziontechgroup.com/ai-customer-support/', 'https://github.com/Zion-support/zion-ai-customer-support'),
            ('📈 Support-Analysen', 'Lösungszahl, Abfragerate, durchschnittliche Bearbeitungszeit, CSAT nach Thema und Sprache.', 'https://ziontechgroup.com/ai-customer-support/', 'https://github.com/Zion-support/zion-ai-customer-support'),
        ],
        'discovery_h2': '🧭 Kostenloser Entdeckung — immer online, immer kostenlos',
        'discovery_p': 'Ihre Kunden erhalten sofortige Antworten, in ihrer eigenen Sprache, 24/7 — und komplexe Themen gehen an Ihr Team mit vollständigem Kontext, niemals verloren. Ihr Support-System wird augenblicklich generiert und per E-Mail an Sie und unser Vertriebsteam (commercial@ziontechgroup.com) gesendet.',
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
    labels = ['📚 Knowledge-Grounded Agent', '🧭 Ticket Triage + Routing', '✅ Resolution Agent', '🌐 Multilingual (5 langs)', '🙋 Human Handoff', '📈 Support Analytics']
    section_html = ''
    for grp, label in zip(cards_groups, labels):
        gh = ''.join(f'<div class="card"><h3>{h}</h3><p>{d}</p><a href="{live}">Live app →</a> · <a href="{repo}">Repo</a></div>' for h, d, live, repo in grp)
        section_html += f'<section><h2>{label}</h2><div class="cards">{gh}</div></section>'
    disc = f'<div class="disc"><h2>{body["discovery_h2"]}</h2><p>{body["discovery_p"]}</p><a class="cta green" href="https://ziontechgroup.com/discovery/">{body["discovery_cta1"]}</a><a class="cta alt" href="https://ziontechgroup.com/zion-app-network/">{body["discovery_cta2"]}</a></div>'
    closing = '<p style="margin-top:24px"><a href="https://ziontechgroup.com">← ziontechgroup.com</a> · <a href="https://github.com/Zion-support/zion-app-network/blob/main/SPOTLIGHT-ai-customer-support-2026.md">Spotlight doc</a> · <a href="https://github.com/Zion-support/zion-app-network/blob/main/APPS_INDEX-BATCH128-CUSTOMERSUPPORT.md">Batch rollup</a></p>'
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
    path = os.path.join(WORK, f'app-network-ai-customer-support-2026{"-"+ext if ext else ""}.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("wrote", path, "len", len(content))
