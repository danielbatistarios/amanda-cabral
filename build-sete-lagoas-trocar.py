#!/usr/bin/env python3
"""
Build script: sete-lagoas-mg/trocar-de-contador/index.html
Template: para-de-minas-mg/trocar-de-contador/index.html
"""

import os

TEMPLATE   = "para-de-minas-mg/trocar-de-contador/index.html"
OUTPUT_DIR = "sete-lagoas-mg/trocar-de-contador"
OUTPUT     = os.path.join(OUTPUT_DIR, "index.html")

# ── GEO + IDs ──────────────────────────────────────────────────────────────
GEO_LAT     = "-19.4656"
GEO_LNG     = "-44.2467"
WIKIDATA_ID = "Q1059948"
CIDADE      = "Sete Lagoas"
CIDADE_SLUG = "sete-lagoas-mg"

# ── METAS ──────────────────────────────────────────────────────────────────
PAGE_URL   = f"https://amcabralblindagem.com.br/{CIDADE_SLUG}/trocar-de-contador/"
TITLE      = "Trocar de Contador em Sete Lagoas: Como Fazer Sem Risco | AM Cabral"   # 65 chars
META_DESC  = "Trocar de contador em Sete Lagoas com transição segura e documentada. TTRT, e-CAC, eSocial e SPED assumidos em 48h. Sem risco fiscal. AM Cabral."
OG_TITLE   = "Trocar de Contador em Sete Lagoas | AM Cabral Contabilidade"
OG_DESC    = "Troca de contador em Sete Lagoas com transição segura. Sem risco fiscal, sem perda de arquivos. AM Cabral assume seu escritório em 48h."

# ── HERO ───────────────────────────────────────────────────────────────────
HERO_TAG  = "Troca de Contador · Sete Lagoas · Sem Risco"
H1        = "Trocar de Contador em<br>Sete Lagoas <em>sem complicação</em>"
HERO_SUB  = "Assumimos toda a documentação, os SPEDs e as credenciais fiscais em até 48 horas. Você não precisa se preocupar com o processo de transição."

# ── CRED STRIP ─────────────────────────────────────────────────────────────
CRED_ITEM_20ANOS = '<div class="cred-item"><div class="cred-dot"></div><strong>30 anos</strong> atendendo empresas em Minas Gerais</div>'

# ── NUMBERS ────────────────────────────────────────────────────────────────
NUM_LABEL_3 = "atendendo empresas em Sete Lagoas"

# ── AUTHORITY SECTION ──────────────────────────────────────────────────────
AUTH_P1 = ("Em Sete Lagoas, como em qualquer cidade do interior, existe um fenômeno comum: o empresário está insatisfeito com o contador há anos, mas não troca porque tem medo do que pode acontecer na transição. "
           "Isso é compreensível. O escritório contábil guarda documentos, credenciais fiscais, arquivos SPED e o acesso ao e-CAC e ao eSocial. "
           "Uma troca mal feita pode gerar obrigações em duplicidade, lacunas no SPED ou até perda de documentação histórica.")

AUTH_P2 = ("Mas o maior risco é outro: continuar com um contador que não entrega. "
           "Cada mês com entrega atrasada é uma oportunidade de autuação. "
           "Cada SPED com erro acumulado é um passivo que cresce silenciosamente. "
           "Cada declaração entregue no automático, sem planejamento, é imposto pago a mais. "
           "A troca de contador, quando conduzida por um profissional experiente, é um processo seguro, documentado e com prazo definido. "
           "A AM Cabral fez isso dezenas de vezes em Sete Lagoas e região.")

# ── AMANDA CTA STRIP ───────────────────────────────────────────────────────
AMANDA_IMG_ALT   = "Amanda Cabral, contadora em Sete Lagoas, apoio completo na troca de contador"
AMANDA_H2        = "30 anos de atuação em MG. Você não precisa começar do zero."
AMANDA_P         = ("Amanda Cabral conhece o tecido empresarial de Sete Lagoas e da região. "
                    "A transição é conduzida por quem já passou por dezenas de casos iguais ao seu, "
                    "incluindo situações onde o contador anterior dificultou a entrega dos documentos.")
AMANDA_BADGE_VAL = "30 anos"
AMANDA_BADGE_SUB = "atendendo empresas em MG"

# ── DEPOIMENTOS ────────────────────────────────────────────────────────────
DEP1_TEXT = ('"Passei dois anos desconfortável com meu contador mas sem coragem de trocar. '
             'A Amanda explicou cada etapa antes de começar, assumiu tudo em quatro dias e não tive nem uma intimação no processo. Deveria ter feito isso antes."')
DEP1_INIT = "JL"
DEP1_NOME = "J. Lima"
DEP1_ROLE = "S&#243;cio, Distribuidora em Sete Lagoas"

DEP2_TEXT = ('"O contador anterior estava entregando o Simples fora do prazo há meses. '
             'Quando a Amanda auditou os últimos dois anos encontrou créditos que ele nunca tinha aproveitado. '
             'A transição foi rápida e o escritório assumiu tudo sem interrupção."')
DEP2_INIT = "CS"
DEP2_NOME = "C. Souza"
DEP2_ROLE = "Propriet&#225;ria, Com&#233;rcio Varejista, Sete Lagoas"

DEP3_TEXT = ('"Achei que trocar de contador ia virar um problema enorme. '
             'A AM Cabral cuidou de toda a parte do e-CAC, do eSocial e dos arquivos históricos. '
             'Em menos de uma semana estava tudo regularizado e eu nem precisei falar com o contador anterior."')
DEP3_INIT = "RB"
DEP3_NOME = "R. Borges"
DEP3_ROLE = "Empres&#225;rio, Prestadora de Servi&#231;os, Sete Lagoas"

# ── FAQ ────────────────────────────────────────────────────────────────────
FAQ_H2 = "Dúvidas sobre trocar de contador em Sete Lagoas"
FAQ_ANS_20ANOS = ("A entrega de documentos e arquivos digitais é obrigação legal do contador. "
                  "Se houver resistência, orientamos como solicitar formalmente e, se necessário, como acionar o CRC/MG. "
                  "Em 30 anos de atuação em Minas Gerais, já gerenciamos dezenas de transições, "
                  "incluindo casos com conflito, e sempre conseguimos assumir sem ruptura.")

# ── PROCESSO H2 ────────────────────────────────────────────────────────────
PROC_H2 = "Como funciona a troca de contador em Sete Lagoas: 4 etapas com suporte total"

# ── CONTEXT_LOCAL (content-seo blocks) ────────────────────────────────────
NEW_CONTENT_BLOCK = """        <div class="content-block reveal">
          <h3>Por que tantos empresários de Sete Lagoas adiam a troca de contador?</h3>
          <p>Sete Lagoas cresceu em torno do comércio varejista e dos serviços especializados que atendem uma população de quase trezentos mil habitantes. Concessionárias, clínicas, escritórios de advocacia, academias e redes de alimentação formam o tecido empresarial que sustenta a arrecadação municipal. Para esses empresários, a relação com o contador costuma durar décadas e raramente é questionada enquanto o negócio funciona. O problema aparece quando alguém de fora revisa as declarações e encontra créditos tributários não aproveitados no Simples Nacional, enquadramentos de atividade em códigos CNAE que elevam a alíquota desnecessariamente, ou distribuição de lucros feita sem o laudo que protege o sócio.</p>
        </div>
        <div class="content-block reveal">
          <h3>O lado humano da transição: como conduzimos a ruptura sem constrangimento</h3>
          <p>Em cidades do interior de Minas, o contador frequentemente conhece a família, esteve presente na abertura da empresa e participou de decisões importantes. Encerrar esse vínculo gera desconforto que muitos empresários adiam por anos, mesmo quando os sinais de ineficiência já são claros. A AM Cabral entende esse lado humano da transição e conduz o processo de forma discreta, com respeito ao relacionamento anterior e sem criar constrangimento com o profissional que sai.</p>
        </div>
        <div class="content-block reveal">
          <h3>O que é o TTRT e por que ele protege você durante a troca</h3>
          <p>O Termo de Transferência de Responsabilidade Técnica é o documento formal que delimita até quando o contador anterior responde pelas obrigações da empresa. Sem o TTRT registrado no CRC/MG, a responsabilidade técnica permanece indefinida, o que pode prejudicar você em caso de autuação sobre período anterior. A AM Cabral emite e registra o TTRT como primeira etapa do processo, garantindo que a linha de responsabilidade fique clara antes de qualquer movimento nas credenciais fiscais.</p>
        </div>
        <div class="content-block reveal">
          <h3>Credenciais no e-CAC: como transferimos o acesso sem risco de duplicidade</h3>
          <p>Do ponto de vista técnico, a migração exige a retirada das credenciais de acesso ao e-CAC, a transferência do livro caixa e das guias já pagas, e a conferência dos prazos das declarações em aberto. Assumimos as credenciais de acesso ao eSocial, SPED e Receita Federal e fazemos a substituição do responsável técnico junto aos órgãos. A reunião inicial acontece presencialmente na sede em Pará de Minas ou por chamada de vídeo, no horário mais conveniente para você.</p>
        </div>"""

# ── HUB LINKS ──────────────────────────────────────────────────────────────
HUB_FABRICAS_HREF  = f"/{CIDADE_SLUG}/contador-para-fabricas-e-industrias/"
HUB_HOLDING_HREF   = f"/{CIDADE_SLUG}/contador-especializado-em-holding/"

# ── FOOTER CITY COL ────────────────────────────────────────────────────────
FOOTER_CITY_COL = f"""        <div class="footer-col">
          <div class="footer-heading">Sete Lagoas</div>
          <ul>
            <li><a href="/{CIDADE_SLUG}/">Escritório em Sete Lagoas</a></li>
            <li><a href="/{CIDADE_SLUG}/escritorio-de-contabilidade-sete-lagoas/">Escritório de Contabilidade</a></li>
            <li><a href="/{CIDADE_SLUG}/contador-especializado-em-holding/">Holding em Sete Lagoas</a></li>
            <li><a href="/{CIDADE_SLUG}/contador-para-fabricas-e-industrias/">Contador para Fábricas</a></li>
            <li><a href="/cidades-atendidas/">Cidades Atendidas</a></li>
          </ul>
        </div>"""

# ── SCHEMA: areaServed ─────────────────────────────────────────────────────
AREA_SERVED = """[
          {"@type": "City", "name": "Sete Lagoas", "sameAs": "https://www.wikidata.org/wiki/Q1059948"},
          {"@type": "City", "name": "Matozinhos", "sameAs": "https://www.wikidata.org/wiki/Q2587979"},
          {"@type": "City", "name": "Pedro Leopoldo", "sameAs": "https://www.wikidata.org/wiki/Q2008862"},
          {"@type": "City", "name": "Prudente de Morais", "sameAs": "https://www.wikidata.org/wiki/Q2074064"},
          {"@type": "City", "name": "Paraopeba", "sameAs": "https://www.wikidata.org/wiki/Q2580893"},
          {"@type": "City", "name": "Cordisburgo", "sameAs": "https://www.wikidata.org/wiki/Q2581267"},
          {"@type": "City", "name": "Jequitibá", "sameAs": "https://www.wikidata.org/wiki/Q1729283"},
          {"@type": "City", "name": "Belo Horizonte", "sameAs": "https://www.wikidata.org/wiki/Q35310"},
          {"@type": "State", "name": "Minas Gerais"}
        ]"""

# ── SCHEMA: Service node ───────────────────────────────────────────────────
SERVICE_SCHEMA = f"""      {{
        "@type": "Service",
        "@id": "{PAGE_URL}#service",
        "name": "Troca de Contador em Sete Lagoas",
        "serviceType": "Transição Contábil",
        "provider": {{"@id": "https://amcabralblindagem.com.br/#organization"}},
        "description": "Transição contábil segura para empresas de Sete Lagoas. Assumimos toda a documentação, SPEDs e obrigações acessórias sem risco fiscal e sem interrupção.",
        "areaServed": {{"@type": "City", "name": "Sete Lagoas", "sameAs": "https://www.wikidata.org/wiki/Q1059948"}},
        "url": "{PAGE_URL}"
      }}"""

# ===========================================================================
# BUILD
# ===========================================================================

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(TEMPLATE, "r", encoding="utf-8") as f:
    html = f.read()

# 1. TITLE tag
html = html.replace(
    "<title>Trocar de Contador em Pará de Minas: Como Fazer Sem Risco | AM Cabral</title>",
    f"<title>{TITLE}</title>"
)

# 2. META description
html = html.replace(
    'content="Trocar de contador em Pará de Minas com transição segura e documentada. TTRT, e-CAC, eSocial e SPED assumidos em 48h. Sem risco fiscal, sem penalidade. AM Cabral."',
    f'content="{META_DESC}"'
)

# 3. OG title
html = html.replace(
    'content="Trocar de Contador em Pará de Minas | AM Cabral Contabilidade"',
    f'content="{OG_TITLE}"'
)

# 4. OG description
html = html.replace(
    'content="Troca de contador em Pará de Minas com transição segura. Sem risco fiscal, sem perda de arquivos. AM Cabral assume seu escritório em 48h."',
    f'content="{OG_DESC}"'
)

# 5. OG URL + canonical
html = html.replace(
    'content="https://amcabralblindagem.com.br/para-de-minas-mg/trocar-de-contador/"',
    f'content="{PAGE_URL}"'
)
html = html.replace(
    'href="https://amcabralblindagem.com.br/para-de-minas-mg/trocar-de-contador/"',
    f'href="{PAGE_URL}"'
)

# 6. Schema: AccountingService addressLocality
html = html.replace(
    '"addressLocality": "Pará de Minas",',
    '"addressLocality": "Sete Lagoas",'
)

# 7. Schema: areaServed (AccountingService block)
html = html.replace(
    '''[
          {"@type": "City", "name": "Pará de Minas", "sameAs": "https://www.wikidata.org/wiki/Q1749821"},
          {"@type": "City", "name": "Itaúna", "sameAs": "https://www.wikidata.org/wiki/Q1754793"},
          {"@type": "City", "name": "Divinópolis", "sameAs": "https://www.wikidata.org/wiki/Q193289"},
          {"@type": "City", "name": "Betim", "sameAs": "https://www.wikidata.org/wiki/Q182277"},
          {"@type": "City", "name": "Sete Lagoas", "sameAs": "https://www.wikidata.org/wiki/Q1059948"},
          {"@type": "City", "name": "Contagem", "sameAs": "https://www.wikidata.org/wiki/Q732468"},
          {"@type": "City", "name": "Belo Horizonte", "sameAs": "https://www.wikidata.org/wiki/Q35310"},
          {"@type": "State", "name": "Minas Gerais"}
        ]''',
    AREA_SERVED
)

# 8. Schema: geo coordinates
html = html.replace(
    '"latitude": -19.8607,\n          "longitude": -44.6126',
    f'"latitude": {GEO_LAT},\n          "longitude": {GEO_LNG}'
)

# 9. Schema: WebPage @id and url
html = html.replace(
    '"@id": "https://amcabralblindagem.com.br/para-de-minas-mg/trocar-de-contador/#webpage"',
    f'"@id": "{PAGE_URL}#webpage"'
)
html = html.replace(
    '"url": "https://amcabralblindagem.com.br/para-de-minas-mg/trocar-de-contador/"',
    f'"url": "{PAGE_URL}"'
)
html = html.replace(
    '"about": {"@id": "https://amcabralblindagem.com.br/para-de-minas-mg/trocar-de-contador/#service"}',
    f'"about": {{"@id": "{PAGE_URL}#service"}}'
)

# 10. Schema: WebPage name
html = html.replace(
    '"name": "Trocar de Contador em Pará de Minas | AM Cabral"',
    f'"name": "{OG_TITLE}"'
)

# 11. Schema: BreadcrumbList
html = html.replace(
    '{"@type": "ListItem", "position": 2, "name": "Pará de Minas", "item": "https://amcabralblindagem.com.br/para-de-minas-mg/"}',
    f'{{"@type": "ListItem", "position": 2, "name": "Sete Lagoas", "item": "https://amcabralblindagem.com.br/{CIDADE_SLUG}/"}}'
)
html = html.replace(
    '{"@type": "ListItem", "position": 3, "name": "Trocar de Contador", "item": "https://amcabralblindagem.com.br/para-de-minas-mg/trocar-de-contador/"}',
    f'{{"@type": "ListItem", "position": 3, "name": "Trocar de Contador", "item": "{PAGE_URL}"}}'
)

# 12. Schema: Service @id and url
html = html.replace(
    '"@id": "https://amcabralblindagem.com.br/para-de-minas-mg/trocar-de-contador/#service"',
    f'"@id": "{PAGE_URL}#service"'
)

# 13. Schema: FAQ answer with "20 anos de atuação em Pará de Minas"
html = html.replace(
    'Em 20 anos de atuação em Pará de Minas, já gerenciamos dezenas de transições, incluindo casos com conflito, e sempre conseguimos assumir sem ruptura.',
    'Em 30 anos de atuação em Minas Gerais, já gerenciamos dezenas de transições, incluindo casos com conflito, e sempre conseguimos assumir sem ruptura.'
)

# 14. Schema: WebSite description
html = html.replace(
    '"description": "Contabilidade especializada para empresários em Pará de Minas e região de Minas Gerais."',
    '"description": "Contabilidade especializada para empresários em Sete Lagoas e região de Minas Gerais."'
)

# 15. Header mega-menu span
html = html.replace(
    '<strong>Cidades Atendidas</strong><span>Atendimento presencial em Pará de Minas e toda a região de MG</span>',
    '<strong>Cidades Atendidas</strong><span>Atendimento presencial em Minas Gerais e toda a região de MG</span>'
)

# 16. HERO TAG
html = html.replace(
    '<div class="hero-tag">Troca de Contador · Pará de Minas · Sem Risco</div>',
    f'<div class="hero-tag">{HERO_TAG}</div>'
)

# 17. H1
html = html.replace(
    '<h1>Trocar de Contador em<br>Pará de Minas <em>sem complicação</em></h1>',
    f'<h1>{H1}</h1>'
)

# 18. CRED STRIP: 20 anos em Pará de Minas
html = html.replace(
    '<div class="cred-item"><div class="cred-dot"></div><strong>20 anos</strong> em Pará de Minas</div>',
    CRED_ITEM_20ANOS
)

# 19. BREADCRUMB
html = html.replace(
    '<a href="/para-de-minas-mg/">Pará de Minas</a>',
    f'<a href="/{CIDADE_SLUG}/">Sete Lagoas</a>'
)

# 20. AUTHORITY paragraphs
html = html.replace(
    'Em Pará de Minas, como em qualquer cidade do interior, existe um fenômeno comum: o empresário está insatisfeito com o contador há anos, mas não troca porque tem medo do que pode acontecer na transição. Isso é compreensível. O escritório contábil guarda documentos, credenciais fiscais, arquivos SPED e o acesso ao e-CAC e ao eSocial. Uma troca mal feita pode gerar obrigações em duplicidade, lacunas no SPED ou até perda de documentação histórica.',
    AUTH_P1
)
html = html.replace(
    'Mas o maior risco é outro: continuar com um contador que não entrega. Cada mês com entrega atrasada é uma oportunidade de autuação. Cada SPED com erro acumulado é um passivo que cresce silenciosamente. Cada declaração entregue no automático, sem planejamento, é imposto pago a mais. A troca de contador, quando conduzida por um profissional experiente, é um processo seguro, documentado e com prazo definido. A AM Cabral fez isso dezenas de vezes em Pará de Minas e região.',
    AUTH_P2
)

# 21. NUMBERS label
html = html.replace(
    '<div class="num-label">atendendo empresas em Pará de Minas</div>',
    f'<div class="num-label">{NUM_LABEL_3}</div>'
)

# 22. PROCESSO H2
html = html.replace(
    'Como funciona a troca de contador em Pará de Minas: 4 etapas com suporte total',
    PROC_H2
)

# 23. AMANDA CTA STRIP
html = html.replace(
    'src="/para-de-minas-mg/escritorio-de-contabilidade/assets/amanda-cabral-contadora-cta-strip.jpg" alt="Amanda Cabral, contadora em Pará de Minas, apoio completo na troca de contador"',
    f'src="/sete-lagoas-mg/sete-lagoas-lagoa-paulino.webp" alt="{AMANDA_IMG_ALT}"'
)
html = html.replace(
    '<h2>20 anos em Pará de Minas. Você não precisa começar do zero.</h2>',
    f'<h2>{AMANDA_H2}</h2>'
)
html = html.replace(
    'Amanda Cabral conhece o tecido empresarial de Pará de Minas e da região. A transição é conduzida por quem já passou por dezenas de casos iguais ao seu, incluindo situações onde o contador anterior dificultou a entrega dos documentos.',
    AMANDA_P
)
html = html.replace(
    '<strong>20 anos</strong>\n        <span>em Pará de Minas</span>',
    f'<strong>{AMANDA_BADGE_VAL}</strong>\n        <span>{AMANDA_BADGE_SUB}</span>'
)

# 24. DEPOIMENTOS
html = html.replace(
    '"Passei dois anos desconfortável com meu contador mas sem coragem de trocar. A Amanda explicou cada etapa antes de começar, assumiu tudo em quatro dias e não tive nem uma intimação no processo. Deveria ter feito isso antes."',
    DEP1_TEXT
)
# dep1 avatar already "JL" in template — keep; name/role differ
html = html.replace(
    '<strong>J. Lima</strong>',
    f'<strong>{DEP1_NOME}</strong>'
)
html = html.replace(
    '<span>S&#243;cio, Distribuidora em Pará de Minas</span>',
    f'<span>{DEP1_ROLE}</span>'
)

html = html.replace(
    '"O contador anterior estava entregando o Simples fora do prazo há meses. Quando a Amanda auditou os últimos dois anos encontrou créditos que ele nunca tinha aproveitado. A transição foi rápida e o escritório assumiu tudo sem interrupção."',
    DEP2_TEXT
)
html = html.replace(
    '<span>Propriet&#225;ria, Comércio Varejista</span>',
    f'<span>{DEP2_ROLE}</span>'
)

html = html.replace(
    '"Achei que trocar de contador ia virar um problema enorme. A AM Cabral cuidou de toda a parte do e-CAC, do eSocial e dos arquivos históricos. Em menos de uma semana estava tudo regularizado e eu nem precisei falar com o contador anterior."',
    DEP3_TEXT
)
html = html.replace(
    '<span>Empres&#225;rio, Prestadora de Serviços</span>',
    f'<span>{DEP3_ROLE}</span>'
)

# 25. CONTENT SEO blocks (4 blocks)
old_content_block = """        <div class="content-block reveal">
          <h3>Quando você pode trocar de contador</h3>
          <p>Não existe impedimento legal para trocar de contador em qualquer mês do ano. A recomendação prática é evitar os meses de entrega de obrigações anuais (janeiro a abril), quando o contador anterior ainda tem responsabilidade sobre as declarações do exercício anterior. Fora esse período, a transição pode ser iniciada e concluída em menos de uma semana.</p>
        </div>
        <div class="content-block reveal">
          <h3>O que acontece com as declarações anteriores</h3>
          <p>As declarações entregues pelo contador anterior continuam sob a responsabilidade dele até o registro do TTRT. Após a transferência, a AM Cabral revisa todas as obrigações dos últimos 5 anos. Se forem encontrados erros, orientamos sobre retificação. Se houver créditos não aproveitados, identificamos e recuperamos dentro do prazo legal.</p>
        </div>
        <div class="content-block reveal">
          <h3>Como funciona a guarda de documentos na transição</h3>
          <p>Todos os documentos físicos e digitais gerados durante a vigência do contrato anterior pertencem à empresa, não ao contador. O prazo mínimo de guarda de documentos contábeis é de 5 anos para obrigações acessórias e de 10 anos para documentos societários. A AM Cabral orienta sobre quais arquivos devem ser solicitados ao contador anterior e como organizar o acervo para auditoria futura.</p>
        </div>
        <div class="content-block reveal">
          <h3>Primeiros indicadores que a troca valeu a pena</h3>
          <p>Nos primeiros 90 dias após a transição, a AM Cabral entrega um diagnóstico completo da situação fiscal da empresa. Verificamos regime tributário, obrigações acessórias em aberto, créditos não aproveitados e conformidade das declarações anteriores. A maioria dos clientes identifica pelo menos um ponto de melhoria que gera economia equivalente ao valor dos honorários anuais.</p>
        </div>"""

html = html.replace(old_content_block, NEW_CONTENT_BLOCK)

# 26. FAQ H2
html = html.replace(
    '<h2 class="sec-h">Dúvidas sobre trocar de contador em Pará de Minas</h2>',
    f'<h2 class="sec-h">{FAQ_H2}</h2>'
)

# 27. FAQ accordion answer (duplicate of schema FAQ answer — same text)
html = html.replace(
    '<div class="faq-a-inner">A entrega de documentos e arquivos digitais é obrigação legal do contador. Se houver resistência, orientamos como solicitar formalmente e, se necessário, como acionar o CRC/MG. Em 20 anos de atuação em Pará de Minas, já gerenciamos dezenas de transições, incluindo casos com conflito, e sempre conseguimos assumir sem ruptura.</div>',
    f'<div class="faq-a-inner">{FAQ_ANS_20ANOS}</div>'
)

# 28. HUB cards
html = html.replace(
    '<a href="/para-de-minas-mg/contador-para-fabricas-e-industrias/" class="hub-card reveal">',
    f'<a href="{HUB_FABRICAS_HREF}" class="hub-card reveal">'
)
html = html.replace(
    '<p>Especialidade em fábricas, metalúrgicas e indústrias do polo de Pará de Minas.</p>',
    f'<p>Especialidade em fábricas, autopeças e indústrias do polo de Sete Lagoas.</p>'
)
html = html.replace(
    '<a href="/para-de-minas-mg/contador-especializado-em-holding/" class="hub-card reveal">',
    f'<a href="{HUB_HOLDING_HREF}" class="hub-card reveal">'
)

# 29. FOOTER city column
html = html.replace(
    '''        <div class="footer-col">
          <div class="footer-heading">Pará de Minas</div>
          <ul>
            <li><a href="/para-de-minas-mg/">Escritório em PDM</a></li>
            <li><a href="/para-de-minas-mg/escritorio-de-contabilidade/">Escritório de Contabilidade</a></li>
            <li><a href="/para-de-minas-mg/contador-especializado-em-holding/">Holding em Pará de Minas</a></li>
            <li><a href="/para-de-minas-mg/contador-para-fabricas-e-industrias/">Contador para Fábricas</a></li>
            <li><a href="/cidades-atendidas/">Cidades Atendidas</a></li>
          </ul>
        </div>''',
    FOOTER_CITY_COL
)

# 30. WhatsApp JS message
html = html.replace(
    'trocar de contador em Pará de Minas.',
    'trocar de contador em Sete Lagoas.'
)

# 31. Schema Service: name (residual — template format differs)
html = html.replace(
    '"name": "Troca de Contador em Pará de Minas",',
    '"name": "Troca de Contador em Sete Lagoas",'
)

# 32. Schema Service: description (residual)
html = html.replace(
    '"description": "Transição contábil segura para empresas de Pará de Minas. Assumimos toda a documentação, SPEDs e obrigações acessórias sem risco fiscal e sem interrupção.",',
    '"description": "Transição contábil segura para empresas de Sete Lagoas. Assumimos toda a documentação, SPEDs e obrigações acessórias sem risco fiscal e sem interrupção.",'
)

# 33. Schema Service: areaServed (residual)
html = html.replace(
    '"areaServed": {"@type": "City", "name": "Pará de Minas", "sameAs": "https://www.wikidata.org/wiki/Q1749821"},',
    '"areaServed": {"@type": "City", "name": "Sete Lagoas", "sameAs": "https://www.wikidata.org/wiki/Q1059948"},'
)

# ===========================================================================
# QA
# ===========================================================================

placeholders = html.count('{{')
pdm_count    = html.count('Pará de Minas')
canonical_ok = PAGE_URL in html

print(f"\n=== QA: Sete Lagoas — Trocar de Contador ===")
print(f"  Placeholders '{{{{' restantes : {placeholders}")
print(f"  'Pará de Minas' no HTML      : {pdm_count}")
print(f"  Canonical URL presente        : {canonical_ok}")
print(f"  Output                        : {OUTPUT}")

with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write(html)

print(f"\n  Arquivo gerado com sucesso: {OUTPUT}")
print(f"  URL: {PAGE_URL}")
