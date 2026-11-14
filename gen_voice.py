import os

WORK = '/Users/miami2/.hermes/profiles/agent-finops-ops/cache/apphub'
os.makedirs(WORK, exist_ok=True)

BASE = 'https://ziontechgroup.com/zion-app-network/app'
CANON = f'{BASE}/app-network-voice-field-2026.html'
L = {
    'pt': f'{BASE}/app-network-voice-field-2026-pt.html',
    'es': f'{BASE}/app-network-voice-field-2026-es.html',
    'fr': f'{BASE}/app-network-voice-field-2026-fr.html',
    'de': f'{BASE}/app-network-voice-field-2026-de.html',
}
LANGS = [('en', CANON), ('pt-BR', L['pt']), ('es', L['es']), ('fr', L['fr']), ('de', L['de'])]

BODY = {
    'en': {
        'langbar': '<nav class="langbar">🌐 <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-voice-field-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-voice-field-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-voice-field-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-voice-field-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-voice-field-2026-de.html">Deutsch</a></nav>',
        'title': 'AI Voice & Missed-Call Automation — Field Services — Zion Tech Group',
        'description': 'Wake-on-call voice agent answers missed calls, books the job, and dispatches the technician — 24/7 in your language.',
        'h1': '📞 AI Voice & Missed-Call Automation for Field Services',
        'pitch': 'A single coordinated voice-automation module for local services: wake-on-call, job booking, site capture, and technician dispatch — online and free, with a 40%+ markup margin for Zion. Built for electricians, plumbers, HVAC, locksmiths, contractors and field teams.',
        'cards': [
            ('📞 Wake-on-Call Voice Agent', 'Answers the phone when your team is busy, captures the site address and job summary, books the job.', 'https://ziontechgroup.com/voice-field-automation/', 'https://github.com/Zion-support/zion-voice-field-automation'),
            ('📅 Job Booking & Dispatch', 'Converts a call into a dispatcher queue with postcode, site count and SLA — no more dropped quotes.', 'https://ziontechgroup.com/voice-field-automation/', 'https://github.com/Zion-support/zion-voice-field-automation'),
            ('🌐 5-Language Call Answering', 'Answers in the customer\'s language — EN / Português / Español / Français / Deutsch — matching the network standard.', 'https://ziontechgroup.com/voice-field-automation/', 'https://github.com/Zion-support/zion-voice-field-automation'),
            ('📊 Missed-Call → Booking Analytics', 'Missed-call rate, conversion per call, answer time and booked-vs-quoted by operator.', 'https://ziontechgroup.com/voice-field-automation/', 'https://github.com/Zion-support/zion-voice-field-automation'),
            ('🔔 Auto-Handoff to Technicians', 'Flags every call as unassigned after 60 seconds and pages the on-duty field tech.', 'https://ziontechgroup.com/voice-field-automation/', 'https://github.com/Zion-support/zion-voice-field-automation'),
            ('💬 SMS / WhatsApp Confirmation', 'Caller gets a one-touch confirmation so the job is never lost between the shop floor and the site.', 'https://ziontechgroup.com/voice-field-automation/', 'https://github.com/Zion-support/zion-voice-field-automation'),
        ],
        'discovery_h2': '🧭 Free AI Discovery — always online, always free',
        'discovery_p': 'Need a voice-automation rollout for your field team? Take our free Discovery questionnaire: your personalised AI discovery report is generated instantly and emailed to you and our commercial team (commercial@ziontechgroup.com) for fast, tailored follow-up.',
        'discovery_cta1': 'Start Free Discovery',
        'discovery_cta2': 'Browse the App Network',
    },
    'pt': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-voice-field-2026.html">English</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-voice-field-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-voice-field-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-voice-field-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-voice-field-2026-de.html">Deutsch</a></nav>',
        'title': 'Automação de Voz com IA e Chamadas Perdidas — Serviços de Campo — Zion Tech Group',
        'description': 'Agente de voz wake-on-call responde a chamadas perdidas, agenda o trabalho e despacha o técnico — 24/7, no seu idioma.',
        'h1': '📞 Automação de Voz com IA para Serviços de Campo',
        'pitch': 'Módulo único de automação por voz para serviços locais: wake-on-call, agendamento de trabalho, captura de sites e despacho de técnicos — online e gratuito, com margem de 40%+ para a Zion. Feito para eletricistas, encanadores, climatização, fechadores, contratistas e equipes de campo.',
        'cards': [
            ('📞 Agente de Voz Wake-on-Call', 'Responde o telefone quando a sua equipe está ocupada, capta o endereço do site e o resumo do trabalho e agenda o serviço.', 'https://ziontechgroup.com/voice-field-automation/', 'https://github.com/Zion-support/zion-voice-field-automation'),
            ('📅 Agendamento e Despacho de Trabalhos', 'Converte uma chamada em uma fila de despacho com número de postos, localização e SLA — sem perder propostas.', 'https://ziontechgroup.com/voice-field-automation/', 'https://github.com/Zion-support/zion-voice-field-automation'),
            ('🌐 Atendimento por telefone em 5 idiomas', 'Atende no idioma do cliente — EN / Português / Español / Français / Deutsch — em conformidade com o padrão da rede.', 'https://ziontechgroup.com/voice-field-automation/', 'https://github.com/Zion-support/zion-voice-field-automation'),
            ('📊 Analytics de Chamadas perdidas → Agendamento', 'Taxa de chamadas perdidas, conversão por chamada, tempo de resposta e agendados versus propostos por operador.', 'https://ziontechgroup.com/voice-field-automation/', 'https://github.com/Zion-support/zion-voice-field-automation'),
            ('🔔 Despacho automático para técnicos', 'Sinaliza cada chamada como não atribuída após 60 segundos e avisa o técnico de campo em serviço.', 'https://ziontechgroup.com/voice-field-automation/', 'https://github.com/Zion-support/zion-voice-field-automation'),
            ('💬 Confirmação por SMS / WhatsApp', 'O chamado recebe uma confirmação com um toque para que o trabalho nunca seja perdido entre o fundo da loja e o local.', 'https://ziontechgroup.com/voice-field-automation/', 'https://github.com/Zion-support/zion-voice-field-automation'),
        ],
        'discovery_h2': '🧭 Descoberta Gratuita de IA — sempre online, sempre gratuita',
        'discovery_p': 'Precisa de um desdobramento de automação por voz para a sua equipa de campo? Responda o nosso questionário de Descoberta: o seu relatório de IA personalizado é gerado instantaneamente e enviado por e-mail para si e para a nossa equipa comercial (commercial@ziontechgroup.com) para um seguimento rápido e personalizado.',
        'discovery_cta1': 'Iniciar Descoberta Gratuita',
        'discovery_cta2': 'Navegar pela Rede de Aplicativos',
    },
    'es': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-voice-field-2026.html">English</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-voice-field-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-voice-field-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-voice-field-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-voice-field-2026-de.html">Deutsch</a></nav>',
        'title': 'Automatización de Voz con IA y Llamadas Perdidas — Servicios de Campo — Zion Tech Group',
        'description': 'Agente de voz wake-on-call contesta las llamadas perdidas, agenda el trabajo y despacha al técnico — 24/7, en su idioma.',
        'h1': '📞 Automatización de Voz con IA para Servicios de Campo',
        'pitch': 'Módulo único de automatización por voz para servicios locales: wake-on-call, agendamiento de trabajo, captura de sitio y despacho de técnicos — online y gratuito, con margen de 40%+ para la Zion. Hecho para electricistas, plumbers, climatización, cerrajeros, contratistas y equipos de campo.',
        'cards': [
            ('📞 Agente de Voz Wake-on-Call', 'Contesta el teléfono cuando el equipo está ocupado, capta la dirección del sitio y el resumen del trabajo y agenda el servicio.', 'https://ziontechgroup.com/voice-field-automation/', 'https://github.com/Zion-support/zion-voice-field-automation'),
            ('📅 Agendamiento y Despacho de Trabajos', 'Convierte una llamada en una cola de despacho con número de postos, ubicación y SLA — sin perder propuestas.', 'https://ziontechgroup.com/voice-field-automation/', 'https://github.com/Zion-support/zion-voice-field-automation'),
            ('🌐 Contestación por teléfono en 5 idiomas', 'Contestando en el idioma del cliente — EN / Portugués / Español / Francés / Alemán — según el estándar de la red.', 'https://ziontechgroup.com/voice-field-automation/', 'https://github.com/Zion-support/zion-voice-field-automation'),
            ('📊 Analytics de llamadas perdidas → Agendamiento', 'Tasa de llamadas perdidas, conversión por llamada, tiempo de respuesta y agendaados versus ofertados por operador.', 'https://ziontechgroup.com/voice-field-automation/', 'https://github.com/Zion-support/zion-voice-field-automation'),
            ('🔔 Despacho automático a técnicos', 'Marca cada llamada como no asignada después de 60 segundos y avisa al técnico de campo en servicio.', 'https://ziontechgroup.com/voice-field-automation/', 'https://github.com/Zion-support/zion-voice-field-automation'),
            ('💬 Confirmación por SMS / WhatsApp', 'El llamado recibe una confirmación con un toque para que el trabajo nunca se pierda entre la planta y el sitio.', 'https://ziontechgroup.com/voice-field-automation/', 'https://github.com/Zion-support/zion-voice-field-automation'),
        ],
        'discovery_h2': '🧭 Descubrimiento Gratuito de IA — siempre en línea, siempre gratuito',
        'discovery_p': '¿Necesita un despliegue de automatización por voz para su equipo de campo? Respondan nuestro cuestionario de Descubrimiento: su informe personalizado de IA se genera instantáneamente y se envía por correo a usted y a nuestro equipo comercial (commercial@ziontechgroup.com) para un seguimiento rápido y personalizado.',
        'discovery_cta1': 'Comenzar Descubrimiento Gratuito',
        'discovery_cta2': 'Explorar la Red de Aplicaciones',
    },
    'fr': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-voice-field-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-voice-field-2026-fr.html">Français</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-voice-field-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-voice-field-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-voice-field-2026-de.html">Deutsch</a></nav>',
        'title': 'Automatisation vocale IA et appels manqués — Services de terrain — Zion Tech Group',
        'description': 'Agent vocal wake-on-call répond aux appels manqués, planifie la mission et envoie le technicien — 24h/24, dans votre langue.',
        'h1': '📞 Automatisation vocale IA pour services de terrain',
        'pitch': 'Module d\'automatisation vocale unique pour services locaux : wake-on-call, créez une mission, capturez le site et envoyez le technicien — en ligne et gratuit, avec une marge de 40%+ pour la Zion. Conçu pour les électriciens, plombiers, Climatisation, serruriers, entrepreneurs et équipes de terrain.',
        'cards': [
            ('📞 Agent vocal Wake-on-Call', 'Répond au téléphone quand l\'équipe est occupée, capture l\'adresse du site et le résumé de la mission, planifie le travail.', 'https://ziontechgroup.com/voice-field-automation/', 'https://github.com/Zion-support/zion-voice-field-automation'),
            ('📅 Planification et expédition de missions', 'Transforme un appel en une file d\'attente de dispatch avec le nombre de postes, la localisation et la SLA — sans perdre les propositions.', 'https://ziontechgroup.com/voice-field-automation/', 'https://github.com/Zion-support/zion-voice-field-automation'),
            ('🌐 Traduction vocale 5 langues', 'En répondant dans la langue du client — EN / Portugais / Espagnol / Français / Allemand — selon la norme du réseau.', 'https://ziontechgroup.com/voice-field-automation/', 'https://github.com/Zion-support/zion-voice-field-automation'),
            ('📊 Analytics des appels manqués → Planification', 'Taux d\'appels manqués, conversion par appel, temps de réponse et planifiés par rapport aux propositions par opérateur.', 'https://ziontechgroup.com/voice-field-automation/', 'https://github.com/Zion-support/zion-voice-field-automation'),
            ('🔔 Envoie automatique vers techniciens', 'Marque chaque appel comme non attribué après 60 secondes et prévient le technicien de terrain en service.', 'https://ziontechgroup.com/voice-field-automation/', 'https://github.com/Zion-support/zion-voice-field-automation'),
            ('💬 Confirmation SMS / WhatsApp', 'L\'appelant reçoit une confirmation avec un toucher pour que la mission ne soit jamais perdue entre l\'atelier et le site.', 'https://ziontechgroup.com/voice-field-automation/', 'https://github.com/Zion-support/zion-voice-field-automation'),
        ],
        'discovery_h2': '🧭 Découverte gratuite d\'IA — toujours en ligne, toujours gratuite',
        'discovery_p': 'Vous avez besoin d\'un déploiement d\'automatisation vocale pour votre équipe de terrain ? Répondez à notre questionnaire de Découverte : votre rapport personnalisé d\'IA est généré instantanément et envoyé par e-mail à vous et à notre équipe commerciale (commercial@ziontechgroup.com) pour un suivi rapide et personnalisé.',
        'discovery_cta1': 'Commencer la Découverte Gratuite',
        'discovery_cta2': 'Parcourir le Réseau d\'Applications',
    },
    'de': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-voice-field-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-voice-field-2026-de.html">Deutsch</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-voice-field-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-voice-field-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-voice-field-2026-fr.html">Français</a></nav>',
        'title': 'KI-Voice & Abgehen-Vermeidung Autoisierung für Feld-Services — Zion Tech Group',
        'description': 'Wake-on-Call Sprache-Agent beantwortet verpasste Anrufe, bucht die Aufgabe und schickt den Techniker — 24/7, in Ihrer Sprache.',
        'h1': '📞 KI-Voice & Abgehen-Vermeidung Autoisierung für Feld-Services',
        'pitch': 'Einheitliches Sprache-Auto-Modul für lokale Dienstleistungen: Wake-on-Call, Buchung, Sammeln der Site und Versand des Technikers — online und kostenlos, mit 40%+ Marge. Gemacht für Elektriker, Versorger, Kältetechnik, Schlosser, Auftragnehmer und Feld-Teams.',
        'cards': [
            ('📞 Wake-on-Call Sprache-Agent', 'Antwortet die Telefon, wenn das Team belegt ist, erfasst die Adresse der Site und das Zusammenfassung der Aufgabe und bucht den Dienst.', 'https://ziontechgroup.com/voice-field-automation/', 'https://github.com/Zion-support/zion-voice-field-automation'),
            ('📅 Buchung und Versand', 'Wandelt ein Anruf in eine Warteschlange von Dispatch mit Postleitzahl, Standort und SLA — ohne Vorhaben verlieren.', 'https://ziontechgroup.com/voice-field-automation/', 'https://github.com/Zion-support/zion-voice-field-automation'),
            ('🌐 5-Sprachen Anrufbeantwortung', 'Antwortet in der Sprache des Kunden — EN / Português / Español / Français / Deutsch — gemäß dem Netz-Standard.', 'https://ziontechgroup.com/voice-field-automation/', 'https://github.com/Zion-support/zion-voice-field-automation'),
            ('📊 Analytics von verpassten Anrufen → Buchung', 'Quote von verpassten Anrufen, Konversion pro Anruf, Antwortzeit und gebucht versus angeboten pro Operator.', 'https://ziontechgroup.com/voice-field-automation/', 'https://github.com/Zion-support/zion-voice-field-automation'),
            ('🔔 Auto-Send an Techniker', 'Markiert jeden Anruf als nicht zugewiesen nach 60 Sekunden und warnt den Feld-Techniker in Dienst.', 'https://ziontechgroup.com/voice-field-automation/', 'https://github.com/Zion-support/zion-voice-field-automation'),
            ('💬 SMS / WhatsApp Bestätigung', 'Den Anrufer erhält eine Bestätigung mit einem Tipp, damit die Aufgabe nie zwischen der Werkbühne und dem Standort verloren geht.', 'https://ziontechgroup.com/voice-field-automation/', 'https://github.com/Zion-support/zion-voice-field-automation'),
        ],
        'discovery_h2': '🧭 Kostenloser KI-Entdeckung — immer online, immer kostenlos',
        'discovery_p': 'Sie benötigen ein Sprache-Auto-Durchbruch für Ihr Feld-Team? Beantworten Sie unser Entdeckungsfragebogen: Ihr personalisierter KI-Bericht wird sofort generiert und per E-Mail an Sie und unser Vertriebsteam (commercial@ziontechgroup.com) gesendet für ein schnelles und personalisiertes Nachverfolgung.',
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
    cards_groups = [body['cards'][:3], body['cards'][3:6], body['cards'][6:9]]
    labels = ['🎯 Wake-on-Call & Booking', '📋 Field-Tech Dispatch', '🌎 5-Language Outbound', '🆕 Open-Source Voice Agent']
    section_html = ''
    for grp, label in zip(cards_groups, labels):
        gh = ''.join(f'<div class="card"><h3>{h}</h3><p>{d}</p><a href="{live}">Live app →</a> · <a href="{repo}">Repo</a></div>' for h, d, live, repo in grp)
        section_html += f'<section><h2>{label}</h2><div class="cards">{gh}</div></section>'
    disc = f'<div class="disc"><h2>{body["discovery_h2"]}</h2><p>{body["discovery_p"]}</p><a class="cta green" href="https://ziontechgroup.com/discovery/">{body["discovery_cta1"]}</a><a class="cta alt" href="https://ziontechgroup.com/zion-app-network/">{body["discovery_cta2"]}</a></div>'
    closing = '<p style="margin-top:24px"><a href="https://ziontechgroup.com">← ziontechgroup.com</a> · <a href="https://github.com/Zion-support/zion-app-network/blob/main/SPOTLIGHT-voice-field-2026.md">Spotlight doc</a> · <a href="https://github.com/Zion-support/zion-app-network/blob/main/APPS_INDEX-BATCH115-VOICE.md">Batch rollup</a></p>'
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
    path = os.path.join(WORK, f'app-network-voice-field-2026{"-"+ext if ext else ""}.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("wrote", path, "len", len(content))
