import os

WORK = '/Users/miami2/.hermes/profiles/agent-finops-ops/cache/apphub'
os.makedirs(WORK, exist_ok=True)

BASE = 'https://ziontechgroup.com/zion-app-network/app'
CANON = f'{BASE}/app-network-ai-sdr-multi-agent-2026.html'
L = {
    'pt': f'{BASE}/app-network-ai-sdr-multi-agent-2026-pt.html',
    'es': f'{BASE}/app-network-ai-sdr-multi-agent-2026-es.html',
    'fr': f'{BASE}/app-network-ai-sdr-multi-agent-2026-fr.html',
    'de': f'{BASE}/app-network-ai-sdr-multi-agent-2026-de.html',
}
LANGS = [('en', CANON), ('pt-BR', L['pt']), ('es', L['es']), ('fr', L['fr']), ('de', L['de'])]

BODY = {
    'en': {
        'langbar': '<nav class="langbar">🌐 <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sdr-multi-agent-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sdr-multi-agent-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sdr-multi-agent-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sdr-multi-agent-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sdr-multi-agent-2026-de.html">Deutsch</a></nav>',
        'title': 'AI SDR & Multi-Agent Lead Agent — 24/7 Account-Based Outbound — Zion Tech Group',
        'description': 'Free AI SDR & Multi-Agent Lead Agent hub: prospector + enrichment + personalised outreach + sequencing + qualification, orchestrating the full account-based outbound pipeline for FE\'s & technicians.',
        'h1': '🤖 AI SDR & Multi-Agent Lead Agent',
        'pitch': 'An SDR agent for every lead we\'ve already worked with — researches, writes, follows up, and books meetings, 24/7, in your language, no cold calling. Multi-agent orchestrator (prospector → enrichment → writer → sequencer → inbox → qualification) with human-in-the-loop review. Feeds the CRM, HubSpot, and the agent marketplace.',
        'cards': [
            ('🔍 Prospector Agent', 'Finds ICP-matched accounts from your email history + external signals (intent, firmographics).', 'https://ziontechgroup.com/ai-sdr-multi-agent/', 'https://github.com/Zion-support/zion-ai-sdr-multi-agent'),
            ('📦 Enrichment Agent', 'Adds verified contact + firmographics + buying signals; writes CRM records.', 'https://ziontechgroup.com/ai-sdr-multi-agent/', 'https://github.com/Zion-support/zion-ai-sdr-multi-agent'),
            ('✍️ Writer Agent (personalised)', 'Calibrated to the intent signal + prior company engagement; human review 3–5 min/account.', 'https://ziontechgroup.com/ai-sdr-multi-agent/', 'https://github.com/Zion-support/zion-ai-sdr-multi-agent'),
            ('🔄 Sequencer Agent (multi-step)', 'Runs follow-up sequences across email + LinkedIn; adaptive based on reply behavior.', 'https://ziontechgroup.com/ai-sdr-multi-agent/', 'https://github.com/Zion-support/zion-ai-sdr-multi-agent'),
            ('📥 Inbox + Qualification Agent', 'Classifies replies, scores intent, routes qualified leads to meeting booking.', 'https://ziontechgroup.com/ai-sdr-multi-agent/', 'https://github.com/Zion-support/zion-ai-sdr-multi-agent'),
            ('📆 Meeting Booking + CRM Sync', 'Books confirmed leads via calendar; syncs full conversation context to HubSpot.', 'https://ziontechgroup.com/ai-sdr-multi-agent/', 'https://github.com/Zion-support/zion-ai-sdr-multi-agent'),
        ],
        'discovery_h2': '🧭 Free Discovery — always online, always free',
        'discovery_p': 'Get a multi-agent outbound system for every lead we\'ve already worked with — research, personalise, follow up, and book meetings, 24/7. Your system is generated instantly and emailed to you and our commercial team (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Start Free Discovery',
        'discovery_cta2': 'Browse the App Network',
    },
    'pt': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sdr-multi-agent-2026.html">English</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sdr-multi-agent-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sdr-multi-agent-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sdr-multi-agent-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sdr-multi-agent-2026-de.html">Deutsch</a></nav>',
        'title': 'SDR com IA e Agente Multi-Agente de Leads — outbound de conta base 24/7 — Zion Tech Group',
        'description': 'Hub gratuito de SDR com IA e Agente Multi-Agente de Leads: prospetor + enriquecimento + outreach personalizado + sequenciador + qualificação, orquestrando o pipeline de outbound de conta base, para FE\'s & técnicos.',
        'h1': '🤖 SDR com IA e Agente Multi-Agente de Leads',
        'pitch': 'Um agente SDR para cada lead com quem já trabalhamos — pesquisa, escreve, faz follow-up e agenda reuniões, 24/7, no seu idioma, sem ligações frias. Orquestrador multi-agente (prospector → enriquecimento → escritor → sequenciador → caixa de entrada → qualificação) com revisão humana. Alimenta o CRM, HubSpot e o marketplace de agentes.',
        'cards': [
            ('🔍 Agente Prospector', 'Encontra contas ICP compatíveis a partir do histórico de e-mail + sinais externos (intenção, firmographics).', 'https://ziontechgroup.com/ai-sdr-multi-agent/', 'https://github.com/Zion-support/zion-ai-sdr-multi-agent'),
            ('📦 Agente de Enriquecimento', 'Adiciona contato verificado + firmographics + sinais de compra; escreve registros no CRM.', 'https://ziontechgroup.com/ai-sdr-multi-agent/', 'https://github.com/Zion-support/zion-ai-sdr-multi-agent'),
            ('✍️ Agente Escritor (personalizado)', 'Calibrado à sinal de intenção + histórico de engajamento da empresa; revisão humana em 3–5 min/conta.', 'https://ziontechgroup.com/ai-sdr-multi-agent/', 'https://github.com/Zion-support/zion-ai-sdr-multi-agent'),
            ('🔄 Agente Sequenciador (multistep)', 'Executa sequências de follow-up em e-mail + LinkedIn; adaptativo por comportamento de resposta.', 'https://ziontechgroup.com/ai-sdr-multi-agent/', 'https://github.com/Zion-support/zion-ai-sdr-multi-agent'),
            ('📥 Agente Inbox + Qualificação', 'Classifica respostas, pontua intenção, roteia leads qualificados para agendamento de reuniões.', 'https://ziontechgroup.com/ai-sdr-multi-agent/', 'https://github.com/Zion-support/zion-ai-sdr-multi-agent'),
            ('📆 Agendamento de Reuniões + Sincronia de CRM', 'Agenda reuniões confirmadas via calendário; sincroniza contexto completo das conversas para HubSpot.', 'https://ziontechgroup.com/ai-sdr-multi-agent/', 'https://github.com/Zion-support/zion-ai-sdr-multi-agent'),
        ],
        'discovery_h2': '🧭 Descoberta Gratuita — sempre online, sempre gratuita',
        'discovery_p': 'Receba um sistema de outbound multi-agente para cada lead com quem já trabalhamos — pesquise, personalize, faça follow-up e agende reuniões, 24/7. Seu sistema é gerado instantaneamente e enviado por e-mail para você e nossa equipe comercial (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Iniciar Descoberta Gratuita',
        'discovery_cta2': 'Navegar pela Rede de Aplicativos',
    },
    'es': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sdr-multi-agent-2026.html">English</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sdr-multi-agent-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sdr-multi-agent-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sdr-multi-agent-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sdr-multi-agent-2026-de.html">Deutsch</a></nav>',
        'title': 'SDR con IA y Agente Multi-Agence de Leads — outbound de cuenta basado 24/7 — Zion Tech Group',
        'description': 'Hub gratuito de SDR con IA y Agente Multi-Agence de Leads: prospector + enriquecimiento + outreach personalizado + secuenciador + calificación, orquestrando el pipeline de outbound de cuenta base para FE\'s & técnicos.',
        'h1': '🤖 SDR con IA y Agente Multi-Agence de Leads',
        'pitch': 'Un agente SDR para cada lead con quien ya trabajamos — investiga, escribe, hace follow-up y agenda reuniones, 24/7, en su idioma, sin llamadas frías. Orquestador multi-agente (prospector → enriquecimiento → escritor → secuenciador → buzón → calificación) con revisión humana. Alimenta el CRM, HubSpot y el marketplace de agentes.',
        'cards': [
            ('🔍 Agente Prospector', 'Encuentra cuentas ICP compatibles desde su historial de correo + señales externas (intencionalidad, firmographics).', 'https://ziontechgroup.com/ai-sdr-multi-agent/', 'https://github.com/Zion-support/zion-ai-sdr-multi-agent'),
            ('📦 Agente de Enriquecimiento', 'Añade contacto verificado + firmographics + señales de compra; escribe registros en el CRM.', 'https://ziontechgroup.com/ai-sdr-multi-agent/', 'https://github.com/Zion-support/zion-ai-sdr-multi-agent'),
            ('✍️ Agente Escritor (personalizado)', 'Calibrado a la señal de intención + historial de engagement de la empresa; revisión humana en 3–5 min/cuenta.', 'https://ziontechgroup.com/ai-sdr-multi-agent/', 'https://github.com/Zion-support/zion-ai-sdr-multi-agent'),
            ('🔄 Agente Secuenciador (multistep)', 'Ejecuta secuencias de follow-up en correo + LinkedIn; adaptable por comportamiento de respuesta.', 'https://ziontechgroup.com/ai-sdr-multi-agent/', 'https://github.com/Zion-support/zion-ai-sdr-multi-agent'),
            ('📥 Agente Inbox + Calificación', 'Clasifica respuestas, puntúa intención, enruta leads calificados a agendamiento de reuniones.', 'https://ziontechgroup.com/ai-sdr-multi-agent/', 'https://github.com/Zion-support/zion-ai-sdr-multi-agent'),
            ('📆 Agendamiento de Reuniones + Sincronía de CRM', 'Agenda reuniones confirmadas vía calendario; sincroniza contexto completo de conversaciones a HubSpot.', 'https://ziontechgroup.com/ai-sdr-multi-agent/', 'https://github.com/Zion-support/zion-ai-sdr-multi-agent'),
        ],
        'discovery_h2': '🧭 Descubrimiento Gratuito — siempre en línea, siempre gratuito',
        'discovery_p': 'Obtenga un sistema de outbound multi-agente para cada lead con quien ya trabajamos — investigue, personalised, haga follow-up y agenda reuniones, 24/7. Su sistema se genera instantáneamente y se envía por correo a usted y a nuestro equipo comercial (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Comenzar Descubrimiento Gratuito',
        'discovery_cta2': 'Explorar la Red de Aplicaciones',
    },
    'fr': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sdr-multi-agent-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sdr-multi-agent-2026-fr.html">Français</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sdr-multi-agent-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sdr-multi-agent-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sdr-multi-agent-2026-de.html">Deutsch</a></nav>',
        'title': 'SDR IA et Agent Multi-Agents de Leads — outbound de compte en ligne 24/7 — Zion Tech Group',
        'description': 'Hub gratuit de SDR IA et Agent Multi-Agents de Leads : prospecteur + enrichissement + outreach personnalisé + séquenceur + qualification, orchestrant le pipeline de outbound de compte en ligne, pour FE\'s & techniciens.',
        'h1': '🤖 SDR IA et Agent Multi-Agents de Leads',
        'pitch': 'Un agent SDR pour chaque lead avec qui nous avons déjà travaillé — recherche, rédaction, follow-up, prise de rendez-vous, 24/7, dans votre langue, sans appels froids. Orchestrateur multi-agents (prospecteur → enrichissement → rédacteur → séquenceur → boîte de réception → qualification) avec validation humaine. Alimente le CRM, HubSpot et le marketplace d\'agents.',
        'cards': [
            ('🔍 Agent Prospecteur', 'Trouve les comptes ICP compatibles à partir de l\'historique e-mail + signaux externes (intention, firmographics).', 'https://ziontechgroup.com/ai-sdr-multi-agent/', 'https://github.com/Zion-support/zion-ai-sdr-multi-agent'),
            ('📦 Agent d\'Enrichissement', 'Ajoute le contact vérifié + firmographics + signaux d\'achat ; rédige les enregistrements CRM.', 'https://ziontechgroup.com/ai-sdr-multi-agent/', 'https://github.com/Zion-support/zion-ai-sdr-multi-agent'),
            ('✍️ Agent Rédacteur (personnalisé)', 'Calibré au signal d\'intention + historique d\'engagement de l\'entreprise ; validation humaine en 3–5 min/par compte.', 'https://ziontechgroup.com/ai-sdr-multi-agent/', 'https://github.com/Zion-support/zion-ai-sdr-multi-agent'),
            ('🔄 Agent Séquenceur (multistep)', 'Exécute des séquences de follow-up e-mail + LinkedIn ; adaptatif selon le comportement de réponse.', 'https://ziontechgroup.com/ai-sdr-multi-agent/', 'https://github.com/Zion-support/zion-ai-sdr-multi-agent'),
            ('📥 Agent Boîte de réception + Qualification', 'Classe les réponses, évalue l\'intention, oriente les leads qualifiés vers la prise de rendez-vous.', 'https://ziontechgroup.com/ai-sdr-multi-agent/', 'https://github.com/Zion-support/zion-ai-sdr-multi-agent'),
            ('📆 Prise de RDV + Synchronisation CRM', 'Prend des rendez-vous confirmés via calendrier ; synchronise le contexte complet des conversations vers HubSpot.', 'https://ziontechgroup.com/ai-sdr-multi-agent/', 'https://github.com/Zion-support/zion-ai-sdr-multi-agent'),
        ],
        'discovery_h2': '🧭 Découverte Gratuite — toujours en ligne, toujours gratuite',
        'discovery_p': 'Obtenez un système de outbound multi-agents pour chaque lead avec qui nous avons déjà travaillé — recherche, personnalise, faites un follow-up et prenez des rendez-vous, 24/7. Votre système est généré instantanément et envoyé par e-mail à vous et à notre équipe commerciale (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Commencer la Découverte Gratuite',
        'discovery_cta2': 'Parcourir le Réseau d\'Applications',
    },
    'de': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sdr-multi-agent-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sdr-multi-agent-2026-de.html">Deutsch</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sdr-multi-agent-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sdr-multi-agent-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-sdr-multi-agent-2026-fr.html">Français</a></nav>',
        'title': 'KI-SDR & Multi-Agenten-Lead-Agent — 24/7 Account-Based Outbound — Zion Tech Group',
        'description': 'Kostenloser KI-SDR & Multi-Agenten-Lead-Agent-HuB: Prospector + Anreicherung + personalisierter Outbound + Sequenzierung + Qualifizierung, der den kompletten Account-Based-Outbound-Pipeline orchestriert, für FE\'s & Techniker.',
        'h1': '🤖 KI-SDR & Multi-Agenten-Lead-Agent',
        'pitch': 'Ein SDR-Agent für jeden Lead, mit dem wir bereits gearbeitet haben — recherchiere, schreibe, mache Follow-up und vereinbare Meetings, 24/7, in deiner Sprache, ohne Cold-Calls. Multi-Agenten-Orchestriert (Prospector → Anreicherung → Schreiber → Sequenzer → Posteingang → Qualifizierung) mit menschlicher Freigabe. Speist das CRM, HubSpot und den Agentenmarktplatz.',
        'cards': [
            ('🔍 Prospector-Agent', 'Findet ICP-passende Konten aus deiner E-Mail-Geschichte + externen Signalen (Absicht, Firmendaten).', 'https://ziontechgroup.com/ai-sdr-multi-agent/', 'https://github.com/Zion-support/zion-ai-sdr-multi-agent'),
            ('📦 Anreicherungs-Agent', 'Fügt verifizierte Kontakt + Firmendaten + Kaufsignale hinzu; schreibt CRM-Einträge.', 'https://ziontechgroup.com/ai-sdr-multi-agent/', 'https://github.com/Zion-support/zion-ai-sdr-multi-agent'),
            ('✍️ Schreiber-Agent (personalisiert)', 'Kalibriert auf das Absichts-Signal + vorherige Firmen-Aufklärung; menschliche Freigabe in 3–5 Min/Account.', 'https://ziontechgroup.com/ai-sdr-multi-agent/', 'https://github.com/Zion-support/zion-ai-sdr-multi-agent'),
            ('🔄 Sequenzierungs-Agent (multistep)', 'Führt Follow-up-Sequenzen auf E-Mail + LinkedIn aus; anpassungsfähig nach Antwort-Verhalten.', 'https://ziontechgroup.com/ai-sdr-multi-agent/', 'https://github.com/Zion-support/zion-ai-sdr-multi-agent'),
            ('📥 Posteingang + Qualifizierungs-Agent', 'Klassifiziert Antworten, bewertet Intent, leitet qualifizierte Leads zur Meeting-Buchung.', 'https://ziontechgroup.com/ai-sdr-multi-agent/', 'https://github.com/Zion-support/zion-ai-sdr-multi-agent'),
            ('📆 Meeting-Buchung + CRM-Sync', 'Bucht bestätigte Meetings via Kalender; synchronisiert vollen Gesprächskontext zu HubSpot.', 'https://ziontechgroup.com/ai-sdr-multi-agent/', 'https://github.com/Zion-support/zion-ai-sdr-multi-agent'),
        ],
        'discovery_h2': '🧭 Kostenloser Entdeckung — immer online, immer kostenlos',
        'discovery_p': '-erhalten Sie ein Multi-Agenten-Outbound-System für jeden Lead, mit dem wir bereits gearbeitet haben — recherchiere, personalisieren, mache Follow-up und buchen Sie Meetings, 24/7. Ihr System wird augenblicklich generiert und per E-Mail an Sie und unser Vertriebsteam (commercial@ziontechgroup.com) gesendet.',
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
    labels = ['🔍 Prospector + Enrichment', '✍️ Writer (personalised)', '🔄 Sequencer', '📥 Inbox + Qualification', '📆 Meeting Booking + CRM Sync']
    section_html = ''
    for grp, label in zip(cards_groups, labels):
        gh = ''.join(f'<div class="card"><h3>{h}</h3><p>{d}</p><a href="{live}">Live app →</a> · <a href="{repo}">Repo</a></div>' for h, d, live, repo in grp)
        section_html += f'<section><h2>{label}</h2><div class="cards">{gh}</div></section>'
    disc = f'<div class="disc"><h2>{body["discovery_h2"]}</h2><p>{body["discovery_p"]}</p><a class="cta green" href="https://ziontechgroup.com/discovery/">{body["discovery_cta1"]}</a><a class="cta alt" href="https://ziontechgroup.com/zion-app-network/">{body["discovery_cta2"]}</a></div>'
    closing = '<p style="margin-top:24px"><a href="https://ziontechgroup.com">← ziontechgroup.com</a> · <a href="https://github.com/Zion-support/zion-app-network/blob/main/SPOTLIGHT-ai-sdr-multi-agent-2026.md">Spotlight doc</a> · <a href="https://github.com/Zion-support/zion-app-network/blob/main/APPS_INDEX-BATCH125-SDR.md">Batch rollup</a></p>'
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
    path = os.path.join(WORK, f'app-network-ai-sdr-multi-agent-2026{"-"+ext if ext else ""}.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("wrote", path, "len", len(content))
