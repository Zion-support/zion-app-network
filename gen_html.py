import os

WORK = '/Users/miami2/.hermes/profiles/agent-finops-ops/cache/apphub'
os.makedirs(WORK, exist_ok=True)

BASE = 'https://ziontechgroup.com/zion-app-network/app'
CANON = f'{BASE}/app-network-governance-trust-2026.html'
L = {
 'pt': f'{BASE}/app-network-governance-trust-2026-pt.html',
 'es': f'{BASE}/app-network-governance-trust-2026-es.html',
 'fr': f'{BASE}/app-network-governance-trust-2026-fr.html',
 'de': f'{BASE}/app-network-governance-trust-2026-de.html',
}
LANGS = [('en', CANON), ('pt-BR', L['pt']), ('es', L['es']), ('fr', L['fr']), ('de', L['de'])]

BODY = {
 'en': {
   'langbar': '<nav class="langbar">🌐 <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-governance-trust-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-governance-trust-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-governance-trust-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-governance-trust-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-governance-trust-2026-de.html">Deutsch</a></nav>',
   'title': 'Governance, Risk & Compliance Hub — Zion Tech Group',
   'description': 'Assess readiness, collect audit evidence, track policy change, and enforce safety — one platform for AI governance, risk & compliance.',
   'h1': '⚖️ AI Governance, Risk & Compliance Hub',
   'pitch': 'A single coordinated suite for governing, evaluating, and trusting enterprise AI: readiness scoring, audit evidence, policy tracking, safety enforcement, and live risk evaluation — inside one decision-grade platform. Built for C-suite assurance, SOC 2 / ISO 27001 / GDPR / EU AI Act readiness.',
   'cards': [
     ('🤖 AI Readiness Assessment', 'Scored questionnaire scoring organizational AI maturity with an adoption roadmap and gap analysis.', 'https://ziontechgroup.com/ai-readiness-assessment/', 'https://github.com/Zion-support/ai-readiness-assessment'),
     ('📊 AI Governance Dashboard', 'Enterprise AI governance, model registry, and compliance monitoring in one live view.', 'https://ziontechgroup.com/ai-governance-dashboard/', 'https://github.com/Zion-support/ai-governance-dashboard'),
     ('🛡️ AI Safety & Red-Teaming', 'Safety testing, red-teaming, and safety evaluation frameworks for every AI app in the network.', 'https://ziontechgroup.com/ai-ai-safety/', 'https://github.com/Zion-support/ai-ai-safety'),
     ('📝 Audit Readiness Copilot', 'Audit preparation, evidence workflows, and gap-closure playbooks, guided by named reviewers.', 'https://ziontechgroup.com/audit-readiness-copilot/', 'https://github.com/Zion-support/audit-readiness-copilot'),
     ('🔍 Compliance Evidence Collector', 'Evidence retrieval, audit trails, and source attribution so every finding is traceable.', 'https://ziontechgroup.com/compliance-evidence-collector/', 'https://github.com/Zion-support/compliance-evidence-collector'),
     ('📅 Policy Change Tracker', 'Regulatory and policy change calendars, checklists, and draft generation for continuous compliance.', 'https://ziontechgroup.com/policy-change-tracker/', 'https://github.com/Zion-support/policy-change-tracker'),
     ('🧱 Prompt Shield (Runtime Firewall)', 'Detects and blocks prompt-injection attacks at the application edge — the trust layer for AI agents.', 'https://ziontechgroup.com/prompt-shield/', 'https://github.com/Zion-support/prompt-shield'),
     ('📦 Governance Evidence Pack', 'Copy-ready evidence packs (AI readiness, compliance, audit) assembled from the suite above. Free, open-source.', 'https://ziontechgroup.com/zion-governance-evidence-pack/', 'https://github.com/Zion-support/zion-governance-evidence-pack'),
     ('📊 AI Risk Evaluator', 'Consolidated AI risk scoring matrix (safety, governance, readiness, compliance) for board-level review.', 'https://ziontechgroup.com/zion-ai-risk-evaluator/', 'https://github.com/Zion-support/zion-ai-risk-evaluator'),
   ],
   'discovery_h2': '🧭 Free AI Discovery — always online, always free',
   'discovery_p': 'Need a governance-focused rollout? Take our free Discovery questionnaire: your personalized AI discovery report is generated instantly and emailed to you and our commercial team (commercial@ziontechgroup.com) for fast, tailored follow-up.',
   'discovery_cta1': 'Start Free Discovery',
   'discovery_cta2': 'Browse the App Network',
 },
 'pt': {
   'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-governance-trust-2026.html">English</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-governance-trust-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-governance-trust-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-governance-trust-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-governance-trust-2026-de.html">Deutsch</a></nav>',
   'title': 'Central de Governança, Risco e Conformidade — Zion Tech Group',
   'description': 'Avalie a maturidade, cole comprovantes de auditoria, tracke mudanças de política e boque segurança — uma plataforma para governança, risco e conformidade de IA.',
   'h1': '⚖️ Central de Governança, Risco e Conformidade',
   'pitch': 'Um pacote coordinado para governar, avaliar e confiar em IA empresarial: pontuação de maturidade, provas de auditoria, acompanhamento de políticas, segurança de aplicação e avaliação de risco em tempo real — em uma única plataforma.',
   'cards': [
     ('🤖 Avaliação de Maturidade de IA', 'Questionário pontuado que escoreia a maturidade da IA da organização com um plano de adoção e análise de gaps.', 'https://ziontechgroup.com/ai-readiness-assessment/', 'https://github.com/Zion-support/ai-readiness-assessment'),
     ('📊 Painel de Governança de IA', 'Governança empresarial de IA, registro de modelos e monitoramento de conformidade em um painel ativo.', 'https://ziontechgroup.com/ai-governance-dashboard/', 'https://github.com/Zion-support/ai-governance-dashboard'),
     ('🛡️ Segurança e Red-Teaming de IA', 'Testes de segurança, red-teaming e frameworks de avaliação de segurança para cada aplicativo de IA.', 'https://ziontechgroup.com/ai-ai-safety/', 'https://github.com/Zion-support/ai-ai-safety'),
     ('📝 Copilot de Preparação para Auditoria', 'Procedimentos de prova, workflows de auditoria e playlists de fechamento de lacunas, orientados por revisores.', 'https://ziontechgroup.com/audit-readiness-copilot/', 'https://github.com/Zion-support/audit-readiness-copilot'),
     ('🔍 Coletor de Provas de Conformidade', 'Retirada de provas, trilhas de auditoria e atribuição de origem para que toda conclusão seja rastreável.', 'https://ziontechgroup.com/compliance-evidence-collector/', 'https://github.com/Zion-support/compliance-evidence-collector'),
     ('📅 Rastreio de Mudanças de Política', 'Calendários de mudanças regulatórias, checklists e geração de rascunhos para conformidade contínua.', 'https://ziontechgroup.com/policy-change-tracker/', 'https://github.com/Zion-support/policy-change-tracker'),
     ('🧱 Prompt Shield (Firewall de Tempo Real)', 'Detecta e bloqueia ataques de injeção de prompts na borda da aplicação — a camada de confiança para agentes de IA.', 'https://ziontechgroup.com/prompt-shield/', 'https://github.com/Zion-support/prompt-shield'),
     ('📦 Pacote de Provas de Governança', 'Pacotes de provas prontos (maturidade, conformidade, auditoria) montados a partir do pacote acima. Gratuito, de código aberto.', 'https://ziontechgroup.com/zion-governance-evidence-pack/', 'https://github.com/Zion-support/zion-governance-evidence-pack'),
     ('📊 Avaliador de Risco de IA', 'Matriz consolidada de pontuação de risco de IA (segurança, governança, maturidade, conformidade) para auditoria executiva.', 'https://ziontechgroup.com/zion-ai-risk-evaluator/', 'https://github.com/Zion-support/zion-ai-risk-evaluator'),
   ],
   'discovery_h2': '🧭 Descoberta Gratuita de IA — sempre online, sempre gratuita',
   'discovery_p': 'Precisa de uma implantação focada em governança? Responda nosso questionário de Descoberta: o seu relatório de IA personalizado é gerado instantaneamente e enviado por e-mail para você e nossa equipe comercial (commercial@ziontechgroup.com) para um seguimento rápido e personalizado.',
   'discovery_cta1': 'Iniciar Descoberta Gratuita',
   'discovery_cta2': 'Navegar pela Rede de Aplicativos',
 },
 'es': {
   'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-governance-trust-2026.html">English</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-governance-trust-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-governance-trust-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-governance-trust-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-governance-trust-2026-de.html">Deutsch</a></nav>',
   'title': 'Fiabilidad, Riesgo y Conformidad — Zion Tech Group',
   'description': 'Evalúa la madurez, recoge pruebas de auditoría, rastrea cambios de política y bloquea seguridad — una plataforma para gobernanza, riesgo y conformidad de IA.',
   'h1': '⚖️ Fiabilidad, Riesgo y Conformidad',
   'pitch': 'Un paquete coordinado para gobernar, evaluar y confiar en IA empresarial: puntuación de madurez, pruebas de auditoría, seguimiento de políticas, seguridad y evaluación de riesgo en tiempo real — en una sola plataforma.',
   'cards': [
     ('🤖 Evaluación de Madurez de IA', 'Cuestionario puntuado que mide la madurez de IA de la organización con un plan de adopción y análisis de brechas.', 'https://ziontechgroup.com/ai-readiness-assessment/', 'https://github.com/Zion-support/ai-readiness-assessment'),
     ('📊 Panel de Governabilidad de IA', 'Governabilidad empresarial de IA, registro de modelos y monitorización de conformidad en una vista activa.', 'https://ziontechgroup.com/ai-governance-dashboard/', 'https://github.com/Zion-support/ai-governance-dashboard'),
     ('🛡️ Seguridad y Red-Teaming de IA', 'Pruebas de seguridad, red-teaming y marcos de evaluación de seguridad para cada aplicación de IA.', 'https://ziontechgroup.com/ai-ai-safety/', 'https://github.com/Zion-support/ai-ai-safety'),
     ('📝 Copilot de Preparación para Auditoría', 'Flujos de prueba, procedimientos de auditoría y fichas de cierre de brechas, supervisados por revisores designados.', 'https://ziontechgroup.com/audit-readiness-copilot/', 'https://github.com/Zion-support/audit-readiness-copilot'),
     ('🔍 Recopilador de Pruebas de Conformidad', 'Recogida de pruebas, trazabilidad de auditoría y atribución de fuentes para que todo hallazgo sea trazable.', 'https://ziontechgroup.com/compliance-evidence-collector/', 'https://github.com/Zion-support/compliance-evidence-collector'),
     ('📅 Seguimiento de Cambios de Política', 'Calendarios de cambios regulatorios, listas de comprobación y generación de borradores para conformidad continua.', 'https://ziontechgroup.com/policy-change-tracker/', 'https://github.com/Zion-support/policy-change-tracker'),
     ('🧱 Prompt Shield (Firewall en Tiempo Real)', 'Detecta y bloquea ataques de inyección de prompts en el borde de la aplicación — la capa de confianza para agentes de IA.', 'https://ziontechgroup.com/prompt-shield/', 'https://github.com/Zion-support/prompt-shield'),
     ('📦 Paquete de Pruebas de Governabilidad', 'Paquetes de pruebas listos (madurez, conformidad, auditoría) ensamblados a partir del paquete anterior. Gratuito, código abierto.', 'https://ziontechgroup.com/zion-governance-evidence-pack/', 'https://github.com/Zion-support/zion-governance-evidence-pack'),
     ('📊 Evaluador de Riesgo de IA', 'Matriz consolidada de puntuación de riesgo de IA (seguridad, gobernanza, madurez, conformidad) para revisión direccional.', 'https://ziontechgroup.com/zion-ai-risk-evaluator/', 'https://github.com/Zion-support/zion-ai-risk-evaluator'),
   ],
   'discovery_h2': '🧭 Descubrimiento Gratuito de IA — siempre en línea, siempre gratuito',
   'discovery_p': '¿Necesita un despliegue orientado a gobernanza? Responda nuestro cuestionario de Descubrimiento: su informe personalizado de IA se genera instantáneamente y se envía por correo a usted y a nuestro equipo comercial (commercial@ziontechgroup.com) para un seguimiento rápido y personalizado.',
   'discovery_cta1': 'Comenzar Descubrimiento Gratuito',
   'discovery_cta2': 'Explorar la Red de Aplicaciones',
 },
 'fr': {
   'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-governance-trust-2026.html">English</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-governance-trust-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-governance-trust-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-governance-trust-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-governance-trust-2026-de.html">Deutsch</a></nav>',
   'title': 'Gouvernance, Risque et Conformité — Zion Tech Group',
   'description': 'Évaluez la maturité, recueillez les preuves d\'audit, suivez les changements de politique et activez la sécurité — une plateforme de gouvernance, de risque et de conformité de l\'IA.',
   'h1': '⚖️ Gouvernance, Risque et Conformité de l\'IA',
   'pitch': 'Un pack coordonné pour gouverner, évaluer et faire confiance à l\'IA économique : score de maturité, preuves d\'audit, suivi des politiques, sécurité et évaluation de risque en temps réel — dans une seule plateforme.',
   'cards': [
     ('🤖 Évaluation de la Maturité IA', 'Questionnaire noté mesurant la maturité de l\'IA de l\'organisation avec un plan d\'adoption et une analyse des écarts.', 'https://ziontechgroup.com/ai-readiness-assessment/', 'https://github.com/Zion-support/ai-readiness-assessment'),
     ('📊 Tableaux de Bord de Gouvernance IA', 'Gouvernance économique d\'IA, registre de modèles et surveillance de la conformité dans un tableau de bord actif.', 'https://ziontechgroup.com/ai-governance-dashboard/', 'https://github.com/Zion-support/ai-governance-dashboard'),
     ('🛡️ Sécurité et Red-Teaming IA', 'Tests de sécurité, red-teaming et cadres d\'évaluation de la sécurité pour chaque application IA.', 'https://ziontechgroup.com/ai-ai-safety/', 'https://github.com/Zion-support/ai-ai-safety'),
     ('📝 Copilote de Préparation aux Audit', 'Procédures de preuve, flux d\'audit et fiches de clôture des écarts, supervisés par des réviseurs désignés.', 'https://ziontechgroup.com/audit-readiness-copilot/', 'https://github.com/Zion-support/audit-readiness-copilot'),
     ('🔍 Collecteur de Preuves de Conformité', 'Récupération de preuves, traçabilité d\'audit et attribution des sources pour que chaque constat soit traçable.', 'https://ziontechgroup.com/compliance-evidence-collector/', 'https://github.com/Zion-support/compliance-evidence-collector'),
     ('📅 Suivi des Changements de Politique', 'Calendriers de changements réglementaires, listes de contrôle et génération de brouillons pour une conformité continue.', 'https://ziontechgroup.com/policy-change-tracker/', 'https://github.com/Zion-support/policy-change-tracker'),
     ('🧱 Prompt Shield (Firewall en Temps Réel)', 'Détecte et bloque les attaques par injection de prompts au bord de l\'application — la couche de confiance pour les agents IA.', 'https://ziontechgroup.com/prompt-shield/', 'https://github.com/Zion-support/prompt-shield'),
     ('📦 Pack de Preuves de Gouvernance', 'Pack de preuves prêts (maturité, conformité, audit) assemblés à partir du pack précédent. Gratuit, code source ouvert.', 'https://ziontechgroup.com/zion-governance-evidence-pack/', 'https://github.com/Zion-support/zion-governance-evidence-pack'),
     ('📊 Évaluateur de Risque IA', 'Matrice consolidée de notation de risque IA (sécurité, gouvernance, maturité, conformité) pour un contrôle directionnel.', 'https://ziontechgroup.com/zion-ai-risk-evaluator/', 'https://github.com/Zion-support/zion-ai-risk-evaluator'),
   ],
   'discovery_h2': '🧭 Découverte Gratuite d\'IA — toujours en ligne, toujours gratuite',
   'discovery_p': 'Vous avez besoin d\'un déploiement axé sur la gouvernance ? Répondez à notre questionnaire de Découverte : votre rapport personnalisé d\'IA est généré instantanément et envoyé par e-mail à vous et à notre équipe commerciale (commercial@ziontechgroup.com) pour un suivi rapide et personnalisé.',
   'discovery_cta1': 'Commencer la Découverte Gratuite',
   'discovery_cta2': 'Parcourir le Réseau d\'Applications',
 },
 'de': {
   'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-governance-trust-2026.html">English</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-governance-trust-2026-de.html">Deutsch</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-governance-trust-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-governance-trust-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-governance-trust-2026-fr.html">Français</a></nav>',
   'title': 'Gewalt, Risiko & Compliance — Zion Tech Group',
   'description': 'Ermitteln Sie die Reife, sammeln Sie Audit-Belege, verfolgen Sie Policy-Änderungen und aktivieren Sie Sicherheit — eine Plattform für KI-Governance, Risiko und Compliance.',
   'h1': '⚖️ KI-Governance, Risiko & Compliance',
   'pitch': 'Ein koordinierter Paket zum Gouvernieren, Bewerten und Vertrauen in Unternehmens-KI: Reifescore, Audit-Belege, Policy-Verfolgung, Sicherheit und Risikobewertung in Echtzeit — in einer einzigen Plattform.',
   'cards': [
     ('🤖 KI-Reifebewertung', 'Befragung mit Punktzahl zur Messung der KI-Reife eines Unternehmens mit einem Innovationsplan und Lückenanalyse.', 'https://ziontechgroup.com/ai-readiness-assessment/', 'https://github.com/Zion-support/ai-readiness-assessment'),
     ('📊 Dashboard für KI-Governance', 'Unternehmens-KI-Governance, Modellumfeld und Compliance-Monitoring in einer aktiven Ansicht.', 'https://ziontechgroup.com/ai-governance-dashboard/', 'https://github.com/Zion-support/ai-governance-dashboard'),
     ('🛡️ KI-Sicherheit & Red-Teaming', 'Sicherheitstests, Red-Teaming und Rahmenwerke zur Sicherheitsbewertung für jede KI-Anwendung.', 'https://ziontechgroup.com/ai-ai-safety/', 'https://github.com/Zion-support/ai-ai-safety'),
     ('📝 Audit-Readiness-Copilot', 'Nachweisverfahren, Audit-Flüsse und Schließspiele, geleitet von benannten Prüfern.', 'https://ziontechgroup.com/audit-readiness-copilot/', 'https://github.com/Zion-support/audit-readiness-copilot'),
     ('🔍 Compliance-Beweis-Sammler', 'Nachweise sammeln, Audit-Tracking und Quellenangaben, damit jedes Ergebnis rückverfolgbar ist.', 'https://ziontechgroup.com/compliance-evidence-collector/', 'https://github.com/Zion-support/compliance-evidence-collector'),
     ('📅 Policy-Änderung-Stracker', 'Zeitpläne für regulatorische Änderungen, Checklisten und Entwurfsgenerierung für kontinuierliche Compliance.', 'https://ziontechgroup.com/policy-change-tracker/', 'https://github.com/Zion-support/policy-change-tracker'),
     ('🧱 Prompt Shield (Echtzeits-Firewall)', 'Erkennt und blockiert Prompt-Injection-Angriffe an der Anwendungsgrenze — die Vertrauenschicht für KI-Agenten.', 'https://ziontechgroup.com/prompt-shield/', 'https://github.com/Zion-support/prompt-shield'),
     ('📦 Governance-Beweis-Paket', 'Bereitgestellte Beweispakete (Reife, Compliance, Audit) aus dem vorherigen Paket zusammen assemblieren. Kostenlos, Open-Source.', 'https://ziontechgroup.com/zion-governance-evidence-pack/', 'https://github.com/Zion-support/zion-governance-evidence-pack'),
     ('📊 KI-Risikobewertung', 'Konsolidierte Risikowertungsmatrix (Sicherheit, Governance, Reife, Compliance) für die leitungsebene.', 'https://ziontechgroup.com/zion-ai-risk-evaluator/', 'https://github.com/Zion-support/zion-ai-risk-evaluator'),
   ],
   'discovery_h2': '🧭 Kostenloser KI-Entdeckung — immer online, immer kostenlos',
   'discovery_p': 'Sie benötigen eine auf Governance ausgerichtete Einführung? Beantworten Sie unser Entdeckungsfragebogen: Ihr personalisierter KI-Bericht wird sofort generiert und per E-Mail an Sie und unser Vertriebsteam (commercial@ziontechgroup.com) gesendet für ein schnelles und personalisiertes Nachverfolgung.',
   'discovery_cta1': 'Kostenlosen Entdeckung starten',
   'discovery_cta2': 'App-Netzwerk durchsuchen',
 },
}

def alternate_links():
    out = []
    for l2, u in LANGS:
        out.append(f'<link rel="alternate" hreflang="{l2}" href="{u}" />')
    return ''.join(out)

CSS = "body{font-family:system-ui,sans-serif;margin:0;color:#0f172a;background:#f8fafc}header,footer{background:#0b1220;color:#fff;padding:1rem}main{max-width:1100px;margin:0 auto;padding:1.5rem}.langbar{margin-bottom:1rem}.langbar a.active{color:#2563eb;font-weight:600}.cards{display:grid;gap:1rem}.card{background:#fff;border:1px solid #e2e8f0;border-radius:12px;padding:1rem;box-shadow:0 1px 3px rgba(15,23,42,.06)}.card h3{margin:.4rem 0 .3rem;color:#0f172a}.card p{color:#475569;font-size:.92rem}.card a{color:#2563eb;font-weight:600;text-decoration:none}.disc{background:#f1f5f9;border:1px solid #e2e8f0;border-radius:12px;padding:1.25rem;margin-top:1.25rem}.disc h2{margin-top:0}.disc .cta{display:inline-block;margin-top:.75rem;padding:.7rem 1.1rem;border-radius:8px;text-decoration:none;font-weight:650}.disc .cta.green{background:#059669;color:#fff}.disc .cta.alt{background:#0f172a;color:#fff}footer{background:#0b1220;color:#94a3b8;padding:1rem}footer a{color:#64748b}"

def assemble(lang):
    url_map = {'en': CANON, 'pt': L['pt'], 'es': L['es'], 'fr': L['fr'], 'de': L['de']}
    body = BODY[lang]
    urls = dict(LANGS); urls['en'] = CANON
    al = alternate_links()
    cards_groups = [body['cards'][:3], body['cards'][3:6], body['cards'][6:9]]
    labels = ['🎯 Readiness & Evaluation', '📋 Audit Evidence & Compliance', '⚡ Safety Enforcement (New)', '🆕 Newly Published (Open Source)']
    section_html = ''
    for grp, label in zip(cards_groups, labels):
        gh = ''.join(f'<div class="card"><h3>{h}</h3><p>{d}</p><a href="{live}">Live app →</a> · <a href="{repo}">Repo</a></div>' for h, d, live, repo in grp)
        section_html += f'<section><h2>{label}</h2><div class="cards">{gh}</div></section>'
    disc = f'<div class="disc"><h2>{body["discovery_h2"]}</h2><p>{body["discovery_p"]}</p><a class="cta green" href="https://ziontechgroup.com/discovery/">{body["discovery_cta1"]}</a><a class="cta alt" href="https://ziontechgroup.com/zion-app-network/">{body["discovery_cta2"]}</a></div>'
    closing = '<p style="margin-top:24px"><a href="https://ziontechgroup.com">← ziontechgroup.com</a> · <a href="https://github.com/Zion-support/zion-app-network/blob/main/SPOTLIGHT-governance-trust-2026.md">Spotlight doc</a> · <a href="https://github.com/Zion-support/zion-app-network/blob/main/APPS_INDEX-BATCH114-GOVERNANCE.md">Batch rollup</a></p>'
    footer = '<footer>© 2026 Zion Tech Group — <a href="https://ziontechgroup.com">ziontechgroup.com</a> · Part of the Zion AI App Network</footer>'
    return f'''<!DOCTYPE html>
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
    path = os.path.join(WORK, f'app-network-governance-trust-2026{"-"+ext if ext else ""}.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("wrote", path, "len", len(content))
