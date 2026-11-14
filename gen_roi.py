import os

WORK = '/Users/miami2/.hermes/profiles/agent-finops-ops/cache/apphub'
os.makedirs(WORK, exist_ok=True)

BASE = 'https://ziontechgroup.com/zion-app-network/app'
CANON = f'{BASE}/app-network-saas-optimization-2026.html'
L = {
    'pt': f'{BASE}/app-network-saas-optimization-2026-pt.html',
    'es': f'{BASE}/app-network-saas-optimization-2026-es.html',
    'fr': f'{BASE}/app-network-saas-optimization-2026-fr.html',
    'de': f'{BASE}/app-network-saas-optimization-2026-de.html',
}
LANGS = [('en', CANON), ('pt-BR', L['pt']), ('es', L['es']), ('fr', L['fr']), ('de', L['de'])]

BODY = {
    'en': {
        'langbar': '<nav class="langbar">🌐 <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-saas-optimization-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-saas-optimization-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-saas-optimization-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-saas-optimization-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-saas-optimization-2026-de.html">Deutsch</a></nav>',
        'title': 'SaaS Optimization & ROI Calculator — Save Your Cloud & SaaS Spend — Zion Tech Group',
        'description': 'Free SaaS Optimization & ROI Calculator: find unutilized seats, idle cloud spend and redundant subscriptions — model the payback of right-sizing in minutes.',
        'h1': '💰 SaaS Optimization & ROI Calculator',
        'pitch': 'Free, always-online FinOps calculator: find the cost waste in your software and AI stack — unutilized seats, idle cloud spend, redundant subscriptions — and model the payback of right-sizing. Export a ROI PDF (Zion logo) to share with your CFO.',
        'cards': [
            ('🔍 License Waster Audit', 'Unutilized seats, SSO inactivity, redundant subscriptions — quantified in one click.', 'https://ziontechgroup.com/saas-optimization/', 'https://github.com/Zion-support/zion-saas-optimization'),
            ('☁️ Cloud Spend Modeler', 'Idle instances, over-provisioned agents, commitment gaps — modeled per workload.', 'https://ziontechgroup.com/saas-optimization/', 'https://github.com/Zion-support/zion-saas-optimization'),
            ('📉 Payback Estimator', 'Right-sizing + deprovisioning ROI with 90-day quick-win targets.', 'https://ziontechgroup.com/saas-optimization/', 'https://github.com/Zion-support/zion-saas-optimization'),
            ('🤖 LLM Cost Optimizer', 'Prompt caching, token efficiency, run cost per 1,000 calls.', 'https://ziontechgroup.com/saas-optimization/', 'https://github.com/Zion-support/zion-saas-optimization'),
            ('📄 ROI Export (Zion logo)', 'Export your waste report as a cleaned ROI PDF to share with CFOs/ops leads.', 'https://ziontechgroup.com/saas-optimization/', 'https://github.com/Zion-support/zion-saas-optimization'),
            ('🧭 Discovery Handoff', 'Waste report → free diagnostic sprint (Batch 116) → agent marketplace (Batch 117) → optimization.', 'https://ziontechgroup.com/saas-optimization/', 'https://github.com/Zion-support/zion-saas-optimization'),
        ],
        'discovery_h2': '🧭 Free Discovery — always online, always free',
        'discovery_p': 'Find the $ you\'re leaking in subscriptions and cloud — before we fix it. Your waste report is generated instantly and emailed to you and our commercial team (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Start Free Discovery',
        'discovery_cta2': 'Browse the App Network',
    },
    'pt': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-saas-optimization-2026.html">English</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-saas-optimization-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-saas-optimization-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-saas-optimization-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-saas-optimization-2026-de.html">Deutsch</a></nav>',
        'title': 'Calculadora de Otimização de SaaS e ROI — Economize no seu Cloud e SaaS — Zion Tech Group',
        'description': 'Calculadora gratuita de Otimização de SaaS e ROI: encontre assentos não utilizados, desperdício de cloud e assinaturas redundantes — modelle o retorno da redimensionamento em minutos.',
        'h1': '💰 Calculadora de Otimização de SaaS e ROI',
        'pitch': 'Calculadora FinOps gratuita e sempre online: encontre o desperdício de custos na sua stack de software e IA — assentos não utilizados, desperdício de cloud, assinaturas redundantes — e modelle o retorno do redimensionamento. Exporte um PDF ROI (logo Zion) para compartilhar com seu CFO.',
        'cards': [
            ('🔍 Auditoria de Assentos', 'Assentos não utilizados, inatividade SSO, assinaturas redundantes — quantificados em um clique.', 'https://ziontechgroup.com/saas-optimization/', 'https://github.com/Zion-support/zion-saas-optimization'),
            ('☁️ Modelador de Custo Cloud', 'Instâncias em estado de inatividade, agentes sobre-dimensionados, lacunas de commit — modelados por carga de trabalho.', 'https://ziontechgroup.com/saas-optimization/', 'https://github.com/Zion-support/zion-saas-optimization'),
            ('📉 Estimador de Retorno', 'ROI de redimensionamento + despacho com metas de ganhos rápidos de 90 dias.', 'https://ziontechgroup.com/saas-optimization/', 'https://github.com/Zion-support/zion-saas-optimization'),
            ('🤖 Otimizador de Custo LLM', 'Aproveitamento de prompt, eficiência de tokens, custo de execução por 1.000 chamadas.', 'https://ziontechgroup.com/saas-optimization/', 'https://github.com/Zion-support/zion-saas-optimization'),
            ('📄 Exportação ROI (logo Zion)', 'Exporte seu relatório de desperdício como um PDF ROI limpo para compartilhar com CFOs e líderes de operações.', 'https://ziontechgroup.com/saas-optimization/', 'https://github.com/Zion-support/zion-saas-optimization'),
            ('🧭 Mão de Obra de Descoberta', 'Relatório de desperdício → sprint diagnóstico gratuito (Lote 116) → marketplace de agentes (Lote 117) → otimização.', 'https://ziontechgroup.com/saas-optimization/', 'https://github.com/Zion-support/zion-saas-optimization'),
        ],
        'discovery_h2': '🧭 Descoberta Gratuita — sempre online, sempre gratuita',
        'discovery_p': 'Encontre o $ que você está vinhando em assinaturas e cloud — antes que a gente arrume. Seu relatório de desperdício é gerado instantaneamente e enviado por e-mail para você e nossa equipe comercial (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Iniciar Descoberta Gratuita',
        'discovery_cta2': 'Navegar pela Rede de Aplicativos',
    },
    'es': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-saas-optimization-2026.html">English</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-saas-optimization-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-saas-optimization-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-saas-optimization-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-saas-optimization-2026-de.html">Deutsch</a></nav>',
        'title': 'Calculadora de Optimización de SaaS y ROI — Ahorre en su Cloud y SaaS — Zion Tech Group',
        'description': 'Calculadora gratuita de Optimización de SaaS y ROI: encuentre assentos no utilizados, gastos de cloud inactivos y suscripciones redundantes — modelice el retorno de la redimensión en minutos.',
        'h1': '💰 Calculadora de Optimización de SaaS y ROI',
        'pitch': 'Calculadora FinOps gratuita y siempre en línea: encontre el desperdicio de costos en su stack de software e IA — assentos no utilizados, gastos de cloud inactivos, suscripciones redundantes — y modelice el retorno de la redimensión. Imprima un PDF ROI (logo Zion) para compartir con su CFO.',
        'cards': [
            ('🔍 Auditoría de Asientos', 'Assentos no utilizados, inactividad SSO, suscripciones redundantes — cuantificados en un clic.', 'https://ziontechgroup.com/saas-optimization/', 'https://github.com/Zion-support/zion-saas-optimization'),
            ('☁️ Modelador de Costo Cloud', 'Instancias en estado de inactividad, agentes sobre-dimensionados, brechas de compromiso — modelados por carga de trabajo.', 'https://ziontechgroup.com/saas-optimization/', 'https://github.com/Zion-support/zion-saas-optimization'),
            ('📉 Estimador de Retorno', 'ROI de redimensionamiento + despacho con metas de ganhos rápidos de 90 días.', 'https://ziontechgroup.com/saas-optimization/', 'https://github.com/Zion-support/zion-saas-optimization'),
            ('🤖 Optimizador de Costo LLM', 'Aproveitamento de prompt, eficiência de tokens, custo de execução por 1.000 chamadas.', 'https://ziontechgroup.com/saas-optimization/', 'https://github.com/Zion-support/zion-saas-optimization'),
            ('📄 Exportação ROI (logo Zion)', 'Exporte seu relatório de desperdício como um PDF ROI limpo para compartilhar com CFOs e líderes de operações.', 'https://ziontechgroup.com/saas-optimization/', 'https://github.com/Zion-support/zion-saas-optimization'),
            ('🧭 Mão de Obra de Descoberta', 'Relatório de desperdício → sprint diagnóstico gratuito (Lote 116) → marketplace de agentes (Lote 117) → otimização.', 'https://ziontechgroup.com/saas-optimization/', 'https://github.com/Zion-support/zion-saas-optimization'),
        ],
        'discovery_h2': '🧭 Descubrimiento Gratuito — siempre en línea, siempre gratuito',
        'discovery_p': 'Encuentre el $ que está perdiendo en suscripciones y cloud — antes de que lo arreglemos. Su informe de desperdicio se genera instantáneamente y se envía por correo a usted y a nuestro equipo comercial (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Comenzar Descubrimiento Gratuito',
        'discovery_cta2': 'Explorar la Red de Aplicaciones',
    },
    'fr': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-saas-optimization-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-saas-optimization-2026-fr.html">Français</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-saas-optimization-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-saas-optimization-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-saas-optimization-2026-de.html">Deutsch</a></nav>',
        'title': 'Calculatrice d\'Optimisation SaaS et ROI — Économisez votre Cloud et SaaS — Zion Tech Group',
        'description': 'Calculatrice gratuite d\'optimisation SaaS et ROI : trouvez les assentos non utilisés, les dépenses cloud inactives et les abonnements redondants — modélisez le retour de la réduction en minutes.',
        'h1': '💰 Calculatrice d\'Optimisation SaaS et ROI',
        'pitch': 'Calculatrice FinOps gratuite et toujours en ligne : trouvez le gaspillage de coûts dans votre stack logicielle et IA — assentos non utilisés, dépenses cloud inactives, abonnements redondants — et modélisez le retour de la réduction. Exportez un PDF ROI (logo Zion) à partager avec votre CFO.',
        'cards': [
            ('🔍 Audit d\'Assentos', 'Assentos non utilisés, inactivité SSO, abonnements redondants — quantifiés en un clic.', 'https://ziontechgroup.com/saas-optimization/', 'https://github.com/Zion-support/zion-saas-optimization'),
            ('☁️ Modeliseur de Coût Cloud', 'Instances en état d\'inactivité, agents sur-dimensionnés, lacunes de commit — modélisés par charge de travail.', 'https://ziontechgroup.com/saas-optimization/', 'https://github.com/Zion-support/zion-saas-optimization'),
            ('📉 Estimateur de Retour', 'ROI de réduction + expédition avec des cibles de gains rapides de 90 jours.', 'https://ziontechgroup.com/saas-optimization/', 'https://github.com/Zion-support/zion-saas-optimization'),
            ('🤖 Optimiseur de Coût LLM', 'Aptitude à l\'usage des prompts, efficacité des tokens, coût d\'exécution par 1.000 appels.', 'https://ziontechgroup.com/saas-optimization/', 'https://github.com/Zion-support/zion-saas-optimization'),
            ('📄 Exportation ROI (logo Zion)', 'Exportez votre rapport de gaspillage en un PDF ROI nettoyé à partager avec vos CMS et chefs d\'équipe.', 'https://ziontechgroup.com/saas-optimization/', 'https://github.com/Zion-support/zion-saas-optimization'),
            ('🧭 Main d\'œuvre de Découverte', 'Rapport de gaspillage → sprint diagnostique gratuit (Lot 116) → marketplace d\'agents (Lot 117) → optimisation.', 'https://ziontechgroup.com/saas-optimization/', 'https://github.com/Zion-support/zion-saas-optimization'),
        ],
        'discovery_h2': '🧭 Découverte Gratuite — toujours en ligne, toujours gratuite',
        'discovery_p': 'Trouvez le $ que vous perdez en abonnements et cloud — avant que nous ne le réparions. Votre rapport de gaspillage est généré instantanément et envoyé par e-mail à vous et à notre équipe commerciale (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Commencer la Découverte Gratuite',
        'discovery_cta2': 'Parcourir le Réseau d\'Applications',
    },
    'de': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-saas-optimization-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-saas-optimization-2026-de.html">Deutsch</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-saas-optimization-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-saas-optimization-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-saas-optimization-2026-fr.html">Français</a></nav>',
        'title': 'SaaS-Optimierungs- & ROI-Kalkulator — Spare Sie auf Ihrem Cloud und SaaS — Zion Tech Group',
        'description': 'Kostenloser SaaS-Optimierungs- und ROI-Kalkulator: finden Sie nicht genutzte Plätze, inaktive Cloud-Ausgaben und redundante Abonnements — modellieren Sie den Rückfluss der Reduzierung in Minuten.',
        'h1': '💰 SaaS-Optimierungs- & ROI-Kalkulator',
        'pitch': 'Kostenloser FinOps-Kalkulator: finden Sie die Kostenverschwendung in Ihrer Software- und KI-Stapel — nicht genutzte Plätze, inaktive Cloud-Ausgaben, redundante Abonnements — und modellieren Sie den Rückfluss der Reduzierung. Exportieren Sie ein PDF mit ROI (Zion-Logo), um es Ihrem CFO zu teilen.',
        'cards': [
            ('🔍 Lizenzzerstörungsprobe', 'Nicht genutzte Plätze, inaktive SSO, redundante Abonnements — quantifiziert in einem Klick.', 'https://ziontechgroup.com/saas-optimization/', 'https://github.com/Zion-support/zion-saas-optimization'),
            ('☁️ Cloud-Kostenvorhalt', 'Inaktive Instanzen, überdimensionierte Agenten, Zusicherungs-Lücken — pro Arbeitslast modelliert.', 'https://ziontechgroup.com/saas-optimization/', 'https://github.com/Zion-support/zion-saas-optimization'),
            ('📉 Rückfluss-Schätzer', 'Reduzierungs-Rückfluss + Export mit 90-Tage-Schnellgewinn-Zielen.', 'https://ziontechgroup.com/saas-optimization/', 'https://github.com/Zion-support/zion-saas-optimization'),
            ('🤖 KI-Kostenschätzer', 'Prompt-Caching, Token-Effizienz, Laufkosten pro 1.000 Aufrufe.', 'https://ziontechgroup.com/saas-optimization/', 'https://github.com/Zion-support/zion-saas-optimization'),
            ('📄 ROI-Export (Zion-Logo)', 'Exportieren Sie Ihren Verschwendungbericht als ein bereinigtes ROI-PDF, um es Ihrem CFO zu teilen.', 'https://ziontechgroup.com/saas-optimization/', 'https://github.com/Zion-support/zion-saas-optimization'),
            ('🧭 Entdeckungs-Handoff', 'Verschwendungbericht → kostenloser Diagnose-Sprint (Nummer 116) → Agenten-Marktplatz (Nummer 117) → Optimierung.', 'https://ziontechgroup.com/saas-optimization/', 'https://github.com/Zion-support/zion-saas-optimization'),
        ],
        'discovery_h2': '🧭 Kostenloser Entdeckung — immer online, immer kostenlos',
        'discovery_p': 'Finden Sie das $, das Sie in Abonnements und Cloud verlieren — bevor wir es reparieren. Ihr Verschwendungbericht wird augenblicklich generiert und per E-Mail an Sie und unser Vertriebsteam (commercial@ziontechgroup.com) gesendet.',
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
    labels = ['🔍 License Waster Audit', '☁️ Cloud Spend Modeler', '📉 Payback Estimator + Export', '🆕 Open-Source Engine']
    section_html = ''
    for grp, label in zip(cards_groups, labels):
        gh = ''.join(f'<div class="card"><h3>{h}</h3><p>{d}</p><a href="{live}">Live app →</a> · <a href="{repo}">Repo</a></div>' for h, d, live, repo in grp)
        section_html += f'<section><h2>{label}</h2><div class="cards">{gh}</div></section>'
    disc = f'<div class="disc"><h2>{body["discovery_h2"]}</h2><p>{body["discovery_p"]}</p><a class="cta green" href="https://ziontechgroup.com/discovery/">{body["discovery_cta1"]}</a><a class="cta alt" href="https://ziontechgroup.com/zion-app-network/">{body["discovery_cta2"]}</a></div>'
    closing = '<p style="margin-top:24px"><a href="https://ziontechgroup.com">← ziontechgroup.com</a> · <a href="https://github.com/Zion-support/zion-app-network/blob/main/SPOTLIGHT-saas-optimization-2026.md">Spotlight doc</a> · <a href="https://github.com/Zion-support/zion-app-network/blob/main/APPS_INDEX-BATCH119-FINOPS.md">Batch rollup</a></p>'
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
    path = os.path.join(WORK, f'app-network-saas-optimization-2026{"-"+ext if ext else ""}.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("wrote", path, "len", len(content))
