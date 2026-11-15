import os

WORK = '/Users/miami2/.hermes/profiles/agent-finops-ops/cache/apphub'
os.makedirs(WORK, exist_ok=True)

BASE = 'https://ziontechgroup.com/zion-app-network/app'
CANON = f'{BASE}/app-network-ai-voice-omnichannel-2026.html'
L = {
    'pt': f'{BASE}/app-network-ai-voice-omnichannel-2026-pt.html',
    'es': f'{BASE}/app-network-ai-voice-omnichannel-2026-es.html',
    'fr': f'{BASE}/app-network-ai-voice-omnichannel-2026-fr.html',
    'de': f'{BASE}/app-network-ai-voice-omnichannel-2026-de.html',
}
LANGS = [('en', CANON), ('pt-BR', L['pt']), ('es', L['es']), ('fr', L['fr']), ('de', L['de'])]

BODY = {
    'en': {
        'langbar': '<nav class="langbar">🌐 <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-voice-omnichannel-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-voice-omnichannel-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-voice-omnichannel-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-voice-omnichannel-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-voice-omnichannel-2026-de.html">Deutsch</a></nav>',
        'title': 'AI Voice & Omnichannel Contact Center — 24/7 Voice + SMS + Chat + WhatsApp',
        'description': 'Free AI Voice & Omnichannel Contact Center hub: voice AI for inbound and outbound campaigns, knowledge-base-grounded answers, qualification, booking, and human handoff — phone, SMS, chat, WhatsApp, and WebRTC, in all five languages.',
        'h1': '🤖 AI Voice & Omnichannel Contact Center',
        'pitch': 'Every phone call — inbound or outbound — gets answered, qualified, and booked, 24/7, in every language we serve, with human handoff when it counts. Voice AI that runs phone + SMS + chat + WhatsApp + WebRTC end-to-end, answers from your knowledge base, writes outcomes to your CRM, and hot-transfers to live agents with full context. Built for Zion\'s client-facing service business.',
        'cards': [
            ('📞 Voice Agent', 'Answers inbound and runs outbound campaigns; qualifies against criteria on a deterministic flow; hot-transfers to a live rep with full call context.', 'https://ziontechgroup.com/ai-voice-omnichannel/', 'https://github.com/Zion-support/zion-ai-voice-omnichannel'),
            ('📱 Omnichannel Coverage', 'Phone, SMS, chat, WhatsApp, and WebRTC with native connectors (Twilio, Genesys, Amazon Connect, SIP trunking) and mid-conversation language switching.', 'https://ziontechgroup.com/ai-voice-omnichannel/', 'https://github.com/Zion-support/zion-ai-voice-omnichannel'),
            ('📚 Knowledge-Grounded Answers', 'Answers from the company\'s knowledge base, FAQ, and policy documents — no hallucination, fully grounded in your assets.', 'https://ziontechgroup.com/ai-voice-omnichannel/', 'https://github.com/Zion-support/zion-ai-voice-omnichannel'),
            ('🗣️ Speech-to-Text + Sentiment', 'Real-time transcription, call scoring, and sentiment analysis for QA and rep coaching.', 'https://ziontechgroup.com/ai-voice-omnichannel/', 'https://github.com/Zion-support/zion-ai-voice-omnichannel'),
            ('📅 Appointment & Lead Booking', 'Confirms, books, and routes qualified leads; writes outcomes to the CRM automatically.', 'https://ziontechgroup.com/ai-voice-omnichannel/', 'https://github.com/Zion-support/zion-ai-voice-omnichannel'),
            ('🙋 Human Handoff', 'Escalates complex cases to live agents with full conversation context, intent data, and a summary of the interaction.', 'https://ziontechgroup.com/ai-voice-omnichannel/', 'https://github.com/Zion-support/zion-ai-voice-omnichannel'),
        ],
        'discovery_h2': '🧭 Free Discovery — always online, always free',
        'discovery_p': 'Tell us your voice + omnichannel needs, and we\'ll plan, build, and configure your 24/7 voice agent — answers from your knowledge base, qualified leads booked, routine requests resolved, complex cases escalated with full context. Your plan is emailed to you and our commercial team (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Start Free Discovery',
        'discovery_cta2': 'Browse the App Network',
    },
    'pt': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-voice-omnichannel-2026.html">English</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-voice-omnichannel-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-voice-omnichannel-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-voice-omnichannel-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-voice-omnichannel-2026-de.html">Deutsch</a></nav>',
        'title': 'Agente de Contato por Voz & Omnichannel — Voz + SMS + Chat + WhatsApp — Zion Tech Group',
        'description': 'Hub gratuito de Agente de Contato por Voz & Omnichannel: voz AI para campanhas inbound e outbound, respostas fundamentadas em base de conhecimento, qualificação, agendamento e mão de mão humana — telefone, SMS, chat, WhatsApp e WebRTC, em todos os cinco idiomas.',
        'h1': '🤖 Agente de Contato por Voz & Omnichannel',
        'pitch': 'Todo chamado telefônico — inbound ou outbound — é atendido, qualificado e contratado, 24/7, em todos os idiomas que atendemos, com mão de mão humana quando conta. Voz AI que roda telefone + SMS + chat + WhatsApp + WebRTC em última instância, responde a partir da sua base de conhecimento, escreve resultados no CRM e transfere para agentes humanos com contexto completo. Feito para o negócio de serviço ao cliente da Zion.',
        'cards': [
            ('📞 Agente de Voz', 'Atende inbound e executa campanhas outbound; qualifica com base em critérios em um fluxo determinístico; transfere instantaneamente para um recrutador com contexto completo da chamada.', 'https://ziontechgroup.com/ai-voice-omnichannel/', 'https://github.com/Zion-support/zion-ai-voice-omnichannel'),
            ('📱 Cobertura Omnichannel', 'Telefone, SMS, chat, WhatsApp e WebRTC com conectores nativos (Twilio, Genesys, Amazon Connect, SIP trunking) e troca de língua durante a conversa.', 'https://ziontechgroup.com/ai-voice-omnichannel/', 'https://github.com/Zion-support/zion-ai-voice-omnichannel'),
            ('📚 Respostas com Base de Conhecimento', 'Responde a partir da base de conhecimento, FAQ e documentos de políticas da empresa — sem alucinação, totalmente fundamentado nos seus ativos.', 'https://ziontechgroup.com/ai-voice-omnichannel/', 'https://github.com/Zion-support/zion-ai-voice-omnichannel'),
            ('🗣️ Fala para Texto + Sentimento', 'Transcrição em tempo real, pontuação de chamadas e análise de sentimentos para QA e coach de recrutadores.', 'https://ziontechgroup.com/ai-voice-omnichannel/', 'https://github.com/Zion-support/zion-ai-voice-omnichannel'),
            ('📅 Agendamento de Visitas e Leads', 'Confirma, agenda e roteia Leads qualificados; escreve resultados automaticamente no CRM.', 'https://ziontechgroup.com/ai-voice-omnichannel/', 'https://github.com/Zion-support/zion-ai-voice-omnichannel'),
            ('🙋 Mão de Mão Humana', 'Escala casos complexos para agentes humanos com contexto completo da conversa, dados de intenção e resumo da interação.', 'https://ziontechgroup.com/ai-voice-omnichannel/', 'https://github.com/Zion-support/zion-ai-voice-omnichannel'),
        ],
        'discovery_h2': '🧭 Descoberta Gratuita — sempre online, sempre gratuita',
        'discovery_p': 'Conte-nos as suas necessidades de voz + omnicanal e nós planejamos, construímos e configuramos o seu agente de voz 24/7 — respostas a partir da sua base de conhecimento, Leads qualificados agendados, pedidos rotineiros resolvidos, casos complexos escalados com contexto completo. O seu plano é enviado por e-mail para você e nossa equipe comercial (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Iniciar Descoberta Gratuita',
        'discovery_cta2': 'Navegar pela Rede de Aplicativos',
    },
    'es': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-voice-omnichannel-2026.html">English</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-voice-omnichannel-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-voice-omnichannel-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-voice-omnichannel-2026-fr.html">Français</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-voice-omnichannel-2026-de.html">Deutsch</a></nav>',
        'title': 'Agente de Contacto por Voz y Omnicanal — Voz + SMS + Chat + WhatsApp — Zion Tech Group',
        'description': 'Hub gratuito de Agente de Contacto por Voz y Omnicanal: voz AI para campañas inbound y outbound, respuestas fundamentadas en base de conocimiento, calificación, agendamiento y mano de mano humana — teléfono, SMS, chat, WhatsApp y WebRTC, en los cinco idiomas.',
        'h1': '🤖 Agente de Contacto por Voz y Omnicanal',
        'pitch': 'Cada llamada telefónica — inbound o outbound — es atendida, calificada y contratada, 24/7, en todos los idiomas que atendemos, con mano de mana humana cuando cuenta. Voz AI que puede manejar teléfono + SMS + chat + WhatsApp + WebRTC en última instancia, responde desde tu base de conocimiento, escribe resultados en tu CRM y transfiere a agentes humanos con contexto completo. Hecho para el negocio de servicio al cliente de Zion.',
        'cards': [
            ('📞 Agente de Voz', 'Atiende inbound y ejecuta campañas outbound; califica según criterios en un flujo determinista; transfiere a un reclutador con contexto completo de la llamada.', 'https://ziontechgroup.com/ai-voice-omnichannel/', 'https://github.com/Zion-support/zion-ai-voice-omnichannel'),
            ('📱 Cobertura Omnichannel', 'Teléfono, SMS, chat, WhatsApp y WebRTC con conectores nativos (Twilio, Genesys, Amazon Connect, SIP trunking) y cambio de idioma durante la conversación.', 'https://ziontechgroup.com/ai-voice-omnichannel/', 'https://github.com/Zion-support/zion-ai-voice-omnichannel'),
            ('📚 Respuestas con Base de Conocimiento', 'Responde desde la base de conocimiento, FAQ y documentos de política de la empresa — sin alucinación, totalmente fundamentado en sus activos.', 'https://ziontechgroup.com/ai-voice-omnichannel/', 'https://github.com/Zion-support/zion-ai-voice-omnichannel'),
            ('🗣️ Voz a Texto + Sentimiento', 'Transcripción en tiempo real, puntuación de llamadas y análisis de sentimiento para QA y coach de reclutadores.', 'https://ziontechgroup.com/ai-voice-omnichannel/', 'https://github.com/Zion-support/zion-ai-voice-omnichannel'),
            ('📅 Agendamiento de Visitas y Leads', 'Confirma, agenda y enruta Leads calificados; escribe resultados automáticamente en el CRM.', 'https://ziontechgroup.com/ai-voice-omnichannel/', 'https://github.com/Zion-support/zion-ai-voice-omnichannel'),
            ('🙋 Mano de Mano Humana', 'Escala casos complejos a agentes humanos con contexto completo de la conversación, datos de intención y resumen de la interacción.', 'https://ziontechgroup.com/ai-voice-omnichannel/', 'https://github.com/Zion-support/zion-ai-voice-omnichannel'),
        ],
        'discovery_h2': '🧭 Descubrimiento Gratuito — siempre en línea, siempre gratuito',
        'discovery_p': 'Dígales sus necesidades de voz + omnicanal y nosotros planificamos, construimos y configuramos su agente de voz 24/7 — respuestas desde su base de conocimiento, Leads calificados agendados, pedidos rotineiros resueltos, casos complejos escalados con contexto completo. Su plan se envía por correo a usted y nuestro equipo comercial (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Comenzar Descubrimiento Gratuito',
        'discovery_cta2': 'Explorar la Red de Aplicaciones',
    },
    'fr': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-voice-omnichannel-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-voice-omnichannel-2026-fr.html">Français</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-voice-omnichannel-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-voice-omnichannel-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-voice-omnichannel-2026-de.html">Deutsch</a></nav>',
        'title': 'Agent de Contact voix et Omnicanal — Voi + SMS + Chat + WhatsApp — Zion Tech Group',
        'description': 'Hub gratuit de Agent de Contact voix et Omnicanal : voix IA pour campagnes inbound et outbound, réponses fondées sur la base de connaissances, qualification, réservation et main d\'ouvrière, téléphone, SMS, chat, WhatsApp et WebRTC, dans les cinq langues.',
        'h1': '🤖 Agent de Contact voix et Omnicanal',
        'pitch': 'Chaque appel téléphonique — entrant ou sortant — est répondu, qualifié et confirmé, 24h/24, 7j/7, dans toutes les langues que nous desservons, avec une main d\'ouvrière humaine quand cela compte. Voix IA qui peut gérer téléphone + SMS + chat + WhatsApp + WebRTC en bout en bout, répond depuis votre base de connaissances, écrit les résultats dans votre CRM et transfère en direct aux agents avec le contexte complet. Conçu pour le business de services à la clientèle de Zion.',
        'cards': [
            ('📞 Agent Voix', 'Répond aux appels entrants et exécute des campagnes sortantes ; qualifie selon des critères dans un flux déterministe ; transfère en direct à un recruteur avec le contexte de la conversation.', 'https://ziontechgroup.com/ai-voice-omnichannel/', 'https://github.com/Zion-support/zion-ai-voice-omnichannel'),
            ('📱 Couverture Omnicanale', 'Téléphone, SMS, chat, WhatsApp et WebRTC avec connecteurs natifs (Twilio, Genesys, Amazon Connect, SIP trunking) et changement de langue en pleine conversation.', 'https://ziontechgroup.com/ai-voice-omnichannel/', 'https://github.com/Zion-support/zion-ai-voice-omnichannel'),
            ('📚 Réponses avec Base de Connaissances', 'Répond depuis la base de connaissances, FAQ et documents de politique de l\'entreprise — sans hallucination, entièrement fondé sur vos actifs.', 'https://ziontechgroup.com/ai-voice-omnichannel/', 'https://github.com/Zion-support/zion-ai-voice-omnichannel'),
            ('🗣️ Reconnaissance Vocale + Sentiment', 'Transcription en temps réel, notation des appels et analyse de sentiment pour la QC et le coaching des recruteurs.', 'https://ziontechgroup.com/ai-voice-omnichannel/', 'https://github.com/Zion-support/zion-ai-voice-omnichannel'),
            ('📅 Réservation de Visites et Leads', 'Confirme, planifie et oriente les Leads qualifiés ; écrit les résultats automatiquement dans le CRM.', 'https://ziontechgroup.com/ai-voice-omnichannel/', 'https://github.com/Zion-support/zion-ai-voice-omnichannel'),
            ('🙋 Main d\'ouvrière Humaine', 'Escalade les cas complexes vers des agents humains avec le contexte complet de la conversation, les données d\'intention et un résumé de l\'interaction.', 'https://ziontechgroup.com/ai-voice-omnichannel/', 'https://github.com/Zion-support/zion-ai-voice-omnichannel'),
        ],
        'discovery_h2': '🧭 Découverte Gratuite — toujours en ligne, toujours gratuite',
        'discovery_p': 'Dites-nous vos besoins voix + omnicanal et nous planifions, construisons et configurons votre agent voix 24/7 — réponses depuis votre base de connaissances, Leads qualifiés confirmés, demandes rotatives résolues, cas complexes escaladés avec contexte complet. Votre plan est envoyé par e-mail à vous et à notre équipe commerciale (commercial@ziontechgroup.com).',
        'discovery_cta1': 'Commencer la Découverte Gratuite',
        'discovery_cta2': 'Parcourir le Réseau d\'Applications',
    },
    'de': {
        'langbar': '<nav class="langbar">🌐 <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-voice-omnichannel-2026.html">English</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-voice-omnichannel-2026-de.html">Deutsch</a> · <a class="active" href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-voice-omnichannel-2026-pt.html">Português</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-voice-omnichannel-2026-es.html">Español</a> · <a href="https://ziontechgroup.com/zion-app-network/app/app-network-ai-voice-omnichannel-2026-fr.html">Français</a></nav>',
        'title': 'KI-Voice- & Omnichannel-Kundenstützung — 24/7 Vot + SMS + Chat + WhatsApp — Zion Tech Group',
        'description': 'Kostenloser KI-Voice- & Omnichannel-Kundenstützungs-HuB: Vot-AI für eingehende und ausgehende Kampagnen, auf Wissensbasis basierende Antworten, Qualifizierung, Buchung und menschliche Handoff-Übergabe — Telefon, SMS, Chat, WhatsApp und WebRTC, in allen fünf Sprachen.',
        'h1': '🤖 KI-Voice- & Omnichannel-Kundenstützung',
        'pitch': 'Jeder Telefonanruf — eingehend oder ausgehend — wird 24/7, in allen Sprachen, die wir bedienen, befristet, qualifiziert und gebucht, mit menschlicher Handoff-Übergabe, wenn es zählt. Voice AI, das Telefon + SMS + Chat + WhatsApp + WebRTC zuständig ausführt, auf Ihrer Wissensbasis antwortet, Ergebnisse in Ihrem CRM schreibt und an lebendige Agenten mit vollständigem Kontext weiterleitet. Für Zion\'s Kundenstützungsgeschäft gebaut.',
        'cards': [
            ('📞 Voice-Agent', 'Beantwortet eingehende Anrufe und führt ausgehende Kampagnen; qualifiziert anhand von Kriterien in einem deterministischen Ablauf; übergibt an einen Recruiter mit vollständigem Kontext des Anrufs.', 'https://ziontechgroup.com/ai-voice-omnichannel/', 'https://github.com/Zion-support/zion-ai-voice-omnichannel'),
            ('📱 Omnichannel-Bedeckung', 'Telefon, SMS, Chat, WhatsApp und WebRTC mit nativem Anschluss (Twilio, Genesys, Amazon Connect, SIP-Truhe) und Sprachumschaltung während des Gesprächs.', 'https://ziontechgroup.com/ai-voice-omnichannel/', 'https://github.com/Zion-support/zion-ai-voice-omnichannel'),
            ('📚 Wissensbasierte Antworten', 'Antworten auf Basis der Wissensbasis, FAQ und Richtlinien des Unternehmens — keine Halluzinationen, vollständig auf Ihren Assets fundiert.', 'https://ziontechgroup.com/ai-voice-omnichannel/', 'https://github.com/Zion-support/zion-ai-voice-omnichannel'),
            ('🗣️ Speech-to-Text + Sentiment', 'Echtzeit-Transkription, Anrufbewertung und Sentimentsanalyse für QC und Agent-Coaching.', 'https://ziontechgroup.com/ai-voice-omnichannel/', 'https://github.com/Zion-support/zion-ai-voice-omnichannel'),
            ('📅 Termin- und Lead-Buchung', 'Bestätigt, bucht und leitet qualifizierte Leads weiter; schreibt Ergebnisse automatisch in das CRM.', 'https://ziontechgroup.com/ai-voice-omnichannel/', 'https://github.com/Zion-support/zion-ai-voice-omnichannel'),
            ('🙋 Menschliche Handoff-Übergabe', 'Eskaliert komplexe Fälle an lebendige Agenten mit vollständigem Gesprächskontext, Intent-Daten und Zusammenfassung der Interaktion.', 'https://ziontechgroup.com/ai-voice-omnichannel/', 'https://github.com/Zion-support/zion-ai-voice-omnichannel'),
        ],
        'discovery_h2': '🧭 Kostenloser Entdeckung — immer online, immer kostenlos',
        'discovery_p': 'Erzählen Sie uns Ihre Voice- und Omnichannel-Bedürfnisse, und wir planen, bauen und konfigurieren Ihre 24/7-Voice-Agenten — Antworten aus Ihrer Wissensbasis, qualifizierte Leads gebucht, routinemäßige Anfragen gelöst, komplexe Fälle mit vollständigem Kontext an Ihr Team eskaliert. Ihr Plan wird per E-Mail an Sie und unser Vertriebsteam (commercial@ziontechgroup.com) gesendet.',
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
    labels = ['📞 Voice Agent', '📱 Omnichannel Coverage', '📚 Knowledge-Grounded Answers', '🗣️ Speech-to-Text + Sentiment', '📅 Appointment & Lead Booking', '🙋 Human Handoff']
    section_html = ''
    for grp, label in zip(cards_groups, labels):
        gh = ''.join(f'<div class="card"><h3>{h}</h3><p>{d}</p><a href="{live}">Live app →</a> · <a href="{repo}">Repo</a></div>' for h, d, live, repo in grp)
        section_html += f'<section><h2>{label}</h2><div class="cards">{gh}</div></section>'
    disc = f'<div class="disc"><h2>{body["discovery_h2"]}</h2><p>{body["discovery_p"]}</p><a class="cta green" href="https://ziontechgroup.com/discovery/">{body["discovery_cta1"]}</a><a class="cta alt" href="https://ziontechgroup.com/zion-app-network/">{body["discovery_cta2"]}</a></div>'
    closing = '<p style="margin-top:24px"><a href="https://ziontechgroup.com">← ziontechgroup.com</a> · <a href="https://github.com/Zion-support/zion-app-network/blob/main/SPOTLIGHT-ai-voice-omnichannel-2026.md">Spotlight doc</a> · <a href="https://github.com/Zion-support/zion-app-network/blob/main/APPS_INDEX-BATCH131-VOICE.md">Batch rollup</a></p>'
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
    path = os.path.join(WORK, f'app-network-ai-voice-omnichannel-2026{"-"+ext if ext else ""}.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("wrote", path, "len", len(content))
