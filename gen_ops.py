import os

WORK = '/Users/miami2/.hermes/profiles/agent-finops-ops/cache/apphub'
os.makedirs(WORK, exist_ok=True)

BASE = 'https://ziontechgroup.com/zion-app-network/app'
CANON = f'{BASE}/app-network-operations-diagnostic-2026.html'
L = {
    'pt': f'{BASE}/app-network-operations-diagnostic-2026-pt.html',
    'es': f'{BASE}/app-network-operations-diagnostic-2026-es.html',
    'fr': f'{BASE}/app-network-operations-diagnostic-2026-fr.html',
    'de': f'{BASE}/app-network-operations-diagnostic-2026-de.html',
}
LANGS = [('en', CANON), ('pt-BR', L['pt']), ('es', L['es']), ('fr', L['fr']), ('de', L['de'])]

BODY = {
    'en': {
        'langbar': '<nav class="langbar">🌐 <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-operations-diagnostic-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-operations-diagnostic-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-operations-diagnostic-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-operations-diagnostic-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-operations-diagnostic-2026-de.html">Deutsch</a></nav>',
        'title': 'AI Operations Diagnostic Sprint — Find Your Bottleneck — Zion Tech Group',
        'description': 'Free 48-hour diagnostic sprint that finds your single highest-value workflow bottleneck and proves the payback — before any build.',
        'h1': '🔍 AI Operations Diagnostic Sprint — Find Your Bottleneck',
        'pitch': 'A free, always-online 48-hour diagnostic sprint: we map your top manual workflows, find the one bottleneck worth automating, and prove the payback before any build. Built for trades, contractors, and local services. Entry into the full apps network (free voice automation, 40%+ markup builds).',
        'cards': [
            ('🔍 Free 48-Hour Diagnostic Sprint', 'We map your top 3 manual workflows and find the single bottleneck worth automating first — no cost, no obligation.', 'https://ziontechgroup.com/ops-diagnostic-sprint/', 'https://github.com/Zion-support/zion-ops-diagnostic-sprint'),
            ('📊 Pain-to-Payback Calculator', 'Hour-by-hour: hours/week saved × fully-loaded hourly cost = annual payback, in plain numbers.', 'https://ziontechgroup.com/ops-diagnostic-sprint/', 'https://github.com/Zion-support/zion-ops-diagnostic-sprint'),
            ('📋 2-Week Scoped Build', 'One workflow, one owner, a costed plan with payback, and a working version in 2 weeks.', 'https://ziontechgroup.com/ops-diagnostic-sprint/', 'https://github.com/Zion-support/zion-ops-diagnostic-sprint'),
            ('🌐 5-Language Intake & Report', 'Intake and diagnostic report in EN / Português / Español / Français / Deutsch.', 'https://ziontechgroup.com/ops-diagnostic-sprint/', 'https://github.com/Zion-support/zion-ops-diagnostic-sprint'),
            ('🔔 Auto-Handoff to Technicians', 'Every flagged bottleneck pages the on-duty operator and closes the loop in the CRM.', 'https://ziontechgroup.com/ops-diagnostic-sprint/', 'https://github.com/Zion-support/zion-ops-diagnostic-sprint'),
            ('💬 SMS / WhatsApp Confirmation', 'Caller gets a one-touch confirmation so nothing is lost between the diagnostic and the build.', 'https://ziontechgroup.com/ops-diagnostic-sprint/', 'https://github.com/Zion-support/zion-ops-diagnostic-sprint'),
        ],
        'discovery_h2': '🧭 Free Discovery — always online, always free',
        'discovery_p': 'Ready to stop working in the weeds? Take our free Discovery questionnaire: your pain-to-payback report is generated instantly and emailed to you and our commercial team (commercial@ziontechgroup.com) for fast, tailored follow-up.',
        'discovery_cta1': 'Start Free Discovery',
        'discovery_cta2': 'Browse the App Network',
    },
    'pt': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-operations-diagnostic-2026.html">English</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-operations-diagnostic-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-operations-diagnostic-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-operations-diagnostic-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-operations-diagnostic-2026-de.html">Deutsch</a></nav>',
        'title': 'Sprint de Diagnóstico de Operações com IA — Encontre o Seu gargalo — Zion Tech Group',
        'description': 'Sprint de diagnóstico gratuito de 48 horas que encontra o seu único gargalo de fluxo de trabalho de alto valor e mostra o retorno — antes de qualquer build.',
        'h1': '🔍 Sprint de Diagnóstico de Operações com IA — Encontre o Seu gargalo',
        'pitch': 'Um sprint de diagnóstico gratuito e sempre online de 48 horas: mapeamos seus principais fluxos de trabalho manuais, encontramos o único gargalo que vale a pena automatizar e comprovamos o retorno antes de qualquer build. Feito para trabalhadores, contratistas e serviços locais. Entrada na rede completa de aplicativos (automação de voz gratuita, builds com 40%+ de margem).',
        'cards': [
            ('🔍 Sprint de Diagnóstico Gratuito de 48 Horas', 'Mapeamos seus 3 principais fluxos de trabalho manuais e encontramos o único gargalo que vale a pena automatizar primeiro — sem custo, sem compromisso.', 'https://ziontechgroup.com/ops-diagnostic-sprint/', 'https://github.com/Zion-support/zion-ops-diagnostic-sprint'),
            ('📊 Calculadora de Retorno no Trabalho', 'Horas/semana economizadas × custo horário total = retorno anual, em números claros.', 'https://ziontechgroup.com/ops-diagnostic-sprint/', 'https://github.com/Zion-support/zion-ops-diagnostic-sprint'),
            ('📋 Build Estruturado de 2 Semanas', 'Um fluxo de trabalho, um responsável, um plano com retorno e uma versão funcional em 2 semanas.', 'https://ziontechgroup.com/ops-diagnostic-sprint/', 'https://github.com/Zion-support/zion-ops-diagnostic-sprint'),
            ('🌐 Ingresso e Relatório em 5 Idiomas', 'Ingresso e relatório de diagnóstico em EN / Português / Español / Français / Deutsch.', 'https://ziontechgroup.com/ops-diagnostic-sprint/', 'https://github.com/Zion-support/zion-ops-diagnostic-sprint'),
            ('🔔 Despacho Automático para Técnicos', 'Todo gargalo sinalizado envia uma mensagem ao operador em serviço e fecha o ciclo no CRM.', 'https://ziontechgroup.com/ops-diagnostic-sprint/', 'https://github.com/Zion-support/zion-ops-diagnostic-sprint'),
            ('💬 Confirmação por SMS / WhatsApp', 'O chamado recebe uma confirmação com um toque para que nada seja perdido entre o diagnóstico e o build.', 'https://ziontechgroup.com/ops-diagnostic-sprint/', 'https://github.com/Zion-support/zion-ops-diagnostic-sprint'),
        ],
        'discovery_h2': '🧭 Descoberta Gratuita — sempre online, sempre gratuita',
        'discovery_p': 'Pronto para parar de trabalhar nos detalhes? Responda o nosso questionário de Descoberta: o seu relatório de retorno no trabalho é gerado instantaneamente e enviado por e-mail para si e para a nossa equipa comercial (commercial@ziontechgroup.com) para um seguimento rápido e personalizado.',
        'discovery_cta1': 'Iniciar Descoberta Gratuita',
        'discovery_cta2': 'Navegar pela Rede de Aplicativos',
    },
    'es': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-operations-diagnostic-2026.html">English</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-operations-diagnostic-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-operations-diagnostic-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-operations-diagnostic-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-operations-diagnostic-2026-de.html">Deutsch</a></nav>',
        'title': 'Sprint de Diagnóstico de Operaciones con IA — Encuentre su Punto de Obstrucción — Zion Tech Group',
        'description': 'Sprint de diagnóstico gratuito de 48 horas que encuentra el único cuello de botella de su flujo de trabajo de alto valor y demuestra el retorno — antes de cualquier build.',
        'h1': '🔍 Sprint de Diagnóstico de Operaciones con IA — Encuentre su Punto de Obstrucción',
        'pitch': 'Un sprint de diagnóstico gratuito y siempre online de 48 horas: mapeamos sus principales flujos de trabajo manuales, encontramos el único cuello de botella que vale la pena automatizar y demostramos el retorno antes de cualquier build. Hecho para trabajadores, contratistas y servicios locales. Entrada en la red completa de aplicaciones (automatización de voz gratuita, builds con 40%+ de margen).',
        'cards': [
            ('🔍 Sprint de Diagnóstico Gratuito de 48 Horas', 'Mapeamos sus 3 principales flujos de trabajo manuales y encontramos el único cuello de botella que vale la pena automatizar primero — sin costo, sin compromiso.', 'https://ziontechgroup.com/ops-diagnostic-sprint/', 'https://github.com/Zion-support/zion-ops-diagnostic-sprint'),
            ('📊 Calculadora de Retorno en el Trabajo', 'Horas/semana ahorradas × costo horario total = retorno anual, en números claros.', 'https://ziontechgroup.com/ops-diagnostic-sprint/', 'https://github.com/Zion-support/zion-ops-diagnostic-sprint'),
            ('📋 Build Estructurado de 2 Semanas', 'Un flujo de trabajo, un responsable, un plan con retorno y una versión funcional en 2 semanas.', 'https://ziontechgroup.com/ops-diagnostic-sprint/', 'https://github.com/Zion-support/zion-ops-diagnostic-sprint'),
            ('🌐 Ingreso y Reporte en 5 Idiomas', 'Ingreso y reporte de diagnóstico en EN / Portugués / Español / Francés / Alemán.', 'https://ziontechgroup.com/ops-diagnostic-sprint/', 'https://github.com/Zion-support/zion-ops-diagnostic-sprint'),
            ('🔔 Despacho Automático a Técnicos', 'Cada cuello de botella señalado envía un mensaje al operador en servicio y cierra el ciclo en el CRM.', 'https://ziontechgroup.com/ops-diagnostic-sprint/', 'https://github.com/Zion-support/zion-ops-diagnostic-sprint'),
            ('💬 Confirmación por SMS / WhatsApp', 'El llamado recibe una confirmación con un toque para que nada se pierda entre el diagnóstico y el build.', 'https://ziontechgroup.com/ops-diagnostic-sprint/', 'https://github.com/Zion-support/zion-ops-diagnostic-sprint'),
        ],
        'discovery_h2': '🧭 Descubrimiento Gratuito — siempre en línea, siempre gratuito',
        'discovery_p': '¿Listo para dejar de trabajar en los detalles? Respondan nuestro cuestionario de Descubrimiento: su informe de retorno en el trabajo se genera instantáneamente y se envía por correo a usted y a nuestro equipo comercial (commercial@ziontechgroup.com) para un seguimiento rápido y personalizado.',
        'discovery_cta1': 'Comenzar Descubrimiento Gratuito',
        'discovery_cta2': 'Explorar la Red de Aplicaciones',
    },
    'fr': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-operations-diagnostic-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-operations-diagnostic-2026-fr.html">Français</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-operations-diagnostic-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-operations-diagnostic-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-operations-diagnostic-2026-de.html">Deutsch</a></nav>',
        'title': 'Sprint de Diagnostic des Opérations IA — Trouvez votre Goulot — Zion Tech Group',
        'description': 'Sprint de diagnostic gratuit de 48 heures qui trouve votre goulot d\'étranglement unique et prouve le rendement — avant toute intégration.',
        'h1': '🔍 Sprint de Diagnostic des Opérations IA — Trouvez votre Goulot',
        'pitch': 'Un sprint de diagnostic gratuit, toujours en ligne, de 48 heures : nous cartonnons vos 3 flux de travail manuels, trouvons le goulot unique à automatiser, et prouvons le rendement avant toute intégration. Conçu pour les artisans, contractors et services locaux. Entrée dans le réseau complet d\'applications (automatisation vocale gratuite, intégrations 40%+ de marge).',
        'cards': [
            ('🔍 Sprint de Diagnostic Gratuit de 48 Heures', 'Nous cartonnons vos 3 flux de travail manuels et trouvons le goulot unique à automatiser en priorité — sans coût, sans engagement.', 'https://ziontechgroup.com/ops-diagnostic-sprint/', 'https://github.com/Zion-support/zion-ops-diagnostic-sprint'),
            ('📊 Calculatrice de Retour sur Investissement', 'Heures/semaine économisées × coût horaire total = rendement annuel, en nombres clairs.', 'https://ziontechgroup.com/ops-diagnostic-sprint/', 'https://github.com/Zion-support/zion-ops-diagnostic-sprint'),
            ('📋 Intégration Élaborée de 2 Semaines', 'Un flux de travail, un responsable, un plan avec rendement et une version fonctionnelle en 2 semaines.', 'https://ziontechgroup.com/ops-diagnostic-sprint/', 'https://github.com/Zion-support/zion-ops-diagnostic-sprint'),
            ('🌐 Moyen de Communication et Rapport en 5 Langues', 'Moyen de communication et rapport de diagnostic en EN / Portugais / Espagnol / Français / Allemand.', 'https://ziontechgroup.com/ops-diagnostic-sprint/', 'https://github.com/Zion-support/zion-ops-diagnostic-sprint'),
            ('🔔 Envoi Automatique aux Techniciens', 'Chaque goulot signalé envoie un message au technicien en service et ferme la boucle dans le CRM.', 'https://ziontechgroup.com/ops-diagnostic-sprint/', 'https://github.com/Zion-support/zion-ops-diagnostic-sprint'),
            ('💬 Confirmation SMS / WhatsApp', 'L\'appelant reçoit une confirmation avec un toucher pour que rien ne soit perdu entre le diagnostic et l\'intégration.', 'https://ziontechgroup.com/ops-diagnostic-sprint/', 'https://github.com/Zion-support/zion-ops-diagnostic-sprint'),
        ],
        'discovery_h2': '🧭 Découverte Gratuite — toujours en ligne, toujours gratuite',
        'discovery_p': 'Prêt à arrêter de travailler dans les détails ? Répondez à notre questionnaire de Découverte : votre rapport de retour sur investissement est généré instantanément et envoyé par e-mail à vous et à notre équipe commerciale (commercial@ziontechgroup.com) pour un suivi rapide et personnalisé.',
        'discovery_cta1': 'Commencer la Découverte Gratuite',
        'discovery_cta2': 'Parcourir le Réseau d\'Applications',
    },
    'de': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-operations-diagnostic-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-operations-diagnostic-2026-de.html">Deutsch</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-operations-diagnostic-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-operations-diagnostic-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-operations-diagnostic-2026-fr.html">Français</a></nav>',
        'title': 'KI-Operations Diagnose-Sprint — Finden Sie Ihren Flaschenhals — Zion Tech Group',
        'description': 'Kostenloser 48-Stunden Diagnose-Sprint, der Ihren einzigen Flaschenhals im Hochwert-Fluss findet und den Return beweist — bevor jede Build.',
        'h1': '🔍 KI-Operations Diagnose-Sprint — Finden Sie Ihren Flaschenhals',
        'pitch': 'Ein kostenloser, immer online verfügbarer 48-Stunden Diagnose-Sprint: Wir kartografieren Ihre top 3 manuellen Workflows, finden den einzigen Flaschenhals, der automatisiert werden soll, und beweisen den Return, bevor jede Build. Gemacht für Handwerker, Contractors und lokale Dienstleistungen. Eintrittskarte ins vollständige App-Netzwerk (kostenlose Sprache-Automatisierung, Builds mit 40%+ Marge).',
        'cards': [
            ('🔍 Kostenloser 48-Stunden Diagnose-Sprint', 'Wir kartografieren Ihre top 3 manuellen Workflows und finden den einzigen Flaschenhals, der automatisiert werden soll — ohne Kosten, ohne Engagement.', 'https://ziontechgroup.com/ops-diagnostic-sprint/', 'https://github.com/Zion-support/zion-ops-diagnostic-sprint'),
            ('📊 Kalkulator des Return auf dem Arbeitsweg', 'Stunden/Woche eingespart × volle Last-Kosten = jährlicher Return, in klaren Zahlen.', 'https://ziontechgroup.com/ops-diagnostic-sprint/', 'https://github.com/Zion-support/zion-ops-diagnostic-sprint'),
            ('📋 2-Wochen Gitäuschte Build', 'Ein Workflow, ein Verantwortlicher, ein plan mit Return und eine funktionierende Version in 2 Wochen.', 'https://ziontechgroup.com/ops-diagnostic-sprint/', 'https://github.com/Zion-support/zion-ops-diagnostic-sprint'),
            ('🌐 5-Sprachen Eingang und Bericht', 'Eingang und Bericht des Diagnose in EN / Português / Español / Français / Deutsch.', 'https://ziontechgroup.com/ops-diagnostic-sprint/', 'https://github.com/Zion-support/zion-ops-diagnostic-sprint'),
            ('🔔 Auto-Send an Techniker', 'Jeder Flaschenhals signalisiert einen Nachrichten an den Dienst-Operator und schließt den Kreis im CRM.', 'https://ziontechgroup.com/ops-diagnostic-sprint/', 'https://github.com/Zion-support/zion-ops-diagnostic-sprint'),
            ('💬 SMS / WhatsApp Bestätigung', 'Der Anrufer erhält eine Bestätigung mit einem Tipp, damit nichts zwischen dem Diagnose und dem Build verloren geht.', 'https://ziontechgroup.com/ops-diagnostic-sprint/', 'https://github.com/Zion-support/zion-ops-diagnostic-sprint'),
        ],
        'discovery_h2': '🧭 Kostenloser Entdeckung — immer online, immer kostenlos',
        'discovery_p': 'Bereit, aufzuhören, in den Details zu arbeiten? Beantworten Sie unser Entdeckungsfragebogen: Ihr Return auf dem Arbeitsweg wird sofort generiert und per E-Mail an Sie und unser Vertriebsteam (commercial@ziontechgroup.com) gesendet für ein schnelles und personalisiertes Nachverfolgung.',
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
    labels = ['🔍 Diagnostic Sprint + Pain-to-Payback', '📋 2-Week Scoped Build', '🌎 5-Language Intake', '🆕 Open-Source Diagnostic Engine']
    section_html = ''
    for grp, label in zip(cards_groups, labels):
        gh = ''.join(f'<div class="card"><h3>{h}</h3><p>{d}</p><a href="{live}">Live app →</a> · <a href="{repo}">Repo</a></div>' for h, d, live, repo in grp)
        section_html += f'<section><h2>{label}</h2><div class="cards">{gh}</div></section>'
    disc = f'<div class="disc"><h2>{body["discovery_h2"]}</h2><p>{body["discovery_p"]}</p><a class="cta green" href="https://ziontechgroup.com/discovery/">{body["discovery_cta1"]}</a><a class="cta alt" href="https://ziontechgroup.com/zion-app-network/">{body["discovery_cta2"]}</a></div>'
    closing = '<p style="margin-top:24px"><a href="https://ziontechgroup.com">← ziontechgroup.com</a> · <a href="https://github.com/Zion-support/zion-app-network/blob/main/SPOTLIGHT-operations-diagnostic-2026.md">Spotlight doc</a> · <a href="https://github.com/Zion-support/zion-app-network/blob/main/APPS_INDEX-BATCH116-OPS.md">Batch rollup</a></p>'
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
    path = os.path.join(WORK, f'app-network-operations-diagnostic-2026{"-"+ext if ext else ""}.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("wrote", path, "len", len(content))
