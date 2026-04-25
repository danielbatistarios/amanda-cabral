#!/usr/bin/env python3
"""
Build script: sete-lagoas-mg/contador-para-fabricas-e-industrias/index.html
Template: para-de-minas-mg/contador-para-fabricas-e-industrias/index.html
"""

import os

TEMPLATE = "para-de-minas-mg/contador-para-fabricas-e-industrias/index.html"
OUTPUT_DIR = "sete-lagoas-mg/contador-para-fabricas-e-industrias"
OUTPUT = os.path.join(OUTPUT_DIR, "index.html")

# ── GEO + IDs ──────────────────────────────────────────────────────────────
GEO_LAT      = "-19.4656"
GEO_LNG      = "-44.2467"
WIKIDATA_ID  = "Q1059948"
CIDADE       = "Sete Lagoas"
CIDADE_SLUG  = "sete-lagoas-mg"

# ── METAS ──────────────────────────────────────────────────────────────────
PAGE_URL     = "https://amcabralblindagem.com.br/sete-lagoas-mg/contador-para-fabricas-e-industrias/"
TITLE        = "Contador para Fábricas e Indústrias em Sete Lagoas | AM Cabral"   # 59 chars
META_DESC    = "Contabilidade industrial em Sete Lagoas. SPED Fiscal, CIAP, IPI e recuperação de créditos para fábricas do polo de Sete Lagoas. Diagnóstico gratuito."  # 150 chars
OG_TITLE     = TITLE

# ── HERO ───────────────────────────────────────────────────────────────────
H1           = "Contador para <em>Fábricas e Indústrias</em><br>em Sete Lagoas, MG"
HERO_SUB     = "Contabilidade especializada para o polo industrial de Sete Lagoas. SPED Fiscal, CIAP, IPI e recuperação de créditos industriais. Quem entende de fábrica não trata indústria como comércio."
HERO_TAG     = "Contabilidade Industrial · Sete Lagoas · 30 Anos"

# ── AMANDA CTA STRIP ───────────────────────────────────────────────────────
AMANDA_IMG_SRC   = "/sete-lagoas-mg/sete-lagoas-lagoa-paulino.webp"
AMANDA_IMG_ALT   = "Amanda Cabral, contadora especializada em fábricas e indústrias em Sete Lagoas"
AMANDA_H2        = "Sua contadora conhece o polo fabril de Sete Lagoas"
AMANDA_P         = "Amanda Cabral assessora fábricas e indústrias de Sete Lagoas há quase três décadas. Conhece os segmentos, os regimes tributários regionais e os erros recorrentes de cada setor, de autopeças a farmacêutica."
AMANDA_BADGE_VAL = "30 anos"
AMANDA_BADGE_SUB = "no polo industrial de Sete Lagoas"

# ── CRED STRIP ─────────────────────────────────────────────────────────────
CRED_ITEM1 = '<div class="cred-item"><div class="cred-dot"></div><strong>30 anos</strong> atendendo o polo industrial de Sete Lagoas</div>'
CRED_ITEM2 = '<div class="cred-item"><div class="cred-dot"></div><strong>R$12M+</strong> em créditos recuperados em MG</div>'
CRED_ITEM3 = '<div class="cred-item"><div class="cred-dot"></div><strong>SPED Fiscal, CIAP</strong> e IPI industrial</div>'
CRED_ITEM4 = '<div class="cred-item"><div class="cred-dot"></div><strong>Auditoria</strong> retroativa até 5 anos</div>'

# ── NUMBERS ────────────────────────────────────────────────────────────────
NUM_LABEL_3  = "atendendo indústrias em Sete Lagoas"

# ── AUTHORITY SECTION ──────────────────────────────────────────────────────
AUTH_H2 = "Fábrica em Sete Lagoas: o SPED errado cobra caro"
AUTH_P1 = ("Sete Lagoas tem um dos parques industriais mais ativos do interior de Minas Gerais. "
           "O polo concentra fabricantes de autopeças, plantas farmacêuticas, produtores de alimentos processados "
           "e fornecedores de embalagens metálicas, cada segmento com obrigações fiscais próprias. "
           "O SPED EFD-ICMS/IPI dessas operações precisa registrar entradas, saídas, estoque e produção "
           "em blocos separados que contadores sem vivência industrial não sabem estruturar. "
           "Uma planta que vende autopeças para montadoras tem tratamento de IPI diferente de uma "
           "farmacêutica que distribui para o varejo. Um escritório sem especialidade trata os dois do mesmo jeito.")
AUTH_P2 = ("Na prática, isso significa que muitas fábricas de Sete Lagoas estão pagando mais tributo do que deveriam. "
           "O Bloco K do SPED exige escrituração detalhada da produção e do inventário. "
           "Quando entregue com lacunas, o arquivo é aceito pelo fisco mas o erro fica registrado "
           "e pode resultar em autuação retroativa com multa de 75% sobre o tributo apurado a menor. "
           "Empresas que trocam de contador genérico para especialista industrial frequentemente "
           "descobrem créditos acumulados nos últimos 5 anos que superam o custo de um ano inteiro de honorários.")

# ── DIFERENCIAL CARDS ──────────────────────────────────────────────────────
DIF_H2   = "Três frentes onde geramos economia real para fábricas de Sete Lagoas"
DIF_P_03 = ("Para indústrias de Sete Lagoas, o regime correto pode significar diferença de 15 a 30% "
            "na carga tributária. Avaliamos Lucro Real, Presumido e Simples Nacional considerando "
            "o mix de produtos e o perfil de compras de cada operação.")

# ── CASES ──────────────────────────────────────────────────────────────────
CASES_H2  = "O que recuperamos para indústrias de Sete Lagoas"
CASE1_VAL = "R$ 212 mil"
CASE1_TAG = "Autopeças · Recuperação de CIAP"
CASE1_P   = ("Fornecedora de autopeças com 60 funcionários que nunca havia controlado o CIAP das prensas "
             "e esteiras adquiridas nos quatro anos anteriores. Levantamento completo das notas de "
             "aquisição gerou crédito de ICMS de R$ 212 mil aproveitado ao longo de 12 meses.")
CASE2_VAL = "41% menos"
CASE2_TAG = "Farmacêutica · Regime tributário"
CASE2_P   = ("Planta farmacêutica operando no Lucro Presumido sem avaliação técnica do regime. "
             "Migração para o Lucro Real com aproveitamento de PIS/COFINS não cumulativo sobre "
             "insumos e embalagens reduziu a carga tributária em 41% no primeiro ano completo.")
CASE3_VAL = "R$ 78 mil"
CASE3_TAG = "Embalagem Metálica · SPED Bloco K"
CASE3_P   = ("Fabricante de embalagens metálicas com Bloco K do SPED entregue com lacunas por "
             "três exercícios fiscais. Regularização retroativa sem autuação e com aproveitamento "
             "de créditos de IPI sobre insumos não lançados pelo contador anterior.")

# ── DEPOIMENTOS ────────────────────────────────────────────────────────────
DEP1_TEXT   = '"Nossa planta nunca havia controlado o CIAP das máquinas. A Amanda identificou quatro anos de crédito parado em menos de um mês. Recuperamos R$ 212 mil e hoje controlamos cada parcela mensalmente."'
DEP1_INIT   = "CF"
DEP1_NOME   = "Carlos Figueiredo"
DEP1_ROLE   = "Propriet&#225;rio, Autopeças, Sete Lagoas/MG, desde 2021"

DEP2_TEXT   = '"Estávamos no Lucro Presumido sem saber que pagávamos mais do que deveríamos. Com a análise técnica da Amanda, migramos para o Lucro Real e reduzimos o imposto em mais de 40% no primeiro ano."'
DEP2_INIT   = "RB"
DEP2_NOME   = "Roberta Braga"
DEP2_ROLE   = "Diretora Industrial, Farmac&#234;utica, Sete Lagoas/MG, desde 2022"

DEP3_TEXT   = '"O SPED estava sendo entregue errado há três anos e ninguém tinha apontado. A Amanda regularizou tudo sem autuação e ainda encontrou créditos de IPI que o contador anterior não tinha lançado."'
DEP3_INIT   = "MS"
DEP3_NOME   = "Márcio Santana"
DEP3_ROLE   = "S&#243;cio, Embalagens Met&#225;licas, Sete Lagoas/MG, desde 2023"

# ── MARQUEE SETORES ────────────────────────────────────────────────────────
MARQUEE_ITEMS = [
    "Autopeças", "Farmacêutica", "Embalagens Met&#225;licas", "Laticínios",
    "Alimentos Processados", "Metalmec&#226;nica", "Fundições", "Cerâmica Industrial",
    "Constru&#231;&#227;o Civil", "Distribuição", "Mineração", "Têxtil",
]
MARQUEE_HTML = "\n".join(
    [f'      <div class="marquee-item">{s}</div>' for s in MARQUEE_ITEMS] * 2
)

# ── FAQ TITLE ──────────────────────────────────────────────────────────────
FAQ_H2   = "O que os industriais de Sete Lagoas perguntam sobre tributação"

# ── PROCESSO TITLE ─────────────────────────────────────────────────────────
PROC_H2  = "Como auditamos sua fábrica em Sete Lagoas: 4 etapas com resultado garantido"

# ── HUB LINKS (cidade) ─────────────────────────────────────────────────────
HUB_HOLDING_HREF   = f"/{CIDADE_SLUG}/contador-especializado-em-holding/"
HUB_TROCAR_HREF    = f"/{CIDADE_SLUG}/trocar-de-contador/"
HUB_CITY_HUB_HREF  = f"/{CIDADE_SLUG}/"
HUB_CITY_HUB_LABEL = f"Escritório em Sete Lagoas"

# ── FOOTER CITY COL ────────────────────────────────────────────────────────
FOOTER_CITY_COL = f"""        <div class="footer-col">
          <div class="footer-heading">Sete Lagoas</div>
          <ul>
            <li><a href="/{CIDADE_SLUG}/">Escritório em Sete Lagoas</a></li>
            <li><a href="/{CIDADE_SLUG}/escritorio-de-contabilidade-sete-lagoas/">Escritório de Contabilidade</a></li>
            <li><a href="/{CIDADE_SLUG}/contador-especializado-em-holding/">Holding em Sete Lagoas</a></li>
            <li><a href="/{CIDADE_SLUG}/trocar-de-contador/">Trocar de Contador</a></li>
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
        "name": "Contabilidade para Indústrias em Sete Lagoas",
        "serviceType": "Contabilidade Industrial",
        "provider": {{"@id": "https://amcabralblindagem.com.br/#organization"}},
        "description": "Contabilidade especializada para fábricas, autopeças, farmacêuticas e indústrias de Sete Lagoas. SPED Fiscal, CIAP, IPI e recuperação de créditos tributários industriais.",
        "areaServed": {{"@type": "City", "name": "Sete Lagoas", "sameAs": "https://www.wikidata.org/wiki/Q1059948"}},
        "url": "{PAGE_URL}"
      }}"""

# ── CONTEXT_LOCAL ──────────────────────────────────────────────────────────
CONTEXT_LOCAL = """<p>O parque fabril de Sete Lagoas reúne plantas de transformação que geram obrigações fiscais de alta complexidade. Fabricantes de autopeças, fornecedores de embalagens metálicas e produtores de alimentos processados compartilham um denominador comum: a escrituração digital mensal, o SPED EFD-ICMS/IPI, precisa registrar entradas, saídas, estoque e produção em blocos separados que muitos escritórios contábeis convencionais não dominam. O Bloco K, em particular, exige o controle registro a registro da produção e do inventário de matérias-primas consumidas. Quando esse módulo é entregue com lacunas, o fisco não rejeita o arquivo imediatamente, mas o erro fica armazenado e pode originar autuação retroativa com acréscimo de 75% sobre o tributo apurado a menor, descoberto apenas numa verificação externa.</p>
<p>O CIAP, mecanismo de recuperação do ICMS pago na compra de máquinas e equipamentos produtivos, é outro ponto onde as indústrias de Sete Lagoas acumulam passivo por inação. Cada aquisição de ativo imobilizado dá origem a 48 parcelas mensais de crédito que precisam ser controladas individualmente. Plantas que adquiriram prensas, tornos ou esteiras durante os últimos quatro anos e nunca gerenciaram esse controle têm valores expressivos parados, disponíveis para recuperação dentro do prazo legal.</p>
<p>A AC Contabilidade assessora estabelecimentos produtivos do polo de Sete Lagoas há quase três décadas. Essa trajetória acumulou diagnóstico preciso sobre os erros mais recorrentes no setor: CFOP incorreto no lançamento de insumos, custo de produção calculado sem segregação adequada entre mão de obra direta e custos indiretos de fabricação, e PIS/COFINS não cumulativo mal apurado em regimes de Lucro Real.</p>
<p>Para gestores industriais de Sete Lagoas que nunca passaram por auditoria tributária retroativa, o diagnóstico gratuito é o ponto de partida. A reunião acontece presencialmente na sede em Pará de Minas ou por chamada de vídeo, no horário mais conveniente para a rotina de produção.</p>"""

# ===========================================================================
# BUILD
# ===========================================================================

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(TEMPLATE, "r", encoding="utf-8") as f:
    html = f.read()

# 1. META tags
html = html.replace(
    "<title>Contador para Fábricas e Indústrias em Pará de Minas | AM Cabral</title>",
    f"<title>{TITLE}</title>"
)
html = html.replace(
    'content="Contador para Fábricas e Indústrias em Pará de Minas | AM Cabral"',
    f'content="{OG_TITLE}"'
)
html = html.replace(
    'content="Contabilidade industrial em Pará de Minas. ICMS-ST, IPI, CIAP, recuperação de créditos. 20 anos atendendo o polo industrial."',
    f'content="{META_DESC}"'
)
html = html.replace(
    'content="Contador especializado em indústria em Pará de Minas. Fundições, metalúrgicas, cerâmicas e laticínios. ICMS, IPI, CIAP, SPED Fiscal e recuperação de créditos. Diagnóstico gratuito."',
    f'content="{META_DESC}"'
)

# 2. Canonical + OG URL
html = html.replace(
    'href="https://amcabralblindagem.com.br/para-de-minas-mg/contador-para-fabricas-e-industrias/"',
    f'href="{PAGE_URL}"'
)
html = html.replace(
    'content="https://amcabralblindagem.com.br/para-de-minas-mg/contador-para-fabricas-e-industrias/"',
    f'content="{PAGE_URL}"'
)

# 3. Schema: WebPage @id and url
html = html.replace(
    '"@id": "https://amcabralblindagem.com.br/para-de-minas-mg/contador-para-fabricas-e-industrias/#webpage"',
    f'"@id": "{PAGE_URL}#webpage"'
)
html = html.replace(
    '"url": "https://amcabralblindagem.com.br/para-de-minas-mg/contador-para-fabricas-e-industrias/"',
    f'"url": "{PAGE_URL}"'
)
html = html.replace(
    '"about": {"@id": "https://amcabralblindagem.com.br/para-de-minas-mg/contador-para-fabricas-e-industrias/#service"}',
    f'"about": {{"@id": "{PAGE_URL}#service"}}'
)

# 4. Schema: BreadcrumbList
html = html.replace(
    '{"@type": "ListItem", "position": 2, "name": "Pará de Minas", "item": "https://amcabralblindagem.com.br/para-de-minas-mg/"}',
    f'{{"@type": "ListItem", "position": 2, "name": "Sete Lagoas", "item": "https://amcabralblindagem.com.br/{CIDADE_SLUG}/"}}'
)
html = html.replace(
    '{"@type": "ListItem", "position": 3, "name": "Contador para Fábricas e Indústrias", "item": "https://amcabralblindagem.com.br/para-de-minas-mg/contador-para-fabricas-e-industrias/"}',
    f'{{"@type": "ListItem", "position": 3, "name": "Contador para Fábricas e Indústrias", "item": "{PAGE_URL}"}}'
)

# 5. Schema: areaServed
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

# 6. Schema: geo coordinates
html = html.replace(
    '"latitude": -19.8607,\n          "longitude": -44.6126',
    f'"latitude": {GEO_LAT},\n          "longitude": {GEO_LNG}'
)

# 7. Schema: Service node (replace entire service block)
html = html.replace(
    '''      {
        "@type": "Service",
        "@id": "https://amcabralblindagem.com.br/para-de-minas-mg/contador-para-fabricas-e-industrias/#service",
        "name": "Contabilidade para Indústrias em Pará de Minas",
        "serviceType": "Contabilidade Industrial",
        "provider": {"@id": "https://amcabralblindagem.com.br/#organization"},
        "description": "Contabilidade especializada para fábricas, metalúrgicas, fundições e indústrias de Pará de Minas. ICMS, IPI, CIAP, SPED Fiscal e recuperação de créditos tributários industriais.",
        "areaServed": {"@type": "City", "name": "Pará de Minas", "sameAs": "https://www.wikidata.org/wiki/Q1749821"},
        "url": "https://amcabralblindagem.com.br/para-de-minas-mg/contador-para-fabricas-e-industrias/"
      }''',
    SERVICE_SCHEMA
)

# 8. Schema: WebSite description (keep as-is; it references Pará de Minas legitimately as physical address)

# 9. HERO TAG
html = html.replace(
    '<div class="hero-tag">Contabilidade Industrial · Pará de Minas · 20 Anos</div>',
    f'<div class="hero-tag">{HERO_TAG}</div>'
)

# 10. H1
html = html.replace(
    '<h1>Contador para <em>Fábricas e Indústrias</em><br>em Pará de Minas</h1>',
    f'<h1>{H1}</h1>'
)

# 11. HERO SUB
html = html.replace(
    'Contabilidade especializada para o polo industrial de Pará de Minas. ICMS, IPI, CIAP, SPED Fiscal e recuperação de créditos industriais. Quem entende de fábrica não trata indústria como comércio.',
    HERO_SUB
)

# 12. CRED STRIP
html = html.replace(
    '<div class="cred-item"><div class="cred-dot"></div><strong>20 anos</strong> atendendo o polo industrial de PDM</div>',
    CRED_ITEM1
)
html = html.replace(
    '<div class="cred-item"><div class="cred-dot"></div><strong>ICMS, IPI, CIAP</strong> e SPED Fiscal industrial</div>',
    CRED_ITEM3
)

# 13. BREADCRUMB
html = html.replace(
    '<a href="/para-de-minas-mg/">Pará de Minas</a>',
    f'<a href="/{CIDADE_SLUG}/">Sete Lagoas</a>'
)

# 14. AUTHORITY H2 + text
html = html.replace(
    'Fábrica não é comércio: a contabilidade errada custa caro',
    AUTH_H2
)
html = html.replace(
    'Pará de Minas tem um dos polos industriais mais diversificados do Centro-Oeste de Minas. O Distrito Industrial Antônio Júlio de Faria concentra metalúrgicas, fundições e cerâmicas. O segundo distrito, às margens da BR-262, abriga laticínios de escala regional e complexos de mineração. Cada segmento tem obrigações fiscais próprias: uma fundição que vende para montadoras de Betim tem tratamento de IPI diferente de uma cerâmica que distribui para o varejo de BH. Um contador sem experiência no setor industrial entrega o SPED errado, deixa crédito de ICMS na mesa e trata custo de produção como despesa operacional.',
    AUTH_P1
)
html = html.replace(
    'Na prática, isso significa que muitas fábricas de Pará de Minas estão pagando mais tributo do que deveriam. O crédito de IPI sobre matéria-prima, o CIAP das máquinas adquiridas e o diferencial de alíquota do ICMS-ST são itens que exigem domínio técnico e atenção mensal. Empresas que trocam de contador genérico para especialista industrial frequentemente descobrem créditos acumulados nos últimos 5 anos que superam o custo de um ano inteiro de honorários.',
    AUTH_P2
)

# 15. NUMBERS label
html = html.replace(
    '<div class="num-label">atendendo indústrias em Pará de Minas</div>',
    f'<div class="num-label">{NUM_LABEL_3}</div>'
)

# 16. DIFERENCIAL H2 + card 03
html = html.replace(
    'Três frentes onde geramos economia real para fábricas',
    DIF_H2
)
html = html.replace(
    'Para indústrias de Pará de Minas, o regime correto pode significar diferença de 15 a 30% na carga tributária. Avaliamos Lucro Real, Presumido e Simples Nacional considerando o mix de produtos e o perfil de compras da empresa.',
    DIF_P_03
)

# 17. AMANDA CTA STRIP
html = html.replace(
    'src="/para-de-minas-mg/escritorio-de-contabilidade/assets/amanda-cabral-contadora-cta-strip.jpg"',
    f'src="{AMANDA_IMG_SRC}"'
)
html = html.replace(
    'alt="Amanda Cabral, contadora especializada em fábricas e indústrias em Pará de Minas"',
    f'alt="{AMANDA_IMG_ALT}"'
)
html = html.replace(
    '<h2>Sua contadora está a 5 minutos do Distrito Industrial</h2>',
    f'<h2>{AMANDA_H2}</h2>'
)
html = html.replace(
    'Amanda Cabral atende fábricas e indústrias de Pará de Minas há 20 anos. Conhece os setores, os regimes tributários regionais e os problemas recorrentes de cada segmento, de fundição a laticínio.',
    AMANDA_P
)
html = html.replace(
    '<strong>20 anos</strong>\n        <span>no polo industrial de Pará de Minas</span>',
    f'<strong>{AMANDA_BADGE_VAL}</strong>\n        <span>{AMANDA_BADGE_SUB}</span>'
)

# 18. FORM H2
html = html.replace(
    '<h2 class="sec-h">Quanto a sua fábrica está deixando na mesa?</h2>',
    '<h2 class="sec-h">Quanto a sua fábrica de Sete Lagoas está deixando na mesa?</h2>'
)

# 19. CASES section
html = html.replace(
    'O que recuperamos para fábricas de Pará de Minas',
    CASES_H2
)
html = html.replace(
    '<div class="case-value">R$ 184 mil</div>',
    f'<div class="case-value">{CASE1_VAL}</div>'
)
html = html.replace(
    '<div class="case-tag">Fundição · Recuperação de créditos</div>',
    f'<div class="case-tag">{CASE1_TAG}</div>'
)
html = html.replace(
    'Fundição do Distrito Industrial com 45 funcionários. Auditoria retroativa de 5 anos revelou créditos de ICMS e IPI sobre matéria-prima e insumos não aproveitados pelo contador anterior. Valor recuperado em 8 meses.',
    CASE1_P
)
html = html.replace(
    '<div class="case-value">38% menos</div>',
    f'<div class="case-value">{CASE2_VAL}</div>'
)
html = html.replace(
    '<div class="case-tag">Cerâmica · Regime tributário</div>',
    f'<div class="case-tag">{CASE2_TAG}</div>'
)
html = html.replace(
    'Ind&#250;stria cer&#226;mica operando no Lucro Presumido sem avaliação técnica. Migração para o Lucro Real com créditos de PIS/COFINS sobre insumos reduziu a carga tributária em 38% no primeiro ano completo.',
    CASE2_P
)
html = html.replace(
    '<div class="case-value">R$ 67 mil</div>',
    f'<div class="case-value">{CASE3_VAL}</div>'
)
html = html.replace(
    '<div class="case-tag">Metalmec&#226;nica · CIAP</div>',
    f'<div class="case-tag">{CASE3_TAG}</div>'
)
html = html.replace(
    'Empresa de autopeças que nunca havia controlado o CIAP das máquinas adquiridas nos 3 anos anteriores. Levantamento das notas de aquisição gerou crédito de ICMS de R$ 67 mil aproveitado ao longo de 18 meses.',
    CASE3_P
)

# 20. MARQUEE
old_marquee = '''      <div class="marquee-item">Metalurgia</div>
      <div class="marquee-item">Fundições</div>
      <div class="marquee-item">Cer&#226;mica Industrial</div>
      <div class="marquee-item">Laticínios</div>
      <div class="marquee-item">Autopeças</div>
      <div class="marquee-item">Mineração</div>
      <div class="marquee-item">Metalmec&#226;nica</div>
      <div class="marquee-item">Alimentos &amp; Bebidas</div>
      <div class="marquee-item">Pl&#225;sticos e Borracha</div>
      <div class="marquee-item">Embalagens</div>
      <div class="marquee-item">Constru&#231;&#227;o Civil</div>
      <div class="marquee-item">Têxtil</div>
      <div class="marquee-item">Metalurgia</div>
      <div class="marquee-item">Fundições</div>
      <div class="marquee-item">Cer&#226;mica Industrial</div>
      <div class="marquee-item">Laticínios</div>
      <div class="marquee-item">Autopeças</div>
      <div class="marquee-item">Mineração</div>
      <div class="marquee-item">Metalmec&#226;nica</div>
      <div class="marquee-item">Alimentos &amp; Bebidas</div>
      <div class="marquee-item">Pl&#225;sticos e Borracha</div>
      <div class="marquee-item">Embalagens</div>
      <div class="marquee-item">Constru&#231;&#227;o Civil</div>
      <div class="marquee-item">Têxtil</div>'''
html = html.replace(old_marquee, MARQUEE_HTML)

# 21. DEPOIMENTOS
html = html.replace(
    '"Nossa fundição trabalhou 4 anos sem aproveitar o CIAP das prensas e fornos. A Amanda fez o levantamento em 2 semanas e recuperamos quase R$ 90 mil em crédito. Hoje não deixo nada na mesa."',
    DEP1_TEXT
)
html = html.replace(
    '<div class="dep-avatar">RM</div>',
    f'<div class="dep-avatar">{DEP1_INIT}</div>'
)
html = html.replace(
    '<strong>R. Mendes</strong>',
    f'<strong>{DEP1_NOME}</strong>'
)
html = html.replace(
    '<span>S&#243;cio-Fundador, Fundição no Distrito Industrial</span>',
    f'<span>{DEP1_ROLE}</span>'
)

html = html.replace(
    '"Eu nem sabia que o contador anterior entregava o SPED errado. Quando a Amanda auditou, encontrou divergências em 3 anos de escrituração. Migramos de contador e nunca mais tivemos intimação fiscal."',
    DEP2_TEXT
)
html = html.replace(
    '<div class="dep-avatar">FC</div>',
    f'<div class="dep-avatar">{DEP2_INIT}</div>'
)
html = html.replace(
    '<strong>F. Costa</strong>',
    f'<strong>{DEP2_NOME}</strong>'
)
html = html.replace(
    '<span>Diretora Industrial, Cer&#226;mica em Pará de Minas</span>',
    f'<span>{DEP2_ROLE}</span>'
)

html = html.replace(
    '"O regime tributário certo fez diferença real. No Presumido, pagávamos mais do que deveríamos. Com o estudo técnico da Amanda, migramos para o Lucro Real e reduzimos o imposto em mais de um terço."',
    DEP3_TEXT
)
html = html.replace(
    '<div class="dep-avatar">PO</div>',
    f'<div class="dep-avatar">{DEP3_INIT}</div>'
)
html = html.replace(
    '<strong>P. Oliveira</strong>',
    f'<strong>{DEP3_NOME}</strong>'
)
html = html.replace(
    '<span>Propriet&#225;rio, Metalúrgica em Pará de Minas</span>',
    f'<span>{DEP3_ROLE}</span>'
)

# 22. PROCESSO H2
html = html.replace(
    'Como funciona a auditoria tributária na sua fábrica: 4 etapas com resultado garantido',
    PROC_H2
)

# 23. FAQ H2
html = html.replace(
    'Dúvidas comuns de industriais em Pará de Minas',
    FAQ_H2
)

# 24. CONTENT SEO — replace CONTEXT_LOCAL section (the 4 paragraphs of knowledge content)
old_content_p = ('<p>O IPI incide na saída do produto industrializado, mas o crédito se forma nas entradas de matéria-prima '
                 'e insumos aplicados na produção.')
new_content_p = '<p>O parque fabril de Sete Lagoas reúne plantas de transformação que geram obrigações fiscais de alta complexidade.'
html = html.replace(old_content_p, new_content_p, 1)

# Replace full content-seo section's content blocks
old_content_block = """        <div class="content-block reveal">
          <h3>Por que o IPI é diferente para cada fábrica</h3>
          <p>O IPI incide na saída do produto industrializado, mas o crédito se forma nas entradas de matéria-prima e insumos aplicados na produção. A alíquota varia conforme a NCM de cada produto. Uma fundição que vende peças brutas tem tratamento diferente de uma que fornece peças usinadas. O domínio da tabela TIPI e dos benefícios fiscais setoriais é o que separa o aproveitamento integral do crédito da perda silenciosa de caixa.</p>
        </div>
        <div class="content-block reveal">
          <h3>CIAP: o crédito que 80% das fábricas ignoram</h3>
          <p>O CIAP permite que a indústria recupere o ICMS pago na aquisição de máquinas e equipamentos do ativo imobilizado em 48 prestações mensais. Para uma fábrica que comprou R$ 500 mil em equipamentos ao longo de 3 anos, o crédito potencial pode superar R$ 60 mil. A maioria das empresas nem sabe que tem esse direito, especialmente quando o equipamento foi adquirido em outro estado com diferencial de alíquota.</p>
        </div>
        <div class="content-block reveal">
          <h3>Lucro Real vs. Presumido para indústrias</h3>
          <p>Para indústrias com margens apertadas, o Lucro Real quase sempre é mais vantajoso. A possibilidade de deduzir despesas reais, aproveitar créditos de PIS/COFINS não cumulativos e compensar prejuízos fiscais cria uma estrutura de apuração mais justa. O Lucro Presumido aplica percentual sobre a receita sem considerar a estrutura de custos, o que penaliza setores como fundição, onde a matéria-prima representa 60% ou mais do faturamento.</p>
        </div>
        <div class="content-block reveal">
          <h3>SPED Fiscal incorreto: quando o erro é silencioso</h3>
          <p>O SPED Fiscal de indústrias tem registros específicos para produção, controle de estoque por lote e movimentação de matéria-prima que não existem no SPED de empresas comerciais. Um contador sem vivência industrial frequentemente entrega o SPED com esses registros ausentes ou incorretos. O fisco não rejeita o arquivo imediatamente, mas o erro fica registrado e pode resultar em autuação retroativa com multa de 75% sobre o tributo apurado a menor. O Bloco K do SPED Fiscal exige escrituração detalhada da produção e do estoque, registro a registro. Poucos contadores sem vivência industrial sabem montar esse módulo corretamente.</p>
        </div>"""

new_content_block = """        <div class="content-block reveal">
          <h3>SPED Fiscal industrial: por que o Bloco K cobra caro quando está errado</h3>
          <p>O Bloco K do SPED EFD-ICMS/IPI exige o controle registro a registro da produção e do inventário. Quando entregue com lacunas, o fisco não rejeita o arquivo imediatamente. O erro fica armazenado e pode originar autuação retroativa com acréscimo de 75% sobre o tributo apurado a menor, descoberto apenas numa verificação externa. Fábricas de Sete Lagoas que nunca auditaram o SPED retroativamente frequentemente encontram divergências em três ou mais exercícios fiscais.</p>
        </div>
        <div class="content-block reveal">
          <h3>CIAP: 48 parcelas de crédito que a maioria das plantas desconhece</h3>
          <p>O CIAP permite recuperar o ICMS pago na compra de máquinas e equipamentos do ativo imobilizado em 48 prestações mensais. Cada aquisição dá origem a parcelas individuais que precisam ser controladas separadamente. Para uma planta que comprou R$ 600 mil em equipamentos ao longo de quatro anos, o crédito potencial pode superar R$ 70 mil. A maioria das empresas nem sabe que tem esse direito, especialmente quando o equipamento foi adquirido de outro estado com diferencial de alíquota.</p>
        </div>
        <div class="content-block reveal">
          <h3>Lucro Real ou Presumido: qual regime favorece a indústria de Sete Lagoas?</h3>
          <p>Para plantas com margens apertadas, o Lucro Real quase sempre é mais vantajoso. A possibilidade de deduzir despesas reais, aproveitar créditos de PIS/COFINS não cumulativos sobre insumos e embalagens, e compensar prejuízos fiscais cria uma estrutura de apuração mais justa. O Lucro Presumido aplica percentual fixo sobre a receita sem considerar a estrutura de custos, o que penaliza operações com alta proporção de matéria-prima, como autopeças e farmacêutica.</p>
        </div>
        <div class="content-block reveal">
          <h3>Como o CFOP incorreto na entrada de insumos gera passivo tributário silencioso</h3>
          <p>O CFOP de cada nota fiscal de entrada determina se o crédito de ICMS e IPI sobre aquele insumo pode ser aproveitado. Um CFOP lançado incorretamente bloqueia o crédito, que fica represado sem gerar benefício de caixa. Nas fábricas de Sete Lagoas, esse erro ocorre com mais frequência em compras interestaduais de matéria-prima, onde o código de operação muda conforme a origem do fornecedor. Auditoria retroativa de cinco anos pode revelar volumes expressivos de crédito disponível para recuperação.</p>
        </div>"""

html = html.replace(old_content_block, new_content_block)

# 25. HUB links
html = html.replace(
    '<a href="/para-de-minas-mg/contador-especializado-em-holding/" class="hub-card reveal">',
    f'<a href="{HUB_HOLDING_HREF}" class="hub-card reveal">'
)
html = html.replace(
    '<a href="/para-de-minas-mg/trocar-de-contador/" class="hub-card reveal">',
    f'<a href="{HUB_TROCAR_HREF}" class="hub-card reveal">'
)

# 26. FOOTER city column
html = html.replace(
    '''        <div class="footer-col">
          <div class="footer-heading">Pará de Minas</div>
          <ul>
            <li><a href="/para-de-minas-mg/">Escritório em PDM</a></li>
            <li><a href="/para-de-minas-mg/escritorio-de-contabilidade/">Escritório de Contabilidade</a></li>
            <li><a href="/para-de-minas-mg/contador-especializado-em-holding/">Holding em Pará de Minas</a></li>
            <li><a href="/para-de-minas-mg/trocar-de-contador/">Trocar de Contador</a></li>
            <li><a href="/cidades-atendidas/">Cidades Atendidas</a></li>
          </ul>
        </div>''',
    FOOTER_CITY_COL
)

# 27. Extra Pará de Minas references in content
# numbers section label (if present)
html = html.replace(
    '<div class="num-label">de atuação em Pará de Minas</div>',
    '<div class="num-label">de atuação em Minas Gerais</div>'
)
# diferencial card regional reference
html = html.replace(
    'como os da região industrial de Pará de Minas.',
    f'como os da região industrial de {CIDADE}.'
)

# 28. Schema: AccountingService addressLocality
html = html.replace(
    '"addressLocality": "Pará de Minas",',
    '"addressLocality": "Sete Lagoas",'
)

# 29. Schema: WebPage name (BreadcrumbList item 3 name)
html = html.replace(
    '"name": "Contador para Fábricas e Indústrias em Pará de Minas | AM Cabral"',
    f'"name": "{TITLE}"'
)

# 30. Schema: Service name and description (any residual)
html = html.replace(
    '"name": "Contabilidade para Indústrias em Pará de Minas"',
    '"name": "Contabilidade para Indústrias em Sete Lagoas"'
)
html = html.replace(
    '"description": "Contabilidade especializada para fábricas, metalúrgicas, fundições e indústrias de Pará de Minas. ICMS, IPI, CIAP, SPED Fiscal e recuperação de créditos tributários industriais."',
    '"description": "Contabilidade especializada para fábricas, autopeças, farmacêuticas e indústrias de Sete Lagoas. SPED Fiscal, CIAP, IPI e recuperação de créditos tributários industriais."'
)
html = html.replace(
    '"areaServed": {"@type": "City", "name": "Pará de Minas", "sameAs": "https://www.wikidata.org/wiki/Q1749821"}',
    '"areaServed": {"@type": "City", "name": "Sete Lagoas", "sameAs": "https://www.wikidata.org/wiki/Q1059948"}'
)

# 31. Schema: Organization description
html = html.replace(
    '"description": "Contabilidade especializada para empresários em Pará de Minas e região de Minas Gerais."',
    '"description": "Contabilidade especializada para empresários em Sete Lagoas e região de Minas Gerais."'
)

# 32. Header mega-menu span
html = html.replace(
    '<strong>Cidades Atendidas</strong><span>Atendimento presencial em Pará de Minas e toda a região de MG</span>',
    '<strong>Cidades Atendidas</strong><span>Atendimento presencial em Minas Gerais e toda a região de MG</span>'
)

# 33. DIF card 03 paragraph (residual from partial replacement)
html = html.replace(
    '<p>Para indústrias de Pará de Minas, o regime correto pode significar diferença de 15 a 30% na carga tributária. Avaliamos Lucro Real, Presumido e Simples Nacional considerando o mix de produtos e o perfil de compras.</p>',
    f'<p>{DIF_P_03}</p>'
)

# 34. Footer address — keep as-is (physical office address, legitimate)

# 35. WhatsApp JS message
html = html.replace(
    'contabilidade industrial em Pará de Minas.',
    'contabilidade industrial em Sete Lagoas.'
)

# ===========================================================================
# QA
# ===========================================================================

placeholders = html.count('{{')
pdm_count = html.count('Pará de Minas')
canonical_ok = PAGE_URL in html

print(f"\n=== QA: Sete Lagoas — Fábricas & Indústrias ===")
print(f"  Placeholders '{{{{' restantes : {placeholders}")
print(f"  'Pará de Minas' no HTML      : {pdm_count}")
print(f"  Canonical URL presente        : {canonical_ok}")
print(f"  Output                        : {OUTPUT}")

with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write(html)

print(f"\n  Arquivo gerado com sucesso: {OUTPUT}")
print(f"  URL: {PAGE_URL}")
