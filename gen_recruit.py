import os

WORK = '/Users/miami2/.hermes/profiles/agent-finops-ops/cache/apphub'
os.makedirs(WORK, exist_ok=True)

BASE = 'https://ziontechgroup.com/zion-app-network/app'
CANON = f'{BASE}/app-network-ai-recruiting-pipeline-2026.html'
L = {
    'pt': f'{BASE}/app-network-ai-recruiting-pipeline-2026-pt.html',
    'es': f'{BASE}/app-network-ai-recruiting-pipeline-2026-es.html',
    'fr': f'{BASE}/app-network-ai-recruiting-pipeline-2026-fr.html',
    'de': f'{BASE}/app-network-ai-recruiting-pipeline-2026-de.html',
}
LANGS = [('en', CANON), ('pt-BR', L['pt']), ('es', L['es']), ('fr', L['fr']), ('de', L['de'])]

BODY = {
    'en': {
        'langbar': '<nav class="langbar">🌐 <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-recruiting-pipeline-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-recruiting-pipeline-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-recruiting-pipeline-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-recruiting-pipeline-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-recruiting-pipeline-2026-de.html">Deutsch</a></nav>',
        'title': 'AI Recruiting Pipeline Agent — End-to-End Hiring Automation — Zion Tech Group',
        'description': 'Free AI Recruiting Pipeline Agent hub: sourcing, conversational screening, interview scheduling, candidate engagement, and ATS/CRM write-back — for FE/technician hiring, done in your language.',
        'h1': '🤖 AI Recruiting Pipeline Agent',
        'pitch': 'Every FE or technician we need is one screen away — sourcing, screening, scheduling, and booked, without a single manual step. Multi-agent orchestrator (sourcing → screening → scheduling → engagement → ATS write-back) with recruiter-in-the-loop approvals. 24/7, multilingual, built for Zion\'s service team.',
        'cards': [
            ('🔍 Sourcing Agent', 'Searches LinkedIn, job boards, and professional networks for FE/technician candidates, ranked by fit.', 'https://ziontechgroup.com/ai-recruiting-pipeline/', 'https://github.com/Zion-support/zion-ai-recruiting-pipeline'),
            ('📝 Screening Agent (conversational)', 'Chat/voice AI screening that scores candidates against role criteria, with interviewer confirmation.', 'https://ziontechgroup.com/ai-recruiting-pipeline/', 'https://github.com/Zion-support/zion-ai-recruiting-pipeline'),
            ('📅 Interview Scheduling Agent', 'Resolves the three-sided scheduling problem (candidate × hiring manager × interviewer) via calendar integration.', 'https://ziontechgroup.com/ai-recruiting-pipeline/', 'https://github.com/Zion-support/zion-ai-recruiting-pipeline'),
            ('🗣️ Candidate Engagement Agent', '24/7 conversational engagement: instant answers, status updates, interview reminders, feedback delivery.', 'https://ziontechgroup.com/ai-recruiting-pipeline/', 'https://github.com/Zion-support/zion-ai-recruiting-pipeline'),
            ('📋 ATS/CRM Write-Back', 'Writes candidate records and interview outcomes to the ATS/CRM (HubSpot), with audit trail.', 'https://ziontechgroup.com/ai-recruiting-pipeline/', 'https://github.com/Zion-support/zion-ai-recruiting-pipeline'),
            ('📊 Pipeline & Time-to-Hire Analytics', 'Dashboards for sourcing sources, time-to-fill, quality-of-hire, and pipeline health.', 'https://ziontechgroup.com/ai-recruiting-pipeline/', 'https://github.com/Zion-support/zion-ai-recruiting-pipeline'),
        ],
        'discovery_h2': '🧭 Free Discovery — always online, always free',
        'discovery_p': 'Get your hiring pipeline automated: sourced, screened, scheduled, and booked, for FE/technicians and service roles. Your pipeline is generated instantly and emailed to you and our commercial team (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Start Free Discovery',
        'discovery_cta2': 'Browse the App Network',
    },
    'pt': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-recruiting-pipeline-2026.html">English</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-recruiting-pipeline-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-recruiting-pipeline-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-recruiting-pipeline-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-recruiting-pipeline-2026-de.html">Deutsch</a></nav>',
        'title': 'Agente Multi-Agente de Recrutamento com IA — automação completa de contratação — Zion Tech Group',
        'description': 'Hub gratuito de Agente Multi-Agente de Recrutamento com IA: sourcing, triagem conversacional, agendamento de entrevistas, engajamento de candidatos e escrita no ATS/CRM — para contratações de FE/técnicos, no seu idioma.',
        'h1': '🤖 Agente Multi-Agente de Recrutamento com IA',
        'pitch': 'Todo FE ou técnico que precisarmos está a um ecrã de distância — sourcing, triagem, agendamento e contratados, sem um único passo manual. Orquestrador multi-agente (sourcing → triagem → agendamento → engajamento → escrita no ATS) com aprovações no recrutador. 24/7, multilíngue, feito para a equipa de serviço Zion.',
        'cards': [
            ('🔍 Agente Sourcing', 'Pesquisa LinkedIn, portais de emprego e redes profissionais de FE/técnicos, classificados por afinidade.', 'https://ziontechgroup.com/ai-recruiting-pipeline/', 'https://github.com/Zion-support/zion-ai-recruiting-pipeline'),
            ('📝 Agente de Triagem (conversacional)', 'Triagem IA conversacional (chat/voz) que pontua candidatos por critérios do cargo, com confirmação do entrevistador.', 'https://ziontechgroup.com/ai-recruiting-pipeline/', 'https://github.com/Zion-support/zion-ai-recruiting-pipeline'),
            ('📅 Agente de Agendamento de Entrevista', 'Resolve o problema de agendamento de três lados (candidato × gestor × entrevistador) via integração de calendário.', 'https://ziontechgroup.com/ai-recruiting-pipeline/', 'https://github.com/Zion-support/zion-ai-recruiting-pipeline'),
            ('🗣️ Agente de Engajamento de Candidatos', 'Engajamento conversacional 24/7: respostas instantâneas, atualizações de estado, lembretes de entrevista, entrega de feedback.', 'https://ziontechgroup.com/ai-recruiting-pipeline/', 'https://github.com/Zion-support/zion-ai-recruiting-pipeline'),
            ('📋 Escrita no ATS/CRM', 'Escreve registos de candidatos e resultados de entrevistas no ATS/CRM (HubSpot), com registo de auditoria.', 'https://ziontechgroup.com/ai-recruiting-pipeline/', 'https://github.com/Zion-support/zion-ai-recruiting-pipeline'),
            ('📊 Análise de Pipeline e Tempo de Preenchimento', 'Painéis de fonte de candidatos, tempo de preenchimento, qualidade de recrutamento e saúde do pipeline.', 'https://ziontechgroup.com/ai-recruiting-pipeline/', 'https://github.com/Zion-support/zion-ai-recruiting-pipeline'),
        ],
        'discovery_h2': '🧭 Descoberta Gratuita — sempre online, sempre gratuita',
        'discovery_p': 'Receba o seu pipeline de contratação automatizado: sourcing, triagem, agendamento e contratados, para FE/técnicos e posições de serviço. O seu pipeline é gerado instantaneamente e enviado por e-mail para você e nossa equipe comercial (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Iniciar Descoberta Gratuita',
        'discovery_cta2': 'Navegar pela Rede de Aplicativos',
    },
    'es': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-recruiting-pipeline-2026.html">English</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-recruiting-pipeline-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-recruiting-pipeline-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-recruiting-pipeline-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-recruiting-pipeline-2026-de.html">Deutsch</a></nav>',
        'title': 'Agente Multi-Agence de Contratación con IA — automatización completa de contratación — Zion Tech Group',
        'description': 'Hub gratuito de Agente Multi-Agence de Contratación con IA: sourcing, triaje conversacional, agendamiento de entrevistas, gestión de candidatos y escritura en ATS/CRM — para contrataciones de FE/técnicos, en su idioma.',
        'h1': '🤖 Agente Multi-Agence de Contratación con IA',
        'pitch': 'Cada FE o técnico que necesitemos está a un ecrá de distancia — sourcing, triaje, agendamiento y contratados, sin un solo paso manual. Orquestador multi-agente (sourcing → triaje → agendamiento → gestión → escritura en ATS) con aprobación del reclutador. 24/7, multilenguaje, hecho para el equipo de servicios Zion.',
        'cards': [
            ('🔍 Agente Sourcing', 'Busca LinkedIn, portales de empleo y redes profesionales de FE/técnicos, clasificados por afinidad.', 'https://ziontechgroup.com/ai-recruiting-pipeline/', 'https://github.com/Zion-support/zion-ai-recruiting-pipeline'),
            ('📝 Agente de Triaje (conversacional)', 'Triage IA conversacional (chat/voz) que puntúa candidatos por criterios del puesto, con confirmación del entrevistador.', 'https://ziontechgroup.com/ai-recruiting-pipeline/', 'https://github.com/Zion-support/zion-ai-recruiting-pipeline'),
            ('📅 Agente de Agendamiento de Entrevistas', 'Resuelve el problema de tres lados (candidato × gestor × entrevistador) vía integración de calendario.', 'https://ziontechgroup.com/ai-recruiting-pipeline/', 'https://github.com/Zion-support/zion-ai-recruiting-pipeline'),
            ('🗣️ Agente de Gestión de Candidatos', 'Gestión conversacional 24/7: respuestas instantáneas, actualizaciones de estado, recordatorios de entrevista, entrega de feedback.', 'https://ziontechgroup.com/ai-recruiting-pipeline/', 'https://github.com/Zion-support/zion-ai-recruiting-pipeline'),
            ('📋 Escritura en ATS/CRM', 'Escribe registros de candidatos y resultados de entrevistas en ATS/CRM (HubSpot), con registro de auditoría.', 'https://ziontechgroup.com/ai-recruiting-pipeline/', 'https://github.com/Zion-support/zion-ai-recruiting-pipeline'),
            ('📊 Análisis de Pipeline y Tiempo de Poblamiento', 'Paneles de fuente de candidatos, tiempo de llenado, calidad de reclutamiento y salud del pipeline.', 'https://ziontechgroup.com/ai-recruiting-pipeline/', 'https://github.com/Zion-support/zion-ai-recruiting-pipeline'),
        ],
        'discovery_h2': '🧭 Descubrimiento Gratuito — siempre en línea, siempre gratuito',
        'discovery_p': 'Obtenga su pipeline de contratación automatizado: sourcing, triaje, agendamiento y contratados, para FE/técnicos y puestos de servicio. Su pipeline se genera instantáneamente y se envía por correo a usted y nuestro equipo comercial (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Comenzar Descubrimiento Gratuito',
        'discovery_cta2': 'Explorar la Red de Aplicaciones',
    },
    'fr': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-recruiting-pipeline-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-recruiting-pipeline-2026-fr.html">Français</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-recruiting-pipeline-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-recruiting-pipeline-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-recruiting-pipeline-2026-de.html">Deutsch</a></nav>',
        'title': 'Agent Multi-Agents de Recrutement IA — automatisation intégrée de l\'embauche — Zion Tech Group',
        'description': 'Hub gratuit de Agent Multi-Agents de Recrutement IA : sourcing, tri conversationnel, planification d\'entretiens, engagement des candidats et écriture ATS/CRM — pour l\'embauche de FE/techniciens, dans votre langue.',
        'h1': '🤖 Agent Multi-Agents de Recrutement IA',
        'pitch': 'Chaque FE ou technicien dont nous avons besoin est à un cran de distance — sourcing, tri, planification et confirmés, sans un seul pas manuel. Orchestrateur multi-agents (sourcing → tri → planification → engagement → écriture ATS) avec validation du recruteur. 24/7, multilingue, conçu pour l\'équipe services Zion.',
        'cards': [
            ('🔍 Agent Sourcing', 'Recherche LinkedIn, offres d\'emploi et réseaux professionnels de FE/techniciens, classés par affinité.', 'https://ziontechgroup.com/ai-recruiting-pipeline/', 'https://github.com/Zion-support/zion-ai-recruiting-pipeline'),
            ('📝 Agent de Tri (conversationnel)', 'Tri IA conversationnel (chat/voix) qui évalue les candidats selon les critères du poste, avec confirmation de l\'entretien.', 'https://ziontechgroup.com/ai-recruiting-pipeline/', 'https://github.com/Zion-support/zion-ai-recruiting-pipeline'),
            ('📅 Agent de Planification d\'Entretiens', 'Résout le problème à trois côtés (candidat × responsable × interviewer) via l\'intégration calendrier.', 'https://ziontechgroup.com/ai-recruiting-pipeline/', 'https://github.com/Zion-support/zion-ai-recruiting-pipeline'),
            ('🗣️ Agent d\'Engagement des Candidats', 'Engagement conversationnel 24/7 : réponses instantanées, mises à jour de statut, rappels d\'entretien, diffusion de feedback.', 'https://ziontechgroup.com/ai-recruiting-pipeline/', 'https://github.com/Zion-support/zion-ai-recruiting-pipeline'),
            ('📋 Écriture ATS/CRM', 'Écrit les dossiers de candidats et résultats d\'entretiens dans l\'ATS/CRM (HubSpot), avec traçabilité.', 'https://ziontechgroup.com/ai-recruiting-pipeline/', 'https://github.com/Zion-support/zion-ai-recruiting-pipeline'),
            ('📊 Analyse de Pipeline et Délai de Plein', 'Tableaux de bord : sources de candidats, délai de remplissage, qualité de recrutement, état du pipeline.', 'https://ziontechgroup.com/ai-recruiting-pipeline/', 'https://github.com/Zion-support/zion-ai-recruiting-pipeline'),
        ],
        'discovery_h2': '🧭 Découverte Gratuite — toujours en ligne, toujours gratuite',
        'discovery_p': 'Obtenez votre pipeline de recrutement automatisé : sourcing, tri, planification et confirmés, pour les postes FE/techniciens et services. Votre pipeline est généré instantanément et envoyé par e-mail à vous et à notre équipe commerciale (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Commencer la Découverte Gratuite',
        'discovery_cta2': 'Parcourir le Réseau d\'Applications',
    },
    'de': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-recruiting-pipeline-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-recruiting-pipeline-2026-de.html">Deutsch</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-recruiting-pipeline-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-recruiting-pipeline-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-recruiting-pipeline-2026-fr.html">Français</a></nav>',
        'title': 'KI-Rekrutierung-Agent & Multi-Agenten-Lead-Agent — Hiring-Vollautomatisierung — Zion Tech Group',
        'description': 'Kostenloser KI-Rekrutierungs-Agent & Multi-Agenten-Lead-Agent-HuB: Sourcing, konversationelle Screening, Interview-Terminplanung, Kandidaten-Engagement und ATS/CRM-Schreibvorgänge — für FE/tchniker-Mietungen, auf deiner Sprache.',
        'h1': '🤖 KI-Rekrutierungs-Agent & Multi-Agenten-Lead-Agent',
        'pitch': 'Jeder FE oder Techniker, den wir benötigen, ist ein Bildschirm entfernt — Sourcing, Screening, Terminplanung und gebucht, ohne einen einzigen manuellen Schritt. Multi-Agenten-Orchestriert (Sourcing → Screening → Terminplanung → Engagement → ATS-Schreibvorgang) mit Freigabe durch den Recruiter. 24/7, mehrsprachig, auf Zion\'s Service-Team zugeschnitten.',
        'cards': [
            ('🔍 Sourcing-Agent', 'Durchsucht LinkedIn, Jobportale und professionelle Netzwerke nach FE/Technikern, sortiert nach Passgenauigkeit.', 'https://ziontechgroup.com/ai-recruiting-pipeline/', 'https://github.com/Zion-support/zion-ai-recruiting-pipeline'),
            ('📝 Screening-Agent (konversationell)', 'Chat/Voice-KI-Screening, das Kandidaten nach Rollenkriterien bewertet, inkl. Freigabe des Interviewers.', 'https://ziontechgroup.com/ai-recruiting-pipeline/', 'https://github.com/Zion-support/zion-ai-recruiting-pipeline'),
            ('📅 Interview-Terminplanungs-Agent', 'Löst das dreiseitige Terminierungsproblem (Kandidat × Anwerber × Interviewer) via Kalender-Integration.', 'https://ziontechgroup.com/ai-recruiting-pipeline/', 'https://github.com/Zion-support/zion-ai-recruiting-pipeline'),
            ('🗣️ Kandidaten-Engagement-Agent', '24/7 konversationelles Engagement: sofortige Antworten, Status-Updates, Interview-Erinnerungen, Feedback-Distribution.', 'https://ziontechgroup.com/ai-recruiting-pipeline/', 'https://github.com/Zion-support/zion-ai-recruiting-pipeline'),
            ('📋 ATS/CRM-Schreibvorgang', 'Schreibt Kandidaten-Einträge und Interview-Ergebnisse in das ATS/CRM (HubSpot) mit Audit-Trail.', 'https://ziontechgroup.com/ai-recruiting-pipeline/', 'https://github.com/Zion-support/zion-ai-recruiting-pipeline'),
            ('📊 Pipeline & Time-to-Hire-Analysen', 'Dashboards für Kandidatenquellen, Time-to-Fill, Hire-Qualität und Pipeline-Health.', 'https://ziontechgroup.com/ai-recruiting-pipeline/', 'https://github.com/Zion-support/zion-ai-recruiting-pipeline'),
        ],
        'discovery_h2': '🧭 Kostenloser Entdeckung — immer online, immer kostenlos',
        'discovery_p': '-Erfahren Sie Ihre Mietung automatisiert: Sourced, gescreened, termingebucht und gebucht, für FE/Techniker und Service-Rollen. Ihr Pipeline wird augenblicklich generiert und per E-Mail an Sie und unser Vertriebsteam (commercial@ziontechgroup.com) gesendet.',
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
    labels = ['🔍 Sourcing + Screening', '📅 Interview Scheduling', '🗣️ Candidate Engagement', '📋 ATS/CRM Write-Back', '📊 Pipeline Analytics']
    section_html = ''
    for grp, label in zip(cards_groups, labels):
        gh = ''.join(f'<div class="card"><h3>{h}</h3><p>{d}</p><a href="{live}">Live app →</a> · <a href="{repo}">Repo</a></div>' for h, d, live, repo in grp)
        section_html += f'<section><h2>{label}</h2><div class="cards">{gh}</div></section>'
    disc = f'<div class="disc"><h2>{body["discovery_h2"]}</h2><p>{body["discovery_p"]}</p><a class="cta green" href="https://ziontechgroup.com/discovery/">{body["discovery_cta1"]}</a><a class="cta alt" href="https://ziontechgroup.com/zion-app-network/">{body["discovery_cta2"]}</a></div>'
    closing = '<p style="margin-top:24px"><a href="https://ziontechgroup.com">← ziontechgroup.com</a> · <a href="https://github.com/Zion-support/zion-app-network/blob/main/SPOTLIGHT-ai-recruiting-pipeline-2026.md">Spotlight doc</a> · <a href="https://github.com/Zion-support/zion-app-network/blob/main/APPS_INDEX-BATCH127-RECRUIT.md">Batch rollup</a></p>'
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
    path = os.path.join(WORK, f'app-network-ai-recruiting-pipeline-2026{"-"+ext if ext else ""}.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("wrote", path, "len", len(content))
