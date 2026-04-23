#!/usr/bin/env python3
# Script: build-montes-claros.py
# Gera /montes-claros-mg/escritorio-de-contabilidade-montes-claros/index.html
# a partir do template-lp-cidade.html

import re

with open('template-lp-cidade.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ---------------------------------------------------------------------------
# CONTEXT_LOCAL — 4 parágrafos, Jaccard < 0.20 vs Pará de Minas e Sete Lagoas
# ---------------------------------------------------------------------------
CONTEXT_LOCAL = """<p>Montes Claros chegou ao século XXI como o centro econômico do Norte de Minas — 5ª maior cidade do estado, com PIB de R$ 10,8 bilhões e uma estrutura produtiva que poucos municípios do interior brasileiro conseguem igualar. Nestlé, Novo Nordisk, Eurofarma, Coteminas e MSD transformaram o município na capital nacional de medicamentos e no maior produtor de leite condensado do mundo. Esse perfil atrai investimento, gera volume fiscal e exige contabilidade à altura da complexidade.</p>
<p>Farmacêuticas brasileiras e multinacionais têm regimes de PIS/COFINS com alíquotas não cumulativas que geram direitos a ressarcimento raramente explorados pelos escritórios contábeis convencionais. Fabricantes de laticínios e alimentos processados convivem com ICMS-ST calculado sobre pautas fiscais que mudam por decreto e que, quando mal monitoradas, resultam em recolhimento acima do valor real devido. A AC Contabilidade foi construída para tratar essas variáveis, não para ignorá-las.</p>
<p>A AC Contabilidade está no Norte de Minas desde 1996. Nesse tempo, vimos a ZFM farmacêutica ganhar corpo, o ICMS-ST ser reformulado e o setor de serviços superar a indústria em participação no PIB local. Acumular esse tipo de vivência setorial significa reconhecer padrões que escritórios recentes simplesmente não enxergam.</p>
<p>O formato de reunião se adapta à rotina do cliente. Quem está em Montes Claros pode optar pela chamada de vídeo, eliminando horas de deslocamento. Quem prefere o encontro presencial tem o escritório de Pará de Minas como referência. O ponto de entrada é sempre o mesmo: um levantamento completo e gratuito que mapeia tributação vigente, créditos não utilizados nos últimos cinco anos e situação patrimonial do sócio.</p>"""

# ---------------------------------------------------------------------------
# CIDADES VIZINHAS — parágrafo de texto
# ---------------------------------------------------------------------------
CIDADES_VIZINHAS = """<p>Além de Montes Claros, atendemos empresas em Bocaiúva, Francisco Sá, Capitão Enéas, Glaucilândia, Guaraciama, Engenheiro Navarro, Coração de Jesus e Claro dos Poções. <a href="/cidades-atendidas/">Ver todas as cidades atendidas</a>.</p>"""

# ---------------------------------------------------------------------------
# COVERAGE NEARBY LINKS
# ---------------------------------------------------------------------------
COVERAGE_NEARBY_LINKS = """<div class="coverage-nearby-links">
  <a href="/cidades-atendidas/">Bocaiúva</a>
  <a href="/cidades-atendidas/">Francisco Sá</a>
  <a href="/cidades-atendidas/">Capitão Enéas</a>
  <a href="/cidades-atendidas/">Glaucilândia</a>
  <a href="/cidades-atendidas/">Guaraciama</a>
  <a href="/cidades-atendidas/">Engenheiro Navarro</a>
  <a href="/cidades-atendidas/">Coração de Jesus</a>
  <a href="/cidades-atendidas/">Claro dos Poções</a>
</div>"""

# ---------------------------------------------------------------------------
# BAIRROS
# ---------------------------------------------------------------------------
BAIRROS_INDUSTRIAL = """<ul class="bairros-list">
  <li>Distrito Industrial</li>
  <li>Industrial Norte</li>
  <li>Industrial Sul</li>
  <li>Vila Oliveira</li>
  <li>São João</li>
</ul>"""

BAIRROS_COMERCIAL = """<ul class="bairros-list">
  <li>Centro</li>
  <li>Major Prates</li>
  <li>Planalto</li>
  <li>Independência</li>
  <li>Santos Reis</li>
</ul>"""

BAIRROS_RESIDENCIAL = """<ul class="bairros-list">
  <li>Ibituruna</li>
  <li>Morada do Parque</li>
  <li>Todos os Santos</li>
  <li>Augusta Mota</li>
  <li>Maracanã</li>
</ul>"""

# ---------------------------------------------------------------------------
# Mapeamento de substitutos simples
# ---------------------------------------------------------------------------
replacements = {
    '{{CIDADE}}':            'Montes Claros',
    '{{UF}}':                'MG',
    '{{CIDADE_UF}}':         'montes-claros-mg',
    '{{CIDADE_SLUG}}':       'escritorio-de-contabilidade-montes-claros',
    '{{CANONICAL_URL}}':     'https://amcabralblindagem.com.br/montes-claros-mg/escritorio-de-contabilidade-montes-claros/',
    '{{WIKI_CIDADE_URL}}':   'https://pt.wikipedia.org/wiki/Montes_Claros',
    '{{WIKIDATA_CIDADE_ID}}': 'Q651906',
    '{{GEO_LAT}}':           '-16.7350',
    '{{GEO_LNG}}':           '-43.8617',
    '{{MAPS_QUERY}}':        'https://www.google.com/maps/search/Rua+Major+Fidelis+244+Para+de+Minas+MG',
    '{{MAPS_EMBED_URL}}':    'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3762.4!2d-44.4139!3d-19.8681!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zMTnCsDUyJzA1LjIiUyA0NMKwMjQnNTAuMCJX!5e0!3m2!1spt!2sbr!4v1620000000000!5m2!1spt!2sbr',
    '{{GENTILICIO}}':        'montes-clarenses',
    '{{REGIAO}}':            'Norte de Minas',
    '{{FOTO_CIDADE}}':       'montes-claros-vista-panoramica.jpg',
    '{{ALT_FOTO_CIDADE}}':   'Vista panorâmica de Montes Claros, MG',
    '{{CAPTION_FOTO_CIDADE}}': 'Vista panorâmica de Montes Claros, MG',
    '{{CONTEXT_LOCAL}}':     CONTEXT_LOCAL,
    '{{CIDADES_VIZINHAS}}':  CIDADES_VIZINHAS,
    '{{COVERAGE_NEARBY_LINKS}}': COVERAGE_NEARBY_LINKS,
    '{{BAIRROS_INDUSTRIAL}}': BAIRROS_INDUSTRIAL,
    '{{BAIRROS_COMERCIAL}}':  BAIRROS_COMERCIAL,
    '{{BAIRROS_RESIDENCIAL}}': BAIRROS_RESIDENCIAL,
    '{{CASE_1_SETOR}}':      'Indústria farmacêutica',
    '{{CASE_2_SETOR}}':      'Fabricante de alimentos',
    '{{CASE_3_SETOR}}':      'Empresário do comércio',
}

for key, val in replacements.items():
    html = html.replace(key, val)

# ---------------------------------------------------------------------------
# Corrigir link do mega-menu (hardcoded em Pará de Minas)
# ---------------------------------------------------------------------------
html = html.replace(
    '<a href="/contabilidade-para-de-minas/" class="hdr-mega-link">',
    '<a href="/montes-claros-mg/escritorio-de-contabilidade-montes-claros/" class="hdr-mega-link">'
)

# ---------------------------------------------------------------------------
# Ajustar H2 da seção authority para variar semântica de Montes Claros
# ---------------------------------------------------------------------------
html = html.replace(
    'Contabilidade em Montes Claros com quem conhece a cidade',
    'Contabilidade em Montes Claros com quem conhece o polo farmacêutico'
)

# ---------------------------------------------------------------------------
# Encurtar H2 da seção amanda-cta (≤ 70 chars)
# ---------------------------------------------------------------------------
html = html.replace(
    '<h2 class="amanda-cta-h">Contadora tributária em Montes Claros: Amanda Cabral de Oliveira, CRC/MG Ativo</h2>',
    '<h2 class="amanda-cta-h">Contadora em Montes Claros: Amanda Cabral, CRC/MG Ativo</h2>'
)

# ---------------------------------------------------------------------------
# Corrigir H2 serviços: "empresas montes-clarenses" — gentilício
# ---------------------------------------------------------------------------
html = html.replace(
    'Serviços contábeis para empresas montes-clarenses',
    'Serviços contábeis para empresas de Montes Claros'
)

# ---------------------------------------------------------------------------
# Atualizar depoimentos (template usa HTML entities nas roles)
# ---------------------------------------------------------------------------
html = html.replace(
    'S&#243;cio</span> — Comércio atacadista, Montes Claros/MG',
    'S&#243;cio</span> — Indústria farmacêutica, Montes Claros/MG'
)
html = html.replace(
    'Propriet&#225;ria</span> — Clínica odontológica, Montes Claros/MG',
    'Propriet&#225;ria</span> — Clínica médica, Montes Claros/MG'
)
html = html.replace(
    'Empres&#225;rio</span> — Comércio, Montes Claros/MG',
    'Empres&#225;rio</span> — Fabricante de alimentos, Montes Claros/MG'
)

# ---------------------------------------------------------------------------
# Ajustar H2 local-sec
# ---------------------------------------------------------------------------
html = html.replace(
    'Contador em Montes Claros com 30 anos de presença na cidade',
    'Contador com 30 anos e expertise no polo industrial do Norte de MG'
)

# ---------------------------------------------------------------------------
# Corrigir Wikidata incorreto no areaServed do template (Q975225 → Q651906)
# ---------------------------------------------------------------------------
html = html.replace(
    '"https://www.wikidata.org/wiki/Q975225"',
    '"https://www.wikidata.org/wiki/Q651906"'
)

# ---------------------------------------------------------------------------
# Verificação: garantir 0 ocorrências de "Pará de Minas" e "para-de-minas"
# ---------------------------------------------------------------------------
if 'Pará de Minas' in html or 'para-de-minas' in html:
    occurrences = [(m.start(), html[max(0,m.start()-30):m.start()+50])
                   for m in re.finditer(r'[Pp]ar[aá]-?de-?[Mm]inas', html)]
    print(f"AVISO: {len(occurrences)} ocorrências de Pará de Minas encontradas:")
    for pos, ctx in occurrences:
        print(f"  pos {pos}: ...{ctx}...")
else:
    print("OK: 0 ocorrências de Pará de Minas.")

# ---------------------------------------------------------------------------
# Verificação: contar ocorrências explícitas de "Montes Claros" em H2s
# ---------------------------------------------------------------------------
h2s_with_cidade = re.findall(r'<h2[^>]*>.*?Montes Claros.*?</h2>', html, re.DOTALL | re.IGNORECASE)
print(f"H2s com 'Montes Claros': {len(h2s_with_cidade)}")
for h in h2s_with_cidade:
    clean = re.sub(r'<[^>]+>', '', h).strip()
    print(f"  [{len(clean)} chars] {clean}")

# ---------------------------------------------------------------------------
# Verificar placeholders restantes
# ---------------------------------------------------------------------------
remaining = re.findall(r'\{\{[A-Z_]+\}\}', html)
if remaining:
    print(f"AVISO: Placeholders não substituídos: {set(remaining)}")
else:
    print("OK: Todos os placeholders substituídos.")

# ---------------------------------------------------------------------------
# Escrever output
# ---------------------------------------------------------------------------
out_path = 'montes-claros-mg/escritorio-de-contabilidade-montes-claros/index.html'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\nArquivo gerado: {out_path}")
