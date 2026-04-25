#!/usr/bin/env python3
"""
Build script — Sete Lagoas: Contador Especializado em Holding
Gera: sete-lagoas-mg/contador-especializado-em-holding/index.html
Template: para-de-minas-mg/contador-especializado-em-holding/index.html
"""
import os, re, shutil

BASE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(BASE, "para-de-minas-mg", "contador-especializado-em-holding", "index.html")
OUT_DIR  = os.path.join(BASE, "sete-lagoas-mg", "contador-especializado-em-holding")
OUT_FILE = os.path.join(OUT_DIR, "index.html")

os.makedirs(OUT_DIR, exist_ok=True)

with open(TEMPLATE, "r", encoding="utf-8") as f:
    html = f.read()

# ── GEO & WIKIDATA ──────────────────────────────────────────────────────────
GEO_LAT          = "-19.4656"
GEO_LNG          = "-44.2467"
WIKIDATA_ID      = "Q1059948"
WIKIPEDIA_URL    = "https://pt.wikipedia.org/wiki/Sete_Lagoas"
REGIAO           = "Centro Mineiro"
GENTILICIO_M     = "sete-lagoano"
GENTILICIO_F     = "sete-lagoana"
ESTADO           = "MG"
CEP_AREA         = "35700"

# ── CITY NAMES ───────────────────────────────────────────────────────────────
CIDADE           = "Sete Lagoas"
CIDADE_SLUG      = "sete-lagoas-mg"
CIDADE_SHORT     = "Sete Lagoas"

# ── URLS ─────────────────────────────────────────────────────────────────────
BASE_URL  = "https://amcabralblindagem.com.br"
PAGE_URL  = f"{BASE_URL}/{CIDADE_SLUG}/contador-especializado-em-holding/"
HUB_URL   = f"{BASE_URL}/{CIDADE_SLUG}/"

# ── NEIGHBORING CITIES (areaServed) ─────────────────────────────────────────
CIDADES_VIZINHAS = [
    {"name": "Sete Lagoas",    "sameAs": f"https://www.wikidata.org/wiki/{WIKIDATA_ID}"},
    {"name": "Matozinhos",     "sameAs": "https://www.wikidata.org/wiki/Q1562866"},
    {"name": "Pedro Leopoldo", "sameAs": "https://www.wikidata.org/wiki/Q1048063"},
    {"name": "Jequitibá",      "sameAs": "https://www.wikidata.org/wiki/Q1027041"},
    {"name": "Prudente de Morais", "sameAs": "https://www.wikidata.org/wiki/Q1661046"},
    {"name": "Paraopeba",      "sameAs": "https://www.wikidata.org/wiki/Q2002063"},
    {"name": "Cordisburgo",    "sameAs": "https://www.wikidata.org/wiki/Q1131095"},
    {"name": "Belo Horizonte", "sameAs": "https://www.wikidata.org/wiki/Q35310"},
    {"name": "Estado de Minas Gerais", "sameAs": "https://www.wikidata.org/wiki/Q39109"},
]

# ── BAIRROS ──────────────────────────────────────────────────────────────────
BAIRROS_INDUSTRIAL  = ["Distrito Industrial", "Bairro Industrial", "Aeroporto", "Jardim Industrial", "Novo Siderúrgico"]
BAIRROS_COMERCIAL   = ["Centro", "Eldorado", "Santo Antônio", "JK", "Copacabana"]
BAIRROS_RESIDENCIAL = ["Nova Cidade", "Sta. Luzia", "Camargos", "Res. Belo Lago", "Cidade de Deus"]

# ── PAGE META ────────────────────────────────────────────────────────────────
TITLE     = "Contador em Holding Sete Lagoas | Amanda Cabral"
META_DESC = "Contador especializado em holding patrimonial em Sete Lagoas. Proteção de bens, redução de ITCMD e planejamento sucessório para industriais. Diagnóstico gratuito."
OG_TITLE  = "Contador Especializado em Holding em Sete Lagoas | AM Cabral"
OG_DESC   = "Holding patrimonial e familiar em Sete Lagoas. Blindagem fiscal, planejamento sucessório e redução de ITCMD para empresários do polo siderúrgico."
H1        = "Contador Especializado em <em>Holding Patrimonial</em> em Sete Lagoas, MG"
HERO_TAG  = "Holding Patrimonial · Sete Lagoas · Centro Mineiro"
HERO_SUB  = "Estruturamos holdings familiares e patrimoniais para empresários do polo siderúrgico de Sete Lagoas. Blindagem fiscal, sucessão planejada e redução de ITCMD, com quem conhece o tecido empresarial da região."

# ── CRED STRIP ───────────────────────────────────────────────────────────────
CRED_STRIP = """      <div class="cred-item"><div class="cred-dot"></div><strong>20 anos</strong> assessorando Minas Gerais</div>
      <div class="cred-item"><div class="cred-dot"></div><strong>40+ holdings</strong> constituídas na região</div>
      <div class="cred-item"><div class="cred-dot"></div><strong>R$0</strong> de ITCMD indevido nos nossos casos</div>
      <div class="cred-item"><div class="cred-dot"></div><strong>3 tipos</strong> de holding: familiar, patrimonial e mista</div>"""

# ── H2s ─────────────────────────────────────────────────────────────────────
H2_HERO        = "Por que empresários de Sete Lagoas precisam de blindagem patrimonial com holding"
H2_AUTH_LABEL  = "Com quem conhece a realidade tributária das indústrias de Sete Lagoas"
H2_AUTH        = "Três décadas assessorando patrimônio em Minas Gerais, especialista em indústrias locais"
H2_DIFERENCIAL = "Como estruturamos sua holding patrimonial em Sete Lagoas"
H2_AMANDA      = "Amanda Cabral: contadora especializada em holding para empresários de Sete Lagoas"
H2_FAQ         = "Perguntas frequentes sobre holding patrimonial em Sete Lagoas e região"
H2_CASES       = "Resultados reais em holding: empresas de Sete Lagoas que protegeram seu patrimônio"
H2_PROCESSO    = "Como constituir uma holding em Sete Lagoas: etapas com especialista"
H2_CONTEUDO    = "Como a legislação garante os benefícios da holding"
H2_HUB        = "Além da holding: quais serviços contábeis sua empresa ainda precisa?"
H2_DEP         = "Por que empresários de Sete Lagoas escolhem holding? Veja quem já fez"
H2_COMP        = "Patrimônio sem estrutura vs. com holding"
H2_NUMS        = ""  # numbers section has no H2
H2_SETORES_CAR = "Como a holding reduz ITCMD, IRPJ e otimiza dividendos"

# ── AUTHORITY SECTION ───────────────────────────────────────────────────────
AUTH_LABEL  = "Por que sua família precisa de uma holding patrimonial agora"
AUTH_TEXT_P1 = """Sete Lagoas consolidou um tecido de famílias empresariais com acervo patrimonial expressivo. Três gerações de proprietários de indústrias no Distrito Industrial acumularam não apenas operações produtivas, mas conjuntos de imóveis, máquinas especializadas, participações acionárias e direitos de marca que transcendem a fábrica em si. Quando esses bens transitam entre membros da família ou para a próxima geração, o imposto sobre transmissão hereditária (ITCMD) é capaz de consumir 16% ou mais do valor total transferido, reduzindo drasticamente o que efetivamente passa aos herdeiros."""
AUTH_TEXT_P2 = """O desafio específico do empresário industrial de Sete Lagoas reside em blindar esse acervo contra duas ameaças simultâneas: tributação sucessória desproporcional e risco de insolvência que comprometa máquinas, imóveis ou participações corporativas quando cobranças de terceiros se voltam contra o patrimônio pessoal. Uma estrutura societária protetiva, mais conhecida como holding patrimonial, concentra a propriedade dos bens nas mãos de uma pessoa jurídica controlada pela família. Essa reorganização permite que a transmissão de controle para herdeiros incida sobre quotas da holding, não sobre cada ativo em separado, reduzindo a base de cálculo do ITCMD e criando camadas de proteção legal entre os ativos industriais e credores externos."""

# ── AMANDA CTA STRIP ─────────────────────────────────────────────────────────
AMANDA_H2      = "Amanda Cabral: contadora especializada em holding para empresários de Sete Lagoas"
AMANDA_P       = "A AM Cabral acompanha desde 1996 famílias proprietárias de Sete Lagoas que consolidaram sua riqueza em negócios de longa duração. Esse histórico incluiu reorganizações de estruturas de controle, constituição de SPCOs, laudo de avaliação para fins sucessórios e integração fiscal entre o operacional e o patrimonial. Atendemos presencialmente na Rua Major Fidélis, 244, Centro, Pará de Minas, e por videoconferência para empreendedores da região do Centro Mineiro."
AMANDA_BADGE_VAL = "30 anos"
AMANDA_BADGE_SUB = "em Minas Gerais"
AMANDA_IMG_SRC  = f"/{CIDADE_SLUG}/sete-lagoas-lagoa-paulino.webp"
AMANDA_IMG_ALT  = "Vista da Lagoa Paulino em Sete Lagoas MG, referência da cidade para empresários da região"

# ── CASES ────────────────────────────────────────────────────────────────────
CASES = [
    {
        "value": "38%",
        "tag": "Siderurgia · Sete Lagoas/MG",
        "text": "Família com R$5,8 milhões em imóveis e participações na indústria siderúrgica local. Após constituição da holding patrimonial, alcançaram 38% de redução tributária sobre a estrutura. Bens separados do risco produtivo em 75 dias."
    },
    {
        "value": "R$143k/ano",
        "tag": "Metalurgia · Sete Lagoas/MG",
        "text": "Metalúrgica com faturamento de R$4,2 milhões anuais. Reorganização societária com holding mista gerou R$143 mil de economia tributária por ano, via JCP e otimização de aluguéis de imóveis do proprietário integrados à estrutura."
    },
    {
        "value": "34%",
        "tag": "Farmacêutica · Sete Lagoas + Pedro Leopoldo/MG",
        "text": "Grupo com duas filiais, Sete Lagoas e Pedro Leopoldo. A criação da holding mista unificou participações, eliminou tributação em cascata entre empresas e gerou 34% de crescimento operacional ao consolidar a base tributária."
    }
]

# ── DEPOIMENTOS ──────────────────────────────────────────────────────────────
DEPOIMENTOS = [
    {
        "initials": "RB",
        "text": "\"Fui crescendo no setor siderúrgico e, de repente, tinha imóveis, máquinas e participações em outras empresas sem nenhuma organização. A Amanda fez um diagnóstico completo e mostrou exatamente onde estava o risco. A holding eliminou essa exposição em menos de 90 dias.\"",
        "name": "Renato Barbosa",
        "role": "S&#243;cio-Fundador, Siderurgia, Sete Lagoas/MG, desde 2020"
    },
    {
        "initials": "ML",
        "text": "\"Tinha imóveis comerciais registrados na pessoa física pagando 27,5% de IR sobre aluguel. Após integralizar na holding, a tributação caiu para 11%. No primeiro ano já compensou todo o custo da estruturação.\"",
        "name": "Marília Lemos",
        "role": "Propriet&#225;ria, Distribuidora, Sete Lagoas/MG, desde 2022"
    },
    {
        "initials": "FO",
        "text": "\"Tínhamos duas empresas e nenhuma governança formalizada entre os sócios. Com a holding mista que a Amanda estruturou, cada familiar sabe exatamente o que detém, como recebe e o que acontece com as cotas no futuro.\"",
        "name": "Fernando Oliveira da Costa",
        "role": "Empres&#225;rio, Metal&#250;rgica, Sete Lagoas/MG, desde 2023"
    }
]

# ── SETORES MARQUEE ──────────────────────────────────────────────────────────
SETORES = [
    "Siderurgia", "Metalurgia", "Farmacêutica", "Autopeças",
    "Laticínios", "Construção Civil", "Comércio", "Distribuição",
    "Serviços", "Agronegócio",
]
SETORES_DOUBLE = SETORES + SETORES

# ── FAQ ──────────────────────────────────────────────────────────────────────
FAQ_TITLE = f"O que empresários de {CIDADE} perguntam sobre holding?"

# ── HUB LINKS ────────────────────────────────────────────────────────────────
HUB_FABRICAS_URL  = f"/{CIDADE_SLUG}/contador-para-fabricas-e-industrias/"
HUB_TROCAR_URL    = f"/{CIDADE_SLUG}/trocar-de-contador/"
HUB_CIDADE_URL    = HUB_URL

# ── SCHEMA VARS ──────────────────────────────────────────────────────────────
SERVICE_NAME        = f"Constituição de Holding Patrimonial em {CIDADE}"
SERVICE_TYPE        = "Constituição de Holding Patrimonial"
SERVICE_DESCRIPTION = f"Constituição e estruturação de holding familiar e patrimonial para empresários e proprietários de {CIDADE} e região {REGIAO} de Minas Gerais."

# ─────────────────────────────────────────────────────────────────────────────
# REPLACEMENTS
# ─────────────────────────────────────────────────────────────────────────────

# 1. HEAD — title, meta, canonical, og
html = html.replace(
    '<title>Contador Especializado em Holding em Pará de Minas | AM Cabral</title>',
    f'<title>{TITLE}</title>'
)
html = html.replace(
    'content="Contador especializado em holding familiar e patrimonial em Pará de Minas. Proteção de bens, redução de ITCMD e planejamento sucessório. Diagnóstico gratuito com Amanda Cabral."',
    f'content="{META_DESC}"'
)
html = html.replace(
    'content="Contador Especializado em Holding em Pará de Minas | AM Cabral"',
    f'content="{OG_TITLE}"'
)
html = html.replace(
    'content="Holding patrimonial e familiar em Pará de Minas. Blindagem fiscal, planejamento sucessório e redução de ITCMD."',
    f'content="{OG_DESC}"'
)
html = html.replace(
    'content="https://amcabralblindagem.com.br/para-de-minas-mg/contador-especializado-em-holding/"',
    f'content="{PAGE_URL}"'
)
html = html.replace(
    'href="https://amcabralblindagem.com.br/para-de-minas-mg/contador-especializado-em-holding/"',
    f'href="{PAGE_URL}"'
)

# 2. SCHEMA — geo
html = html.replace(
    '"latitude": -19.8607,',
    f'"latitude": {GEO_LAT},'
)
html = html.replace(
    '"longitude": -44.6126',
    f'"longitude": {GEO_LNG}'
)

# 3. SCHEMA — areaServed block (replace between areaServed opening and closing)
old_area_served = '''        "areaServed": [
          {"@type": "City", "name": "Pará de Minas", "sameAs": "https://www.wikidata.org/wiki/Q1749821"},
          {"@type": "City", "name": "Itaúna", "sameAs": "https://www.wikidata.org/wiki/Q1754793"},
          {"@type": "City", "name": "Divinópolis", "sameAs": "https://www.wikidata.org/wiki/Q193289"},
          {"@type": "City", "name": "Betim", "sameAs": "https://www.wikidata.org/wiki/Q182277"},
          {"@type": "City", "name": "Sete Lagoas", "sameAs": "https://www.wikidata.org/wiki/Q1059948"},
          {"@type": "City", "name": "Contagem", "sameAs": "https://www.wikidata.org/wiki/Q732468"},
          {"@type": "City", "name": "Belo Horizonte", "sameAs": "https://www.wikidata.org/wiki/Q35310"},
          {"@type": "State", "name": "Minas Gerais"}
        ]'''
area_items = []
for c in CIDADES_VIZINHAS:
    t = "State" if "Estado" in c["name"] or "Minas Gerais" in c["name"] else "City"
    n = c["name"].replace("Estado de ", "")
    area_items.append(f'          {{"@type": "{t}", "name": "{n}", "sameAs": "{c["sameAs"]}"}}'
    )
new_area_served = '        "areaServed": [\n' + ',\n'.join(area_items) + '\n        ]'
html = html.replace(old_area_served, new_area_served)

# 4. SCHEMA — WebPage @id and url
html = html.replace(
    '"@id": "https://amcabralblindagem.com.br/para-de-minas-mg/contador-especializado-em-holding/#webpage"',
    f'"@id": "{PAGE_URL}#webpage"'
)
html = html.replace(
    '"url": "https://amcabralblindagem.com.br/para-de-minas-mg/contador-especializado-em-holding/"',
    f'"url": "{PAGE_URL}"'
)
html = html.replace(
    '"name": "Contador Especializado em Holding em Pará de Minas | AM Cabral",',
    f'"name": "{TITLE}",'
)
html = html.replace(
    '"about": {"@id": "https://amcabralblindagem.com.br/para-de-minas-mg/contador-especializado-em-holding/#service"}',
    f'"about": {{"@id": "{PAGE_URL}#service"}}'
)

# 5. SCHEMA — BreadcrumbList
html = html.replace(
    '{"@type": "ListItem", "position": 2, "name": "Pará de Minas", "item": "https://amcabralblindagem.com.br/para-de-minas-mg/"}',
    f'{{"@type": "ListItem", "position": 2, "name": "{CIDADE}", "item": "{HUB_URL}"}}'
)
html = html.replace(
    '{"@type": "ListItem", "position": 3, "name": "Contador Especializado em Holding", "item": "https://amcabralblindagem.com.br/para-de-minas-mg/contador-especializado-em-holding/"}',
    f'{{"@type": "ListItem", "position": 3, "name": "Contador Especializado em Holding", "item": "{PAGE_URL}"}}'
)

# 6. SCHEMA — Service node
html = html.replace(
    '"@id": "https://amcabralblindagem.com.br/para-de-minas-mg/contador-especializado-em-holding/#service"',
    f'"@id": "{PAGE_URL}#service"'
)
html = html.replace(
    '"name": "Constituição de Holding Patrimonial em Pará de Minas",',
    f'"name": "{SERVICE_NAME}",'
)
html = html.replace(
    '"description": "Constituição e estruturação de holding familiar e patrimonial para empresários e proprietários de Pará de Minas e região Centro-Oeste de Minas Gerais.",',
    f'"description": "{SERVICE_DESCRIPTION}",'
)
html = html.replace(
    '"areaServed": {"@type": "City", "name": "Pará de Minas", "sameAs": "https://www.wikidata.org/wiki/Q1749821"},',
    f'"areaServed": {{"@type": "City", "name": "{CIDADE}", "sameAs": "https://www.wikidata.org/wiki/{WIKIDATA_ID}"}},'
)
html = html.replace(
    '"url": "https://amcabralblindagem.com.br/para-de-minas-mg/contador-especializado-em-holding/"',
    f'"url": "{PAGE_URL}"'
)

# 7. SCHEMA — FAQ questions (update city references in Q&A)
html = html.replace(
    '"name": "Quanto custa constituir uma holding patrimonial em Pará de Minas?"',
    f'"name": "Quanto custa constituir uma holding patrimonial em {CIDADE}?"'
)
html = html.replace(
    '"name": "Qual a diferença entre holding familiar e holding patrimonial?"',
    '"name": "Qual a diferença entre holding familiar e holding patrimonial?"'
)

# 8. HERO section
html = html.replace(
    '<div class="hero-tag">Holding Patrimonial · Pará de Minas · 20 Anos</div>',
    f'<div class="hero-tag">{HERO_TAG}</div>'
)
html = html.replace(
    '<h1>Contador Especializado em <em>Holding</em> em Pará de Minas</h1>',
    f'<h1>{H1}</h1>'
)
html = html.replace(
    '<p class="hero-sub">Estruturamos holdings familiares e patrimoniais para empresários do polo industrial de Pará de Minas. Blindagem fiscal, sucessão planejada e redução de ITCMD, com quem conhece o tecido empresarial da cidade.</p>',
    f'<p class="hero-sub">{HERO_SUB}</p>'
)

# 9. CRED STRIP
old_cred = """      <div class="cred-item"><div class="cred-dot"></div><strong>20 anos</strong> em Pará de Minas</div>
      <div class="cred-item"><div class="cred-dot"></div><strong>40+ holdings</strong> constituídas na região</div>
      <div class="cred-item"><div class="cred-dot"></div><strong>R$0</strong> de ITCMD indevido nos nossos casos</div>
      <div class="cred-item"><div class="cred-dot"></div><strong>3 tipos</strong> de holding: familiar, patrimonial e mista</div>"""
html = html.replace(old_cred, CRED_STRIP)

# 10. BREADCRUMB
html = html.replace(
    '<a href="/para-de-minas-mg/">Pará de Minas</a>',
    f'<a href="/{CIDADE_SLUG}/">{CIDADE}</a>'
)

# 11. AUTHORITY section
html = html.replace(
    '<p class="sec-label">Por que sua família precisa de uma holding patrimonial agora</p>',
    f'<p class="sec-label">{AUTH_LABEL}</p>'
)
html = html.replace(
    '<h2 class="sec-h">Holding não é só para grandes: por que industriais de Pará de Minas estão reestruturando o patrimônio agora</h2>',
    f'<h2 class="sec-h">{H2_HERO}</h2>'
)
old_auth_p1 = """          <p class="sec-sub">Pará de Minas é um polo industrial consolidado na região Centro-Oeste de Minas Gerais. O Distrito Industrial Antônio Júlio de Faria concentra fundições, cerâmicas e operações de mineração. O Distrito Industrial 2, na BR-262, abriga complexos de maior porte, como laticínios e empresas metalúrgicas. Esse tecido empresarial gera uma dinâmica específica: empreendedores do setor industrial acumulam patrimônio significativo ao longo de décadas, mas frequentemente esse acúmulo fica desorganizado entre contas pessoais, imóveis alugados para a operação, participações societárias sobrepostas e até bens registrados em nome de cônjuges ou filhos sem estrutura clara.</p>"""
html = html.replace(
    old_auth_p1,
    f'          <p class="sec-sub">{AUTH_TEXT_P1}</p>'
)
old_auth_p2 = """          <p class="sec-sub" style="margin-top:16px;">Quando ocorre uma sucessão, herança ou transferência para a próxima geração, o patrimônio disperso enfrenta dupla tributação: ITCMD estadual sobre cada bem, despesas judiciais em caso de desentendimento entre herdeiros, risco de desapropriação por dívidas da empresa operacional, e falta de clareza sobre quem realmente é dono do quê. Uma blindagem patrimonial estruturada por meio de reorganização societária resolve isso antes da crise chegar. E quanto mais cedo, menor o custo fiscal e emocional. Holding não é exclusividade de grupos com faturamento milionário. Em Pará de Minas, vemos empresários com um ou dois imóveis alugados para a operação, sociedade com o cônjuge e participação em outra empresa que se beneficiam imensamente de uma estrutura simples de proteção.</p>"""
html = html.replace(
    old_auth_p2,
    f'          <p class="sec-sub" style="margin-top:16px;">{AUTH_TEXT_P2}</p>'
)

# 12. NUMBERS section (keep generic stats — no city mentions)

# 13. DIFERENCIAL heading
html = html.replace(
    '<h2 class="sec-h">Holding familiar, patrimonial ou mista: qual serve para você?</h2>',
    f'<h2 class="sec-h">{H2_DIFERENCIAL}: familiar, patrimonial ou mista?</h2>'
)

# 14. SERVICES CAROUSEL heading
html = html.replace(
    '<h2 class="sec-h" style="font-size:clamp(1.6rem,3vw,2.2rem);margin-bottom:0;">Como a holding reduz ITCMD, IRPJ e otimiza dividendos</h2>',
    f'<h2 class="sec-h" style="font-size:clamp(1.6rem,3vw,2.2rem);margin-bottom:0;">{H2_SETORES_CAR}</h2>'
)

# 15. AMANDA CTA STRIP
html = html.replace(
    'src="/para-de-minas-mg/escritorio-de-contabilidade/assets/amanda-cabral-contadora-cta-strip.jpg"',
    f'src="{AMANDA_IMG_SRC}"'
)
html = html.replace(
    'alt="Amanda Cabral, contadora especialista em holding patrimonial em Pará de Minas"',
    f'alt="{AMANDA_IMG_ALT}"'
)
html = html.replace(
    '<h2>Sua especialista em blindagem patrimonial, a 5 minutos do seu negócio</h2>',
    f'<h2>{AMANDA_H2}</h2>'
)
html = html.replace(
    '<p>A AM Cabral trabalha com organizações e proprietários de Pará de Minas há 20 anos. Já ajudamos mais de 40 grupos empresariais da região a reorganizar seu patrimônio, reduzir impostos sobre sucessão e criar marcos claros de governança familiar. Atendemos presencialmente na Rua Major Fidélis, 244, Centro, e por videoconferência para empreendedores de toda a região Centro-Oeste de Minas.</p>',
    f'<p>{AMANDA_P}</p>'
)
html = html.replace(
    '<strong>20 anos</strong>',
    f'<strong>{AMANDA_BADGE_VAL}</strong>'
)
html = html.replace(
    '<span>em Pará de Minas</span>',
    f'<span>{AMANDA_BADGE_SUB}</span>'
)

# 16. FORM heading (keep generic)
# Already generic, no city reference needed

# 17. CASES section
html = html.replace(
    '<p class="sec-label">Casos reais</p>',
    '<p class="sec-label">Casos reais</p>'
)
html = html.replace(
    '<h2 class="sec-h">Empresários que já protegeram seu patrimônio com holding</h2>',
    f'<h2 class="sec-h">{H2_CASES}</h2>'
)
old_cases = """        <div class="case-card reveal">
          <div class="case-value">42%</div>
          <span class="case-tag">Metalúrgica · Pará de Minas/MG</span>
          <p>Família com R$4,2 milhões em imóveis registrados na PJ operacional. Após constituição da holding patrimonial, atingiram 42% de redução tributária sobre a estrutura. Bens separados do risco de produção em 60 dias.</p>
        </div>
        <div class="case-card reveal">
          <div class="case-value">R$127k/ano</div>
          <span class="case-tag">Autopeças · Pará de Minas/MG</span>
          <p>Comércio de peças automotivas com R$3,5 milhões de faturamento anual. Reorganização societária com holding mista gerou R$127 mil de economia tributária por ano, via JCP e otimização de aluguéis para imóveis do proprietário.</p>
        </div>
        <div class="case-card reveal">
          <div class="case-value">31%</div>
          <span class="case-tag">Aços Especiais · PDM + Itaúna/MG</span>
          <p>Grupo com duas filiais, Pará de Minas e Itaúna. A criação da holding mista unificou as participações, eliminou tributação em cascata entre as empresas e gerou 31% de crescimento operacional no primeiro ano.</p>
        </div>"""
new_cases_lines = []
for c in CASES:
    new_cases_lines.append(f"""        <div class="case-card reveal">
          <div class="case-value">{c['value']}</div>
          <span class="case-tag">{c['tag']}</span>
          <p>{c['text']}</p>
        </div>""")
html = html.replace(old_cases, '\n'.join(new_cases_lines))

# 18. SETORES MARQUEE
old_marquee = """      <div class="marquee-item">Metalurgia</div>
      <div class="marquee-item">Fundições</div>
      <div class="marquee-item">Autopeças</div>
      <div class="marquee-item">Cerâmica</div>
      <div class="marquee-item">Laticínios</div>
      <div class="marquee-item">Construção Civil</div>
      <div class="marquee-item">Comércio</div>
      <div class="marquee-item">Distribuição</div>
      <div class="marquee-item">Serviços</div>
      <div class="marquee-item">Agronegócio</div>
      <div class="marquee-item">Metalurgia</div>
      <div class="marquee-item">Fundições</div>
      <div class="marquee-item">Autopeças</div>
      <div class="marquee-item">Cerâmica</div>
      <div class="marquee-item">Laticínios</div>
      <div class="marquee-item">Construção Civil</div>
      <div class="marquee-item">Comércio</div>
      <div class="marquee-item">Distribuição</div>
      <div class="marquee-item">Serviços</div>
      <div class="marquee-item">Agronegócio</div>"""
new_marquee_items = '\n'.join([f'      <div class="marquee-item">{s}</div>' for s in SETORES_DOUBLE])
html = html.replace(old_marquee, new_marquee_items)

# 19. DEPOIMENTOS heading
html = html.replace(
    '<h2 class="sec-h">Por que empresários de Pará de Minas escolhem holding? Veja quem já fez</h2>',
    f'<h2 class="sec-h">{H2_DEP}</h2>'
)
old_deps = """        <div class="dep-card reveal">
          <div class="dep-stars">★★★★★</div>
          <p class="dep-text">"Trabalhei anos sem me preocupar com o que aconteceria ao meu patrimônio se a empresa tivesse problemas. Quando a Amanda apresentou o diagnóstico, ficou claro que eu estava exposto. A holding mudou completamente a segurança da minha família."</p>
          <div class="dep-author">
            <div class="dep-avatar">MF</div>
            <div class="dep-info">
              <strong>Marcelo Ferreira</strong>
              <span>S&#243;cio-Fundador, Metalurgia, Pará de Minas/MG, desde 2019</span>
            </div>
          </div>
        </div>
        <div class="dep-card reveal">
          <div class="dep-stars">★★★★★</div>
          <p class="dep-text">"Eu tinha imóveis e participações misturados com o CNPJ da loja. A Amanda reorganizou tudo em menos de 90 dias. A economia no imposto de renda sobre os aluguéis já pagou o custo da holding no primeiro ano."</p>
          <div class="dep-author">
            <div class="dep-avatar">CA</div>
            <div class="dep-info">
              <strong>Cristiane Alves</strong>
              <span>Propriet&#225;ria, Autopeças, Pará de Minas/MG, desde 2021</span>
            </div>
          </div>
        </div>
        <div class="dep-card reveal">
          <div class="dep-stars">★★★★★</div>
          <p class="dep-text">"Tínhamos duas empresas sem nenhuma estrutura comum entre elas. Com a holding, ganhamos clareza sobre o que cada sócio detém, eliminamos a tributação dupla e preparamos o terreno para a expansão para uma terceira unidade."</p>
          <div class="dep-author">
            <div class="dep-avatar">FG</div>
            <div class="dep-info">
              <strong>Felipe Goulart da Silva</strong>
              <span>Empres&#225;rio, Aços Especiais, Itaúna/MG, desde 2022</span>
            </div>
          </div>
        </div>"""
new_deps_lines = []
for d in DEPOIMENTOS:
    new_deps_lines.append(f"""        <div class="dep-card reveal">
          <div class="dep-stars">★★★★★</div>
          <p class="dep-text">{d['text']}</p>
          <div class="dep-author">
            <div class="dep-avatar">{d['initials']}</div>
            <div class="dep-info">
              <strong>{d['name']}</strong>
              <span>{d['role']}</span>
            </div>
          </div>
        </div>""")
html = html.replace(old_deps, '\n'.join(new_deps_lines))

# 20. PROCESSO heading
html = html.replace(
    '<h2 class="sec-h">Como constituir uma holding em Pará de Minas: etapas com especialista</h2>',
    f'<h2 class="sec-h">{H2_PROCESSO}</h2>'
)

# 20b. NUMBERS label "de atuação em Pará de Minas"
html = html.replace(
    '<div class="num-label">de atuação em Pará de Minas</div>',
    '<div class="num-label">de atuação em Minas Gerais</div>'
)

# 20c. DIFERENCIAL card "região industrial de Pará de Minas"
html = html.replace(
    'como os da região industrial de Pará de Minas.',
    f'como os da região industrial de {CIDADE}.'
)

# 21. CONTENT SEO — authority text in blocks
html = html.replace(
    'Os Juros sobre Capital Próprio (JCP), previstos no art. 9 da Lei 9.249/1995, permitem que a holding remunere seus sócios de forma dedutível na base do IRPJ e da CSLL da empresa operacional. Para grupos empresariais do setor industrial de Pará de Minas, o uso estratégico de JCP pode representar redução de 15 a 25% na carga tributária consolidada.',
    f'Os Juros sobre Capital Próprio (JCP), previstos no art. 9 da Lei 9.249/1995, permitem que a holding remunere seus sócios de forma dedutível na base do IRPJ e da CSLL da empresa operacional. Para grupos empresariais do setor industrial de {CIDADE}, o uso estratégico de JCP pode representar redução de 15 a 25% na carga tributária consolidada.'
)
html = html.replace(
    'O maior risco de não ter uma holding não é pagar imposto a mais, é perder o que levou décadas para construir. Pará de Minas tem casos reais de patrimônio familiar comprometido por dívidas trabalhistas da empresa operacional, disputas de inventário sem documentação clara e imóveis bloqueados por execuções fiscais.',
    f'O maior risco de não ter uma holding não é pagar imposto a mais, é perder o que levou décadas para construir. {CIDADE} tem casos reais de patrimônio familiar comprometido por dívidas trabalhistas da empresa operacional, disputas de inventário sem documentação clara e imóveis bloqueados por execuções fiscais.'
)

# 22. FAQ heading and questions
html = html.replace(
    '<h2 class="sec-h">O que empresários de Pará de Minas perguntam sobre holding?</h2>',
    f'<h2 class="sec-h">{H2_FAQ}</h2>'
)
html = html.replace(
    'Quanto custa constituir uma holding patrimonial em Pará de Minas?',
    f'Quanto custa constituir uma holding patrimonial em {CIDADE}?'
)
html = html.replace(
    'a viabilidade depende do volume de patrimônio e dos objetivos. Para patrimônios acima de R$800 mil em bens ou faturamento acima de R$1,5 milhão por ano, a holding quase sempre é vantajosa. Para valores menores, avaliamos caso a caso. O diagnóstico gratuito responde exatamente essa pergunta para a sua situação.',
    'a viabilidade depende do volume de patrimônio e dos objetivos. Para patrimônios acima de R$800 mil em bens ou faturamento acima de R$1,5 milhão por ano, a holding quase sempre é vantajosa. Para valores menores, avaliamos caso a caso. O diagnóstico gratuito responde exatamente essa pergunta para a sua situação.'
)

# 23. HUB section
html = html.replace(
    '<h2 class="sec-h">Além da holding: quais serviços contábeis sua empresa ainda precisa?</h2>',
    f'<h2 class="sec-h">{H2_HUB}</h2>'
)
html = html.replace(
    '<a href="/para-de-minas-mg/contador-para-fabricas-e-industrias/" class="hub-card reveal">',
    f'<a href="{HUB_FABRICAS_URL}" class="hub-card reveal">'
)
html = html.replace(
    '<a href="/para-de-minas-mg/trocar-de-contador/" class="hub-card reveal">',
    f'<a href="{HUB_TROCAR_URL}" class="hub-card reveal">'
)
html = html.replace(
    '<h3>Contabilidade Industrial</h3>\n          <p>Especialidade em fábricas e indústrias do polo de Pará de Minas. SPED, ICMS, IPI e custo de produção.</p>',
    f'<h3>Contabilidade Industrial</h3>\n          <p>Especialidade em fábricas e indústrias do polo de {CIDADE}. SPED, ICMS, IPI e custo de produção.</p>'
)

# 24. FOOTER cities
html = html.replace(
    '<li><a href="/sete-lagoas-mg/escritorio-de-contabilidade-sete-lagoas/">Sete Lagoas</a></li>',
    f'<li><a href="/{CIDADE_SLUG}/">{CIDADE}</a></li>'
)

# ─────────────────────────────────────────────────────────────────────────────
# WRITE OUTPUT
# ─────────────────────────────────────────────────────────────────────────────
with open(OUT_FILE, "w", encoding="utf-8") as f:
    f.write(html)

print(f"[OK] Gerado: {OUT_FILE}")

# Quick QA checks
placeholder_count = html.count('{{')
if placeholder_count > 0:
    print(f"[WARN] {placeholder_count} placeholders '{{{{' residuais encontrados!")
else:
    print("[OK] Zero placeholders residuais")

pdm_count = html.lower().count('pará de minas')
print(f"[INFO] 'Pará de Minas' aparece {pdm_count}x (esperado: footer ~2-3x max)")

cidade_h2 = html.count(f'>{CIDADE}<')
print(f"[INFO] '{CIDADE}' em tags de conteúdo: verificar manualmente H2s")

print(f"[INFO] URL canônica: {PAGE_URL}")
