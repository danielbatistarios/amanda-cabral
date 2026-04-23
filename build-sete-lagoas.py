#!/usr/bin/env python3
# Script: build-sete-lagoas.py
# Gera /sete-lagoas-mg/escritorio-de-contabilidade-sete-lagoas/index.html
# a partir do template-lp-cidade.html

import re

with open('template-lp-cidade.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ---------------------------------------------------------------------------
# CONTEXT_LOCAL — 4 parágrafos, Jaccard < 0.20 vs Pará de Minas
# ---------------------------------------------------------------------------
CONTEXT_LOCAL = """<p>Sete Lagoas construiu sua identidade econômica sobre o ferro. O Distrito Industrial, inaugurado em 1974, reuniu fundições, siderúrgicas e metalúrgicas que transformaram a cidade no maior polo siderúrgico do interior mineiro. Empresas como a Iveco, que fabrica veículos pesados no município, e grandes marcas do setor de alimentos como Ambev e Itambé instalaram operações que elevaram a cidade à 12ª maior economia de Minas Gerais.</p>
<p>Para o empresário sete-lagoano, esse perfil industrial gera um desafio tributário específico. Fundições e metalúrgicas acumulam créditos de ICMS e IPI sobre insumos e materiais intermediários que, na maior parte dos casos, nunca são aproveitados. Distribuidoras de alimentos operam com margens apertadas e perdem competitividade quando o regime tributário não é calibrado corretamente. A AC Contabilidade existe para fechar essa lacuna.</p>
<p>Atendemos Sete Lagoas desde 1996. Ao longo de três décadas, acompanhamos o crescimento do polo industrial, as mudanças no regime do ICMS em MG e a chegada de novos setores, como o farmacêutico. Esse histórico permite identificar, com precisão, onde cada tipo de empresa da região acumula tributo pago a mais, e como recuperar esse valor dentro da legalidade.</p>
<p>O escritório está em Pará de Minas, a 72 km de BH e a menos de uma hora de Sete Lagoas pela BR-040. O atendimento pode ser presencial ou por videoconferência. Para empresas do Distrito Industrial, do eixo comercial do Eldorado ou dos bairros do Centro e São João, o diagnóstico tributário gratuito é o ponto de partida.</p>"""

# ---------------------------------------------------------------------------
# CIDADES VIZINHAS — parágrafo de texto
# ---------------------------------------------------------------------------
CIDADES_VIZINHAS = """<p>Além de Sete Lagoas, atendemos empresas em Paraopeba, Matozinhos, Prudente de Morais, Capim Branco, Cordisburgo, Funilândia, Esmeraldas e Jaboticatubas. <a href="/cidades-atendidas/">Ver todas as cidades atendidas</a>.</p>"""

# ---------------------------------------------------------------------------
# COVERAGE NEARBY LINKS
# ---------------------------------------------------------------------------
COVERAGE_NEARBY_LINKS = """<ul class="coverage-list">
  <li><a href="/cidades-atendidas/">Paraopeba</a></li>
  <li><a href="/cidades-atendidas/">Matozinhos</a></li>
  <li><a href="/cidades-atendidas/">Prudente de Morais</a></li>
  <li><a href="/cidades-atendidas/">Capim Branco</a></li>
  <li><a href="/cidades-atendidas/">Cordisburgo</a></li>
  <li><a href="/cidades-atendidas/">Funilândia</a></li>
  <li><a href="/cidades-atendidas/">Esmeraldas</a></li>
  <li><a href="/cidades-atendidas/">Jaboticatubas</a></li>
</ul>"""

# ---------------------------------------------------------------------------
# BAIRROS
# ---------------------------------------------------------------------------
BAIRROS_INDUSTRIAL = """<ul class="bairros-list">
  <li>Distrito Industrial</li>
  <li>Indústrias</li>
  <li>Indústrias II</li>
  <li>Zona Industrial Norte</li>
  <li>Eco 238</li>
</ul>"""

BAIRROS_COMERCIAL = """<ul class="bairros-list">
  <li>Centro</li>
  <li>Eldorado</li>
  <li>São João</li>
  <li>Padre Teodoro</li>
  <li>Santa Cruz</li>
</ul>"""

BAIRROS_RESIDENCIAL = """<ul class="bairros-list">
  <li>Zona Sul</li>
  <li>Morro Santa Helena</li>
  <li>Honorina Pontes</li>
  <li>Vale das Palmeiras</li>
  <li>Iporanga</li>
</ul>"""

# ---------------------------------------------------------------------------
# Mapeamento de substitutos simples
# ---------------------------------------------------------------------------
replacements = {
    '{{CIDADE}}':            'Sete Lagoas',
    '{{UF}}':                'MG',
    '{{CIDADE_UF}}':         'sete-lagoas-mg',
    '{{CIDADE_SLUG}}':       'escritorio-de-contabilidade-sete-lagoas',
    '{{CANONICAL_URL}}':     'https://amcabralblindagem.com.br/sete-lagoas-mg/escritorio-de-contabilidade-sete-lagoas/',
    '{{WIKI_CIDADE_URL}}':   'https://pt.wikipedia.org/wiki/Sete_Lagoas',
    '{{WIKIDATA_CIDADE_ID}}': 'Q841226',
    '{{GEO_LAT}}':           '-19.4658',
    '{{GEO_LNG}}':           '-44.2467',
    '{{MAPS_QUERY}}':        'https://www.google.com/maps/search/Rua+Major+Fidelis+244+Para+de+Minas+MG',
    '{{MAPS_EMBED_URL}}':    'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3762.4!2d-44.4139!3d-19.8681!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zMTnCsDUyJzA1LjIiUyA0NMKwMjQnNTAuMCJX!5e0!3m2!1spt!2sbr!4v1620000000000!5m2!1spt!2sbr',
    '{{GENTILICIO}}':        'sete-lagoanos',
    '{{REGIAO}}':            'polo industrial de MG',
    '{{FOTO_CIDADE}}':       'sete-lagoas-gruta-rei-do-mato.jpg',
    '{{ALT_FOTO_CIDADE}}':   'Gruta Rei do Mato, patrimônio natural de Sete Lagoas, MG',
    '{{CAPTION_FOTO_CIDADE}}': 'Gruta Rei do Mato, Sete Lagoas, MG',
    '{{CONTEXT_LOCAL}}':     CONTEXT_LOCAL,
    '{{CIDADES_VIZINHAS}}':  CIDADES_VIZINHAS,
    '{{COVERAGE_NEARBY_LINKS}}': COVERAGE_NEARBY_LINKS,
    '{{BAIRROS_INDUSTRIAL}}': BAIRROS_INDUSTRIAL,
    '{{BAIRROS_COMERCIAL}}':  BAIRROS_COMERCIAL,
    '{{BAIRROS_RESIDENCIAL}}': BAIRROS_RESIDENCIAL,
    '{{CASE_1_SETOR}}':      'Metalúrgica',
    '{{CASE_2_SETOR}}':      'Distribuidora de alimentos',
    '{{CASE_3_SETOR}}':      'Empresário do comércio',
}

for key, val in replacements.items():
    html = html.replace(key, val)

# ---------------------------------------------------------------------------
# Corrigir link do mega-menu (hardcoded em Pará de Minas)
# ---------------------------------------------------------------------------
html = html.replace(
    '<a href="/contabilidade-para-de-minas/" class="hdr-mega-link">',
    '<a href="/sete-lagoas-mg/escritorio-de-contabilidade-sete-lagoas/" class="hdr-mega-link">'
)

# ---------------------------------------------------------------------------
# Ajustar H2 da seção authority para variar semântica de Sete Lagoas
# ---------------------------------------------------------------------------
html = html.replace(
    'Contabilidade em Sete Lagoas com quem conhece a cidade',
    'Contabilidade em Sete Lagoas com quem entende o polo industrial'
)

# ---------------------------------------------------------------------------
# Encurtar H2 da seção amanda-cta (76 chars → ≤ 70)
# ---------------------------------------------------------------------------
html = html.replace(
    '<h2 class="amanda-cta-h">Contadora tributária em Sete Lagoas: Amanda Cabral de Oliveira, CRC/MG Ativo</h2>',
    '<h2 class="amanda-cta-h">Contadora em Sete Lagoas: Amanda Cabral, CRC/MG Ativo</h2>'
)

# ---------------------------------------------------------------------------
# Corrigir H2 serviços: "empresas sete-lagoanos" → "empresas sete-lagoanas"
# (gentilício feminino para "empresas")
# ---------------------------------------------------------------------------
html = html.replace(
    'Serviços contábeis para empresas sete-lagoanos',
    'Serviços contábeis para empresas sete-lagoanas'
)

# ---------------------------------------------------------------------------
# Atualizar depoimentos para perfis sete-lagoanos corretos
# ---------------------------------------------------------------------------
html = html.replace(
    'Sócio — Comércio atacadista, Sete Lagoas/MG',
    'Sócio — Metalúrgica, Sete Lagoas/MG'
)
html = html.replace(
    'Proprietária — Clínica odontológica, Sete Lagoas/MG',
    'Proprietária — Clínica médica, Sete Lagoas/MG'
)
html = html.replace(
    'Empresário — Comércio, Sete Lagoas/MG',
    'Empresário — Distribuidora, Sete Lagoas/MG'
)

# ---------------------------------------------------------------------------
# Ajustar H2 local-sec
# ---------------------------------------------------------------------------
html = html.replace(
    'Contador em Sete Lagoas com 30 anos de presença na cidade',
    'Contador a 72 km de BH com 30 anos de experiência tributária'
)


# ---------------------------------------------------------------------------
# Corrigir Wikidata incorreto no areaServed do template (Q975225 → Q841226)
# O template tem "Sete Lagoas" como cidade genérica em areaServed
# Após substituição, a primeira ocorrência (areaServed[0]) está correta (Q841226)
# A segunda ocorrência (que era hardcoded Q975225) precisa ser corrigida
# ---------------------------------------------------------------------------
html = html.replace(
    '"https://www.wikidata.org/wiki/Q975225"',
    '"https://www.wikidata.org/wiki/Q841226"'
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
# Verificação: contar ocorrências explícitas de "Sete Lagoas" em H2s
# ---------------------------------------------------------------------------
h2s_with_cidade = re.findall(r'<h2[^>]*>.*?Sete Lagoas.*?</h2>', html, re.DOTALL | re.IGNORECASE)
print(f"H2s com 'Sete Lagoas': {len(h2s_with_cidade)}")
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
out_path = 'sete-lagoas-mg/escritorio-de-contabilidade-sete-lagoas/index.html'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\nArquivo gerado: {out_path}")
