import os

WORK = '/Users/miami2/.hermes/profiles/agent-finops-ops/cache/apphub'
os.makedirs(WORK, exist_ok=True)

BASE = 'https://ziontechgroup.com/zion-app-network/app'
CANON = f'{BASE}/app-network-ai-sales-outreach-2026.html'
L = {
    'pt': f'{BASE}/app-network-ai-sales-outreach-2026-pt.html',
    'es': f'{BASE}/app-network-ai-sales-outreach-2026-es.html',
    'fr': f'{BASE}/app-network-ai-sales-outreach-2026-fr.html',
    'de': f'{BASE}/app-network-ai-sales-outreach-2026-de.html',
}
LANGS = [('en', CANON), ('pt-BR', L['pt']), ('es', L['es']), ('fr', L['fr']), ('de', L['de'])]

BODY = {
    'en': {
        'langbar': '<nav class="langbar">🌐 <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sales-outreach-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sales-outreach-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sales-outreach-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sales-outreach-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sales-outreach-2026-de.html">Deutsch</a></nav>',
        'title': 'AI Sales Outreach & Multi-Channel Engagement — Prospecting Agent — Zion Tech Group',
        'description': 'Free AI Sales Outreach & Multi-Channel Engagement hub: account research, contact enrichment, personalised outreach, multi-touch sequences (email/LinkedIn/phone), reply handling, and CRM write-back — for FE/technician customers and Zion\'s commercial team.',
        'h1': '🤖 AI Sales Outreach & Multi-Channel Engagement',
        'pitch': 'Give every rep a 24/7 army that researches, writes, and follows up across email, LinkedIn, and phone. Multi-channel prospecting agent: research → enrichment → personalised writer → multi-touch sequencing → reply handling → CRM write-back, with the rep in the approval loop. All languages we serve.',
        'cards': [
            ('🔍 Research Agent', 'Monitors target accounts for buying signals, conducts account research across CRM + external sources, surfaces buyer-committee insights.', 'https://ziontechgroup.com/ai-sales-outreach/', 'https://github.com/Zion-support/zion-ai-sales-outreach'),
            ('📦 Enrichment Agent', 'Adds verified contact + firmographics + intent signals from Apollo, ZoomInfo, Surfe, Seamless.', 'https://ziontechgroup.com/ai-sales-outreach/', 'https://github.com/Zion-support/zion-ai-sales-outreach'),
            ('✍️ Writer Agent (personalised)', 'Drafts outreach in each rep\'s voice, personalised by account, multi-channel (email + LinkedIn).', 'https://ziontechgroup.com/ai-sales-outreach/', 'https://github.com/Zion-support/zion-ai-sales-outreach'),
            ('🔄 Sequencing Agent (multi-touch)', 'Multi-touch sequences (Day 1 email, Day 3 LinkedIn, Day 5 case study), adaptive on engagement, optimised send timing.', 'https://ziontechgroup.com/ai-sales-outreach/', 'https://github.com/Zion-support/zion-ai-sales-outreach'),
            ('📥 Reply Handling Agent', 'Classifies replies, drafts follow-ups, routes qualified replies to the rep, books meetings.', 'https://ziontechgroup.com/ai-sales-outreach/', 'https://github.com/Zion-support/zion-ai-sales-outreach'),
            ('📋 CRM Write-Back + Deliverability', 'Logs activity to the CRM (HubSpot), monitors send volume/domain health, rotates inboxes.', 'https://ziontechgroup.com/ai-sales-outreach/', 'https://github.com/Zion-support/zion-ai-sales-outreach'),
        ],
        'discovery_h2': '🧭 Free Discovery — always online, always free',
        'discovery_p': 'Give your reps a 24/7 army that researches, writes, and follows up across email, LinkedIn, and phone — in every language we serve. Your outbound system is generated instantly and emailed to you and our commercial team (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Start Free Discovery',
        'discovery_cta2': 'Browse the App Network',
    },
    'pt': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sales-outreach-2026.html">English</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sales-outreach-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sales-outreach-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sales-outreach-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sales-outreach-2026-de.html">Deutsch</a></nav>',
        'title': 'Agente de Prospecção e Envio Multi-Canal com IA — Zion Tech Group',
        'description': 'Hub gratuito de Agente de Prospecção e Envio Multi-Canal com IA: pesquisa de contas, enriquecimento de contatos, redação personalizada, sequências multi-touch (e-mail/Redes Sociais/Ligue), tratamento de respostas e escrita no CRM — para clientes FE/técnicos e a equipa comercial Zion.',
        'h1': '🤖 Agente de Prospecção e Envio Multi-Canal com IA',
        'pitch': 'Dê aos vossos recrutadores um exército 24/7 que pesquisa, redige e faz follow-up em e-mail, LinkedIn e telefone — em todos os idiomas que atendemos. Agente de prospecção multi-canal: pesquisa → enriquecimento → redactor personalizado → sequências multi-touch → tratamento de respostas → escrita no CRM, com o recrutador na porta de aprovação. Todos os idiomas que atendemos.',
        'cards': [
            ('🔍 Agente de Pesquisa', 'Monitora contas-alvo de sinais de compra, conduz pesquisa de contas via CRM + fontes externas e revela insights do comité de compra.', 'https://ziontechgroup.com/ai-sales-outreach/', 'https://github.com/Zion-support/zion-ai-sales-outreach'),
            ('📦 Agente de Enriquecimento', 'Adiciona contacto verificado + firmographics + sinais de intenção de Apollo, ZoomInfo, Surfe, Seamless.', 'https://ziontechgroup.com/ai-sales-outreach/', 'https://github.com/Zion-support/zion-ai-sales-outreach'),
            ('✍️ Agente Escritor (personalizado)', 'Redige propostas na voz de cada recrutador, personalizadas por conta, multi-canal (e-mail + LinkedIn).', 'https://ziontechgroup.com/ai-sales-outreach/', 'https://github.com/Zion-support/zion-ai-sales-outreach'),
            ('🔄 Agente de Sequenciamento (multi-touch)', 'Sequências multi-touch (Dia 1 e-mail, Dia 3 LinkedIn, Dia 5 estudo de caso), adaptativas à resposta, com timing de envio otimizado.', 'https://ziontechgroup.com/ai-sales-outreach/', 'https://github.com/Zion-support/zion-ai-sales-outreach'),
            ('📥 Agente de Tratamento de Respostas', 'Classifica respostas, redige follow-ups, encaminha Leads qualificados para o recrutador, agenda reuniões.', 'https://ziontechgroup.com/ai-sales-outreach/', 'https://github.com/Zion-support/zion-ai-sales-outreach'),
            ('📋 Escrita no CRM + Mercial Solicitável', 'Regista atividades no CRM (HubSpot), monitora volume de envio/saúde do domínio, rotaciona caixas de correio.', 'https://ziontechgroup.com/ai-sales-outreach/', 'https://github.com/Zion-support/zion-ai-sales-outreach'),
        ],
        'discovery_h2': '🧭 Descoberta Gratuita — sempre online, sempre gratuita',
        'discovery_p': 'Dê aos vossos recrutadores um exército 24/7 que pesquisa, redige e faz follow-up em e-mail, LinkedIn e telefone — em todos os idiomas que atendemos. O seu sistema de prospecção é gerado instantaneamente e enviado por e-mail para você e nossa equipa comercial (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Iniciar Descoberta Gratuita',
        'discovery_cta2': 'Navegar pela Rede de Aplicativos',
    },
    'es': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sales-outreach-2026.html">English</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sales-outreach-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sales-outreach-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sales-outreach-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sales-outreach-2026-de.html">Deutsch</a></nav>',
        'title': 'Agente de Prospección y Envío Multi-Canal con IA — Zion Tech Group',
        'description': 'Hub gratuito de Agente de Prospección y Envío Multi-Canal con IA: investigación de cuentas, enriquecimiento de contactos, redacción personalizada, secuencias multi-touch (e-mail/Redes Sociales/Llamadas), tratamiento de respuestas y escritura en CRM — para clientes FE/técnicos y el equipo comercial Zion.',
        'h1': '🤖 Agente de Prospección y Envío Multi-Canal con IA',
        'pitch': 'Dé a sus reclutadores un ejército 24/7 que investiga, escribe y hace follow-up en correo, LinkedIn y teléfono — en todos los idiomas que atendemos. Agente de prospección multi-canal: investigación → enriquecimiento → redactor personalizado → secuenciación multi-touch → tratamiento de respuestas → escritura en CRM, con el reclutador en la puerta de aprobación. Todos los idiomas que atendemos.',
        'cards': [
            ('🔍 Agente de Investigación', 'Monitorea cuentas objetivo de señales de compra, conduce investigación de cuentas via CRM + fuentes externas y revela insight del comité de compra.', 'https://ziontechgroup.com/ai-sales-outreach/', 'https://github.com/Zion-support/zion-ai-sales-outreach'),
            ('📦 Agente de Enriquecimiento', 'Añade contacto verificado + firmographics + señales de intención de Apollo, ZoomInfo, Surfe, Seamless.', 'https://ziontechgroup.com/ai-sales-outreach/', 'https://github.com/Zion-support/zion-ai-sales-outreach'),
            ('✍️ Agente Escritor (personalizado)', 'Redacta propuestas en la voz de cada reclutador, personalizadas por cuenta, multi-canal (correo + LinkedIn).', 'https://ziontechgroup.com/ai-sales-outreach/', 'https://github.com/Zion-support/zion-ai-sales-outreach'),
            ('🔄 Agente de Secuenciación (multi-touch)', 'Secuencias multi-touch (Día 1 correo, Día 3 LinkedIn, Día 5 caso de estudio), adaptativas a la respuesta, con timing de envío optimizado.', 'https://ziontechgroup.com/ai-sales-outreach/', 'https://github.com/Zion-support/zion-ai-sales-outreach'),
            ('📥 Agente de Tratamiento de Respuestas', 'Clasifica respuestas, redacta follow-ups, enruta Leads calificados al reclutador, agenda reuniones.', 'https://ziontechgroup.com/ai-sales-outreach/', 'https://github.com/Zion-support/zion-ai-sales-outreach'),
            ('📋 Escritura en CRM + Entrega Solicitada', 'Registra actividades en CRM (HubSpot), monitora volumen de envío/salud del dominio, rota carpetas de correo.', 'https://ziontechgroup.com/ai-sales-outreach/', 'https://github.com/Zion-support/zion-ai-sales-outreach'),
        ],
        'discovery_h2': '🧭 Descubrimiento Gratuito — siempre en línea, siempre gratuito',
        'discovery_p': 'Dé a sus reclutadores un ejército 24/7 que investiga, escribe y hace follow-up en correo, LinkedIn y teléfono — en todos los idiomas que atendemos. Su sistema de prospección se genera instantáneamente y se envía por correo a usted y nuestro equipo comercial (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Comenzar Descubrimiento Gratuito',
        'discovery_cta2': 'Explorar la Red de Aplicaciones',
    },
    'fr': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sales-outreach-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sales-outreach-2026-fr.html">Français</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sales-outreach-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sales-outreach-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sales-outreach-2026-de.html">Deutsch</a></nav>',
        'title': 'Agent de Prospection et Envoi Multi-Canaux IA — Zion Tech Group',
        'description': 'Hub gratuit de Agent de Prospection et Envoi Multi-Canaux IA : recherche de comptes, enrichissement de contacts, rédaction personnalisée, séquences multi-touch (e-mail/Réseaux sociaux/Téléphone), traitement des réponses et écriture CRM — pour clients FE/techniciens et l\'équipe commerciale Zion.',
        'h1': '🤖 Agent de Prospection et Envoi Multi-Canaux IA',
        'pitch': 'Donnez à vos recruteurs un corps 24/7 qui recherche, rédige et fait du follow-up sur e-mail, LinkedIn et téléphone — dans toutes les langues que nous desservons. Agent de prospection multi-canal : recherche → enrichissement → rédacteur personnalisé → séquence multi-touch → traitement des réponses → écriture CRM, avec le recruteur à la porte d\'approbation. Toutes les langues desservies.',
        'cards': [
            ('🔍 Agent de Recherche', 'Surveille les comptes cibles de signaux d\'achat, conduit la recherche de comptes via CRM + sources externes, révèle des insights du comité d\'achat.', 'https://ziontechgroup.com/ai-sales-outreach/', 'https://github.com/Zion-support/zion-ai-sales-outreach'),
            ('📦 Agent d\'Enrichissement', 'Ajoute contact vérifié + firmographics + données d\'intention d\'Apollo, ZoomInfo, Surfe, Seamless.', 'https://ziontechgroup.com/ai-sales-outreach/', 'https://github.com/Zion-support/zion-ai-sales-outreach'),
            ('✍️ Agent Rédacteur (personnalisé)', 'Rédige des propositions dans la voix de chaque recruteur, personnalisées par compte, multi-canal (e-mail + LinkedIn).', 'https://ziontechgroup.com/ai-sales-outreach/', 'https://github.com/Zion-support/zion-ai-sales-outreach'),
            ('🔄 Agent de Séquençage (multi-touch)', 'Séquences multi-touch (Jour 1 e-mail, Jour 3 LinkedIn, Jour 5 étude de cas), adaptatives à la réponse, avec timing d\'envoi optimisé.', 'https://ziontechgroup.com/ai-sales-outreach/', 'https://github.com/Zion-support/zion-ai-sales-outreach'),
            ('📥 Agent de Traitement des Réponses', 'Classe les réponses, rédige des follow-ups, oriente les Leads qualifiés vers le recruteur, planifie des rendez-vous.', 'https://ziontechgroup.com/ai-sales-outreach/', 'https://github.com/Zion-support/zion-ai-sales-outreach'),
            ('📋 Écriture CRM + Livraison Demandée', 'Enregistre les activités dans le CRM (HubSpot), surveille le volume d\'envoi/santé du domaine, fait tourner les boîtes de réception.', 'https://ziontechgroup.com/ai-sales-outreach/', 'https://github.com/Zion-support/zion-ai-sales-outreach'),
        ],
        'discovery_h2': '🧭 Découverte Gratuite — toujours en ligne, toujours gratuite',
        'discovery_p': 'Donnez à vos recruteurs un corps 24/7 qui recherche, rédige et fait du follow-up sur e-mail, LinkedIn et téléphone — dans toutes les langues que nous desservons. Votre système de prospection est généré instantanément et envoyé par e-mail à vous et à notre équipe commerciale (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Commencer la Découverte Gratuite',
        'discovery_cta2': 'Parcourir le Réseau d\'Applications',
    },
    'de': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sales-outreach-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sales-outreach-2026-de.html">Deutsch</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sales-outreach-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sales-outreach-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sales-outreach-2026-fr.html">Français</a></nav>',
        'title': 'KI-Sales-Outreach & Multi-Kanal-engagement — Prospektions-Agent — Zion Tech Group',
        'description': 'Kostenloser KI-Sales-Outreach & Multi-Kanal-Engagement-HuB: Kontenforschung, Kontakternährung, personalisierte Kontaktvorschläge, Multi-Touch-Sequenzen (E-Mail/LinkedIn/Telefon), Antwortbearbeitung und CRM-Schreiben — für FE/Techniker-Kunden und das Zion-Vertriebsteam.',
        'h1': '🤖 KI-Sales-Outreach & Multi-Kanal-Engagement',
        'pitch': 'Gewähren Sie jedem Recruiter ein 24/7-Armee, das recherchiert, schreibt und follow-up in E-Mail, LinkedIn und Telefon macht — in allen Sprachen, die wir bedienen. Multi-Kanal-Prospektions-Agent: Forschung → Ernährung → personalisierter Schreiber → Multi-Touch-Sequenz → Antwortverarbeitung → CRM-Schreiben mit Freigabe durch den Recruiter. Alle Sprachen, die wir bedienen.',
        'cards': [
            ('🔍 Forschungs-Agent', 'Überwacht Ziellagen nach Kaufsignalen, führt Kontenforschung via CRM + externe Quellen durch, zeigt Käuferkomitee-Einsichten.', 'https://ziontechgroup.com/ai-sales-outreach/', 'https://github.com/Zion-support/zion-ai-sales-outreach'),
            ('📦 Ernährungs-Agent', 'Fügt verifizierte Kontakt + Firmendaten + Intent-Signale von Apollo, ZoomInfo, Surfe, Seamless hinzu.', 'https://ziontechgroup.com/ai-sales-outreach/', 'https://github.com/Zion-support/zion-ai-sales-outreach'),
            ('✍️ Schreiber-Agent (personalisiert)', 'Verfasst Kontaktvorschläge in der Stimme jedes Recruiters, personalisiert nach Konto, multi-kanal (E-Mail + LinkedIn).', 'https://ziontechgroup.com/ai-sales-outreach/', 'https://github.com/Zion-support/zion-ai-sales-outreach'),
            ('🔄 Sequenzierungs-Agent (multi-touch)', 'Multi-Touch-Sequenzen (Tag 1 E-Mail, Tag 3 LinkedIn, Tag 5 Fallstudie), anpassungsfähig an die Antwort, optimierte Sendezeitpunkte.', 'https://ziontechgroup.com/ai-sales-outreach/', 'https://github.com/Zion-support/zion-ai-sales-outreach'),
            ('📥 Antwortbearbeitungs-Agent', 'Klassifiziert Antworten, verfasst Follow-ups, leitet qualifizierte Antworten an den Recruiter weiter, bucht Meetings.', 'https://ziontechgroup.com/ai-sales-outreach/', 'https://github.com/Zion-support/zion-ai-sales-outreach'),
            ('📋 CRM-Schreibvorgang + Lieferbarkeit', 'Protokolliert Aktivitäten im CRM (HubSpot), überwacht Sendevolumen/Domänengesundheit, rotiert Postfächer.', 'https://ziontechgroup.com/ai-sales-outreach/', 'https://github.com/Zion-support/zion-ai-sales-outreach'),
        ],
        'discovery_h2': '🧭 Kostenloser Entdeckung — immer online, immer kostenlos',
        'discovery_p': '-Geben Sie Ihren Recruitern ein 24/7-Armee, das recherchiert, schreibt und follow-up in E-Mail, LinkedIn und Telefon macht — in allen Sprachen, die wir bedienen. Ihr Outbound-System wird augenblicklich generiert und per E-Mail an Sie und unser Vertriebsteam (commercial@ziontechgroup.com) gesendet.',
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
    labels = ['🔍 Research', '📦 Enrichment', '✍️ Writer (personalised)', '🔄 Sequencing (multi-touch)', '📥 Reply Handling', '📋 CRM Write-Back']
    section_html = ''
    for grp, label in zip(cards_groups, labels):
        gh = ''.join(f'<div class="card"><h3>{h}</h3><p>{d}</p><a href="{live}">Live app →</a> · <a href="{repo}">Repo</a></div>' for h, d, live, repo in grp)
        section_html += f'<section><h2>{label}</h2><div class="cards">{gh}</div></section>'
    disc = f'<div class="disc"><h2>{body["discovery_h2"]}</h2><p>{body["discovery_p"]}</p><a class="cta green" href="https://ziontechgroup.com/discovery/">{body["discovery_cta1"]}</a><a class="cta alt" href="https://ziontechgroup.com/zion-app-network/">{body["discovery_cta2"]}</a></div>'
    closing = '<p style="margin-top:24px"><a href="https://ziontechgroup.com">← ziontechgroup.com</a> · <a href="https://github.com/Zion-support/zion-app-network/blob/main/SPOTLIGHT-ai-sales-outreach-2026.md">Spotlight doc</a> · <a href="https://github.com/Zion-support/zion-app-network/blob/main/APPS_INDEX-BATCH130-OUTREACH.md">Batch rollup</a></p>'
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
    path = os.path.join(WORK, f'app-network-ai-sales-outreach-2026{"-"+ext if ext else ""}.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("wrote", path, "len", len(content))
