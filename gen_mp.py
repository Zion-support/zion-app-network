import os

WORK = '/Users/miami2/.hermes/profiles/agent-finops-ops/cache/apphub'
os.makedirs(WORK, exist_ok=True)

BASE = 'https://ziontechgroup.com/zion-app-network/app'
CANON = f'{BASE}/app-network-agent-marketplace-2026.html'
L = {
    'pt': f'{BASE}/app-network-agent-marketplace-2026-pt.html',
    'es': f'{BASE}/app-network-agent-marketplace-2026-es.html',
    'fr': f'{BASE}/app-network-agent-marketplace-2026-fr.html',
    'de': f'{BASE}/app-network-agent-marketplace-2026-de.html',
}
LANGS = [('en', CANON), ('pt-BR', L['pt']), ('es', L['es']), ('fr', L['fr']), ('de', L['de'])]

BODY = {
    'en': {
        'langbar': '<nav class="langbar">🌐 <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-agent-marketplace-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-agent-marketplace-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-agent-marketplace-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-agent-marketplace-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-agent-marketplace-2026-de.html">Deutsch</a></nav>',
        'title': 'Agent Marketplace for Local Services — Vetted AI Agents — Zion Tech Group',
        'description': 'A curated catalog of narrow, pre-configured AI agents for SMB workflows — triage, quote follow-up, review response — with human approval before anything ships.',
        'h1': '🤖 Agent Marketplace for Local Services',
        'pitch': 'A curated marketplace of narrow, pre-configured AI agents for SMB workflows: service triage, quote follow-up, review response, appointment reminders — all with human-in-the-loop approval. No AI-engineering team required. Built for the SEO/GEO growth team and local-services clients.',
        'cards': [
            ('🧭 Service Triage Agent', 'Answers the phone, logs the job type, routes to the right dispatcher — the same triage Zion manages for local services.', 'https://ziontechgroup.com/agent-marketplace/', 'https://github.com/Zion-support/zion-agent-marketplace'),
            ('📞 Quote Follow-Up Agent', 'Texts/app-SMS the 48-hour follow-up on every unquoted estimate — a $0-lead-recovery automation.', 'https://ziontechgroup.com/agent-marketplace/', 'https://github.com/Zion-support/zion-agent-marketplace'),
            ('⭐ Review Response Agent', 'Drafts SEO/GEO-optimized responses to every new review — one-click, always on-brand, always approved by a human first.', 'https://ziontechgroup.com/agent-marketplace/', 'https://github.com/Zion-support/zion-agent-marketplace'),
            ('📅 Appointment Reminder Agent', 'Texts + WhatsApp reminders 24h and 2h before, with auto-resend on no-show — cuts no-shows by 20-30%.', 'https://ziontechgroup.com/agent-marketplace/', 'https://github.com/Zion-support/zion-agent-marketplace'),
            ('🌐 5-Language Marketplace', 'Catalog + agents in EN / Português / Español / Français / Deutsch, matching the network standard.', 'https://ziontechgroup.com/agent-marketplace/', 'https://github.com/Zion-support/zion-agent-marketplace'),
            ('🔔 Human-in-the-Loop Approval', 'Every agent ships only after a human approves — audit logs, scoped permissions, no silent automation.', 'https://ziontechgroup.com/agent-marketplace/', 'https://github.com/Zion-support/zion-agent-marketplace'),
        ],
        'discovery_h2': '🧭 Free Discovery — always online, always free',
        'discovery_p': 'Stop losing leads to manual follow-up? Take our free Discovery questionnaire: we map your highest-cost workflow and show you a vetted agent for it — in minutes, not months.',
        'discovery_cta1': 'Start Free Discovery',
        'discovery_cta2': 'Browse the App Network',
    },
    'pt': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-agent-marketplace-2026.html">English</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-agent-marketplace-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-agent-marketplace-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-agent-marketplace-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-agent-marketplace-2026-de.html">Deutsch</a></nav>',
        'title': 'Marketplace de Agentes para Serviços Locais — Agentes IA Aprovados — Zion Tech Group',
        'description': 'Um catálogo curado de agentes IA restritos e pré-configurados para fluxos de trabalho de MEI — triagem, follow-up de orçamento, resposta de revisão — com aprovação humana antes de enviar nada.',
        'h1': '🤖 Marketplace de Agentes para Serviços Locais',
        'pitch': 'Um marketplace curado de agentes IA restritos e pré-configurados para fluxos de trabalho de MEI: triagem, follow-up de orçamento, resposta de revisão, lembretes de agendamento — todos com aprovação humana. Sem equipe de IA necessária. Feito para a equipe de crescimento SEO/GEO e clientes de serviços locais.',
        'cards': [
            ('🧭 Agente de Triagem de Serviço', 'Responde o telefone, loga o tipo de trabalho e encaminha para o despachador certo — a mesma triagem que a Zion gerencia para serviços locais.', 'https://ziontechgroup.com/agent-marketplace/', 'https://github.com/Zion-support/zion-agent-marketplace'),
            ('📞 Agente de Follow-Up de Orçamento', 'Envia SMS/app do follow-up das 48h de cada orçamento não respondido — uma automação de recuperação de leads de $0.', 'https://ziontechgroup.com/agent-marketplace/', 'https://github.com/Zion-support/zion-agent-marketplace'),
            ('⭐ Agente de Resposta de Revisão', 'Redige respostas otimizadas para SEO/GEO para cada nova revisão — um toque, sempre no estilo da marca, sempre aprovado por um humano.', 'https://ziontechgroup.com/agent-marketplace/', 'https://github.com/Zion-support/zion-agent-marketplace'),
            ('📅 Agente de Lembrete de Agendamento', 'Envia SMS + WhatsApp de lembretes 24h e 2h antes, com reenvio automático em caso de não comparecimento — reduzu não-show em 20-30%.', 'https://ziontechgroup.com/agent-marketplace/', 'https://github.com/Zion-support/zion-agent-marketplace'),
            ('🌐 Marketplace em 5 Idiomas', 'Catálogo + agentes em EN / Português / Español / Français / Deutsch, em conformidade com o padrão da rede.', 'https://ziontechgroup.com/agent-marketplace/', 'https://github.com/Zion-support/zion-agent-marketplace'),
            ('🔔 Aprovação Humana no Loop', 'Toda agente sai apenas após aprovação humana — auditoria de logs, permissões escopadas, sem automação silenciosa.', 'https://ziontechgroup.com/agent-marketplace/', 'https://github.com/Zion-support/zion-agent-marketplace'),
        ],
        'discovery_h2': '🧭 Descoberta Gratuita — sempre online, sempre gratuita',
        'discovery_p': 'Para parar de perder leads com follow-up manual? Responda o nosso questionário de Descoberta: mapeamos o seu fluxo de trabalho de maior custo e mostramos um agente aprovado para ele — em minutos, não em meses.',
        'discovery_cta1': 'Iniciar Descoberta Gratuita',
        'discovery_cta2': 'Navegar pela Rede de Aplicativos',
    },
    'es': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-agent-marketplace-2026.html">English</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-agent-marketplace-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-agent-marketplace-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-agent-marketplace-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-agent-marketplace-2026-de.html">Deutsch</a></nav>',
        'title': 'Marketplace de Agentes para Servicios Locales — Agentes IA Aprobados — Zion Tech Group',
        'description': 'Un catálogo curado de agentes IA restrictos y pre-configurados para flujos de trabajo de PYME — triaje, seguimiento de cotización, respuesta de revisión — con aprobación humana antes de enviar nada.',
        'h1': '🤖 Marketplace de Agentes para Servicios Locales',
        'pitch': 'Un marketplace curado de agentes IA restrictos y pre-configurados para flujos de trabajo de PYME: triaje, seguimiento de cotización, respuesta de revisión, recordatorios de citas — todos con aprobación humana. Sin equipo de IA necesario. Hecho para el equipo de crecimiento SEO/GEO y clientes de servicios locales.',
        'cards': [
            ('🧭 Agente de Triaje de Servicio', 'Contesta el teléfono, registra el tipo de trabajo y enruta al despachador correcto — el mismo triaje que la Zion gestiona para servicios locales.', 'https://ziontechgroup.com/agent-marketplace/', 'https://github.com/Zion-support/zion-agent-marketplace'),
            ('📞 Agente de Seguimiento de Cotización', 'Envía SMS/app del seguimiento de 48h a cada cotización sin responder — una automatización de recuperación de leads de $0.', 'https://ziontechgroup.com/agent-marketplace/', 'https://github.com/Zion-support/zion-agent-marketplace'),
            ('⭐ Agente de Respuesta de Revisión', 'Redacta respuestas optimizadas para SEO/GEO a cada nueva revisión — un toque, siempre en la marca, siempre aprobado por un humano.', 'https://ziontechgroup.com/agent-marketplace/', 'https://github.com/Zion-support/zion-agent-marketplace'),
            ('📅 Agente de Recordatorio de Cita', 'Envía SMS + WhatsApp de recordatorios 24h y 2h antes, con reenvío automático en no-show — reduce los no-show un 20-30%.', 'https://ziontechgroup.com/agent-marketplace/', 'https://github.com/Zion-support/zion-agent-marketplace'),
            ('🌐 Marketplace en 5 Idiomas', 'Catálogo + agentes en EN / Portugués / Español / Francés / Alemán, según el estándar de la red.', 'https://ziontechgroup.com/agent-marketplace/', 'https://github.com/Zion-support/zion-agent-marketplace'),
            ('🔔 Aprobación Humana en el Bucle', 'Todo agente sale solo tras aprobación humana — auditoría de logs, permisos escopados, sin automatización silenciosa.', 'https://ziontechgroup.com/agent-marketplace/', 'https://github.com/Zion-support/zion-agent-marketplace'),
        ],
        'discovery_h2': '🧭 Descubrimiento Gratuito — siempre en línea, siempre gratuito',
        'discovery_p': '¿Listo para dejar de perder leads con seguimiento manual? Respondan nuestro cuestionario de Descubrimiento: mapeamos su flujo de trabajo de mayor costo y muestran un agente aprobado para él — en minutos, no en meses.',
        'discovery_cta1': 'Comenzar Descubrimiento Gratuito',
        'discovery_cta2': 'Explorar la Red de Aplicaciones',
    },
    'fr': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-agent-marketplace-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-agent-marketplace-2026-fr.html">Français</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-agent-marketplace-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-agent-marketplace-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-agent-marketplace-2026-de.html">Deutsch</a></nav>',
        'title': 'Marché d\'Agents pour Services Locaux — Agents IA Validés — Zion Tech Group',
        'description': 'Un catalogue curaté d\'agents IA restrictés et pré-configurés pour flux de travail de PMI — triage, suivi de devis, réponse de revision — avec validation humaine avant envoi.',
        'h1': '🤖 Marché d\'Agents pour Services Locaux',
        'pitch': 'Un marché curaté d\'agents IA restrictés et pré-configurés pour flux de travail de PMI : triage, suivi de devis, réponse de révision, rappels de rendez-vous — tous avec validation humaine. Sans équipe d\'IA. Conçu pour l\'équipe de croissance SEO/GEO et clients de services locaux.',
        'cards': [
            ('🧭 Agent de Triage de Service', 'Répond au téléphone, logge le type de mission, oriente vers le bon dispatcher — le même triage que la Zion gère pour services locaux.', 'https://ziontechgroup.com/agent-marketplace/', 'https://github.com/Zion-support/zion-agent-marketplace'),
            ('📞 Agent de Suivi de Devis', 'Envoie SMS/app du suivi 48h sur chaque devis non répondu — une automatisation de récupération de leads à 0 €.', 'https://ziontechgroup.com/agent-marketplace/', 'https://github.com/Zion-support/zion-agent-marketplace'),
            ('⭐ Agent de Réponse de Revision', 'Rédige des réponses optimisées SEO/GEO pour chaque nouvelle révision — un clic, toujours sur marque, toujours validé par un humain.', 'https://ziontechgroup.com/agent-marketplace/', 'https://github.com/Zion-support/zion-agent-marketplace'),
            ('📅 Agent de Rappel de Rendez-vous', 'Envoie SMS + WhatsApp de rappels 24h et 2h avant, avec renvoi automatique en cas de non-présentation — réduit les non-déplacements de 20-30%.', 'https://ziontechgroup.com/agent-marketplace/', 'https://github.com/Zion-support/zion-agent-marketplace'),
            ('🌐 Marché en 5 Langues', 'Catalogue + agents en EN / Portugais / Español / Français / Deutsch, selon le standard du réseau.', 'https://ziontechgroup.com/agent-marketplace/', 'https://github.com/Zion-support/zion-agent-marketplace'),
            ('🔔 Validation Humaine dans la Boucle', 'Tout agent part qu\'après validation humaine — audit de logs, permissions escopées, sans automatisation silencieuse.', 'https://ziontechgroup.com/agent-marketplace/', 'https://github.com/Zion-support/zion-agent-marketplace'),
        ],
        'discovery_h2': '🧭 Découverte Gratuite — toujours en ligne, toujours gratuite',
        'discovery_p': 'Prêt à arreter de perdre des leads avec suivi manuel ? Répondez à notre questionnaire de Découverte : nous cartonnons votre flux de travail de plus grand coût et montrons un agent validé pour ça — en minutes, pas en mois.',
        'discovery_cta1': 'Commencer la Découverte Gratuite',
        'discovery_cta2': 'Parcourir le Réseau d\'Applications',
    },
    'de': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-agent-marketplace-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-agent-marketplace-2026-de.html">Deutsch</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-agent-marketplace-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-agent-marketplace-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-agent-marketplace-2026-fr.html">Français</a></nav>',
        'title': 'Agenten-Marktplatz für Lokale Dienstleistungen — Genehmigte KI-Agenten — Zion Tech Group',
        'description': 'Ein kuratiertes Katalog von enge, vor-konfigurierten KI-Agenten für SMB-Workflows — Triage, Antennen-Follow-up, Rezension-Reaktion — mit menschlicher Genehmigung, bevor etwas verschickt wird.',
        'h1': '🤖 Agenten-Marktplatz für Lokale Dienstleistungen',
        'pitch': 'Ein kuratiertes Marktplatz von enge, vor-konfigurierten KI-Agenten für SMB-Workflows: Dienstleistung-Triage, Antennen-Follow-up, Rezension-Reaktion, Termin-Erinnerung — alle mit menschlicher Freigabe. Kein KI-Team erforderlich. Gemacht für das SEO/GEO-Wachstums-Team und lokale Kunden.',
        'cards': [
            ('🧭 Dienstleistung-Triage-Agent', 'Antwortet das Telefon, loggt den Job-Typ und leitet zum richtigen Dispatch — die selbe Triage, die Zion für lokale Dienstleistungen managt.', 'https://ziontechgroup.com/agent-marketplace/', 'https://github.com/Zion-support/zion-agent-marketplace'),
            ('📞 Anschluss-Follow-up Agent', 'Sendet SMS/app das 48h Follow-up auf jede ungeantwortete Kostenersäumnis — eine $0-Führungs-Triangle-Automatisierung.', 'https://ziontechgroup.com/agent-marketplace/', 'https://github.com/Zion-support/zion-agent-marketplace'),
            ('⭐ Rezension-Reaktion Agent', 'Entwirft SEO/GEO optimierte Antworten auf jede neue Rezension — ein Tipp, immer auf Marke, immer von einem Mensch erster genehmigt.', 'https://ziontechgroup.com/agent-marketplace/', 'https://github.com/Zion-support/zion-agent-marketplace'),
            ('📅 Termin-Erinnerung Agent', 'Sendet SMS + WhatsApp Erinnerungen 24h und 2h vor, mit automatischem Senden bei Abbruch — reduzierte Abbrüche um 20-30%.', 'https://ziontechgroup.com/agent-marketplace/', 'https://github.com/Zion-support/zion-agent-marketplace'),
            ('🌐 5-Sprachen Marktplatz', 'Katalog + Agenten in EN / Português / Español / Français / Deutsch, gemäß dem Netz-Standard.', 'https://ziontechgroup.com/agent-marketplace/', 'https://github.com/Zion-support/zion-agent-marketplace'),
            ('🔔 Menschliche Freigabe im Loop', 'Jeder Agent geht nur nach menschlicher Freigabe — Audit der Logs, permissions escopades, ohne stille Automatisierung.', 'https://ziontechgroup.com/agent-marketplace/', 'https://github.com/Zion-support/zion-agent-marketplace'),
        ],
        'discovery_h2': '🧭 Kostenloser Entdeckung — immer online, immer kostenlos',
        'discovery_p': 'Bereit, lose führende durch manuelles Follow-up zu verlieren? Beantworten Sie unser Entdeckungsfragebogen: wir kartografieren Ihren teuersten Workflow und zeigen Ihnen einen validierten Agenten dafür — in Minuten, nicht in Monaten.',
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
    labels = ['🧭 Triage + Quote-Follow-Up', '📞 Review-Response + Reminders', '🌎 5-Language Marketplace', '🆕 Open-Source Agent Stack']
    section_html = ''
    for grp, label in zip(cards_groups, labels):
        gh = ''.join(f'<div class="card"><h3>{h}</h3><p>{d}</p><a href="{live}">Live app →</a> · <a href="{repo}">Repo</a></div>' for h, d, live, repo in grp)
        section_html += f'<section><h2>{label}</h2><div class="cards">{gh}</div></section>'
    disc = f'<div class="disc"><h2>{body["discovery_h2"]}</h2><p>{body["discovery_p"]}</p><a class="cta green" href="https://ziontechgroup.com/discovery/">{body["discovery_cta1"]}</a><a class="cta alt" href="https://ziontechgroup.com/zion-app-network/">{body["discovery_cta2"]}</a></div>'
    closing = '<p style="margin-top:24px"><a href="https://ziontechgroup.com">← ziontechgroup.com</a> · <a href="https://github.com/Zion-support/zion-app-network/blob/main/SPOTLIGHT-agent-marketplace-2026.md">Spotlight doc</a> · <a href="https://github.com/Zion-support/zion-app-network/blob/main/APPS_INDEX-BATCH117-MP.md">Batch rollup</a></p>'
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
    path = os.path.join(WORK, f'app-network-agent-marketplace-2026{"-"+ext if ext else ""}.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("wrote", path, "len", len(content))
