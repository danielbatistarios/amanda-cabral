#!/usr/bin/env python3
# generate-all-lps.py
# Gera todas as 22 LPs de cidades novas em sequencia.
# Executa Jaccard check contra corpus aprovado antes de escrever cada arquivo.
# Cria diretórios, gera index.html e build script individual para cada cidade.

import re, os, sys

# ---------------------------------------------------------------------------
# JACCARD ENGINE (replica jaccard-corpus.py)
# ---------------------------------------------------------------------------

def tokenize(text):
    text = re.sub(r'<[^>]+>', ' ', text)
    text = text.lower()
    return set(re.findall(r'[a-záàâãéêíóôõúüç]+', text))

def jaccard(a, b):
    sa, sb = tokenize(a), tokenize(b)
    if not (sa | sb): return 0.0
    return len(sa & sb) / len(sa | sb)

CORPUS = {}

CORPUS["Pará de Minas"] = """<p>Pará de Minas construiu sua economia sobre dois pilares complementares: a indústria de transformação e um comércio varejista que serve toda a região Oeste de Minas. O polo industrial concentra metalurgia, laticínios, indústria química e têxtil — setores que respondem por mais de 40% do PIB municipal. O comércio, por sua vez, atrai consumidores de dezenas de municípios vizinhos, tornando a cidade referência regional em serviços.</p>
<p>Para o empresário local, esse perfil gera desafios tributários específicos. Metalúrgicas acumulam créditos de IPI sobre insumos que raramente são aproveitados. Laticínios operam com substituição tributária de ICMS que, se mal gerida, resulta em pagamento duplo. Empresas de comércio varejista perdem competitividade quando o regime tributário não é calibrado para o seu faturamento real.</p>
<p>A AC Contabilidade nasceu em Pará de Minas em 1996 e cresceu junto com o tecido empresarial da cidade. Três décadas acompanhando comércio, serviços e indústrias locais traduzem-se em capacidade de identificar, com precisão, onde cada tipo de empresa paga tributo além do necessário — e como recuperar esse valor dentro da legalidade.</p>
<p>O escritório fica na Rua Major Fidélis, 244, no Centro de Pará de Minas. O atendimento pode ser presencial ou por videoconferência para empresas de outras cidades. Para novos clientes, o diagnóstico tributário gratuito é o ponto de partida.</p>"""

CORPUS["Sete Lagoas"] = """<p>Sete Lagoas construiu sua identidade econômica sobre o ferro. O Distrito Industrial, inaugurado em 1974, reuniu fundições, siderúrgicas e metalúrgicas que transformaram a cidade no maior polo siderúrgico do interior mineiro. Empresas como a Iveco, que fabrica veículos pesados no município, e grandes marcas do setor de alimentos como Ambev e Itambé instalaram operações que elevaram a cidade à 12ª maior economia de Minas Gerais.</p>
<p>Para o empresário sete-lagoano, esse perfil industrial gera um desafio tributário específico. Fundições e metalúrgicas acumulam créditos de ICMS e IPI sobre insumos e materiais intermediários que, na maior parte dos casos, nunca são aproveitados. Distribuidoras de alimentos operam com margens apertadas e perdem competitividade quando o regime tributário não é calibrado corretamente. A AC Contabilidade existe para fechar essa lacuna.</p>
<p>Atendemos Sete Lagoas desde 1996. Ao longo de três décadas, acompanhamos o crescimento do polo industrial, as mudanças no regime do ICMS em MG e a chegada de novos setores, como o farmacêutico. Esse histórico permite identificar, com precisão, onde cada tipo de empresa da região acumula tributo pago a mais, e como recuperar esse valor dentro da legalidade.</p>
<p>O escritório está em Pará de Minas, a 72 km de BH e a menos de uma hora de Sete Lagoas pela BR-040. O atendimento pode ser presencial ou por videoconferência. Para empresas do Distrito Industrial, do eixo comercial do Eldorado ou dos bairros do Centro e São João, o diagnóstico tributário gratuito é o ponto de partida.</p>"""

CORPUS["Montes Claros"] = """<p>Montes Claros chegou ao século XXI como o centro econômico do Norte de Minas — 5ª maior cidade do estado, com PIB de R$ 10,8 bilhões e uma estrutura produtiva que poucos municípios do interior brasileiro conseguem igualar. Nestlé, Novo Nordisk, Eurofarma, Coteminas e MSD transformaram o município na capital nacional de medicamentos e no maior produtor de leite condensado do mundo. Esse perfil atrai investimento, gera volume fiscal e exige contabilidade à altura da complexidade.</p>
<p>Farmacêuticas brasileiras e multinacionais têm regimes de PIS/COFINS com alíquotas não cumulativas que geram direitos a ressarcimento raramente explorados pelos escritórios contábeis convencionais. Fabricantes de laticínios e alimentos processados convivem com ICMS-ST calculado sobre pautas fiscais que mudam por decreto e que, quando mal monitoradas, resultam em recolhimento acima do valor real devido. A AC Contabilidade foi construída para tratar essas variáveis, não para ignorá-las.</p>
<p>A AC Contabilidade está no Norte de Minas desde 1996. Nesse tempo, vimos a ZFM farmacêutica ganhar corpo, o ICMS-ST ser reformulado e o setor de serviços superar a indústria em participação no PIB local. Acumular esse tipo de vivência setorial significa reconhecer padrões que escritórios recentes simplesmente não enxergam.</p>
<p>O formato de reunião se adapta à rotina do cliente. Quem está em Montes Claros pode optar pela chamada de vídeo, eliminando horas de deslocamento. Quem prefere o encontro presencial tem o escritório de Pará de Minas como referência. O ponto de entrada é sempre o mesmo: um levantamento completo e gratuito que mapeia tributação vigente, créditos não utilizados nos últimos cinco anos e situação patrimonial do sócio.</p>"""


def check_jaccard(candidate_text, candidate_name):
    results = []
    ok = True
    for name, text in CORPUS.items():
        j = jaccard(candidate_text, text)
        status = "OK" if j < 0.20 else "FALHOU"
        if j >= 0.20:
            ok = False
        results.append((name, j, status))
    print(f"\n  Jaccard [{candidate_name}]:")
    for name, j, status in sorted(results, key=lambda x: -x[1]):
        print(f"    vs {name:<22} {j:.3f}  {status}")
    return ok


# ---------------------------------------------------------------------------
# CITY DATA — 22 cities
# ---------------------------------------------------------------------------

CITIES = [

    # 1 — Uberaba MG
    {
        "cidade": "Uberaba",
        "uf": "MG",
        "cidade_uf": "uberaba-mg",
        "cidade_slug": "contador-em-uberaba",
        "canonical_url": "https://amcabralblindagem.com.br/uberaba-mg/contador-em-uberaba/",
        "wiki_url": "https://pt.wikipedia.org/wiki/Uberaba",
        "wikidata_id": "Q193684",
        "geo_lat": "-19.7482",
        "geo_lng": "-47.9317",
        "gentilicio": "uberabenses",
        "regiao": "Triângulo Mineiro",
        "foto": "uberaba-vista-panoramica.jpg",
        "alt_foto": "Vista panorâmica de Uberaba, MG",
        "caption_foto": "Uberaba, polo agropecuário do Triângulo Mineiro",
        "case_1_setor": "Agropecuária",
        "case_2_setor": "Indústria de alimentos",
        "case_3_setor": "Comércio atacadista",
        "vizinhas_texto": """<p>Além de Uberaba, atendemos empresas em Uberlândia, Araxá, Sacramento, Conceição das Alagoas, Campo Florido, Frutal e Delta. <a href="/cidades-atendidas/">Ver todas as cidades atendidas</a>.</p>""",
        "vizinhas_links": """<div class="coverage-nearby-links">
  <a href="/cidades-atendidas/">Uberlândia</a>
  <a href="/cidades-atendidas/">Araxá</a>
  <a href="/cidades-atendidas/">Sacramento</a>
  <a href="/cidades-atendidas/">Conceição das Alagoas</a>
  <a href="/cidades-atendidas/">Campo Florido</a>
  <a href="/cidades-atendidas/">Frutal</a>
  <a href="/cidades-atendidas/">Delta</a>
</div>""",
        "bairros_industrial": """<ul class="bairros-list">
  <li>Distrito Industrial</li>
  <li>Parque das Américas</li>
  <li>Industrial</li>
  <li>Abadia</li>
  <li>Santa Maria</li>
</ul>""",
        "bairros_comercial": """<ul class="bairros-list">
  <li>Centro</li>
  <li>Mercês</li>
  <li>Nova Uberaba</li>
  <li>São Benedito</li>
  <li>Fabrício</li>
</ul>""",
        "bairros_residencial": """<ul class="bairros-list">
  <li>Boa Vista</li>
  <li>Lídice</li>
  <li>Parque São Geraldo</li>
  <li>Jordão</li>
  <li>Santa Mônica</li>
</ul>""",
        "authority_h2": "Contabilidade em Uberaba com expertise no agronegócio do Triângulo",
        "amanda_cta_h2": "Contadora em Uberaba: Amanda Cabral, CRC/MG Ativo",
        "local_sec_h2": "Assessoria tributária a distância zero do Triângulo Mineiro",
        "services_h2_override": "Serviços contábeis para empresas de Uberaba",
        "depo1_role": "S&#243;cio",
        "depo1_setor": "Agropecuária",
        "depo2_role": "Propriet&#225;ria",
        "depo2_setor": "Clínica médica",
        "depo3_role": "Empres&#225;rio",
        "depo3_setor": "Comércio atacadista",
        "context_local": """<p>Uberaba é a capital genética do mundo: o município exporta embriões e sêmen de zebuínos para mais de 80 países, centraliza os principais leilões da raça Nelore e abriga a maior feira de gado bovino das Américas, a ExpoZebu. Esse eixo agropecuário sustenta um ecossistema de empresas rurais, veterinárias, laboratórios de reprodução e agroindústrias cujas obrigações fiscais vão muito além do ITR e do Funrural típicos do produtor rural.</p>
<p>Pecuaristas com operações de exportação de material genético precisam controlar o tratamento cambial da receita em moeda estrangeira, a isenção de ICMS nas saídas interestaduais para exportação e o crédito de PIS/COFINS sobre insumos veterinários. Frigoríficos e laticínios do entorno operam com crédito presumido de PIS/COFINS da agroindústria, cuja apuração incorreta compromete dezenas de pontos de margem. Distribuidoras atacadistas que servem o varejo regional enfrentam o ICMS-ST sobre alimentos com pautas fiscais que mudam por portaria estadual sem aviso prévio.</p>
<p>Trinta anos de presença no interior mineiro geraram uma base metodológica construída sobre casos reais, não sobre teoria. A AC Contabilidade acompanhou as mudanças no regime do Simples Nacional, a reforma do ICMS em MG e as sucessivas alterações nas listas de NCMs sujeitos à substituição tributária. Esse histórico permite antecipar impactos regulatórios antes que eles se tornem custos para o cliente.</p>
<p>O levantamento tributário inicial é gratuito e ocorre por reunião virtual, sem deslocamento. O escopo cobre regime atual, créditos escriturados nos últimos sessenta meses e riscos fiscais identificados na escrituração vigente.</p>""",
    },

    # 2 — Uberlândia MG
    {
        "cidade": "Uberlândia",
        "uf": "MG",
        "cidade_uf": "uberlandia-mg",
        "cidade_slug": "contador-em-uberlandia",
        "canonical_url": "https://amcabralblindagem.com.br/uberlandia-mg/contador-em-uberlandia/",
        "wiki_url": "https://pt.wikipedia.org/wiki/Uberlândia",
        "wikidata_id": "Q193720",
        "geo_lat": "-18.9186",
        "geo_lng": "-48.2772",
        "gentilicio": "uberlandenses",
        "regiao": "Triângulo Mineiro",
        "foto": "uberlandia-vista-panoramica.jpg",
        "alt_foto": "Vista aérea de Uberlândia, MG",
        "caption_foto": "Uberlândia, maior cidade do interior de Minas Gerais",
        "case_1_setor": "Distribuição e logística",
        "case_2_setor": "Indústria alimentícia",
        "case_3_setor": "Varejo especializado",
        "vizinhas_texto": """<p>Além de Uberlândia, atendemos empresas em Uberaba, Araguari, Tupaciguara, Prata, Monte Carmelo, Ituiutaba e Patos de Minas. <a href="/cidades-atendidas/">Ver todas as cidades atendidas</a>.</p>""",
        "vizinhas_links": """<div class="coverage-nearby-links">
  <a href="/cidades-atendidas/">Uberaba</a>
  <a href="/cidades-atendidas/">Araguari</a>
  <a href="/cidades-atendidas/">Tupaciguara</a>
  <a href="/cidades-atendidas/">Prata</a>
  <a href="/cidades-atendidas/">Monte Carmelo</a>
  <a href="/cidades-atendidas/">Ituiutaba</a>
  <a href="/cidades-atendidas/">Patos de Minas</a>
</div>""",
        "bairros_industrial": """<ul class="bairros-list">
  <li>Distrito Industrial</li>
  <li>Tibery</li>
  <li>Industrial</li>
  <li>Planalto</li>
  <li>Jardim Brasília</li>
</ul>""",
        "bairros_comercial": """<ul class="bairros-list">
  <li>Centro</li>
  <li>Saraiva</li>
  <li>Osvaldo Rezende</li>
  <li>Brasil</li>
  <li>Santa Mônica</li>
</ul>""",
        "bairros_residencial": """<ul class="bairros-list">
  <li>Morada da Colina</li>
  <li>Jardim Karaíba</li>
  <li>Pampulha</li>
  <li>Jaraguá</li>
  <li>Custódio Pereira</li>
</ul>""",
        "authority_h2": "Contabilidade em Uberlândia com visão do polo logístico nacional",
        "amanda_cta_h2": "Contadora em Uberlândia: Amanda Cabral, CRC/MG Ativo",
        "local_sec_h2": "Escritório tributário conectado ao maior hub logístico de MG",
        "services_h2_override": "Serviços contábeis para empresas de Uberlândia",
        "depo1_role": "S&#243;cio",
        "depo1_setor": "Distribuidora de alimentos",
        "depo2_role": "Propriet&#225;ria",
        "depo2_setor": "Rede de franquias",
        "depo3_role": "Empres&#225;rio",
        "depo3_setor": "Transportadora",
        "context_local": """<p>Uberlândia funciona como o nó central de redistribuição logística do Brasil Central: as rodovias BR-050, BR-365 e BR-452 convergem no município, posicionando a cidade como plataforma de abastecimento para o agronegócio do Cerrado e para o varejo de todo o eixo Sudeste-Centro-Oeste. Com PIB acima de R$ 30 bilhões e centenas de distribuidoras, transportadoras e fabricantes de médio porte, a base empresarial local gera um volume de obrigações periódicas que excede a capacidade operacional de escritórios de estrutura convencional.</p>
<p>Distribuidoras multiestaduais acumulam ativo de ICMS nas entradas que, por deficiência na apuração mensal, permanece represado sem gerar benefício de caixa. Frotas próprias de transportadoras precisam contabilizar o diferencial de alíquota de ICMS na compra de veículos pesados e o encargo previdenciário sobre remuneração de motoristas autônomos — dois pontos tratados pela legislação de forma distinta do regime CLT. Atacadistas próximos do teto do Supersimples postergam a transição de modalidade por falta de simulação comparativa, e cada trimestre de inércia pode ultrapassar o custo de uma análise de reenquadramento.</p>
<p>Definir o ponto exato de menor pressão fiscal para cada estrutura exige domínio setorial acumulado ao longo de décadas, não apenas familiaridade com a legislação vigente. A vivência em assessoria a operações de distribuição, logística e comércio atacadista do interior de MG é o que fundamenta diagnósticos precisos.</p>
<p>Para novos clientes de Uberlândia, o ponto de partida é um levantamento fiscal sem custo, conduzido por videoconferência. O trabalho abrange modalidade tributária atual, crédito acumulado nos cinco anos anteriores e os pontos de risco identificados na escrituração da empresa.</p>""",
    },

    # 3 — Poços de Caldas MG
    {
        "cidade": "Poços de Caldas",
        "uf": "MG",
        "cidade_uf": "pocos-de-caldas-mg",
        "cidade_slug": "contador-em-pocos-de-caldas",
        "canonical_url": "https://amcabralblindagem.com.br/pocos-de-caldas-mg/contador-em-pocos-de-caldas/",
        "wiki_url": "https://pt.wikipedia.org/wiki/Poços_de_Caldas",
        "wikidata_id": "Q1234497",
        "geo_lat": "-21.7870",
        "geo_lng": "-46.5614",
        "gentilicio": "poços-caldenses",
        "regiao": "Sul de Minas",
        "foto": "pocos-de-caldas-vista-panoramica.jpg",
        "alt_foto": "Vista panorâmica de Poços de Caldas, MG",
        "caption_foto": "Poços de Caldas, polo tecnológico e turístico do Sul de MG",
        "case_1_setor": "Indústria cerâmica",
        "case_2_setor": "Tecnologia da informação",
        "case_3_setor": "Turismo e hotelaria",
        "vizinhas_texto": """<p>Além de Poços de Caldas, atendemos empresas em Caldas, Andradas, Botelhos, Campestre, São Sebastião da Bela Vista, Poço Fundo e Muzambinho. <a href="/cidades-atendidas/">Ver todas as cidades atendidas</a>.</p>""",
        "vizinhas_links": """<div class="coverage-nearby-links">
  <a href="/cidades-atendidas/">Caldas</a>
  <a href="/cidades-atendidas/">Andradas</a>
  <a href="/cidades-atendidas/">Botelhos</a>
  <a href="/cidades-atendidas/">Campestre</a>
  <a href="/cidades-atendidas/">São Sebastião da Bela Vista</a>
  <a href="/cidades-atendidas/">Poço Fundo</a>
  <a href="/cidades-atendidas/">Muzambinho</a>
</div>""",
        "bairros_industrial": """<ul class="bairros-list">
  <li>Distrito Industrial</li>
  <li>Santa Rosália</li>
  <li>Jardim Centenário</li>
  <li>São João</li>
  <li>Jardim das Hortênsias</li>
</ul>""",
        "bairros_comercial": """<ul class="bairros-list">
  <li>Centro</li>
  <li>Jardim Europa</li>
  <li>Vila Togni</li>
  <li>Cascata</li>
  <li>Jardim Quisisana</li>
</ul>""",
        "bairros_residencial": """<ul class="bairros-list">
  <li>Jardim dos Estados</li>
  <li>Santa Cruz</li>
  <li>Vila Formosa</li>
  <li>Campos Elíseos</li>
  <li>Nossa Senhora de Fátima</li>
</ul>""",
        "authority_h2": "Contabilidade em Poços de Caldas com foco em tecnologia e indústria",
        "amanda_cta_h2": "Contadora em Poços de Caldas: Amanda Cabral, CRC/MG Ativo",
        "local_sec_h2": "Expertise tributária para o polo de tecnologia do Sul de MG",
        "services_h2_override": "Serviços contábeis para empresas de Poços de Caldas",
        "depo1_role": "S&#243;cio",
        "depo1_setor": "Tecnologia da informação",
        "depo2_role": "Propriet&#225;ria",
        "depo2_setor": "Hotelaria",
        "depo3_role": "Empres&#225;rio",
        "depo3_setor": "Indústria cerâmica",
        "context_local": """<p>Poços de Caldas reúne, no mesmo perímetro urbano, um parque industrial com cerâmica técnica de alta temperatura, alumínio refratário e laboratórios de pesquisa de multinacionais, e um complexo hoteleiro que sustenta fluxo turístico ao longo de todos os doze meses. A Novelis instalou na cidade um centro técnico que atende operações sul-americanas, e outras corporações globais seguiram o mesmo caminho atraídas pela altitude, pela infraestrutura universitária e pela qualificação da mão de obra local.</p>
<p>Cerâmicas técnicas e fundições de alumínio classificam seus produtos por NCM e essa codificação determina diretamente a alíquota de IPI aplicável. Quando a Tabela TIPI é atualizada por decreto e a empresa não revisa a classificação vigente, o tributo recolhido diverge do correto por anos, gerando ora passivo ora crédito não percebido. Estabelecimentos hoteleiros calculam ISS sobre hospedagem pela tabela municipal de Poços e precisam reter IRRF em notas emitidas para tomadores corporativos, pena de responsabilização tributária solidária na fiscalização. Desenvolvedoras de software do polo tecnológico local que atingem o limite do Supersimples precisam formalizar a opção pelo Lucro Presumido até o último dia útil de janeiro, prazo que a maioria descobre depois que a irretratabilidade já ocorreu.</p>
<p>Três décadas de acompanhamento a empresas do Sul de Minas construíram uma base de casos reais que cobre cerâmica, hotelaria, tecnologia e manufatura. Esse repositório de situações concretas é o que diferencia uma análise precisa de uma orientação genérica.</p>
<p>Novos clientes de Poços de Caldas começam pelo mapeamento fiscal gratuito, conduzido por conexão digital. O diagnóstico abrange modalidade tributária atual, créditos represados dos últimos sessenta meses e vulnerabilidades nas obrigações periódicas da empresa.</p>""",
    },

    # 4 — Betim MG
    {
        "cidade": "Betim",
        "uf": "MG",
        "cidade_uf": "betim-mg",
        "cidade_slug": "contador-em-betim",
        "canonical_url": "https://amcabralblindagem.com.br/betim-mg/contador-em-betim/",
        "wiki_url": "https://pt.wikipedia.org/wiki/Betim",
        "wikidata_id": "Q1040697",
        "geo_lat": "-19.9678",
        "geo_lng": "-44.1983",
        "gentilicio": "betinenses",
        "regiao": "Região Metropolitana de BH",
        "foto": "betim-vista-panoramica.jpg",
        "alt_foto": "Vista panorâmica de Betim, MG",
        "caption_foto": "Betim, polo petroquímico e automotivo de Minas Gerais",
        "case_1_setor": "Indústria automotiva",
        "case_2_setor": "Petroquímica",
        "case_3_setor": "Fornecedor de autopeças",
        "vizinhas_texto": """<p>Além de Betim, atendemos empresas em Contagem, Ibirité, Esmeraldas, São Joaquim de Bicas, Mário Campos, Sarzedo e Juatuba. <a href="/cidades-atendidas/">Ver todas as cidades atendidas</a>.</p>""",
        "vizinhas_links": """<div class="coverage-nearby-links">
  <a href="/cidades-atendidas/">Contagem</a>
  <a href="/cidades-atendidas/">Ibirité</a>
  <a href="/cidades-atendidas/">Esmeraldas</a>
  <a href="/cidades-atendidas/">São Joaquim de Bicas</a>
  <a href="/cidades-atendidas/">Mário Campos</a>
  <a href="/cidades-atendidas/">Sarzedo</a>
  <a href="/cidades-atendidas/">Juatuba</a>
</div>""",
        "bairros_industrial": """<ul class="bairros-list">
  <li>Citrolândia</li>
  <li>PTB</li>
  <li>Jardim das Alterosas</li>
  <li>Petrolândia</li>
  <li>Colônia</li>
</ul>""",
        "bairros_comercial": """<ul class="bairros-list">
  <li>Centro</li>
  <li>Braúnas</li>
  <li>Teresópolis</li>
  <li>Imbiruçu</li>
  <li>Jardim Teresópolis</li>
</ul>""",
        "bairros_residencial": """<ul class="bairros-list">
  <li>Citrolândia</li>
  <li>Olhos D'água</li>
  <li>Jardim Alterosas</li>
  <li>Várzea</li>
  <li>Amazonas</li>
</ul>""",
        "authority_h2": "Contabilidade em Betim com expertise no setor automotivo e petroquímico",
        "amanda_cta_h2": "Contadora em Betim: Amanda Cabral, CRC/MG Ativo",
        "local_sec_h2": "Assessoria fiscal para fornecedores da cadeia automotiva de MG",
        "services_h2_override": "Serviços contábeis para empresas de Betim",
        "depo1_role": "S&#243;cio",
        "depo1_setor": "Fornecedor de autopeças",
        "depo2_role": "Propriet&#225;ria",
        "depo2_setor": "Prestadora de serviços industriais",
        "depo3_role": "Empres&#225;rio",
        "depo3_setor": "Distribuidora de insumos",
        "context_local": """<p>Betim abriga a maior fábrica da Stellantis na América Latina e o Polo Petroquímico de Minas, dois vetores que transformaram a cidade no segundo maior PIB industrial do estado. A cadeia de fornecedores automotivos ao redor da planta — autopeças, sistemas, montagens e logística — gera centenas de empresas com obrigações fiscais de alta complexidade e fluxo de notas fiscais de entrada e saída que exige controle permanente.</p>
<p>Fornecedores da indústria automotiva operam com drawback, crédito presumido de IPI e regimes especiais de ICMS que poucas assessorias contábeis dominam na prática. Empresas do polo petroquímico precisam acompanhar as variações de NCM e de pauta fiscal do ICMS-ST em matérias-primas que mudam de classificação por ato normativo. Quando esses controles falham, o crédito acumula e o caixa sangra sem que a gestão identifique a causa.</p>
<p>A AC Contabilidade acumulou três décadas de vivência com os regimes tributários específicos da indústria mineira. Essa bagagem se traduz em capacidade de mapear, em auditoria retroativa de cinco anos, os créditos não aproveitados e quantificar o retorno concreto antes de formalizar qualquer proposta.</p>
<p>O formato de atendimento se adapta à rotina industrial: videoconferência em qualquer horário ou visita presencial ao escritório de Pará de Minas. Para novos clientes em Betim, a avaliação tributária inicial não tem custo e não exige compromisso de contratação.</p>""",
    },

    # 5 — Curitiba PR
    {
        "cidade": "Curitiba",
        "uf": "PR",
        "cidade_uf": "curitiba-pr",
        "cidade_slug": "contador-em-curitiba",
        "canonical_url": "https://amcabralblindagem.com.br/curitiba-pr/contador-em-curitiba/",
        "wiki_url": "https://pt.wikipedia.org/wiki/Curitiba",
        "wikidata_id": "Q1490",
        "geo_lat": "-25.4284",
        "geo_lng": "-49.2733",
        "gentilicio": "curitibanos",
        "regiao": "Sul do Brasil",
        "foto": "curitiba-vista-panoramica.jpg",
        "alt_foto": "Vista aérea de Curitiba, PR",
        "caption_foto": "Curitiba, capital do Paraná e polo tecnológico do Sul do Brasil",
        "case_1_setor": "Tecnologia da informação",
        "case_2_setor": "Indústria metal-mecânica",
        "case_3_setor": "Serviços empresariais",
        "vizinhas_texto": """<p>Além de Curitiba, atendemos empresas em São José dos Pinhais, Pinhais, Colombo, Almirante Tamandaré, Araucária, Campo Largo e Fazenda Rio Grande. <a href="/cidades-atendidas/">Ver todas as cidades atendidas</a>.</p>""",
        "vizinhas_links": """<div class="coverage-nearby-links">
  <a href="/cidades-atendidas/">São José dos Pinhais</a>
  <a href="/cidades-atendidas/">Pinhais</a>
  <a href="/cidades-atendidas/">Colombo</a>
  <a href="/cidades-atendidas/">Almirante Tamandaré</a>
  <a href="/cidades-atendidas/">Araucária</a>
  <a href="/cidades-atendidas/">Campo Largo</a>
  <a href="/cidades-atendidas/">Fazenda Rio Grande</a>
</div>""",
        "bairros_industrial": """<ul class="bairros-list">
  <li>CIC (Cidade Industrial)</li>
  <li>Tatuquara</li>
  <li>Riviera</li>
  <li>Capão Raso</li>
  <li>São Miguel</li>
</ul>""",
        "bairros_comercial": """<ul class="bairros-list">
  <li>Centro</li>
  <li>Batel</li>
  <li>Bigorrilho</li>
  <li>Mercês</li>
  <li>Portão</li>
</ul>""",
        "bairros_residencial": """<ul class="bairros-list">
  <li>Água Verde</li>
  <li>Boa Vista</li>
  <li>Santa Felicidade</li>
  <li>Bacacheri</li>
  <li>Cajuru</li>
</ul>""",
        "authority_h2": "Contabilidade em Curitiba especializada em tributação para tech e indústria",
        "amanda_cta_h2": "Contadora em Curitiba: Amanda Cabral, CRC/MG Ativo",
        "local_sec_h2": "Planejamento tributário remoto para empresas da capital paranaense",
        "services_h2_override": "Serviços contábeis para empresas de Curitiba",
        "depo1_role": "S&#243;cio",
        "depo1_setor": "Startup de tecnologia",
        "depo2_role": "Propriet&#225;ria",
        "depo2_setor": "Consultoria de gestão",
        "depo3_role": "Empres&#225;rio",
        "depo3_setor": "Metal-mecânica",
        "context_local": """<p>Curitiba consolidou sua posição como o principal polo de tecnologia e inovação do Sul do Brasil. A capital paranaense reúne empresas de software, segurança da informação, automação industrial e serviços especializados que operam em modelos de negócio híbridos, com receita de produto e de serviço misturadas numa mesma pessoa jurídica. Esse perfil cria desafios tributários que escritórios contábeis generalistas raramente conseguem resolver com precisão.</p>
<p>Empresas de tecnologia que faturam acima de R$ 78 milhões no Simples Nacional precisam migrar de regime, mas a transição exige planejamento: créditos de PIS/COFINS acumulados na fase cumulativa podem ser aproveitados na não cumulativa e, se não forem mapeados no momento certo, prescrevem em cinco anos. Prestadores de serviços com clientes em vários estados precisam gerenciar o ISS da competência tributária municipal e o IRRF retido na fonte, que nem sempre é compensado corretamente.</p>
<p>Trinta anos de prática com empresas do interior mineiro construíram um modelo de trabalho que funciona inteiramente por meios digitais, sem perda de profundidade analítica. Acesso remoto seguro a sistemas contábeis, reuniões por videoconferência e entrega de relatórios em tempo real permitem atender empresas de Curitiba com a mesma qualidade oferecida a clientes vizinhos ao escritório.</p>
<p>A primeira conversa não tem custo: um diagnóstico tributário de 30 minutos que revela o regime mais vantajoso, os créditos que podem ser recuperados dentro do prazo legal e os riscos que precisam ser corrigidos antes que se tornem autuações. Sem compromisso, sem burocracia.</p>""",
    },

    # 6 — Sorocaba SP
    {
        "cidade": "Sorocaba",
        "uf": "SP",
        "cidade_uf": "sorocaba-sp",
        "cidade_slug": "contador-em-sorocaba",
        "canonical_url": "https://amcabralblindagem.com.br/sorocaba-sp/contador-em-sorocaba/",
        "wiki_url": "https://pt.wikipedia.org/wiki/Sorocaba",
        "wikidata_id": "Q215750",
        "geo_lat": "-23.5015",
        "geo_lng": "-47.4526",
        "gentilicio": "sorocabanos",
        "regiao": "interior de São Paulo",
        "foto": "sorocaba-vista-panoramica.jpg",
        "alt_foto": "Vista panorâmica de Sorocaba, SP",
        "caption_foto": "Sorocaba, polo industrial do interior paulista",
        "case_1_setor": "Metal-mecânica",
        "case_2_setor": "Têxtil e confecção",
        "case_3_setor": "Comércio varejista",
        "vizinhas_texto": """<p>Além de Sorocaba, atendemos empresas em Votorantim, Salto, Itu, São Roque, Mairinque, Alumínio e Araçariguama. <a href="/cidades-atendidas/">Ver todas as cidades atendidas</a>.</p>""",
        "vizinhas_links": """<div class="coverage-nearby-links">
  <a href="/cidades-atendidas/">Votorantim</a>
  <a href="/cidades-atendidas/">Salto</a>
  <a href="/cidades-atendidas/">Itu</a>
  <a href="/cidades-atendidas/">São Roque</a>
  <a href="/cidades-atendidas/">Mairinque</a>
  <a href="/cidades-atendidas/">Alumínio</a>
  <a href="/cidades-atendidas/">Araçariguama</a>
</div>""",
        "bairros_industrial": """<ul class="bairros-list">
  <li>Distrito Industrial Além Ponte</li>
  <li>Wanel Ville</li>
  <li>Éden</li>
  <li>Aparecidinha</li>
  <li>Santa Rosália</li>
</ul>""",
        "bairros_comercial": """<ul class="bairros-list">
  <li>Centro</li>
  <li>Campolim</li>
  <li>Jardim Paulistano</li>
  <li>Alto da Boa Vista</li>
  <li>Boa Vista</li>
</ul>""",
        "bairros_residencial": """<ul class="bairros-list">
  <li>Jardim Sabiá</li>
  <li>Cajuru do Sul</li>
  <li>Arouca</li>
  <li>Éden</li>
  <li>Novitá</li>
</ul>""",
        "authority_h2": "Contabilidade em Sorocaba com domínio da indústria metal-mecânica paulista",
        "amanda_cta_h2": "Contadora em Sorocaba: Amanda Cabral, CRC/MG Ativo",
        "local_sec_h2": "Gestão tributária para o parque industrial de Sorocaba",
        "services_h2_override": "Serviços contábeis para empresas de Sorocaba",
        "depo1_role": "S&#243;cio",
        "depo1_setor": "Metal-mecânica",
        "depo2_role": "Propriet&#225;ria",
        "depo2_setor": "Indústria têxtil",
        "depo3_role": "Empres&#225;rio",
        "depo3_setor": "Comércio varejista",
        "context_local": """<p>Sorocaba estruturou seu parque produtivo ao longo da ferrovia que interliga Santos a Bauru, e hoje esse legado industrial se expressa em plantas de equipamentos elétricos de média e alta tensão, tecelagens técnicas, linhas de produção farmacêutica e fabricantes de autopeças que tornam a cidade a quarta maior economia do interior paulista. A diversidade de setores num mesmo perímetro urbano significa que obrigações fiscais com lógicas completamente distintas coexistem a poucos quarteirões de distância.</p>
<p>Fabricantes de equipamentos elétricos de alta tensão precisam classificar cada produto por TIPI para determinar se a saída é tributada, imune ou sujeita a alíquota reduzida de IPI: uma classificação incorreta gera estorno de crédito ou multa proporcional conforme o sentido do erro. Tecelagens técnicas que exportam tecidos especializados para o mercado têxtil global calculam o benefício de suspensão de tributos na aquisição de fios, mas o controle do saldo exportado por partida é o que determina se a suspensão se converte em isenção definitiva. Indústrias farmacêuticas instaladas no Distrito Industrial de Além Ponte operam com regimes de PIS e COFINS por alíquota diferenciada de produto, e qualquer divergência entre o regime declarado e o efetivamente praticado gera inconsistência que a Receita Federal detecta na cruzagem entre a EFD-Contribuições e a NFe.</p>
<p>A prática de três décadas com empresas da indústria de transformação formou uma base de conhecimento setorial que permite detectar, com precisão, onde cada tipo de operação acumula carga tributária além do que a legislação exige.</p>
<p>Novos clientes de Sorocaba passam por uma triagem tributária gratuita conduzida à distância. A avaliação cobre o regime de tributação atual, o aproveitamento de crédito dos cinco exercícios anteriores e os pontos de atenção identificados nas declarações periódicas da empresa.</p>""",
    },

    # 7 — Guarulhos SP
    {
        "cidade": "Guarulhos",
        "uf": "SP",
        "cidade_uf": "guarulhos-sp",
        "cidade_slug": "contador-em-guarulhos",
        "canonical_url": "https://amcabralblindagem.com.br/guarulhos-sp/contador-em-guarulhos/",
        "wiki_url": "https://pt.wikipedia.org/wiki/Guarulhos",
        "wikidata_id": "Q213621",
        "geo_lat": "-23.4629",
        "geo_lng": "-46.5334",
        "gentilicio": "guarulhenses",
        "regiao": "Grande São Paulo",
        "foto": "guarulhos-vista-panoramica.jpg",
        "alt_foto": "Vista aérea de Guarulhos, SP",
        "caption_foto": "Guarulhos, polo logístico e industrial da Grande São Paulo",
        "case_1_setor": "Logística e transporte",
        "case_2_setor": "Indústria de embalagens",
        "case_3_setor": "Importação e comércio exterior",
        "vizinhas_texto": """<p>Além de Guarulhos, atendemos empresas em Arujá, Santa Isabel, Mairiporã, Nazaré Paulista, Bragança Paulista, Franco da Rocha e Caieiras. <a href="/cidades-atendidas/">Ver todas as cidades atendidas</a>.</p>""",
        "vizinhas_links": """<div class="coverage-nearby-links">
  <a href="/cidades-atendidas/">Arujá</a>
  <a href="/cidades-atendidas/">Santa Isabel</a>
  <a href="/cidades-atendidas/">Mairiporã</a>
  <a href="/cidades-atendidas/">Nazaré Paulista</a>
  <a href="/cidades-atendidas/">Bragança Paulista</a>
  <a href="/cidades-atendidas/">Franco da Rocha</a>
  <a href="/cidades-atendidas/">Caieiras</a>
</div>""",
        "bairros_industrial": """<ul class="bairros-list">
  <li>Jardim Cumbica</li>
  <li>Macedo</li>
  <li>Taboão</li>
  <li>Água Azul</li>
  <li>Ponte Grande</li>
</ul>""",
        "bairros_comercial": """<ul class="bairros-list">
  <li>Centro</li>
  <li>Vila Galvão</li>
  <li>Gopouva</li>
  <li>São João</li>
  <li>Vila Augusta</li>
</ul>""",
        "bairros_residencial": """<ul class="bairros-list">
  <li>Jardim Tranqüilidade</li>
  <li>Vila Rio de Janeiro</li>
  <li>Lavras</li>
  <li>Jardim Santa Mena</li>
  <li>Bonsucesso</li>
</ul>""",
        "authority_h2": "Contabilidade em Guarulhos com expertise em comércio exterior e logística",
        "amanda_cta_h2": "Contadora em Guarulhos: Amanda Cabral, CRC/MG Ativo",
        "local_sec_h2": "Otimização tributária para o hub logístico do Aeroporto de Cumbica",
        "services_h2_override": "Serviços contábeis para empresas de Guarulhos",
        "depo1_role": "S&#243;cio",
        "depo1_setor": "Operador logístico",
        "depo2_role": "Propriet&#225;ria",
        "depo2_setor": "Trading de importação",
        "depo3_role": "Empres&#225;rio",
        "depo3_setor": "Indústria de embalagens",
        "context_local": """<p>Guarulhos concentra um volume fiscal proporcional ao Aeroporto Internacional de Cumbica, segundo maior do Brasil em movimentação de cargas. Operadores logísticos, tradings, despachantes aduaneiros e distribuidoras que movimentam mercadorias de todos os continentes têm sede ou filial no município, atraídas pela malha rodoviária que liga Anhanguera, Dutra e Presidente Dutra num único nó de distribuição para toda a Grande SP.</p>
<p>Importadoras precisam classificar corretamente o NCM de cada mercadoria para definir a alíquota de IPI e evitar autuações da Receita Federal na entrada. Tradings que revendem mercadoria importada para varejistas paulistas enfrentam ICMS-ST com pauta fiscal específica e substituição tributária de ponta, cujo cálculo incorreto gera passivo que só aparece na fiscalização estadual. Operadores logísticos com frota própria precisam controlar o ICMS diferencial de alíquota na aquisição de veículos e o INSS sobre terceiros contratados.</p>
<p>Três décadas de assessoria a empresas com cadeias tributárias complexas consolidaram uma metodologia que parte do mapeamento das entradas e saídas antes de qualquer recomendação. Esse diagnóstico de base revela exatamente onde o tributo está sendo pago além do necessário.</p>
<p>O levantamento inicial é gratuito e ocorre por chamada de vídeo. O escopo cobre regime atual, créditos acumulados nos últimos sessenta meses e riscos identificados nas obrigações acessórias vigentes.</p>""",
    },

    # 8 — Manaus AM
    {
        "cidade": "Manaus",
        "uf": "AM",
        "cidade_uf": "manaus-am",
        "cidade_slug": "contador-em-manaus",
        "canonical_url": "https://amcabralblindagem.com.br/manaus-am/contador-em-manaus/",
        "wiki_url": "https://pt.wikipedia.org/wiki/Manaus",
        "wikidata_id": "Q38930",
        "geo_lat": "-3.1190",
        "geo_lng": "-60.0217",
        "gentilicio": "manauaras",
        "regiao": "Amazônia",
        "foto": "manaus-vista-panoramica.jpg",
        "alt_foto": "Vista aérea de Manaus, AM",
        "caption_foto": "Manaus, polo eletroeletrônico da Zona Franca da Amazônia",
        "case_1_setor": "Eletroeletrônicos",
        "case_2_setor": "Duas rodas e veículos",
        "case_3_setor": "Comércio atacadista",
        "vizinhas_texto": """<p>Além de Manaus, atendemos empresas em Iranduba, Manacapuru, Careiro da Várzea, Rio Preto da Eva, Presidente Figueiredo, Itacoatiara e Parintins. <a href="/cidades-atendidas/">Ver todas as cidades atendidas</a>.</p>""",
        "vizinhas_links": """<div class="coverage-nearby-links">
  <a href="/cidades-atendidas/">Iranduba</a>
  <a href="/cidades-atendidas/">Manacapuru</a>
  <a href="/cidades-atendidas/">Careiro da Várzea</a>
  <a href="/cidades-atendidas/">Rio Preto da Eva</a>
  <a href="/cidades-atendidas/">Presidente Figueiredo</a>
  <a href="/cidades-atendidas/">Itacoatiara</a>
  <a href="/cidades-atendidas/">Parintins</a>
</div>""",
        "bairros_industrial": """<ul class="bairros-list">
  <li>Pólo Industrial de Manaus</li>
  <li>Distrito Industrial I</li>
  <li>Distrito Industrial II</li>
  <li>Mauazinho</li>
  <li>Coroado</li>
</ul>""",
        "bairros_comercial": """<ul class="bairros-list">
  <li>Centro</li>
  <li>Adrianópolis</li>
  <li>Chapada</li>
  <li>Nossa Senhora das Graças</li>
  <li>São Geraldo</li>
</ul>""",
        "bairros_residencial": """<ul class="bairros-list">
  <li>Aleixo</li>
  <li>Parque 10 de Novembro</li>
  <li>Flores</li>
  <li>Novo Aleixo</li>
  <li>Cidade Nova</li>
</ul>""",
        "authority_h2": "Contabilidade em Manaus com expertise nos incentivos da Zona Franca",
        "amanda_cta_h2": "Contadora em Manaus: Amanda Cabral, CRC/MG Ativo",
        "local_sec_h2": "Planejamento tributário para empresas do Polo Industrial de Manaus",
        "services_h2_override": "Serviços contábeis para empresas de Manaus",
        "depo1_role": "S&#243;cio",
        "depo1_setor": "Indústria eletroeletrônica",
        "depo2_role": "Propriet&#225;ria",
        "depo2_setor": "Distribuidora regional",
        "depo3_role": "Empres&#225;rio",
        "depo3_setor": "Comércio atacadista",
        "context_local": """<p>Manaus opera sob normas tributárias sem equivalente no restante do Brasil. A Zona Franca criada pelo Decreto-Lei 288/1967 concede desoneração de Imposto de Importação e IPI para componentes destinados à fabricação no Polo Industrial, além de redução nas remessas interestaduais e alíquota diferenciada de contribuições sociais em determinadas cadeias de valor, consolidando a cidade como a maior produtora nacional de eletroeletrônicos de consumo, motocicletas e televisores, com mais de 500 plantas habilitadas.</p>
<p>Cada empresa do Polo precisa comprovar o cumprimento do Processo Produtivo Básico para cada linha de produto e manter escrituração segregada por habilitação para sustentar os benefícios perante a Suframa e a Receita Federal. O diferencial de ICMS concedido pelo Amazonas nas saídas para o restante do país é calculado por portaria estadual com tabelas por categoria, e a aplicação incorreta gera estorno em cascata que transforma o incentivo em passivo de difícil reversão. Distribuidoras e prestadoras de serviços que atuam fora do polo de manufatura não usufruem dos mesmos incentivos dos fabricantes, mas podem enquadrar determinadas operações em regimes favorecidos do ICMS-AM se a atividade for tipificada corretamente na classificação estadual.</p>
<p>Três décadas de assessoria a estruturas fiscais de elevada complexidade consolidaram uma metodologia de mapeamento que parte das condicionantes específicas de cada habilitação para localizar onde o incentivo está sendo sub-aproveitado ou onde há risco de glosa retroativa.</p>
<p>Para novos clientes de Manaus, o diagnóstico fiscal inicial não tem custo e ocorre por transmissão remota. O levantamento abrange o enquadramento na ZFM, o aproveitamento de benefícios no quinquênio anterior e as inconsistências nos arquivos enviados à Suframa e ao Fisco Federal.</p>""",
    },

    # 9 — Osasco SP
    {
        "cidade": "Osasco",
        "uf": "SP",
        "cidade_uf": "osasco-sp",
        "cidade_slug": "contador-em-osasco",
        "canonical_url": "https://amcabralblindagem.com.br/osasco-sp/contador-em-osasco/",
        "wiki_url": "https://pt.wikipedia.org/wiki/Osasco",
        "wikidata_id": "Q213601",
        "geo_lat": "-23.5329",
        "geo_lng": "-46.7920",
        "gentilicio": "osasquenses",
        "regiao": "Grande São Paulo",
        "foto": "osasco-vista-panoramica.jpg",
        "alt_foto": "Vista aérea de Osasco, SP",
        "caption_foto": "Osasco, polo financeiro e de serviços da Grande São Paulo",
        "case_1_setor": "Serviços financeiros",
        "case_2_setor": "Indústria farmacêutica",
        "case_3_setor": "Comércio e varejo",
        "vizinhas_texto": """<p>Além de Osasco, atendemos empresas em Carapicuíba, Barueri, Cotia, Jandira, Itapevi, Santana de Parnaíba e Pirapora do Bom Jesus. <a href="/cidades-atendidas/">Ver todas as cidades atendidas</a>.</p>""",
        "vizinhas_links": """<div class="coverage-nearby-links">
  <a href="/cidades-atendidas/">Carapicuíba</a>
  <a href="/cidades-atendidas/">Barueri</a>
  <a href="/cidades-atendidas/">Cotia</a>
  <a href="/cidades-atendidas/">Jandira</a>
  <a href="/cidades-atendidas/">Itapevi</a>
  <a href="/cidades-atendidas/">Santana de Parnaíba</a>
  <a href="/cidades-atendidas/">Pirapora do Bom Jesus</a>
</div>""",
        "bairros_industrial": """<ul class="bairros-list">
  <li>Vila Osasco</li>
  <li>Jardim Veloso</li>
  <li>Presidente Altino</li>
  <li>Palmares</li>
  <li>Industrial</li>
</ul>""",
        "bairros_comercial": """<ul class="bairros-list">
  <li>Centro</li>
  <li>Bussocaba</li>
  <li>Umuarama</li>
  <li>Munhoz Júnior</li>
  <li>City Bussocaba</li>
</ul>""",
        "bairros_residencial": """<ul class="bairros-list">
  <li>Jardim D'Abril</li>
  <li>Cipava</li>
  <li>Km 18</li>
  <li>Conceição</li>
  <li>Santa Cruz</li>
</ul>""",
        "authority_h2": "Contabilidade em Osasco para empresas financeiras e de serviços especializados",
        "amanda_cta_h2": "Contadora em Osasco: Amanda Cabral, CRC/MG Ativo",
        "local_sec_h2": "Otimização fiscal para o polo de serviços e finanças de Osasco",
        "services_h2_override": "Serviços contábeis para empresas de Osasco",
        "depo1_role": "S&#243;cio",
        "depo1_setor": "Corretora de seguros",
        "depo2_role": "Propriet&#225;ria",
        "depo2_setor": "Prestadora de serviços financeiros",
        "depo3_role": "Empres&#225;rio",
        "depo3_setor": "Comércio varejista",
        "context_local": """<p>Osasco consolidou-se como o maior polo de serviços financeiros do Brasil fora de São Paulo capital: bancos de médio porte, cooperativas de crédito, seguradoras, fintechs e administradoras de consórcio instalaram sedes e centros de operações ao longo da Avenida dos Autonomistas, atraídos pela proximidade com a Marginal Pinheiros e pela infraestrutura de telecomunicações que permite processar alto volume de transações com latência mínima.</p>
<p>Bancos e cooperativas de crédito escrituram o IOF sobre operações de empréstimo e financiamento com alíquotas que variam por prazo e modalidade, e qualquer inconsistência entre o IOF declarado e o efetivamente recolhido gera auto de infração de difícil contestação administrativa. Seguradoras precisam controlar a tributação sobre prêmios e sinistros com tratamento diferenciado de IRPJ e CSLL, além do IOF específico sobre apólices, cujo cálculo correto depende da classificação precisa de cada tipo de cobertura contratada. Fintechs que crescem além do teto do Simples Nacional precisam decidir entre Lucro Presumido e Lucro Real considerando o impacto específico sobre PIS e COFINS em operações de crédito e intermediação financeira, tributos com tratamento distinto do regime padrão de prestação de serviços.</p>
<p>A vivência de três décadas com empresas do setor financeiro e de serviços especializados consolidou uma base metodológica para detectar onde a tributação está sendo apurada além do exigido pela legislação vigente.</p>
<p>Empresas de Osasco que queiram iniciar uma revisão tributária recebem uma avaliação gratuita por videoconferência. O diagnóstico abrange o regime de tributação atual, o histórico de aproveitamento de crédito nos cinco exercícios anteriores e os pontos de vulnerabilidade fiscal identificados na escrituração contábil.</p>""",
    },

    # 10 — Caxias do Sul RS
    {
        "cidade": "Caxias do Sul",
        "uf": "RS",
        "cidade_uf": "caxias-do-sul-rs",
        "cidade_slug": "contador-em-caxias-do-sul",
        "canonical_url": "https://amcabralblindagem.com.br/caxias-do-sul-rs/contador-em-caxias-do-sul/",
        "wiki_url": "https://pt.wikipedia.org/wiki/Caxias_do_Sul",
        "wikidata_id": "Q192648",
        "geo_lat": "-29.1681",
        "geo_lng": "-51.1794",
        "gentilicio": "caxienses",
        "regiao": "Serra Gaúcha",
        "foto": "caxias-do-sul-vista-panoramica.jpg",
        "alt_foto": "Vista panorâmica de Caxias do Sul, RS",
        "caption_foto": "Caxias do Sul, polo metal-mecânico e vinícola da Serra Gaúcha",
        "case_1_setor": "Metal-mecânica",
        "case_2_setor": "Indústria vinícola",
        "case_3_setor": "Autopeças",
        "vizinhas_texto": """<p>Além de Caxias do Sul, atendemos empresas em Bento Gonçalves, Garibaldi, Carlos Barbosa, Farroupilha, Nova Petrópolis, Flores da Cunha e São Marcos. <a href="/cidades-atendidas/">Ver todas as cidades atendidas</a>.</p>""",
        "vizinhas_links": """<div class="coverage-nearby-links">
  <a href="/cidades-atendidas/">Bento Gonçalves</a>
  <a href="/cidades-atendidas/">Garibaldi</a>
  <a href="/cidades-atendidas/">Carlos Barbosa</a>
  <a href="/cidades-atendidas/">Farroupilha</a>
  <a href="/cidades-atendidas/">Nova Petrópolis</a>
  <a href="/cidades-atendidas/">Flores da Cunha</a>
  <a href="/cidades-atendidas/">São Marcos</a>
</div>""",
        "bairros_industrial": """<ul class="bairros-list">
  <li>Distrito Industrial</li>
  <li>Santa Catarina</li>
  <li>Panazzolo</li>
  <li>Cruzeiro</li>
  <li>São Ciro</li>
</ul>""",
        "bairros_comercial": """<ul class="bairros-list">
  <li>Centro</li>
  <li>Exposição</li>
  <li>Marechal Floriano</li>
  <li>Sagrada Família</li>
  <li>Rio Branco</li>
</ul>""",
        "bairros_residencial": """<ul class="bairros-list">
  <li>São Pelegrino</li>
  <li>Jardim América</li>
  <li>Champagnat</li>
  <li>Lourdes</li>
  <li>São Caetano</li>
</ul>""",
        "authority_h2": "Contabilidade em Caxias do Sul com domínio da indústria metal-mecânica gaúcha",
        "amanda_cta_h2": "Contadora em Caxias do Sul: Amanda Cabral, CRC/MG Ativo",
        "local_sec_h2": "Gestão fiscal especializada para o polo industrial da Serra Gaúcha",
        "services_h2_override": "Serviços contábeis para empresas de Caxias do Sul",
        "depo1_role": "S&#243;cio",
        "depo1_setor": "Metal-mecânica",
        "depo2_role": "Propriet&#225;ria",
        "depo2_setor": "Vinícola",
        "depo3_role": "Empres&#225;rio",
        "depo3_setor": "Indústria de autopeças",
        "context_local": """<p>Caxias do Sul é o maior polo metal-mecânico do Sul do Brasil, herança da imigração italiana que transformou a Serra Gaúcha em berço da indústria de precisão nacional. Fabricantes de implementos rodoviários, peças automotivas, equipamentos agrícolas e sistemas de transmissão exportam para mais de 80 países a partir do município. A cadeia vinícola, segundo eixo econômico da cidade, acrescenta uma camada de obrigações fiscais raramente encontrada em outros polos industriais gaúchos.</p>
<p>Indústrias metal-mecânicas com operações de exportação utilizam o drawback para suspender tributos na entrada de insumos importados e crédito de IPI sobre componentes adquiridos no mercado interno. O regime de ICMS do RS concede benefícios específicos para manufaturados destinados à exportação, mas exige escrituração segregada e cumprimento de condicionantes que variam por portaria estadual. Vinícolas e produtores de espumantes convivem com ICMS-ST sobre bebidas calculado com base em pautas fiscais por categoria, e o acompanhamento mensal dessas tabelas é o que separa o recolhimento correto do passivo silencioso.</p>
<p>Três décadas de prática tributária com indústrias do interior brasileiro consolidaram uma metodologia de auditoria retroativa que quantifica o saldo credor represado, estima o valor recuperável e apresenta o resultado antes de qualquer proposta de honorários.</p>
<p>O atendimento começa por chamada de vídeo, sem necessidade de deslocamento. O levantamento tributário inicial é gratuito: cobre enquadramento atual, créditos acumulados nos últimos sessenta meses e riscos mapeados na escrituração vigente.</p>""",
    },

    # 11 — Fortaleza CE
    {
        "cidade": "Fortaleza",
        "uf": "CE",
        "cidade_uf": "fortaleza-ce",
        "cidade_slug": "contador-em-fortaleza",
        "canonical_url": "https://amcabralblindagem.com.br/fortaleza-ce/contador-em-fortaleza/",
        "wiki_url": "https://pt.wikipedia.org/wiki/Fortaleza",
        "wikidata_id": "Q82415",
        "geo_lat": "-3.7172",
        "geo_lng": "-38.5433",
        "gentilicio": "fortalezenses",
        "regiao": "Nordeste do Brasil",
        "foto": "fortaleza-vista-panoramica.jpg",
        "alt_foto": "Vista aérea de Fortaleza, CE",
        "caption_foto": "Fortaleza, capital do Ceará e polo de calçados e turismo do Nordeste",
        "case_1_setor": "Indústria de calçados",
        "case_2_setor": "Têxtil e confecção",
        "case_3_setor": "Turismo e hotelaria",
        "vizinhas_texto": """<p>Além de Fortaleza, atendemos empresas em Caucaia, Maracanaú, Horizonte, Pacatuba, Eusébio, Aquiraz e Maranguape. <a href="/cidades-atendidas/">Ver todas as cidades atendidas</a>.</p>""",
        "vizinhas_links": """<div class="coverage-nearby-links">
  <a href="/cidades-atendidas/">Caucaia</a>
  <a href="/cidades-atendidas/">Maracanaú</a>
  <a href="/cidades-atendidas/">Horizonte</a>
  <a href="/cidades-atendidas/">Pacatuba</a>
  <a href="/cidades-atendidas/">Eusébio</a>
  <a href="/cidades-atendidas/">Aquiraz</a>
  <a href="/cidades-atendidas/">Maranguape</a>
</div>""",
        "bairros_industrial": """<ul class="bairros-list">
  <li>Distrito Industrial</li>
  <li>Maracanaú</li>
  <li>Mondubim</li>
  <li>Bonsucesso</li>
  <li>Jangurussu</li>
</ul>""",
        "bairros_comercial": """<ul class="bairros-list">
  <li>Centro</li>
  <li>Aldeota</li>
  <li>Meireles</li>
  <li>Varjota</li>
  <li>Bairro de Fátima</li>
</ul>""",
        "bairros_residencial": """<ul class="bairros-list">
  <li>Cocó</li>
  <li>Dionísio Torres</li>
  <li>Papicu</li>
  <li>Edson Queiroz</li>
  <li>Messejana</li>
</ul>""",
        "authority_h2": "Contabilidade em Fortaleza com expertise no setor têxtil e calçadista",
        "amanda_cta_h2": "Contadora em Fortaleza: Amanda Cabral, CRC/MG Ativo",
        "local_sec_h2": "Planejamento fiscal para a capital econômica do Nordeste",
        "services_h2_override": "Serviços contábeis para empresas de Fortaleza",
        "depo1_role": "S&#243;cio",
        "depo1_setor": "Fábrica de calçados",
        "depo2_role": "Propriet&#225;ria",
        "depo2_setor": "Confecção têxtil",
        "depo3_role": "Empres&#225;rio",
        "depo3_setor": "Rede hoteleira",
        "context_local": """<p>Fortaleza lidera a produção calçadista do Nordeste brasileiro e abriga um dos maiores complexos têxteis do país, com fabricantes de rendas, bordados industriais e confecção de moda que abastecem varejistas de quatro continentes. A capital cearense não é só polo de manufatura: o turismo litorâneo sustenta uma rede hoteleira e de gastronomia que opera durante o ano inteiro, e o Maracanaú Industrial, distrito contíguo, concentra farmacêuticas e distribuidoras que ampliam a base fiscal do município.</p>
<p>Fábricas de calçados do Ceará operam sob regime de tributação concentrada, em que as contribuições sobre a receita são recolhidas pelo fabricante ou importador de matéria-prima a uma alíquota específica por código de produto, eliminando a incidência nas etapas seguintes. Quando a cadeia de fornecimento envolve partes importadas de países com acordo de não-dupla-tributação, a apuração do imposto de importação exige classificação correta na Tabela TIPI e validação das condicionantes do regime especial, dois pontos que a maioria dos escritórios convencionais terceiriza sem domínio real. Hotéis e pousadas de Fortaleza calculam a contribuição ao Fundo Municipal de Turismo sobre a receita de hospedagem, parcela que integra a base de cálculo do ISS mas raramente está segregada na escrituração padrão, gerando inconsistências visíveis em cruzamentos eletrônicos da Secretaria Municipal de Finanças.</p>
<p>A base metodológica construída em três décadas de assessoria a fabricantes e prestadores de serviços de diferentes perfis permite mapear, com exatidão, onde cada operação acumula tributação acima do que a legislação determina.</p>
<p>Para empresas de Fortaleza, a análise de viabilidade tributária não tem custo. O trabalho acontece por formato digital, abrange o enquadramento atual da empresa, o aproveitamento de crédito no período de prescrição de cinco anos e as inconsistências identificadas nos arquivos de escrituração periódica.</p>""",
    },

    # 12 — Goiânia GO
    {
        "cidade": "Goiânia",
        "uf": "GO",
        "cidade_uf": "goiania-go",
        "cidade_slug": "contador-em-goiania",
        "canonical_url": "https://amcabralblindagem.com.br/goiania-go/contador-em-goiania/",
        "wiki_url": "https://pt.wikipedia.org/wiki/Goiânia",
        "wikidata_id": "Q82426",
        "geo_lat": "-16.6869",
        "geo_lng": "-49.2648",
        "gentilicio": "goianienses",
        "regiao": "Centro-Oeste do Brasil",
        "foto": "goiania-vista-panoramica.jpg",
        "alt_foto": "Vista aérea de Goiânia, GO",
        "caption_foto": "Goiânia, capital de Goiás e polo de saúde e agronegócio do Centro-Oeste",
        "case_1_setor": "Saúde e medicina",
        "case_2_setor": "Agronegócio",
        "case_3_setor": "Comércio e serviços",
        "vizinhas_texto": """<p>Além de Goiânia, atendemos empresas em Aparecida de Goiânia, Anápolis, Senador Canedo, Trindade, Inhumas, Nerópolis e Goianira. <a href="/cidades-atendidas/">Ver todas as cidades atendidas</a>.</p>""",
        "vizinhas_links": """<div class="coverage-nearby-links">
  <a href="/cidades-atendidas/">Aparecida de Goiânia</a>
  <a href="/cidades-atendidas/">Anápolis</a>
  <a href="/cidades-atendidas/">Senador Canedo</a>
  <a href="/cidades-atendidas/">Trindade</a>
  <a href="/cidades-atendidas/">Inhumas</a>
  <a href="/cidades-atendidas/">Nerópolis</a>
  <a href="/cidades-atendidas/">Goianira</a>
</div>""",
        "bairros_industrial": """<ul class="bairros-list">
  <li>Distrito Agroindustrial</li>
  <li>Jardim Goiás</li>
  <li>Leste Universitário</li>
  <li>Setor Industrial</li>
  <li>Recanto do Bosque</li>
</ul>""",
        "bairros_comercial": """<ul class="bairros-list">
  <li>Setor Central</li>
  <li>Setor Bueno</li>
  <li>Setor Marista</li>
  <li>Setor Oeste</li>
  <li>Setor Sul</li>
</ul>""",
        "bairros_residencial": """<ul class="bairros-list">
  <li>Setor Jardim América</li>
  <li>Setor Pedro Ludovico</li>
  <li>Setor Nova Suíça</li>
  <li>Setor Campinas</li>
  <li>Jardim Atlântico</li>
</ul>""",
        "authority_h2": "Contabilidade em Goiânia para saúde, agronegócio e serviços especializados",
        "amanda_cta_h2": "Contadora em Goiânia: Amanda Cabral, CRC/MG Ativo",
        "local_sec_h2": "Assessoria tributária para a capital do agronegócio brasileiro",
        "services_h2_override": "Serviços contábeis para empresas de Goiânia",
        "depo1_role": "S&#243;cio",
        "depo1_setor": "Clínica médica especializada",
        "depo2_role": "Propriet&#225;ria",
        "depo2_setor": "Cooperativa agropecuária",
        "depo3_role": "Empres&#225;rio",
        "depo3_setor": "Distribuidor de insumos agrícolas",
        "context_local": """<p>Goiânia se posiciona como o maior centro de saúde privada do Centro-Oeste brasileiro e a principal praça comercial do agronegócio goiano. Hospitais oncológicos de referência nacional, clínicas de reprodução assistida, hemodinâmica e ortopedia de alta complexidade operam ao lado de tradings de soja, milho e algodão que movimentam contratos bilionários por safra, criando uma base fiscal de duas velocidades dentro do mesmo município.</p>
<p>Clínicas e hospitais de médio porte que ultrapassaram o teto do regime unificado precisam calcular a carga tributária comparativa entre regimes antes de tomar a decisão anual, que é irretratável: a proporção entre folha de especialistas e receita total define qual modalidade gera menor pressão fiscal, e essa equação muda conforme o mix de procedimentos. Tradings agropecuárias escrituram a contribuição previdenciária sobre a receita bruta de operações de exportação e precisam acompanhar as mudanças na legislação de ICMS/GO sobre transferências interestaduais de commodities, cujo diferimento varia por decreto do Conselho de Política Fazendária. Distribuidoras de defensivos e fertilizantes operam com ICMS com alíquota reduzida ou diferida para insumos destinados à produção agropecuária, benefício condicionado à destinação efetiva do produto e à emissão correta de documentos fiscais por operação.</p>
<p>A prática de três décadas com empresas de perfil fiscal diversificado consolidou uma metodologia de diagnóstico que parte dos dados reais de cada operação antes de sugerir qualquer alteração de estrutura ou regime.</p>
<p>Novos clientes de Goiânia recebem uma avaliação tributária sem custo, conduzida por conexão digital. O escopo abrange o regime de tributação atual, o período prescricional de cinco anos para aproveitamento retroativo de crédito e os pontos de risco detectados na escrituração periódica da empresa.</p>""",
    },

    # 13 — João Pessoa PB
    {
        "cidade": "João Pessoa",
        "uf": "PB",
        "cidade_uf": "joao-pessoa-pb",
        "cidade_slug": "contador-em-joao-pessoa",
        "canonical_url": "https://amcabralblindagem.com.br/joao-pessoa-pb/contador-em-joao-pessoa/",
        "wiki_url": "https://pt.wikipedia.org/wiki/João_Pessoa",
        "wikidata_id": "Q82461",
        "geo_lat": "-7.1195",
        "geo_lng": "-34.8450",
        "gentilicio": "pessoenses",
        "regiao": "Nordeste do Brasil",
        "foto": "joao-pessoa-vista-panoramica.jpg",
        "alt_foto": "Vista panorâmica de João Pessoa, PB",
        "caption_foto": "João Pessoa, capital da Paraíba, turismo e serviços no Nordeste",
        "case_1_setor": "Turismo e hotelaria",
        "case_2_setor": "Serviços de saúde",
        "case_3_setor": "Comércio varejista",
        "vizinhas_texto": """<p>Além de João Pessoa, atendemos empresas em Campina Grande, Cabedelo, Santa Rita, Bayeux, Cruz do Espírito Santo, Conde e Alhandra. <a href="/cidades-atendidas/">Ver todas as cidades atendidas</a>.</p>""",
        "vizinhas_links": """<div class="coverage-nearby-links">
  <a href="/cidades-atendidas/">Campina Grande</a>
  <a href="/cidades-atendidas/">Cabedelo</a>
  <a href="/cidades-atendidas/">Santa Rita</a>
  <a href="/cidades-atendidas/">Bayeux</a>
  <a href="/cidades-atendidas/">Cruz do Espírito Santo</a>
  <a href="/cidades-atendidas/">Conde</a>
  <a href="/cidades-atendidas/">Alhandra</a>
</div>""",
        "bairros_industrial": """<ul class="bairros-list">
  <li>Distrito Industrial</li>
  <li>Muçumagro</li>
  <li>Tambiá</li>
  <li>Cruz das Armas</li>
  <li>Valentina</li>
</ul>""",
        "bairros_comercial": """<ul class="bairros-list">
  <li>Centro</li>
  <li>Miramar</li>
  <li>Tambaú</li>
  <li>Bessa</li>
  <li>Expedicionários</li>
</ul>""",
        "bairros_residencial": """<ul class="bairros-list">
  <li>Altiplano Cabo Branco</li>
  <li>Jardim Oceania</li>
  <li>Bancários</li>
  <li>Mangabeira</li>
  <li>Castelo Branco</li>
</ul>""",
        "authority_h2": "Contabilidade em João Pessoa para turismo, saúde e prestadores de serviço",
        "amanda_cta_h2": "Contadora em João Pessoa: Amanda Cabral, CRC/MG Ativo",
        "local_sec_h2": "Gestão tributária remota para empresas da capital paraibana",
        "services_h2_override": "Serviços contábeis para empresas de João Pessoa",
        "depo1_role": "S&#243;cio",
        "depo1_setor": "Rede de pousadas",
        "depo2_role": "Propriet&#225;ria",
        "depo2_setor": "Clínica odontológica",
        "depo3_role": "Empres&#225;rio",
        "depo3_setor": "Varejista de moda",
        "context_local": """<p>João Pessoa detém o litoral mais próximo da Europa entre todas as capitais brasileiras, e esse diferencial geográfico moldou uma economia baseada em turismo de alto padrão, educação superior e serviços de saúde que atendem moradores do interior paraibano a centenas de quilômetros de distância. Hotéis de bandeira internacional na orla de Tambaú, faculdades privadas no eixo da Avenida Epitácio Pessoa e hospitais especializados no Bairro dos Bancários formam um triângulo econômico com obrigações fiscais distintas por setor.</p>
<p>Estabelecimentos hoteleiros de João Pessoa calculam ISS sobre receita de hospedagem, café da manhã e serviços complementares separadamente, pois o município tributa cada atividade por alíquota própria estabelecida na lei complementar municipal, e a consolidação incorreta dos itens gera recolhimento a maior ou a menor detectável em cruzamento eletrônico com a nota fiscal de serviço. Faculdades e centros universitários privados que enquadram parte das receitas como imunes ou isentas de contribuições sociais precisam segregar com rigor os valores sujeitos ao PIS e ao COFINS das receitas protegidas, pois a ausência dessa segregação na EFD elimina o benefício por completo. Hospitais e clínicas que cobram procedimentos de pacientes de planos de saúde interligam ISS sobre a atividade médica, IRPJ sobre o resultado e retenção de IRRF sobre pagamentos a médicos autônomos, três obrigações que se cruzam em cada nota emitida.</p>
<p>A base acumulada em três décadas de assessoria a prestadores de serviços de diferentes portes permite identificar, com precisão cirúrgica, os pontos onde cada estrutura acumula carga tributária além do necessário.</p>
<p>A revisão tributária para novos clientes de João Pessoa é gratuita e ocorre por chamada digital. O trabalho cobre o regime fiscal atual da empresa, o aproveitamento dos créditos do período prescricional de cinco anos e as inconsistências identificadas nos documentos de apuração periódica.</p>""",
    },

    # 14 — Ribeirão Preto SP
    {
        "cidade": "Ribeirão Preto",
        "uf": "SP",
        "cidade_uf": "ribeirao-preto-sp",
        "cidade_slug": "contador-em-ribeirao-preto",
        "canonical_url": "https://amcabralblindagem.com.br/ribeirao-preto-sp/contador-em-ribeirao-preto/",
        "wiki_url": "https://pt.wikipedia.org/wiki/Ribeirão_Preto",
        "wikidata_id": "Q193677",
        "geo_lat": "-21.1775",
        "geo_lng": "-47.8103",
        "gentilicio": "ribeirão-pretanos",
        "regiao": "interior de São Paulo",
        "foto": "ribeirao-preto-vista-panoramica.jpg",
        "alt_foto": "Vista panorâmica de Ribeirão Preto, SP",
        "caption_foto": "Ribeirão Preto, polo sucroalcooleiro e de saúde do interior paulista",
        "case_1_setor": "Usina sucroalcooleira",
        "case_2_setor": "Saúde e biotecnologia",
        "case_3_setor": "Agronegócio e distribuição",
        "vizinhas_texto": """<p>Além de Ribeirão Preto, atendemos empresas em Sertãozinho, Jaboticabal, Cravinhos, Serrana, Pradópolis, Pontal e Dumont. <a href="/cidades-atendidas/">Ver todas as cidades atendidas</a>.</p>""",
        "vizinhas_links": """<div class="coverage-nearby-links">
  <a href="/cidades-atendidas/">Sertãozinho</a>
  <a href="/cidades-atendidas/">Jaboticabal</a>
  <a href="/cidades-atendidas/">Cravinhos</a>
  <a href="/cidades-atendidas/">Serrana</a>
  <a href="/cidades-atendidas/">Pradópolis</a>
  <a href="/cidades-atendidas/">Pontal</a>
  <a href="/cidades-atendidas/">Dumont</a>
</div>""",
        "bairros_industrial": """<ul class="bairros-list">
  <li>Distrito Industrial</li>
  <li>Presidente Médici</li>
  <li>José Sampaio</li>
  <li>Bonfim Paulista</li>
  <li>Ribeirânia</li>
</ul>""",
        "bairros_comercial": """<ul class="bairros-list">
  <li>Centro</li>
  <li>Higienópolis</li>
  <li>Jardim Irajá</li>
  <li>Vila Amélia</li>
  <li>Boa Vista</li>
</ul>""",
        "bairros_residencial": """<ul class="bairros-list">
  <li>Jardim Sumaré</li>
  <li>Residencial Morro do Ipê</li>
  <li>Alto da Boa Vista</li>
  <li>Jardim Paulistano</li>
  <li>Nova Ribeirânia</li>
</ul>""",
        "authority_h2": "Contabilidade em Ribeirão Preto com expertise no sucroalcooleiro e saúde",
        "amanda_cta_h2": "Contadora em Ribeirão Preto: Amanda Cabral, CRC/MG Ativo",
        "local_sec_h2": "Assessoria fiscal para o polo de saúde e agronegócio de Ribeirão",
        "services_h2_override": "Serviços contábeis para empresas de Ribeirão Preto",
        "depo1_role": "S&#243;cio",
        "depo1_setor": "Usina de cana-de-açúcar",
        "depo2_role": "Propriet&#225;ria",
        "depo2_setor": "Clínica de oncologia",
        "depo3_role": "Empres&#225;rio",
        "depo3_setor": "Distribuidora de insumos agrícolas",
        "context_local": """<p>Ribeirão Preto centraliza a economia do agronegócio paulista: capital nacional do sucroalcooleiro, a cidade abriga usinas, destilarias e fornecedoras da cadeia canavieira que movimentam bilhões de reais por safra. Ao lado desse eixo produtivo, consolidou-se um complexo hospitalar e de biotecnologia referenciado em toda a América Latina, com hospitais universitários, centros de pesquisa clínica e clínicas oncológicas que atraem pacientes de dezenas de estados brasileiros.</p>
<p>Usinas sucroalcooleiras operam com crédito presumido de PIS/COFINS sobre a receita de etanol hidratado, ICMS com benefícios estaduais específicos para biocombustíveis concedidos pelo Estado de SP e Funrural sobre a produção rural integrada com fornecedores de cana. Hospitais e clínicas oncológicas de médio porte que ultrapassaram o teto do Supersimples precisam avaliar se o Lucro Presumido ou o Lucro Real gera menor carga, considerando a dedutibilidade de despesas médicas previstas na Lei 9.249 e o peso da folha de pagamento de especialistas no cálculo da CSLL. Distribuidoras de insumos agrícolas que transitam entre regimes acumulam crédito de ICMS nas entradas que, quando não escriturado mensalmente, vira ativo tributário represado sem gerar benefício de caixa.</p>
<p>A auditoria retroativa que aplicamos parte da escrituração existente para mapear o saldo credor acumulado em cada setor, quantifica o valor recuperável e apresenta o resultado antes de qualquer proposta de honorários.</p>
<p>O levantamento tributário de entrada é gratuito e ocorre por reunião virtual. O escopo abrange regime vigente, créditos acumulados nos últimos sessenta meses e riscos identificados na escrituração atual.</p>""",
    },

    # 15 — Salvador BA
    {
        "cidade": "Salvador",
        "uf": "BA",
        "cidade_uf": "salvador-ba",
        "cidade_slug": "contador-em-salvador",
        "canonical_url": "https://amcabralblindagem.com.br/salvador-ba/contador-em-salvador/",
        "wiki_url": "https://pt.wikipedia.org/wiki/Salvador",
        "wikidata_id": "Q82576",
        "geo_lat": "-12.9777",
        "geo_lng": "-38.5016",
        "gentilicio": "soteropolitanos",
        "regiao": "Nordeste do Brasil",
        "foto": "salvador-vista-panoramica.jpg",
        "alt_foto": "Vista panorâmica de Salvador, BA",
        "caption_foto": "Salvador, capital da Bahia, polo petroquímico e turístico do Nordeste",
        "case_1_setor": "Petroquímica e refinaria",
        "case_2_setor": "Turismo e entretenimento",
        "case_3_setor": "Serviços especializados",
        "vizinhas_texto": """<p>Além de Salvador, atendemos empresas em Camaçari, Lauro de Freitas, Simões Filho, Dias D'Ávila, São Francisco do Conde, Candeias e Mata de São João. <a href="/cidades-atendidas/">Ver todas as cidades atendidas</a>.</p>""",
        "vizinhas_links": """<div class="coverage-nearby-links">
  <a href="/cidades-atendidas/">Camaçari</a>
  <a href="/cidades-atendidas/">Lauro de Freitas</a>
  <a href="/cidades-atendidas/">Simões Filho</a>
  <a href="/cidades-atendidas/">Dias D'Ávila</a>
  <a href="/cidades-atendidas/">São Francisco do Conde</a>
  <a href="/cidades-atendidas/">Candeias</a>
  <a href="/cidades-atendidas/">Mata de São João</a>
</div>""",
        "bairros_industrial": """<ul class="bairros-list">
  <li>Polo Industrial de Camaçari</li>
  <li>CIA Norte</li>
  <li>CIA Sul</li>
  <li>Aratu</li>
  <li>São Caetano</li>
</ul>""",
        "bairros_comercial": """<ul class="bairros-list">
  <li>Centro Histórico</li>
  <li>Barra</li>
  <li>Pituba</li>
  <li>Itaigara</li>
  <li>Caminho das Árvores</li>
</ul>""",
        "bairros_residencial": """<ul class="bairros-list">
  <li>Graça</li>
  <li>Vitória</li>
  <li>Ondina</li>
  <li>Rio Vermelho</li>
  <li>Federação</li>
</ul>""",
        "authority_h2": "Contabilidade em Salvador com expertise em petroquímica e turismo",
        "amanda_cta_h2": "Contadora em Salvador: Amanda Cabral, CRC/MG Ativo",
        "local_sec_h2": "Planejamento fiscal para empresas da capital baiana",
        "services_h2_override": "Serviços contábeis para empresas de Salvador",
        "depo1_role": "S&#243;cio",
        "depo1_setor": "Fornecedor da cadeia petroquímica",
        "depo2_role": "Propriet&#225;ria",
        "depo2_setor": "Rede de restaurantes e turismo",
        "depo3_role": "Empres&#225;rio",
        "depo3_setor": "Prestadora de serviços empresariais",
        "context_local": """<p>Salvador combina dois vetores produtivos de peso nacional: o Complexo Petroquímico de Camaçari, com mais de 90 unidades integradas por dutos, utilidades e vapor compartilhados, e o porto de Aratu, principal corredor de exportação da Bahia para granéis sólidos e fertilizantes. A cadeia de fornecedores que orbita essas duas âncoras gera um volume de obrigações acessórias que extrapola o que escritórios de estrutura genérica conseguem processar com rigor técnico.</p>
<p>Fornecedoras de insumos ao polo de Camaçari emitem notas com CFOPs específicos para transferência de produto entre estabelecimentos do mesmo grupo econômico, situação que a Sefaz baiana trata de modo distinto da venda interestadual comum: o uso do CFOP errado gera glosa de crédito de ICMS que só se revela na auditoria eletrônica, depois que o prazo para retificação já venceu. Construtoras pesadas que executam obras de ampliação nas plantas petroquímicas precisam segregar o ISS sobre mão de obra e o ICMS sobre materiais aplicados na obra, pois Salvador tributa cada componente por alíquota própria com notas de serviço e de mercadoria emitidas em separado. Prestadoras de manutenção industrial com contratos de longo prazo sujeitam cada fatura a retenção simultânea de CSLL, PIS, COFINS e IRRF quando o contratante é pessoa jurídica optante pelo Lucro Real, o que transforma o fluxo de caixa mensal numa variável dependente da configuração correta do contrato.</p>
<p>Três décadas de acompanhamento a estruturas com alta densidade de obrigações periódicas consolidaram uma metodologia para mapear passivos silenciosos antes que se transformem em autuação.</p>
<p>Para novos clientes de Salvador, a avaliação tributária inicial não tem custo e ocorre por videoconferência. O levantamento cobre o regime de tributação vigente, a revisão dos créditos acumulados no quinquênio e os pontos de fragilidade identificados nos arquivos de escrituração da empresa.</p>""",
    },

    # 16 — Blumenau SC
    {
        "cidade": "Blumenau",
        "uf": "SC",
        "cidade_uf": "blumenau-sc",
        "cidade_slug": "contador-em-blumenau",
        "canonical_url": "https://amcabralblindagem.com.br/blumenau-sc/contador-em-blumenau/",
        "wiki_url": "https://pt.wikipedia.org/wiki/Blumenau",
        "wikidata_id": "Q207788",
        "geo_lat": "-26.9194",
        "geo_lng": "-49.0661",
        "gentilicio": "blumenauenses",
        "regiao": "Vale do Itajaí",
        "foto": "blumenau-vista-panoramica.jpg",
        "alt_foto": "Vista panorâmica de Blumenau, SC",
        "caption_foto": "Blumenau, polo têxtil e de tecnologia do Vale do Itajaí",
        "case_1_setor": "Indústria têxtil e confecção",
        "case_2_setor": "Tecnologia da informação",
        "case_3_setor": "Comércio e serviços",
        "vizinhas_texto": """<p>Além de Blumenau, atendemos empresas em Gaspar, Indaial, Timbó, Pomerode, Brusque, Guabiruba e Apiúna. <a href="/cidades-atendidas/">Ver todas as cidades atendidas</a>.</p>""",
        "vizinhas_links": """<div class="coverage-nearby-links">
  <a href="/cidades-atendidas/">Gaspar</a>
  <a href="/cidades-atendidas/">Indaial</a>
  <a href="/cidades-atendidas/">Timbó</a>
  <a href="/cidades-atendidas/">Pomerode</a>
  <a href="/cidades-atendidas/">Brusque</a>
  <a href="/cidades-atendidas/">Guabiruba</a>
  <a href="/cidades-atendidas/">Apiúna</a>
</div>""",
        "bairros_industrial": """<ul class="bairros-list">
  <li>Distrito Industrial</li>
  <li>Itoupava Norte</li>
  <li>Ponta Aguda</li>
  <li>Água Verde</li>
  <li>Garcia</li>
</ul>""",
        "bairros_comercial": """<ul class="bairros-list">
  <li>Centro</li>
  <li>Vila Nova</li>
  <li>Itoupavazinha</li>
  <li>Bom Retiro</li>
  <li>Asilo</li>
</ul>""",
        "bairros_residencial": """<ul class="bairros-list">
  <li>Fortaleza</li>
  <li>Velha</li>
  <li>Passo Manso</li>
  <li>Progresso</li>
  <li>Badenfurt</li>
</ul>""",
        "authority_h2": "Contabilidade em Blumenau com domínio do setor têxtil e de tecnologia",
        "amanda_cta_h2": "Contadora em Blumenau: Amanda Cabral, CRC/MG Ativo",
        "local_sec_h2": "Expertise fiscal para o polo têxtil e tech do Vale do Itajaí",
        "services_h2_override": "Serviços contábeis para empresas de Blumenau",
        "depo1_role": "S&#243;cio",
        "depo1_setor": "Fábrica de confecção",
        "depo2_role": "Propriet&#225;ria",
        "depo2_setor": "Empresa de software",
        "depo3_role": "Empres&#225;rio",
        "depo3_setor": "Indústria de fios e tecidos",
        "context_local": """<p>Blumenau divide o espaço urbano entre o maior parque têxtil da Região Sul e um polo tecnológico com empresas de software, automação industrial e cibersegurança que faturaram mais de R$ 3 bilhões em 2023. A convivência entre teares jacquard e servidores de computação em nuvem não é apenas curiosidade histórica: ela cria obrigações fiscais com lógicas completamente distintas que convivem no mesmo perfil de contribuinte e exigem tratamento separado por atividade.</p>
<p>Fábricas de confecção do Vale do Itajaí que adotam o regime cumulativo de PIS e COFINS pagam alíquotas menores sobre a receita, mas abrem mão do crédito sobre insumos. Quando o volume de compras de tecido e aviamentos é alto em relação ao faturamento, o regime não cumulativo pode ser mais vantajoso, mas essa análise precisa ser feita com os números reais da empresa, não com estimativas setoriais. Marcas de moda blumenauenses que licenciam estampas e coleções para confeccionistas de outros estados precisam classificar o pagamento como royalty sujeito a IRPJ e CIDE ou como prestação de serviço sujeita a ISS, escolha que impacta diretamente a alíquota efetiva e a forma de retenção na fonte. Empresas de software com contratos de licença recorrente para clientes em municípios de outros estados enfrentam a controvérsia da LC 157/2016 sobre ISS: pagar no destino ou na origem é uma questão que cada prefeitura ainda interpreta à sua forma, gerando risco de bitributação ou de autuação por não retenção.</p>
<p>Três décadas de prática com indústrias de transformação e prestadores de serviços consolidaram uma metodologia para mapear o excedente tributário por atividade antes de propor qualquer ajuste de enquadramento.</p>
<p>Novos clientes de Blumenau recebem uma avaliação fiscal gratuita por videoconferência. O diagnóstico abrange o regime de tributação em vigor, os direitos creditórios dos últimos cinco exercícios e os pontos de inconsistência identificados na escrituração da empresa.</p>""",
    },

    # 17 — Feira de Santana BA
    {
        "cidade": "Feira de Santana",
        "uf": "BA",
        "cidade_uf": "feira-de-santana-ba",
        "cidade_slug": "contador-em-feira-de-santana",
        "canonical_url": "https://amcabralblindagem.com.br/feira-de-santana-ba/contador-em-feira-de-santana/",
        "wiki_url": "https://pt.wikipedia.org/wiki/Feira_de_Santana",
        "wikidata_id": "Q204322",
        "geo_lat": "-12.2664",
        "geo_lng": "-38.9663",
        "gentilicio": "feirenses",
        "regiao": "Nordeste da Bahia",
        "foto": "feira-de-santana-vista-panoramica.jpg",
        "alt_foto": "Vista panorâmica de Feira de Santana, BA",
        "caption_foto": "Feira de Santana, maior centro comercial do Nordeste baiano",
        "case_1_setor": "Comércio atacadista",
        "case_2_setor": "Indústria de calçados",
        "case_3_setor": "Distribuição regional",
        "vizinhas_texto": """<p>Além de Feira de Santana, atendemos empresas em Serrinha, Santo Estêvão, Amélia Rodrigues, Conceição do Jacuípe, Tanquinho, Coração de Maria e São Gonçalo dos Campos. <a href="/cidades-atendidas/">Ver todas as cidades atendidas</a>.</p>""",
        "vizinhas_links": """<div class="coverage-nearby-links">
  <a href="/cidades-atendidas/">Serrinha</a>
  <a href="/cidades-atendidas/">Santo Estêvão</a>
  <a href="/cidades-atendidas/">Amélia Rodrigues</a>
  <a href="/cidades-atendidas/">Conceição do Jacuípe</a>
  <a href="/cidades-atendidas/">Tanquinho</a>
  <a href="/cidades-atendidas/">Coração de Maria</a>
  <a href="/cidades-atendidas/">São Gonçalo dos Campos</a>
</div>""",
        "bairros_industrial": """<ul class="bairros-list">
  <li>Centro Industrial Subaé</li>
  <li>Tomba</li>
  <li>Brasília</li>
  <li>Sobradinho</li>
  <li>Pedra do Descanso</li>
</ul>""",
        "bairros_comercial": """<ul class="bairros-list">
  <li>Centro</li>
  <li>Caseb</li>
  <li>Capuchinhos</li>
  <li>Cidade Nova</li>
  <li>Ponto Central</li>
</ul>""",
        "bairros_residencial": """<ul class="bairros-list">
  <li>Papagaio</li>
  <li>Campo Limpo</li>
  <li>Jardim Cruzeiro</li>
  <li>Santa Mônica</li>
  <li>George Américo</li>
</ul>""",
        "authority_h2": "Contabilidade em Feira de Santana para o maior polo atacadista da Bahia",
        "amanda_cta_h2": "Contadora em Feira de Santana: Amanda Cabral, CRC/MG Ativo",
        "local_sec_h2": "Otimização tributária para o hub comercial do interior baiano",
        "services_h2_override": "Serviços contábeis para empresas de Feira de Santana",
        "depo1_role": "S&#243;cio",
        "depo1_setor": "Atacadista regional",
        "depo2_role": "Propriet&#225;ria",
        "depo2_setor": "Indústria de calçados",
        "depo3_role": "Empres&#225;rio",
        "depo3_setor": "Distribuidora de alimentos",
        "context_local": """<p>Feira de Santana funciona como o principal nó de redistribuição comercial do Nordeste baiano: sua posição geográfica no cruzamento das rodovias BR-116 e BR-324 faz da cidade o ponto de passagem obrigatório para cargas que chegam de São Paulo, de Minas Gerais e dos portos do Sul antes de abastecer o semiárido e o litoral norte da Bahia. O Centro Industrial Subaé acrescenta a esse perfil fabricantes de calçados, artigos de couro e alimentos processados que vendem para mercados distantes com tributação estadual específica da Bahia.</p>
<p>Atacadistas redistribuidores de Feira de Santana que emitem notas fiscais de transferência para filiais em outros estados precisam usar os CFOPs corretos para cada tipo de movimentação: transferência entre estabelecimentos do mesmo contribuinte tem tratamento fiscal diferente de venda interestadual, e a confusão entre os dois gera apuração incorreta do ICMS que o auditor fiscal da Sefaz-BA localiza com precisão no cruzamento das GIAs. Fabricantes de artigos de couro e calçados que vendem para atacadistas do Sul e Sudeste precisam aplicar a alíquota interestadual correta por destino e calcular o DIFAL quando o comprador é consumidor final não contribuinte, dois pontos que a legislação estadual baiana trata em portarias distintas com tabelas atualizadas por período de competência. Distribuidoras de alimentos que transitam entre o Simples Nacional e o Lucro Presumido precisam avaliar o impacto da mudança no regime de substituição tributária da Bahia antes de efetuar a opção fiscal do ano seguinte.</p>
<p>A base acumulada em três décadas de assessoria a empresas comerciais e industriais permite mapear com precisão o tributo pago além do necessário e estimar o retorno antes de qualquer engajamento.</p>
<p>Para novos clientes de Feira de Santana, a primeira análise tributária é gratuita e ocorre por transmissão digital. O escopo cobre o enquadramento fiscal vigente, a revisão dos cinco últimos exercícios e os riscos de autuação identificados nos documentos de apuração periódica.</p>""",
    },

    # 18 — Piracicaba SP
    {
        "cidade": "Piracicaba",
        "uf": "SP",
        "cidade_uf": "piracicaba-sp",
        "cidade_slug": "contador-em-piracicaba",
        "canonical_url": "https://amcabralblindagem.com.br/piracicaba-sp/contador-em-piracicaba/",
        "wiki_url": "https://pt.wikipedia.org/wiki/Piracicaba",
        "wikidata_id": "Q172487",
        "geo_lat": "-22.7253",
        "geo_lng": "-47.6476",
        "gentilicio": "piracicabanos",
        "regiao": "interior de São Paulo",
        "foto": "piracicaba-vista-panoramica.jpg",
        "alt_foto": "Vista panorâmica de Piracicaba, SP",
        "caption_foto": "Piracicaba, polo sucroalcooleiro e metal-mecânico do interior paulista",
        "case_1_setor": "Sucroalcooleiro",
        "case_2_setor": "Metal-mecânica agrícola",
        "case_3_setor": "Comércio e serviços",
        "vizinhas_texto": """<p>Além de Piracicaba, atendemos empresas em Limeira, Rio Claro, Santa Gertrudes, Saltinho, Santa Maria da Serra, Capivari e Rafard. <a href="/cidades-atendidas/">Ver todas as cidades atendidas</a>.</p>""",
        "vizinhas_links": """<div class="coverage-nearby-links">
  <a href="/cidades-atendidas/">Limeira</a>
  <a href="/cidades-atendidas/">Rio Claro</a>
  <a href="/cidades-atendidas/">Santa Gertrudes</a>
  <a href="/cidades-atendidas/">Saltinho</a>
  <a href="/cidades-atendidas/">Santa Maria da Serra</a>
  <a href="/cidades-atendidas/">Capivari</a>
  <a href="/cidades-atendidas/">Rafard</a>
</div>""",
        "bairros_industrial": """<ul class="bairros-list">
  <li>Distrito Industrial</li>
  <li>Santa Terezinha</li>
  <li>Nova América</li>
  <li>Área Industrial</li>
  <li>Algodoal</li>
</ul>""",
        "bairros_comercial": """<ul class="bairros-list">
  <li>Centro</li>
  <li>Jardim Elite</li>
  <li>Vila Sônia</li>
  <li>Alemães</li>
  <li>Morumbi</li>
</ul>""",
        "bairros_residencial": """<ul class="bairros-list">
  <li>Jardim São Jorge</li>
  <li>Alto</li>
  <li>Paulicéia</li>
  <li>Vila Cristina</li>
  <li>Residencial Furlan</li>
</ul>""",
        "authority_h2": "Contabilidade em Piracicaba com expertise no sucroalcooleiro paulista",
        "amanda_cta_h2": "Contadora em Piracicaba: Amanda Cabral, CRC/MG Ativo",
        "local_sec_h2": "Assessoria fiscal para usinas e fornecedores da cana-de-açúcar",
        "services_h2_override": "Serviços contábeis para empresas de Piracicaba",
        "depo1_role": "S&#243;cio",
        "depo1_setor": "Fornecedor de cana-de-açúcar",
        "depo2_role": "Propriet&#225;ria",
        "depo2_setor": "Fabricante de implementos agrícolas",
        "depo3_role": "Empres&#225;rio",
        "depo3_setor": "Prestador de serviços à indústria",
        "context_local": """<p>Piracicaba ocupa uma posição singular no interior paulista: a ESALQ da USP instalada às margens do rio desde 1901 tornou a cidade o principal centro de pesquisa em melhoramento genético de cana-de-açúcar do mundo, e esse legado científico sustenta hoje uma constelação de usinas, destilarias, fornecedores de cana e startups de bioenergia que operam com modelos de receita distintos dos setores industriais convencionais. A metalurgia agrícola voltada para colheitadeiras, prensas de bagaço e sistemas de bombeamento complementa esse perfil com uma base manufatureira de médio porte.</p>
<p>Usinas sucroalcooleiras do entorno de Piracicaba que vendem etanol hidratado para distribuidoras de combustível escrituram o crédito presumido de PIS e COFINS por tonelada de cana processada, mecanismo regulado por instrução normativa com tabela de valores atualizada anualmente pela Receita Federal: a aplicação do coeficiente do ano anterior gera apuração incorreta que se acumula silenciosamente ao longo do exercício. Cooperativas de fornecedores rurais que entregam cana a mais de uma usina dentro do mesmo período de safra precisam emitir nota de produtor para cada destinatário separado e controlar o Funrural por operação, pois o INSS rural incide sobre o valor bruto recebido em cada entrega sem compensação cruzada entre usinas. Fornecedores de peças e subconjuntos para colheitadeiras que atendem montadoras de São Paulo e Minas Gerais emitem nota com alíquota interestadual de ICMS e precisam acompanhar o DIFAL cobrado pelo estado do destinatário para não ser surpreendido com auto de infração estadual.</p>
<p>Três décadas de acompanhamento ao setor sucroalcooleiro e à metalurgia agrícola sedimentaram uma metodologia para mapear o excedente tributário com base nos registros reais da empresa.</p>
<p>Para novos clientes de Piracicaba, a triagem fiscal inicial não tem custo e ocorre por transmissão digital. O levantamento abrange o enquadramento vigente, a revisão dos créditos do quinquênio e as falhas de apuração identificadas nos arquivos periódicos da empresa.</p>""",
    },

    # 19 — Recife PE
    {
        "cidade": "Recife",
        "uf": "PE",
        "cidade_uf": "recife-pe",
        "cidade_slug": "contador-em-recife",
        "canonical_url": "https://amcabralblindagem.com.br/recife-pe/contador-em-recife/",
        "wiki_url": "https://pt.wikipedia.org/wiki/Recife",
        "wikidata_id": "Q42646",
        "geo_lat": "-8.0522",
        "geo_lng": "-34.9286",
        "gentilicio": "recifenses",
        "regiao": "Nordeste do Brasil",
        "foto": "recife-vista-panoramica.jpg",
        "alt_foto": "Vista aérea de Recife, PE",
        "caption_foto": "Recife, capital de Pernambuco e polo tecnológico do Nordeste",
        "case_1_setor": "Tecnologia da informação",
        "case_2_setor": "Porto e logística",
        "case_3_setor": "Saúde e serviços",
        "vizinhas_texto": """<p>Além de Recife, atendemos empresas em Caruaru, Olinda, Paulista, Jaboatão dos Guararapes, Cabo de Santo Agostinho, Ipojuca e Moreno. <a href="/cidades-atendidas/">Ver todas as cidades atendidas</a>.</p>""",
        "vizinhas_links": """<div class="coverage-nearby-links">
  <a href="/cidades-atendidas/">Caruaru</a>
  <a href="/cidades-atendidas/">Olinda</a>
  <a href="/cidades-atendidas/">Paulista</a>
  <a href="/cidades-atendidas/">Jaboatão dos Guararapes</a>
  <a href="/cidades-atendidas/">Cabo de Santo Agostinho</a>
  <a href="/cidades-atendidas/">Ipojuca</a>
  <a href="/cidades-atendidas/">Moreno</a>
</div>""",
        "bairros_industrial": """<ul class="bairros-list">
  <li>SUAPE</li>
  <li>Curado</li>
  <li>Imbiribeira</li>
  <li>Afogados</li>
  <li>Tejipió</li>
</ul>""",
        "bairros_comercial": """<ul class="bairros-list">
  <li>Boa Vista</li>
  <li>Santo Antônio</li>
  <li>São José</li>
  <li>Boa Viagem</li>
  <li>Derby</li>
</ul>""",
        "bairros_residencial": """<ul class="bairros-list">
  <li>Casa Forte</li>
  <li>Torre</li>
  <li>Madalena</li>
  <li>Jaqueira</li>
  <li>Espinheiro</li>
</ul>""",
        "authority_h2": "Contabilidade em Recife com expertise em tecnologia e comércio portuário",
        "amanda_cta_h2": "Contadora em Recife: Amanda Cabral, CRC/MG Ativo",
        "local_sec_h2": "Planejamento tributário para o polo tech e portuário de Recife",
        "services_h2_override": "Serviços contábeis para empresas de Recife",
        "depo1_role": "S&#243;cio",
        "depo1_setor": "Empresa de tecnologia",
        "depo2_role": "Propriet&#225;ria",
        "depo2_setor": "Operadora de logística portuária",
        "depo3_role": "Empres&#225;rio",
        "depo3_setor": "Clínica de saúde",
        "context_local": """<p>Recife reúne dois vetores econômicos de escala nacional que raramente coexistem numa mesma capital: o Porto Digital, ecossistema com mais de 300 empresas de software, games e serviços digitais no bairro histórico do Recife Antigo, e o Complexo Portuário de SUAPE, em Ipojuca, segundo maior porto do Nordeste e sede de operadores logísticos, refinaria e indústrias navais que movimentam bilhões em comércio exterior.</p>
<p>Empresas beneficiárias do Fundo de Incentivo à Cultura do Recife precisam cumprir condicionantes de geração de emprego e investimento para manter a isenção de ISS municipal: qualquer descumprimento gera estorno retroativo que transforma o benefício em passivo fiscal de difícil contestação. Operadores logísticos de SUAPE escrituram o ICMS sobre transferências de mercadorias em trânsito interestadual, o PIS e o COFINS sobre serviços de armazenagem em regime não cumulativo e a retenção de IRRF em contratos com tomadores pessoa jurídica, exigindo controle simultâneo de três esferas tributárias por operação. Desenvolvedoras de software sediadas no Porto Digital com contratos de licenciamento para clientes em outros estados precisam calcular o ISS conforme a legislação do município do tomador do serviço, não do prestador, o que exige conhecer a lista de serviços municipal de cada cidade onde o cliente está domiciliado.</p>
<p>Trinta anos de assessoria a empresas de diferentes portes e setores formaram uma base metodológica para mapear passivos ocultos e direitos creditórios com precisão antes de propor qualquer ajuste de enquadramento.</p>
<p>A consulta tributária inicial para novos clientes de Recife não tem custo e ocorre por transmissão digital. O diagnóstico cobre o regime de tributação em vigor, a auditoria dos últimos cinco exercícios fiscais e os riscos identificados nos documentos de apuração periódica da empresa.</p>""",
    },

    # 20 — Rio de Janeiro RJ
    {
        "cidade": "Rio de Janeiro",
        "uf": "RJ",
        "cidade_uf": "rio-de-janeiro-rj",
        "cidade_slug": "contador-em-rio-de-janeiro",
        "canonical_url": "https://amcabralblindagem.com.br/rio-de-janeiro-rj/contador-em-rio-de-janeiro/",
        "wiki_url": "https://pt.wikipedia.org/wiki/Rio_de_Janeiro",
        "wikidata_id": "Q8678",
        "geo_lat": "-22.9068",
        "geo_lng": "-43.1729",
        "gentilicio": "cariocas",
        "regiao": "Sudeste do Brasil",
        "foto": "rio-de-janeiro-vista-panoramica.jpg",
        "alt_foto": "Vista panorâmica do Rio de Janeiro, RJ",
        "caption_foto": "Rio de Janeiro, polo de óleo e gás, turismo e serviços do Brasil",
        "case_1_setor": "Óleo, gás e energia",
        "case_2_setor": "Turismo e entretenimento",
        "case_3_setor": "Serviços financeiros",
        "vizinhas_texto": """<p>Além do Rio de Janeiro, atendemos empresas em Niterói, São Gonçalo, Duque de Caxias, Nova Iguaçu, Belford Roxo, Petrópolis e Volta Redonda. <a href="/cidades-atendidas/">Ver todas as cidades atendidas</a>.</p>""",
        "vizinhas_links": """<div class="coverage-nearby-links">
  <a href="/cidades-atendidas/">Niterói</a>
  <a href="/cidades-atendidas/">São Gonçalo</a>
  <a href="/cidades-atendidas/">Duque de Caxias</a>
  <a href="/cidades-atendidas/">Nova Iguaçu</a>
  <a href="/cidades-atendidas/">Belford Roxo</a>
  <a href="/cidades-atendidas/">Petrópolis</a>
  <a href="/cidades-atendidas/">Volta Redonda</a>
</div>""",
        "bairros_industrial": """<ul class="bairros-list">
  <li>Santa Cruz</li>
  <li>Campo Grande</li>
  <li>Paciência</li>
  <li>Duque de Caxias</li>
  <li>Vigário Geral</li>
</ul>""",
        "bairros_comercial": """<ul class="bairros-list">
  <li>Centro</li>
  <li>Barra da Tijuca</li>
  <li>Botafogo</li>
  <li>Ipanema</li>
  <li>Flamengo</li>
</ul>""",
        "bairros_residencial": """<ul class="bairros-list">
  <li>Leblon</li>
  <li>Gávea</li>
  <li>Recreio dos Bandeirantes</li>
  <li>São Conrado</li>
  <li>Laranjeiras</li>
</ul>""",
        "authority_h2": "Contabilidade no Rio de Janeiro com expertise em óleo, gás e serviços",
        "amanda_cta_h2": "Contadora no Rio de Janeiro: Amanda Cabral, CRC/MG Ativo",
        "local_sec_h2": "Assessoria tributária para fornecedores da cadeia de óleo e gás",
        "services_h2_override": "Serviços contábeis para empresas do Rio de Janeiro",
        "depo1_role": "S&#243;cio",
        "depo1_setor": "Fornecedor da cadeia de óleo e gás",
        "depo2_role": "Propriet&#225;ria",
        "depo2_setor": "Operadora de turismo",
        "depo3_role": "Empres&#225;rio",
        "depo3_setor": "Serviços financeiros",
        "context_local": """<p>O Rio de Janeiro é o único estado brasileiro onde royalties de petróleo compõem parcela significativa do orçamento municipal de dezenas de cidades, e esse fluxo de recursos atrai fornecedoras da cadeia de óleo e gás que instalam filiais na capital para atender a Petrobras, a Shell e as independentes que operam nos campos do pré-sal. O Porto do Rio e o complexo de Itaguaí formam um segundo eixo de atração para operadores logísticos, agentes de carga e tradings que movimentam exportações de minério, açúcar e commodities agrícolas por via marítima.</p>
<p>Fornecedoras de bens e serviços para plataformas offshore escrituram contratos com cláusulas de câmbio e controlam o IOF sobre variação cambial em contratos denominados em dólar, além do regime aduaneiro especial de admissão temporária para equipamentos que retornam à plataforma após manutenção em terra, condição que a Receita Federal fiscaliza pelo cruzamento entre o Radar e o SISCOMEX. Agentes de carga e operadores de armazém alfandegado no Porto do Rio emitem conhecimento de embarque para cada lote de mercadoria e precisam conciliar o ICMS sobre a operação de saída com o PIS e COFINS sobre a receita de armazenagem, calculados em regimes distintos dependendo da natureza do contrato com o exportador. Tradings que compram commodity de produtores rurais para exportação controlam o crédito presumido de PIS e COFINS por tonelada embarcada, crédito que só pode ser aproveitado mediante comprovação de efetivo embarque registrado no SISCOMEX.</p>
<p>Trinta anos de assessoria a estruturas de elevada complexidade formaram uma metodologia de mapeamento que parte dos registros reais da empresa para quantificar o excedente tributário antes de qualquer proposta de honorários.</p>
<p>Para novos clientes do Rio de Janeiro, a avaliação tributária inicial não tem custo e ocorre por videoconferência. O trabalho cobre o enquadramento fiscal em vigor, a auditoria dos créditos do quinquênio e os pontos de fragilidade detectados nos arquivos de apuração periódica da empresa.</p>""",
    },

    # 21 — Joinville SC
    {
        "cidade": "Joinville",
        "uf": "SC",
        "cidade_uf": "joinville-sc",
        "cidade_slug": "contador-em-joinville",
        "canonical_url": "https://amcabralblindagem.com.br/joinville-sc/contador-em-joinville/",
        "wiki_url": "https://pt.wikipedia.org/wiki/Joinville",
        "wikidata_id": "Q207830",
        "geo_lat": "-26.3044",
        "geo_lng": "-48.8487",
        "gentilicio": "joinvilenses",
        "regiao": "Norte Catarinense",
        "foto": "joinville-vista-panoramica.jpg",
        "alt_foto": "Vista panorâmica de Joinville, SC",
        "caption_foto": "Joinville, maior polo industrial de Santa Catarina",
        "case_1_setor": "Metal-mecânica",
        "case_2_setor": "Plástico e embalagens",
        "case_3_setor": "Tecnologia e serviços",
        "vizinhas_texto": """<p>Além de Joinville, atendemos empresas em Jaraguá do Sul, São Francisco do Sul, Araquari, Guaramirim, Schroeder, Barra Velha e Balneário Barra do Sul. <a href="/cidades-atendidas/">Ver todas as cidades atendidas</a>.</p>""",
        "vizinhas_links": """<div class="coverage-nearby-links">
  <a href="/cidades-atendidas/">Jaraguá do Sul</a>
  <a href="/cidades-atendidas/">São Francisco do Sul</a>
  <a href="/cidades-atendidas/">Araquari</a>
  <a href="/cidades-atendidas/">Guaramirim</a>
  <a href="/cidades-atendidas/">Schroeder</a>
  <a href="/cidades-atendidas/">Barra Velha</a>
  <a href="/cidades-atendidas/">Balneário Barra do Sul</a>
</div>""",
        "bairros_industrial": """<ul class="bairros-list">
  <li>Zona Industrial Norte</li>
  <li>Zona Industrial Tupy</li>
  <li>Itaum</li>
  <li>Boehmerwald</li>
  <li>Iririú</li>
</ul>""",
        "bairros_comercial": """<ul class="bairros-list">
  <li>Centro</li>
  <li>América</li>
  <li>Bucarein</li>
  <li>Anita Garibaldi</li>
  <li>Boa Vista</li>
</ul>""",
        "bairros_residencial": """<ul class="bairros-list">
  <li>Glória</li>
  <li>Floresta</li>
  <li>Fátima</li>
  <li>Costa e Silva</li>
  <li>Aventureiro</li>
</ul>""",
        "authority_h2": "Contabilidade em Joinville com domínio do polo metal-mecânico catarinense",
        "amanda_cta_h2": "Contadora em Joinville: Amanda Cabral, CRC/MG Ativo",
        "local_sec_h2": "Expertise fiscal para o maior parque industrial de Santa Catarina",
        "services_h2_override": "Serviços contábeis para empresas de Joinville",
        "depo1_role": "S&#243;cio",
        "depo1_setor": "Metal-mecânica",
        "depo2_role": "Propriet&#225;ria",
        "depo2_setor": "Fabricante de plásticos",
        "depo3_role": "Empres&#225;rio",
        "depo3_setor": "Prestadora de serviços industriais",
        "context_local": """<p>Joinville concentra o maior parque industrial de Santa Catarina, ancorado pela Tupy, referência mundial em fundidos de ferro e alumínio para autopeças, pela Tigre em conexões plásticas, pela Embraco em compressores herméticos e pela Whirlpool em refrigeração doméstica. A presença de empresas desse porte transforma a cidade em polo de fornecedores especializados em usinagem, tratamento superficial e controle dimensional que atendem exigências técnicas equivalentes às de montadoras europeias e norte-americanas.</p>
<p>Fundições e usinadores que fornecem para a cadeia automotiva global precisam atender requisitos de rastreabilidade de lotes que cruzam com a escrituração fiscal: cada peça tem código de produto, peso e composição que determinam a alíquota de ICMS-SC aplicável na saída e a base de cálculo do ICMS em caso de exportação indireta via trading company. Fabricantes de compressores herméticos e refrigeradores que exportam para a União Europeia precisam comprovar a origem brasileira de cada componente para aproveitar os benefícios de isenção fiscal previstos nos acordos comerciais bilaterais, e essa comprovação passa pela escrituração correta do conteúdo regional na nota fiscal de exportação. O porto de São Francisco do Sul, principal ponto de embarque do polo Norte Catarinense, opera sob regras alfandegárias específicas para carga frigorificada e equipamentos em fase de testes que geram obrigações acessórias distintas das exportações convencionais.</p>
<p>A prática de três décadas com indústrias de alta complexidade técnica consolidou uma metodologia para mapear passivos fiscais silenciosos e direitos tributários não aproveitados com base na escrituração real da empresa.</p>
<p>Novos clientes de Joinville recebem uma avaliação tributária gratuita por videoconferência. O trabalho cobre o regime de tributação em vigor, a revisão dos últimos cinco anos de apuração e os pontos de vulnerabilidade fiscal identificados nos registros contábeis da empresa.</p>""",
    },

    # 22 — Campinas SP
    {
        "cidade": "Campinas",
        "uf": "SP",
        "cidade_uf": "campinas-sp",
        "cidade_slug": "contador-em-campinas",
        "canonical_url": "https://amcabralblindagem.com.br/campinas-sp/contador-em-campinas/",
        "wiki_url": "https://pt.wikipedia.org/wiki/Campinas",
        "wikidata_id": "Q193699",
        "geo_lat": "-22.9099",
        "geo_lng": "-47.0626",
        "gentilicio": "campineiros",
        "regiao": "interior de São Paulo",
        "foto": "campinas-vista-panoramica.jpg",
        "alt_foto": "Vista aérea de Campinas, SP",
        "caption_foto": "Campinas, polo de tecnologia e agronegócio do interior paulista",
        "case_1_setor": "Tecnologia da informação",
        "case_2_setor": "Agronegócio e biotecnologia",
        "case_3_setor": "Indústria de alta tecnologia",
        "vizinhas_texto": """<p>Além de Campinas, atendemos empresas em Americana, Sumaré, Hortolândia, Valinhos, Vinhedo, Paulínia e Jaguariúna. <a href="/cidades-atendidas/">Ver todas as cidades atendidas</a>.</p>""",
        "vizinhas_links": """<div class="coverage-nearby-links">
  <a href="/cidades-atendidas/">Americana</a>
  <a href="/cidades-atendidas/">Sumaré</a>
  <a href="/cidades-atendidas/">Hortolândia</a>
  <a href="/cidades-atendidas/">Valinhos</a>
  <a href="/cidades-atendidas/">Vinhedo</a>
  <a href="/cidades-atendidas/">Paulínia</a>
  <a href="/cidades-atendidas/">Jaguariúna</a>
</div>""",
        "bairros_industrial": """<ul class="bairros-list">
  <li>Distrito Industrial</li>
  <li>CIATEC I</li>
  <li>CIATEC II</li>
  <li>Parque Taquaral</li>
  <li>São Bernardo</li>
</ul>""",
        "bairros_comercial": """<ul class="bairros-list">
  <li>Centro</li>
  <li>Cambuí</li>
  <li>Bosque</li>
  <li>Cambui</li>
  <li>Nova Campinas</li>
</ul>""",
        "bairros_residencial": """<ul class="bairros-list">
  <li>Taquaral</li>
  <li>Jardim Guanabara</li>
  <li>Barão Geraldo</li>
  <li>Sousas</li>
  <li>Jardim Chapadão</li>
</ul>""",
        "authority_h2": "Contabilidade em Campinas com expertise em tecnologia e inovação",
        "amanda_cta_h2": "Contadora em Campinas: Amanda Cabral, CRC/MG Ativo",
        "local_sec_h2": "Planejamento tributário para o polo tech e agro de Campinas",
        "services_h2_override": "Serviços contábeis para empresas de Campinas",
        "depo1_role": "S&#243;cio",
        "depo1_setor": "Empresa de tecnologia",
        "depo2_role": "Propriet&#225;ria",
        "depo2_setor": "Startup de biotecnologia",
        "depo3_role": "Empres&#225;rio",
        "depo3_setor": "Indústria de alta tecnologia",
        "context_local": """<p>Campinas abriga o maior volume de patentes depositadas no INPI por empresas do interior paulista, reflexo de um ecossistema científico formado pela Unicamp, pela EMBRAPA e pelo CPqD que gerou spin-offs de semicondutores, sistemas embarcados e soluções de agri-tech ao longo de quatro décadas. O eixo petroquímico de Paulínia, com a refinaria da Petrobras e unidades da Dow e da Basf, conecta esse ambiente de inovação a uma cadeia de fornecimento de insumos industriais com escala de exportação.</p>
<p>Spin-offs universitários que captam recursos da FINEP por chamada de subvenção econômica precisam separar a verba de custeio da verba de capital no plano de contas: custeio transita pelo resultado e compõe a base de IRPJ e CSLL, capital é controlado no ativo imobilizado e tem depreciação fiscal diferente da contábil, distinção que a Receita Federal verifica no cruzamento entre a ECF e os relatórios de prestação de contas enviados à agência de fomento. Refinaria e fornecedoras de insumos petroquímicos de Paulínia escrituram o ICMS-SP com benefícios de diferimento concedidos por regime especial: cada remessa de nafta ou petroquímico básico para o polo de ABC tem CFOP e alíquota específicos que mudam conforme o tipo de destinatário, e a aplicação do código errado gera estorno de crédito que aparece somente na auditoria eletrônica da Sefaz. Distribuidoras de insumos agropecuários do eixo Campinas-Americana que revendem para produtores rurais de outros estados apuram o ICMS com substituição tributária e precisam acompanhar a pauta de valores de base de cálculo publicada por cada estado de destino, porque a pauta varia por mês e a nota com base defasada gera auto de diferença de cálculo no estado receptor.</p>
<p>Trinta anos de trabalho com contribuintes de perfil heterogêneo geraram uma base técnica para mapear o tributo pago além do necessário com precisão operacional.</p>
<p>Para novos clientes de Campinas, a triagem fiscal inicial é gratuita e ocorre por videoconferência. O escopo abrange o enquadramento atual, os créditos acumulados nos últimos sessenta meses e as falhas de escrituração detectadas nos arquivos digitais da empresa.</p>""",
    },
]


# ---------------------------------------------------------------------------
# BUILD FUNCTION
# ---------------------------------------------------------------------------

def build_city(city, template_html, build_scripts_dir):
    cidade = city["cidade"]
    print(f"\n{'='*60}")
    print(f"  Gerando: {cidade} {city['uf']}")
    print(f"{'='*60}")

    # Jaccard check
    ok = check_jaccard(city["context_local"], cidade)
    if not ok:
        print(f"  ERRO: Jaccard falhou para {cidade}. Abortando esta cidade.")
        return False

    html = template_html

    # Simple replacements
    replacements = {
        '{{CIDADE}}':            cidade,
        '{{UF}}':                city["uf"],
        '{{CIDADE_UF}}':         city["cidade_uf"],
        '{{CIDADE_SLUG}}':       city["cidade_slug"],
        '{{CANONICAL_URL}}':     city["canonical_url"],
        '{{WIKI_CIDADE_URL}}':   city["wiki_url"],
        '{{WIKIDATA_CIDADE_ID}}': city["wikidata_id"],
        '{{GEO_LAT}}':           city["geo_lat"],
        '{{GEO_LNG}}':           city["geo_lng"],
        '{{MAPS_QUERY}}':        'https://www.google.com/maps/search/Rua+Major+Fidelis+244+Para+de+Minas+MG',
        '{{MAPS_EMBED_URL}}':    'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3762.4!2d-44.4139!3d-19.8681!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zMTnCsDUyJzA1LjIiUyA0NMKwMjQnNTAuMCJX!5e0!3m2!1spt!2sbr!4v1620000000000!5m2!1spt!2sbr',
        '{{GENTILICIO}}':        city["gentilicio"],
        '{{REGIAO}}':            city["regiao"],
        '{{FOTO_CIDADE}}':       city["foto"],
        '{{ALT_FOTO_CIDADE}}':   city["alt_foto"],
        '{{CAPTION_FOTO_CIDADE}}': city["caption_foto"],
        '{{CONTEXT_LOCAL}}':     city["context_local"],
        '{{CIDADES_VIZINHAS}}':  city["vizinhas_texto"],
        '{{COVERAGE_NEARBY_LINKS}}': city["vizinhas_links"],
        '{{BAIRROS_INDUSTRIAL}}': city["bairros_industrial"],
        '{{BAIRROS_COMERCIAL}}':  city["bairros_comercial"],
        '{{BAIRROS_RESIDENCIAL}}': city["bairros_residencial"],
        '{{CASE_1_SETOR}}':      city["case_1_setor"],
        '{{CASE_2_SETOR}}':      city["case_2_setor"],
        '{{CASE_3_SETOR}}':      city["case_3_setor"],
    }

    for key, val in replacements.items():
        html = html.replace(key, val)

    # Fix mega-menu hardcoded link
    html = html.replace(
        '<a href="/contabilidade-para-de-minas/" class="hdr-mega-link">',
        f'<a href="/{city["cidade_uf"]}/{city["cidade_slug"]}/" class="hdr-mega-link">'
    )

    # Fix authority H2
    html = html.replace(
        f'Contabilidade em {cidade} com quem conhece a cidade',
        city["authority_h2"]
    )

    # Fix amanda-cta H2
    html = html.replace(
        f'<h2 class="amanda-cta-h">Contadora tributária em {cidade}: Amanda Cabral de Oliveira, CRC/MG Ativo</h2>',
        f'<h2 class="amanda-cta-h">{city["amanda_cta_h2"]}</h2>'
    )

    # Fix services H2
    html = html.replace(
        f'Serviços contábeis para empresas {city["gentilicio"]}',
        city["services_h2_override"]
    )

    # Fix local-sec H2
    html = html.replace(
        f'Contador em {cidade} com 30 anos de presença na cidade',
        city["local_sec_h2"]
    )

    # Fix Wikidata Q975225 placeholder (template default)
    html = html.replace(
        '"https://www.wikidata.org/wiki/Q975225"',
        f'"https://www.wikidata.org/wiki/{city["wikidata_id"]}"'
    )

    # Fix testimonial roles
    html = html.replace(
        f'S&#243;cio</span> — Comércio atacadista, {cidade}/{city["uf"]}',
        f'{city["depo1_role"]}</span> — {city["depo1_setor"]}, {cidade}/{city["uf"]}'
    )
    html = html.replace(
        f'Propriet&#225;ria</span> — Clínica odontológica, {cidade}/{city["uf"]}',
        f'{city["depo2_role"]}</span> — {city["depo2_setor"]}, {cidade}/{city["uf"]}'
    )
    html = html.replace(
        f'Empres&#225;rio</span> — Comércio, {cidade}/{city["uf"]}',
        f'{city["depo3_role"]}</span> — {city["depo3_setor"]}, {cidade}/{city["uf"]}'
    )

    # Verifications
    prev_cities = ['Pará de Minas', 'para-de-minas', 'Sete Lagoas', 'sete-lagoas', 'Montes Claros', 'montes-claros']
    has_prev = [c for c in prev_cities if c in html]
    if has_prev:
        print(f"  AVISO: Referências a cidades anteriores encontradas: {has_prev}")
    else:
        print(f"  OK: 0 referências a cidades anteriores.")

    remaining = re.findall(r'\{\{[A-Z_]+\}\}', html)
    if remaining:
        print(f"  AVISO: Placeholders não substituídos: {set(remaining)}")
    else:
        print(f"  OK: Todos os placeholders substituídos.")

    # Create output directory
    out_dir = f'{city["cidade_uf"]}/{city["cidade_slug"]}'
    os.makedirs(out_dir, exist_ok=True)

    out_path = f'{out_dir}/index.html'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"  Arquivo gerado: {out_path}")

    # Add to corpus
    CORPUS[cidade] = city["context_local"]

    return True


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    with open('template-lp-cidade.html', 'r', encoding='utf-8') as f:
        template = f.read()

    success_count = 0
    failed = []

    for city in CITIES:
        ok = build_city(city, template, '.')
        if ok:
            success_count += 1
        else:
            failed.append(city["cidade"])

    print(f"\n{'='*60}")
    print(f"  RESULTADO FINAL: {success_count}/{len(CITIES)} cidades geradas")
    if failed:
        print(f"  FALHAS: {failed}")
    else:
        print(f"  Todas as cidades geradas com sucesso.")
    print(f"{'='*60}")
