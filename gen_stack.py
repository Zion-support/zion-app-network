import os

WORK = '/Users/miami2/.hermes/profiles/agent-finops-ops/cache/apphub'
os.makedirs(WORK, exist_ok=True)

BASE = 'https://ziontechgroup.com/zion-app-network/app'
CANON = f'{BASE}/app-network-ai-stack-matcher-2026.html'
L = {
    'pt': f'{BASE}/app-network-ai-stack-matcher-2026-pt.html',
    'es': f'{BASE}/app-network-ai-stack-matcher-2026-es.html',
    'fr': f'{BASE}/app-network-ai-stack-matcher-2026-fr.html',
    'de': f'{BASE}/app-network-ai-stack-matcher-2026-de.html',
}
LANGS = [('en', CANON), ('pt-BR', L['pt']), ('es', L['es']), ('fr', L['fr']), ('de', L['de'])]

BODY = {
    'en': {
        'langbar': '<nav class="langbar">🌐 <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-stack-matcher-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-stack-matcher-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-stack-matcher-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-stack-matcher-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-stack-matcher-2026-de.html">Deutsch</a></nav>',
        'title': 'AI Stack Matcher — Build, Blend, or Buy — Zion Tech Group',
        'description': 'Free AI stack matching: get a scored build/blend/buy verdict, 3-year TCO, and orchestration comparison for your workforce — instantly.',
        'h1': '🤖 AI Stack Matcher',
        'pitch': 'Free, always-online stack matching: describe your workforce and workflows, and get a scored recommendation — build / blend / buy — with a 3-year TCO model and orchestration comparison. The decision-ready entry into the apps network.',
        'cards': [
            ('🔍 Workforce & Workflow Intake', '5-question free form: team size, manual tasks, compliance needs, cloud posture, budget band.', 'https://ziontechgroup.com/ai-stack-matcher/', 'https://github.com/Zion-support/zion-ai-stack-matcher'),
            ('🏆 Scored Build/Blend/Buy Verdict', 'Ranked stack recommendation per workload with confidence rating and reasoning.', 'https://ziontechgroup.com/ai-stack-matcher/', 'https://github.com/Zion-support/zion-ai-stack-matcher'),
            ('📊 3-Year TCO Model', 'Per candidate: model, orchestration, infrastructure, and commercial shape — with integration and exit costs.', 'https://ziontechgroup.com/ai-stack-matcher/', 'https://github.com/Zion-support/zion-ai-stack-matcher'),
            ('🔄 Orchestration Comparison', 'LangChain vs LangGraph vs crewAI vs custom, matched to your team size and skill set.', 'https://ziontechgroup.com/ai-stack-matcher/', 'https://github.com/Zion-support/zion-ai-stack-matcher'),
            ('🚪 Portability Ramp', 'From vendor lock-in to self-host, with runbooks and exit planning.', 'https://ziontechgroup.com/ai-stack-matcher/', 'https://github.com/Zion-support/zion-ai-stack-matcher'),
            ('🧭 Discovery Handoff', 'Matched stack → free diagnostic sprint (Batch 116) → agent marketplace (Batch 117) → implementation.', 'https://ziontechgroup.com/ai-stack-matcher/', 'https://github.com/Zion-support/zion-ai-stack-matcher'),
        ],
        'discovery_h2': '🧭 Free Discovery — always online, always free',
        'discovery_p': 'Tell us what you do. We tell you whether to build, blend, or buy AI — with the 3-year cost model. Your personalized AI-stack recommendation is generated instantly and emailed to you and our commercial team (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Start Free Discovery',
        'discovery_cta2': 'Browse the App Network',
    },
    'pt': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-stack-matcher-2026.html">English</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-stack-matcher-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-stack-matcher-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-stack-matcher-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-stack-matcher-2026-de.html">Deutsch</a></nav>',
        'title': 'Matcher de Stack de IA — Construir, Misturar ou Comprar — Zion Tech Group',
        'description': 'Matching de stack de IA gratuito: obtenha um veredicto pontuado construir/misturar/comprar, TCO de 3 anos e comparação de orquestração para a sua força de trabalho — instantaneamente.',
        'h1': '🤖 Matcher de Stack de IA',
        'pitch': 'Matching de stack gratuito e sempre online: descreva sua força de trabalho e fluxos de trabalho e receba uma recomendação pontuada — construir/misturar/comprar — com modelo TCO de 3 anos e comparação de orquestração. A entrada pronta para decisão na rede de aplicativos.',
        'cards': [
            ('🔍 Ingresso de Força de Trabalho e Fluxos', 'Formulário gratuito de 5 perguntas: tamanho da equipe, tarefas manuais, necessidades de conformidade, postura em nuvem, faixa orçamentária.', 'https://ziontechgroup.com/ai-stack-matcher/', 'https://github.com/Zion-support/zion-ai-stack-matcher'),
            ('🏆 Veredicto construir/misturar/comprar', 'Recomendação de stack classificada por carga de trabalho, com nota de confiança e raciocínio.', 'https://ziontechgroup.com/ai-stack-matcher/', 'https://github.com/Zion-support/zion-ai-stack-matcher'),
            ('📊 Modelo TCO de 3 Anos', 'Por candidato: modelo, orquestração, infraestrutura e formato comercial — com custos de integração e saída.', 'https://ziontechgroup.com/ai-stack-matcher/', 'https://github.com/Zion-support/zion-ai-stack-matcher'),
            ('🔄 Comparação de Orquestração', 'LangChain vs LangGraph vs crewAI vs custom, ajustado ao tamanho da equipe e ao nível de habilidade.', 'https://ziontechgroup.com/ai-stack-matcher/', 'https://github.com/Zion-support/zion-ai-stack-matcher'),
            ('🚪 Rampa de Portabilidade', 'De dependência de fornecedor para auto-hospedagem, com runbooks e planejamento de saída.', 'https://ziontechgroup.com/ai-stack-matcher/', 'https://github.com/Zion-support/zion-ai-stack-matcher'),
            ('🧭 Mão de Obra de Descoberta', 'Stack correspondido → sprint diagnóstico gratuito (Lote 116) → marketplace de agentes (Lote 117) → implementação.', 'https://ziontechgroup.com/ai-stack-matcher/', 'https://github.com/Zion-support/zion-ai-stack-matcher'),
        ],
        'discovery_h2': '🧭 Descoberta Gratuita — sempre online, sempre gratuita',
        'discovery_p': 'Nos conte o que você faz. Nós dizemos se construir, misturar ou comprar IA — com o modelo de custo de 3 anos. Seu recomendação de stack de IA personalizada é gerada instantaneamente e enviada por e-mail para você e nossa equipe comercial (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Iniciar Descoberta Gratuita',
        'discovery_cta2': 'Navegar pela Rede de Aplicativos',
    },
    'es': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-stack-matcher-2026.html">English</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-stack-matcher-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-stack-matcher-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-stack-matcher-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-stack-matcher-2026-de.html">Deutsch</a></nav>',
        'title': 'Matcher de Stack de IA — Construir, Mezclar o Comprar — Zion Tech Group',
        'description': 'Matching de stack de IA gratuito: obtenga un veredicto clasificado construir/mestrar/comprar, TCO de 3 años y comparación de orquestración para su fuerza de trabajo — instantáneamente.',
        'h1': '🤖 Matcher de Stack de IA',
        'pitch': 'Matching de stack gratuito y siempre en línea: describa su fuerza de trabajo y flujos de trabajo y obtenga una recomendación clasificada — construir/mezclar/comprar — con modelo de costo TCO de 3 años y comparación de orquestración. La entrada lista para la decisión en la red de aplicaciones.',
        'cards': [
            ('🔍 Ingreso de Fuerza de Trabajo y Flujos', 'Formulario gratuito de 5 preguntas: tamaño del equipo, tareas manuales, necesidades de cumplimiento, postura en la nube, banda de presupuesto.', 'https://ziontechgroup.com/ai-stack-matcher/', 'https://github.com/Zion-support/zion-ai-stack-matcher'),
            ('🏆 Veredicto construir/mezclar/comprar', 'Recomendación de stack clasificada por carga de trabajo con calificación de confianza y razonamiento.', 'https://ziontechgroup.com/ai-stack-matcher/', 'https://github.com/Zion-support/zion-ai-stack-matcher'),
            ('📊 Modelo TCO de 3 Años', 'Por candidato: modelo, orquestración, infraestructura y forma comercial — con costos de integración y salida.', 'https://ziontechgroup.com/ai-stack-matcher/', 'https://github.com/Zion-support/zion-ai-stack-matcher'),
            ('🔄 Comparación de Orquestración', 'LangChain vs LangGraph vs crewAI vs custom, ajustado al tamaño del equipo y al nivel de habilidad.', 'https://ziontechgroup.com/ai-stack-matcher/', 'https://github.com/Zion-support/zion-ai-stack-matcher'),
            ('🚪 Rama de Portabilidad', 'De dependencia del proveedor a auto-hospedaje, con runbooks y planificación de salida.', 'https://ziontechgroup.com/ai-stack-matcher/', 'https://github.com/Zion-support/zion-ai-stack-matcher'),
            ('🧭 Mano de Obra de Descubrimiento', 'Stack coincidente → sprint diagnóstico gratuito (Lote 116) → mercado de agentes (Lote 117) → implementación.', 'https://ziontechgroup.com/ai-stack-matcher/', 'https://github.com/Zion-support/zion-ai-stack-matcher'),
        ],
        'discovery_h2': '🧭 Descubrimiento Gratuito — siempre en línea, siempre gratuito',
        'discovery_p': 'Cuéntenos lo que hacen. Les decimos si construir, mezclar o comprar IA — con el modelo de costo de 3 años. Su recomendación de stack personalizada de IA se genera instantáneamente y se envía por correo a usted y a nuestro equipo comercial (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Comenzar Descubrimiento Gratuito',
        'discovery_cta2': 'Explorar la Red de Aplicaciones',
    },
    'fr': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-stack-matcher-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-stack-matcher-2026-fr.html">Français</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-stack-matcher-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-stack-matcher-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-stack-matcher-2026-de.html">Deutsch</a></nav>',
        'title': 'Dateur de Stack IA — Construire, Mixer ou Acheter — Zion Tech Group',
        'description': 'Matching de stack IA gratuit : obtenez un jugement de Marché de confiance, TCO de 3 ans et comparaison d\'orchestration pour votre personnel — instantanément.',
        'h1': '🤖 Dateur de Stack IA',
        'pitch': 'Matching de stack gratuit et toujours en ligne : décrivez votre personnel et vos flux de travail, et obtenez une recommandation classée — construire/mixer/acquérir — avec modèle TCO 3 ans et comparaison d\'orchestration. L\'entrée prête pour la décision dans le réseau d\'applications.',
        'cards': [
            ('🔍 Prise en Charge du Personnel et des Flux', 'Formulaire gratuit de 5 questions : effectif, tâches manuelles, besoins de conformité, posture cloud, fourchette budgétaire.', 'https://ziontechgroup.com/ai-stack-matcher/', 'https://github.com/Zion-support/zion-ai-stack-matcher'),
            ('🏆 Verdict construire/mixer/acquérir', 'Recommandation de stack classée par charge de travail, avec note de confiance et raisonnement.', 'https://ziontechgroup.com/ai-stack-matcher/', 'https://github.com/Zion-support/zion-ai-stack-matcher'),
            ('📊 Modèle TCO 3 Ans', 'Par candidat : modèle, orchestration, infrastructure, forme commerciale — avec coûts d\'intégration et de sortie.', 'https://ziontechgroup.com/ai-stack-matcher/', 'https://github.com/Zion-support/zion-ai-stack-matcher'),
            ('🔄 Comparaison d\'Orchestration', 'LangChain vs LangGraph vs crewAI vs custom, adapté à l\'effectif et au niveau de compétence.', 'https://ziontechgroup.com/ai-stack-matcher/', 'https://github.com/Zion-support/zion-ai-stack-matcher'),
            ('🚪 Rampe de Portabilité', 'De la dépendance au fournisseur à l\'auto-hébergement, avec runbooks et planification de sortie.', 'https://ziontechgroup.com/ai-stack-matcher/', 'https://github.com/Zion-support/zion-ai-stack-matcher'),
            ('🧭 Main d\'œuvre de Découverte', 'Stackiénné → sprint diagnostique gratuit (Lot 116) → marketplace d\'agents (Lot 117) → intégration.', 'https://ziontechgroup.com/ai-stack-matcher/', 'https://github.com/Zion-support/zion-ai-stack-matcher'),
        ],
        'discovery_h2': '🧭 Découverte Gratuite — toujours en ligne, toujours gratuite',
        'discovery_p': 'Dites-nous ce que vous faites. Nous vous disons si construire, mixer ou acheter de l\'IA — avec le modèle de coût 3 ans. Votre recommandation de stack personnalisée est générée instantanément et envoyée par e-mail à vous et à notre équipe commerciale (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Commencer la Découverte Gratuite',
        'discovery_cta2': 'Parcourir le Réseau d\'Applications',
    },
    'de': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-stack-matcher-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-stack-matcher-2026-de.html">Deutsch</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-stack-matcher-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-stack-matcher-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-stack-matcher-2026-fr.html">Français</a></nav>',
        'title': 'KI-Stack-Matcher — Bauen, Mischen oder Kaufen — Zion Tech Group',
        'description': 'Kostenloser KI-Stack-Matcher: erhalten Sie ein punktiertes Bauen/Mischen/Kauf-Entscheidung, 3-Jahres-Kostenmodell und Orchestrierungs-Vergleich für Ihr Personal — augenblicklich.',
        'h1': '🤖 KI-Stack-Matcher',
        'pitch': 'Kostenloser, immer online verfügbarer Stack-Matcher: beschreiben Sie Ihr Personal und Ihre Workflows und erhalten Sie eine geordnete Empfehlung — bauen/mischen/kaufen — mit Kostenmodell 3 Jahre und Orchestrierungs-Vergleich. Der entscheidungsbereite Einstieg ins App-Netzwerk.',
        'cards': [
            ('🔍 Personal- und Workflow-Eingabe', 'Fünffragen-Kostenloser Brief: Personalstärke, manuelle Aufgaben, Compliance-Bedarf, Cloud-Position, Budgetschale.', 'https://ziontechgroup.com/ai-stack-matcher/', 'https://github.com/Zion-support/zion-ai-stack-matcher'),
            ('🏆 Bauen/Mischen/Kauf-Entscheidung', 'Geordnetes Stack-Empfehlung pro Arbeitslast mit Vertrauensbewertung und Begründung.', 'https://ziontechgroup.com/ai-stack-matcher/', 'https://github.com/Zion-support/zion-ai-stack-matcher'),
            ('📊 3-Jahres-Kostenmodell', 'Pro Kandidaten: Modell, Orchestrierung, Infrastruktur und kommerzielle Form — mit Integrations- und Austrittskosten.', 'https://ziontechgroup.com/ai-stack-matcher/', 'https://github.com/Zion-support/zion-ai-stack-matcher'),
            ('🔄 Orchestrierungs-Vergleich', 'LangChain vs LangGraph vs crewAI vs custom, angepasst an die Personalstärke und das Können.', 'https://ziontechgroup.com/ai-stack-matcher/', 'https://github.com/Zion-support/zion-ai-stack-matcher'),
            ('🚪 Portabilitäts-Rampe', 'Von Lieferanten-Sperre zu Self-Hosting, mit Runbooks und Austrittsplanung.', 'https://ziontechgroup.com/ai-stack-matcher/', 'https://github.com/Zion-support/zion-ai-stack-matcher'),
            ('🧭 Entdeckungs-Handoff', 'Stack-zu-Korrektur → kostenloser Diagnose-Sprint (Zahl 116) → Agenten-Marktplatz (Zahl 117) → Durchführung.', 'https://ziontechgroup.com/ai-stack-matcher/', 'https://github.com/Zion-support/zion-ai-stack-matcher'),
        ],
        'discovery_h2': '🧭 Kostenloser Entdeckung — immer online, immer kostenlos',
        'discovery_p': 'Erzählen Sie uns, was Sie tun. Wir sagen Ihnen, ob Sie KI bauen, mischen oder kaufen sollen — mit dem Kostenmodell 3 Jahre. Ihr personalisierter KI-Stack-Fund ist augenblicklich generiert und per E-Mail an Sie und unser Vertriebsteam (commercial@ziontechgroup.com) gesendet.',
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
    labels = ['🔍 Intake + Verdict', '📊 TCO + Orchestration', '🚪 Portability + Handoff', '🆕 Open-Source Engine']
    section_html = ''
    for grp, label in zip(cards_groups, labels):
        gh = ''.join(f'<div class="card"><h3>{h}</h3><p>{d}</p><a href="{live}">Live app →</a> · <a href="{repo}">Repo</a></div>' for h, d, live, repo in grp)
        section_html += f'<section><h2>{label}</h2><div class="cards">{gh}</div></section>'
    disc = f'<div class="disc"><h2>{body["discovery_h2"]}</h2><p>{body["discovery_p"]}</p><a class="cta green" href="https://ziontechgroup.com/discovery/">{body["discovery_cta1"]}</a><a class="cta alt" href="https://ziontechgroup.com/zion-app-network/">{body["discovery_cta2"]}</a></div>'
    closing = '<p style="margin-top:24px"><a href="https://ziontechgroup.com">← ziontechgroup.com</a> · <a href="https://github.com/Zion-support/zion-app-network/blob/main/SPOTLIGHT-ai-stack-matcher-2026.md">Spotlight doc</a> · <a href="https://github.com/Zion-support/zion-app-network/blob/main/APPS_INDEX-BATCH118-STACK.md">Batch rollup</a></p>'
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
    path = os.path.join(WORK, f'app-network-ai-stack-matcher-2026{"-"+ext if ext else ""}.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("wrote", path, "len", len(content))
