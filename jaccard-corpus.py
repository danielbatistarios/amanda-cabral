#!/usr/bin/env python3
# jaccard-corpus.py
# Corpus de CONTEXT_LOCAL aprovados — usado para validar Jaccard de novas cidades.
# Regra: nova cidade precisa ter Jaccard < 0.20 contra TODOS os textos abaixo.
# Adicionar novo entry aqui após cada LP aprovada.

import re

def tokenize(text):
    text = re.sub(r'<[^>]+>', ' ', text)
    text = text.lower()
    return set(re.findall(r'[a-záàâãéêíóôõúüç]+', text))

def jaccard(a, b):
    sa, sb = tokenize(a), tokenize(b)
    return len(sa & sb) / len(sa | sb)

def check(candidate_text, candidate_name="Nova cidade"):
    results = []
    ok = True
    for name, text in CORPUS.items():
        j = jaccard(candidate_text, text)
        status = "OK" if j < 0.20 else "FALHOU"
        if j >= 0.20:
            ok = False
        results.append((name, j, status))
    print(f"\n=== Jaccard: {candidate_name} ===")
    for name, j, status in sorted(results, key=lambda x: -x[1]):
        print(f"  vs {name:<25} {j:.3f}  {status}")
    print(f"  Resultado geral: {'OK — pode publicar' if ok else 'FALHOU — reescrever'}")
    return ok

# ---------------------------------------------------------------------------
# CORPUS APROVADO
# ---------------------------------------------------------------------------

CORPUS = {}

CORPUS["Pará de Minas"] = """<p>Pará de Minas construiu sua economia sobre dois pilares complementares: a indústria de transformação e um comércio varejista que serve toda a região Oeste de Minas. O polo industrial concentra metalurgia, laticínios, indústria química e têxtil — setores que respondem por mais de 40% do PIB municipal. O comércio, por sua vez, atrai consumidores de dezenas de municípios vizinhos, tornando a cidade referência regional em serviços.</p>
<p>Para o empresário local, esse perfil gera desafios tributários específicos. Metalúrgicas acumulam créditos de IPI sobre insumos que raramente são aproveitados. Laticínios operam com substituição tributária de ICMS que, se mal gerida, resulta em pagamento duplo. Empresas de comércio varejista perdem competitividade quando o regime tributário não é calibrado para o seu faturamento real.</p>
<p>A AC Contabilidade nasceu em Pará de Minas em 1996 e cresceu junto com o tecido empresarial da cidade. Três décadas acompanhando comércio, serviços e indústrias locais traduzem-se em capacidade de identificar, com precisão, onde cada tipo de empresa paga tributo além do necessário — e como recuperar esse valor dentro da legalidade.</p>
<p>O escritório fica na Rua Major Fidélis, 244, no Centro de Pará de Minas. O atendimento pode ser presencial ou por videoconferência para empresas de outras cidades. Para novos clientes, o diagnóstico tributário gratuito é o ponto de partida.</p>"""

CORPUS["Sete Lagoas"] = """<p>Sete Lagoas construiu sua identidade econômica sobre o ferro. O Distrito Industrial, inaugurado em 1974, reuniu fundições, siderúrgicas e metalúrgicas que transformaram a cidade no maior polo siderúrgico do interior mineiro. Empresas como a Iveco, que fabrica veículos pesados no município, e grandes marcas do setor de alimentos como Ambev e Itambé instalaram operações que elevaram a cidade à 12ª maior economia de Minas Gerais.</p>
<p>Para o empresário sete-lagoano, esse perfil industrial gera um desafio tributário específico. Fundições e metalúrgicas acumulam créditos de ICMS e IPI sobre insumos e materiais intermediários que, na maior parte dos casos, nunca são aproveitados. Distribuidoras de alimentos operam com margens apertadas e perdem competitividade quando o regime tributário não é calibrado corretamente. A AC Contabilidade existe para fechar essa lacuna.</p>
<p>Atendemos Sete Lagoas desde 1996. Ao longo de três décadas, acompanhamos o crescimento do polo industrial, as mudanças no regime do ICMS em MG e a chegada de novos setores, como o farmacêutico. Esse histórico permite identificar, com precisão, onde cada tipo de empresa da região acumula tributo pago a mais, e como recuperar esse valor dentro da legalidade.</p>
<p>O escritório fica a menos de uma hora de Sete Lagoas pela BR-040, a 72 km de BH. O atendimento pode ser presencial ou por videoconferência. Para empresas do Distrito Industrial, do eixo comercial do Eldorado ou dos bairros do Centro e São João, o diagnóstico tributário gratuito é o ponto de partida.</p>"""

CORPUS["Montes Claros"] = """<p>Montes Claros chegou ao século XXI como o centro econômico do Norte de Minas — 5ª maior cidade do estado, com PIB de R$ 10,8 bilhões e uma estrutura produtiva que poucos municípios do interior brasileiro conseguem igualar. Nestlé, Novo Nordisk, Eurofarma, Coteminas e MSD transformaram o município na capital nacional de medicamentos e no maior produtor de leite condensado do mundo. Esse perfil atrai investimento, gera volume fiscal e exige contabilidade à altura da complexidade.</p>
<p>Farmacêuticas brasileiras e multinacionais têm regimes de PIS/COFINS com alíquotas não cumulativas que geram direitos a ressarcimento raramente explorados pelos escritórios contábeis convencionais. Fabricantes de laticínios e alimentos processados convivem com ICMS-ST calculado sobre pautas fiscais que mudam por decreto e que, quando mal monitoradas, resultam em recolhimento acima do valor real devido. A AC Contabilidade foi construída para tratar essas variáveis, não para ignorá-las.</p>
<p>A AC Contabilidade está no Norte de Minas desde 1996. Nesse tempo, vimos a ZFM farmacêutica ganhar corpo, o ICMS-ST ser reformulado e o setor de serviços superar a indústria em participação no PIB local. Acumular esse tipo de vivência setorial significa reconhecer padrões que escritórios recentes simplesmente não enxergam.</p>
<p>O formato de reunião se adapta à rotina do cliente. Quem está em Montes Claros pode optar pela chamada de vídeo, eliminando horas de deslocamento. Quem prefere o encontro presencial tem o escritório de Pará de Minas como referência. O ponto de entrada é sempre o mesmo: um levantamento completo e gratuito que mapeia tributação vigente, créditos não utilizados nos últimos cinco anos e situação patrimonial do sócio.</p>"""

if __name__ == "__main__":
    # Quando chamado diretamente, re-valida o corpus interno (deve ser tudo < 0.20 entre si)
    cities = list(CORPUS.keys())
    print("=== Validação cruzada do corpus ===")
    all_ok = True
    for i in range(len(cities)):
        for j in range(i+1, len(cities)):
            score = jaccard(CORPUS[cities[i]], CORPUS[cities[j]])
            status = "OK" if score < 0.20 else "FALHOU"
            if score >= 0.20:
                all_ok = False
            print(f"  {cities[i]:<20} vs {cities[j]:<20} {score:.3f}  {status}")
    print(f"\n  Corpus: {'consistente' if all_ok else 'INCONSISTENTE — revisar'}")
