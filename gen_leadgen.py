import os

WORK = '/Users/miami2/.hermes/profiles/agent-finops-ops/cache/apphub'
os.makedirs(WORK, exist_ok=True)

BASE = 'https://ziontechgroup.com/zion-app-network/app'
CANON = f'{BASE}/app-network-sales-leadgen-2026.html'
L = {
    'pt': f'{BASE}/app-network-sales-leadgen-2026-pt.html',
    'es': f'{BASE}/app-network-sales-leadgen-2026-es.html',
    'fr': f'{BASE}/app-network-sales-leadgen-2026-fr.html',
    'de': f'{BASE}/app-network-sales-leadgen-2026-de.html',
}
LANGS = [('en', CANON), ('pt-BR', L['pt']), ('es', L['es']), ('fr', L['fr']), ('de', L['de'])]

BODY = {
    'en': {
        'langbar': '<nav class="langbar">🌐 <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-sales-leadgen-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-sales-leadgen-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-sales-leadgen-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-sales-leadgen-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-sales-leadgen-2026-de.html">Deutsch</a></nav>',
        'title': 'AI Sales & Lead-Gen Specialist — Find Your Best Leads — Zion Tech Group',
        'description': 'Free AI Sales & Lead-Gen Specialist hub: scan your email history for qualified leads by location, enrich them, and turn them into booked work — no cold call needed.',
        'h1': '🤖 AI Sales & Lead-Gen Specialist',
        'pitch': 'Free, always-online lead generation: find every lead we\'ve already worked with — in your area, in your language — and turn them into booked work. Scan all labels (oldest to newest) for service requests and technician inquiries, enrich contacts, and hand off to CRM, outreach, and the agent marketplace. For FE\'s & technicians — top priority.',
        'cards': [
            ('📧 Email-Thread Lead Scanner', 'Scans all labels (inbox + folders, oldest to newest) for service requests and technician inquiries — ranked by commercial value.', 'https://ziontechgroup.com/sales-leadgen/', 'https://github.com/Zion-support/zion-sales-leadgen'),
            ('📦 Lead Enrichment', 'Adds contact + buying signals: location, company, prior-work history, pricing range — ready for CRM.', 'https://ziontechgroup.com/sales-leadgen/', 'https://github.com/Zion-support/zion-sales-leadgen'),
            ('🧾 CRM Write-Back Draft', 'Drafts a HubSpot contact record (name, email, lead source, score) for Commercial review — no manual entry.', 'https://ziontechgroup.com/sales-leadgen/', 'https://github.com/Zion-support/zion-sales-leadgen'),
            ('💬 Outreach Draft (personalised)', 'Writes a personalised cold-email draft (commercial@ziontechgroup.com c/c) + a follow-up reminder schedule.', 'https://ziontechgroup.com/sales-leadgen/', 'https://github.com/Zion-support/zion-sales-leadgen'),
            ('📊 Lead Scoring & Quota', 'Ranks leads by commercial value; hides internal markup — shows only the client-facing price range for outreach.', 'https://ziontechgroup.com/sales-leadgen/', 'https://github.com/Zion-support/zion-sales-leadgen'),
            ('🔁 Discovery Handoff', 'Leads → agent marketplace (Batch 117) + implementation vault (Batch 121) + vertical trust (Batch 122).', 'https://ziontechgroup.com/sales-leadgen/', 'https://github.com/Zion-support/zion-sales-leadgen'),
        ],
        'discovery_h2': '🧭 Free Discovery — always online, always free',
        'discovery_p': 'Find every lead we\'ve already worked with — in your area — and turn them into booked work, without a single cold call. Your ranked lead list + enriched contacts + outreach draft are generated instantly and emailed to you and our commercial team (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Start Free Discovery',
        'discovery_cta2': 'Browse the App Network',
    },
    'pt': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-sales-leadgen-2026.html">English</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-sales-leadgen-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-sales-leadgen-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-sales-leadgen-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-sales-leadgen-2026-de.html">Deutsch</a></nav>',
        'title': 'Especialista de Vendas e Geração de Leads com IA — Encontre seus Melhores Leads — Zion Tech Group',
        'description': 'Hub gratuito de Especialista de Vendas e Geração de Leads com IA: varra o histórico de e-mails em busca de leads qualificados por localização, enriquece-os e transforma-os em trabalhos contratados — sem necessidade de chamado frio.',
        'h1': '🤖 Especialista de Vendas e Geração de Leads com IA',
        'pitch': 'Geração de leads sempre online: encontre todos os leads com quem já trabalhamos — na sua área, em seu idioma — e transforme-os em trabalhos contratados. Varra todas as etiquetas (mais antigas para as mais novas) em busca de solicitações de serviço e inquiry de técnicos, enriquece contatos e encaminha para CRM, outreach e marketplace de agentes. Para FE\'s & técnicos — prioridade.',
        'cards': [
            ('📧 Escanear Leads por Thread de E-mail', 'Varre todas as etiquetas (inbox + pastas, mais antigas para as mais novas) em busca de solicitações de serviço e inquiry de técnicos — classificados por valor comercial.', 'https://ziontechgroup.com/sales-leadgen/', 'https://github.com/Zion-support/zion-sales-leadgen'),
            ('📦 Enriquecimento de Leads', 'Adiciona contato + sinais de compra: localização, empresa, histórico de trabalho anterior, faixa de preço — pronto para CRM.', 'https://ziontechgroup.com/sales-leadgen/', 'https://github.com/Zion-support/zion-sales-leadgen'),
            ('🧾 Rascunho de Escrita de CRM', 'Rascunha um registro de contato HubSpot (nome, e-mail, fonte do lead, pontuação) para revisão da equipe comercial — sem entrada manual.', 'https://ziontechgroup.com/sales-leadgen/', 'https://github.com/Zion-support/zion-sales-leadgen'),
            ('💬 Rascunho de Outreach (personalizado)', 'Redige um rascunho de e-mail de vendas personalizado (commercial@ziontechgroup.com c/c) + um programa de lembretes de retorno.', 'https://ziontechgroup.com/sales-leadgen/', 'https://github.com/Zion-support/zion-sales-leadgen'),
            ('📊 Classificação e Cotas de Leads', 'Classifica leads por valor comercial; esconde a margem interna — mostra apenas a faixa de preço para o cliente na proposta.', 'https://ziontechgroup.com/sales-leadgen/', 'https://github.com/Zion-support/zion-sales-leadgen'),
            ('🔁 Mão de Obra de Descoberta', 'Leads → marketplace de agentes (Lote 117) + vault de implantação (Lote 121) + confiança vertical (Lote 122).', 'https://ziontechgroup.com/sales-leadgen/', 'https://github.com/Zion-support/zion-sales-leadgen'),
        ],
        'discovery_h2': '🧭 Descoberta Gratuita — sempre online, sempre gratuita',
        'discovery_p': 'Encontre todos os leads com quem já trabalhamos — na sua área, em seu idioma — e transforme-os em trabalhos contratados, sem um único chamado frio. Sua lista de leads classificada + contatos enriquecidos + rascunho de outreach são gerados instantaneamente e enviados por e-mail para você e nossa equipe comercial (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Iniciar Descoberta Gratuita',
        'discovery_cta2': 'Navegar pela Rede de Aplicativos',
    },
    'es': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-sales-leadgen-2026.html">English</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-sales-leadgen-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-sales-leadgen-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-sales-leadgen-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-sales-leadgen-2026-de.html">Deutsch</a></nav>',
        'title': 'Especialista de Ventas y Generación de Leads con IA — Encuentra tus Mejores Leads — Zion Tech Group',
        'description': 'Hub gratuito de Especialista de Ventas y Generación de Leads con IA: escanee el historial de correo electrónico en busca de leads calificados por ubicación, enriquezca los contactos y conviértalos en trabajos contratados — sin necesidad de llamadas frías.',
        'h1': '🤖 Especialista de Ventas y Generación de Leads con IA',
        'pitch': 'Generación de leads siempre online: encuentre todos los leads con los que ya trabajamos — en su área, en su idioma — y conviértalos en trabajos contratados. Escanee todas las etiquetas (de las más antiguas a las más nuevas) en busca de solicitudes de servicio y consultas de técnicos, enriquezca contactos y reenvíe al CRM, al outreach y al marketplace de agentes. Para FE\'s y técnicos — prioridad.',
        'cards': [
            ('📧 Escáner de Threads de Correo', 'Escanee todas las etiquetas (bandeja de entrada + carpetas, más antiguas primero) en busca de solicitudes de servicio y consultas de técnicos — clasificados por valor comercial.', 'https://ziontechgroup.com/sales-leadgen/', 'https://github.com/Zion-support/zion-sales-leadgen'),
            ('📦 Enriquecimiento de Leads', 'Agrega contacto + señales de compra: ubicación, empresa, historial de trabajo anterior, rango de precios — listo para CRM.', 'https://ziontechgroup.com/sales-leadgen/', 'https://github.com/Zion-support/zion-sales-leadgen'),
            ('🧾 Borrador de Escritura de CRM', 'Redacta un registro de contacto HubSpot (nombre, e-mail, fuente del lead, puntuación) para revisión del equipo comercial — sin entrada manual.', 'https://ziontechgroup.com/sales-leadgen/', 'https://github.com/Zion-support/zion-sales-leadgen'),
            ('💬 Borrador de Outreach (personalizado)', 'Redacta un borrador de correo de ventas personalizado (commercial@ziontechgroup.com c/c) + un programa de recordatorios de seguimiento.', 'https://ziontechgroup.com/sales-leadgen/', 'https://github.com/Zion-support/zion-sales-leadgen'),
            ('📊 Clasificación y Cotas de Leads', 'Clasifica los leads por valor comercial; oculta la margen interna — muestra solo el rango de precio para el cliente en la propuesta.', 'https://ziontechgroup.com/sales-leadgen/', 'https://github.com/Zion-support/zion-sales-leadgen'),
            ('🔁 Mano de Obra de Descubrimiento', 'Leads → marketplace de agentes (Lote 117) + vault de implementación (Lote 121) + confianza vertical (Lote 122).', 'https://ziontechgroup.com/sales-leadgen/', 'https://github.com/Zion-support/zion-sales-leadgen'),
        ],
        'discovery_h2': '🧭 Descubrimiento Gratuito — siempre en línea, siempre gratuito',
        'discovery_p': 'Encuentre todos los leads con los que ya trabajamos — en su área, en su idioma — y conviértalos en trabajos contratados, sin una sola llamada fría. Su lista de leads clasificada + contactos enriquecidos + borrador de outreach se generan instantáneamente y se envían por correo a usted y a nuestro equipo comercial (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Comenzar Descubrimiento Gratuito',
        'discovery_cta2': 'Explorar la Red de Aplicaciones',
    },
    'fr': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-sales-leadgen-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-sales-leadgen-2026-fr.html">Français</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-sales-leadgen-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-sales-leadgen-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-sales-leadgen-2026-de.html">Deutsch</a></nav>',
        'title': 'Specialiste des Ventes et des Leads IA — Trouvez vos Meilleurs Leads — Zion Tech Group',
        'description': 'Hub gratuit de spécialiste commercial et génération de leads IA : analysez l\'historique des e-mails pour trouver des leads qualifiés par localisation, enrichissez-les et transformez-les en travaux confirmés — sans appel téléphonique.',
        'h1': '🤖 Spécialiste des Ventes et des Leads IA',
        'pitch': 'Génération de leads toujours en ligne : trouvez tous les leads avec lesquels nous avons déjà travaillé — dans votre région, dans votre langue — et transformez-les en travaux confirmés. Analysez toutes les étiquettes (de la plus ancienne à la plus récente) en recherche de demandes de service et de nouvelles d\'techniciens, enrichissez les contacts et orientez vers le CRM, l\'outreach et le marketplace d\'agents. Pour FE\'s et techniciens — priorité.',
        'cards': [
            ('📧 Analyseur de Threads de E-mail', 'Analyse toutes les étiquettes (boîte de réception + dossiers, plus anciennes d\'abord) en recherche de demandes de service et de nouvelles de techniciens — classés par valeur commerciale.', 'https://ziontechgroup.com/sales-leadgen/', 'https://github.com/Zion-support/zion-sales-leadgen'),
            ('📦 Enrichissement de Leads', 'Ajoute le contact + les indications d\'achat : localisation, entreprise, historique de travaux antérieurs, gamme de prix — prêt pour le CRM.', 'https://ziontechgroup.com/sales-leadgen/', 'https://github.com/Zion-support/zion-sales-leadgen'),
            ('🧾 Brouillon d\'Écriture du CRM', 'Rédige un enregistrement de contact HubSpot (nom, e-mail, source du lead, score) pour révision du commercial — sans saisie manuelle.', 'https://ziontechgroup.com/sales-leadgen/', 'https://github.com/Zion-support/zion-sales-leadgen'),
            ('💬 Brouillon d\'Outreach (personnalisé)', 'Rédige un brouillon d\'e-mail commercial personnalisé (commercial@ziontechgroup.com c/c) + un programme de rappels de retour.', 'https://ziontechgroup.com/sales-leadgen/', 'https://github.com/Zion-support/zion-sales-leadgen'),
            ('📊 Classement et Plafonds de Leads', 'Classe les leads par valeur commerciale ; cache la marge interne — affiche seulement la gamme de prix pour le client dans la proposition.', 'https://ziontechgroup.com/sales-leadgen/', 'https://github.com/Zion-support/zion-sales-leadgen'),
            ('🔁 Main d\'œuvre de Découverte', 'Leads → marketplace d\'agents (Lot 117) + vault d\'implémentation (Lot 121) + confiance verticale (Lot 122).', 'https://ziontechgroup.com/sales-leadgen/', 'https://github.com/Zion-support/zion-sales-leadgen'),
        ],
        'discovery_h2': '🧭 Découverte Gratuite — toujours en ligne, toujours gratuite',
        'discovery_p': 'Trouvez tous les leads avec lesquels nous avons déjà travaillé — dans votre région, dans votre langue — et transformez-les en travaux confirmés, sans un seul appel téléphonique. Votre liste de leads classés + contacts étoilés + brouillon d\'outreach sont générés instantanément et envoyés par e-mail à vous et à notre équipe commerciale (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Commencer la Découverte Gratuite',
        'discovery_cta2': 'Parcourir le Réseau d\'Applications',
    },
    'de': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-sales-leadgen-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-sales-leadgen-2026-de.html">Deutsch</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-sales-leadgen-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-sales-leadgen-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-sales-leadgen-2026-fr.html">Français</a></nav>',
        'title': 'KI-Handel & Leads-Spezialist — Finden Sie Ihre Besten Leads — Zion Tech Group',
        'description': 'Kostenloser KI-Handel & Leads-Spezialist-Hub: durchsuchen Sie Ihre E-Mail-Geschichte nach qualifizierten Leads nach Standort, bereichern Sie diese und verwandeln Sie sie in gebuchte Arbeit — ohne Cold-Call.',
        'h1': '🤖 KI-Handel & Leads-Spezialist',
        'pitch': 'Immer online geführte Lead-Generierung: finden Sie alle Leads, mit denen wir bereits gearbeitet haben — in Ihrer Region, in Ihrer Sprache — und verwandeln Sie sie in gebuchte Arbeit. Durchsuchen Sie alle Labels (e-Mail-Posteingang + Ordner, älteste zuerst) nach Servicenotrufen und Technikeranfragen, bereichern Sie Kontakte und leiten Sie weiter zum CRM, zum Outbound und zum Agentenmarktplatz. Für FE\'s und Techniker — Priorität.',
        'cards': [
            ('📧 E-Mail-Thread-Led-Scanner', 'Durchsucht alle Labels (Posteingang + Ordner, ältest zuerst) nach Servicenotrufen und Technikern — nach kommerzieller Wertigkeit sortiert.', 'https://ziontechgroup.com/sales-leadgen/', 'https://github.com/Zion-support/zion-sales-leadgen'),
            ('📦 Leads-Anreicherung', 'Fügt Kontakt + Kaufimpulse hinzu: Standort, Firma, Vorlahauflists, Preisspanne — einsatzbereit für CRM.', 'https://ziontechgroup.com/sales-leadgen/', 'https://github.com/Zion-support/zion-sales-leadgen'),
            ('🧾 CRM-Schreibvorgang (Entwurf)', 'Erstellt einen HubSpot-Kontoeintrag (Name, E-Mail, Lead-Quelle, Score) für die Prüfung durch den Vertrieb — ohne manuelle Eingabe.', 'https://ziontechgroup.com/sales-leadgen/', 'https://github.com/Zion-support/zion-sales-leadgen'),
            ('💬 Outbound-Brust Entwurf', 'Schreibt einen personalisierten Cold-Email-Entwurf (commercial@ziontechgroup.com c/c) + ein Erinnerungsprogramm.', 'https://ziontechgroup.com/sales-leadgen/', 'https://github.com/Zion-support/zion-sales-leadgen'),
            ('📊 Leads-Ranking & Quoten', 'Sortiert Leads nach kommerzieller Wertigkeit; blendet die internen Markierungsrisiken aus — zeigt nur den Preissektor für das Kundenangebot.', 'https://ziontechgroup.com/sales-leadgen/', 'https://github.com/Zion-support/zion-sales-leadgen'),
            ('🔁 Entdeckungs-Handoff', 'Leads → Agenten-Marktplatz (Zahl 117) + Implementierungshaller (Zahl 121) + vertikale Anweisung (Zahl 122).', 'https://ziontechgroup.com/sales-leadgen/', 'https://github.com/Zion-support/zion-sales-leadgen'),
        ],
        'discovery_h2': '🧭 Kostenloser Entdeckung — immer online, immer kostenlos',
        'discovery_p': 'Finden Sie alle Leads, mit denen wir bereits gearbeitet haben — in Ihrer Region, in Ihrer Sprache — und verwandeln Sie sie in gebuchte Arbeit, ohne einen einzigen Cold-Call. Ihre klassifizierten Leads + angereicherte Kontakte + Outbound-Entwurf werden augenblicklich generiert und per E-Mail an Sie und unser Vertriebsteam (commercial@ziontechgroup.com) gesendet.',
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
    labels = ['📧 Email-Thread Lead Scanner', '📦 Lead Enrichment + CRM Write-Back', '💬 Outreach Draft + Follow-up', '🔁 Discovery Handoff']
    section_html = ''
    for grp, label in zip(cards_groups, labels):
        gh = ''.join(f'<div class="card"><h3>{h}</h3><p>{d}</p><a href="{live}">Live app →</a> · <a href="{repo}">Repo</a></div>' for h, d, live, repo in grp)
        section_html += f'<section><h2>{label}</h2><div class="cards">{gh}</div></section>'
    disc = f'<div class="disc"><h2>{body["discovery_h2"]}</h2><p>{body["discovery_p"]}</p><a class="cta green" href="https://ziontechgroup.com/discovery/">{body["discovery_cta1"]}</a><a class="cta alt" href="https://ziontechgroup.com/zion-app-network/">{body["discovery_cta2"]}</a></div>'
    closing = '<p style="margin-top:24px"><a href="https://ziontechgroup.com">← ziontechgroup.com</a> · <a href="https://github.com/Zion-support/zion-app-network/blob/main/SPOTLIGHT-sales-leadgen-2026.md">Spotlight doc</a> · <a href="https://github.com/Zion-support/zion-app-network/blob/main/APPS_INDEX-BATCH123-LEADGEN.md">Batch rollup</a></p>'
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
    path = os.path.join(WORK, f'app-network-sales-leadgen-2026{"-"+ext if ext else ""}.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("wrote", path, "len", len(content))
