#!/usr/bin/env python3
"""
Script para reescrever LOCAL CONTEXT de cidades com dados econômicos reais.
Processa: lê HTML, valida Jaccard, substitui conteúdo, atualiza corpus.
"""

import re
import os
from pathlib import Path

def tokenize(text):
    text = re.sub(r'<[^>]+>', ' ', text)
    text = text.lower()
    return set(re.findall(r'[a-záàâãéêíóôõúüç]+', text))

def jaccard(a, b):
    sa, sb = tokenize(a), tokenize(b)
    if len(sa | sb) == 0:
        return 1.0
    return len(sa & sb) / len(sa | sb)

# Corpus aprovado (extraído do jaccard-corpus.py)
CORPUS = {
    "Pará de Minas": """<p>Pará de Minas construiu sua economia sobre dois pilares complementares: a indústria de transformação e um comércio varejista que serve toda a região Oeste de Minas.</p>""",
    "Sete Lagoas": """<p>Sete Lagoas construiu sua identidade econômica sobre o ferro. O Distrito Industrial, inaugurado em 1974.</p>""",
    "Montes Claros": """<p>Montes Claros chegou ao século XXI como o centro econômico do Norte de Minas.</p>""",
    "Uberaba": """<p>Uberaba é a capital genética do mundo: o município exporta embriões e sêmen de zebuínos.</p>""",
    "Uberlândia": """<p>Uberlândia funciona como o nó central de redistribuição logística do Brasil Central.</p>""",
    "Poços de Caldas": """<p>Poços de Caldas reúne, no mesmo perímetro urbano, um parque industrial com cerâmica técnica.</p>""",
    "Betim": """<p>Betim abriga a maior fábrica da Stellantis na América Latina.</p>""",
    "Curitiba": """<p>Curitiba consolidou sua posição como o principal polo de tecnologia e inovação do Sul do Brasil.</p>""",
    "Sorocaba": """<p>Sorocaba estruturou seu parque produtivo ao longo da ferrovia.</p>""",
    "Guarulhos": """<p>Guarulhos concentra um volume fiscal proporcional ao Aeroporto Internacional de Cumbica.</p>""",
    "Manaus": """<p>Manaus opera sob normas tributárias sem equivalente no restante do Brasil.</p>""",
    "Osasco": """<p>Osasco consolidou-se como o maior polo de serviços financeiros do Brasil fora de São Paulo capital.</p>""",
    "Caxias do Sul": """<p>Caxias do Sul é o maior polo metal-mecânico do Sul do Brasil.</p>""",
    "Fortaleza": """<p>Fortaleza lidera a produção calçadista do Nordeste brasileiro.</p>""",
    "Goiânia": """<p>Goiânia se posiciona como o maior centro de saúde privada do Centro-Oeste brasileiro.</p>""",
    "João Pessoa": """<p>João Pessoa detém o litoral mais próximo da Europa entre todas as capitais brasileiras.</p>""",
    "Ribeirão Preto": """<p>Ribeirão Preto centraliza a economia do agronegócio paulista.</p>""",
    "Salvador": """<p>Salvador combina dois vetores produtivos de peso nacional: o Complexo Petroquímico de Camaçari.</p>""",
    "Blumenau": """<p>Blumenau divide o espaço urbano entre o maior parque têxtil da Região Sul.</p>""",
    "Feira de Santana": """<p>Feira de Santana funciona como o principal nó de redistribuição comercial do Nordeste baiano.</p>""",
    "Piracicaba": """<p>Piracicaba ocupa uma posição singular no interior paulista.</p>""",
    "Recife": """<p>Recife reúne dois vetores econômicos de escala nacional que raramente coexistem.</p>""",
    "Rio de Janeiro": """<p>O Rio de Janeiro é o único estado brasileiro onde royalties de petróleo compõem parcela significativa.</p>""",
    "Joinville": """<p>Joinville concentra o maior parque industrial de Santa Catarina.</p>""",
    "Campinas": """<p>Campinas abriga o maior volume de patentes depositadas no INPI.</p>""",
}

cities_config = [
    {
        "name": "Betim",
        "path": "/Users/jrios/amanda-cabral-contadora/betim-mg/contador-em-betim/index.html",
        "h2": "Planejamento tributário para indústrias automotivas e petroquímicas em Minas Gerais",
        "data": {
            "p1": "Betim abriga a maior fábrica da Stellantis na América Latina, segundo maior PIB industrial do estado. O Polo Petroquímico de Minas e a cadeia de fornecedores automotivos com centenas de empresas especializadas transformaram a cidade em centro de fabricação de autopeças, sistemas de transmissão e logística de alta complexidade tributária.",
            "p2": "Fornecedores da indústria automotiva operam com drawback, crédito presumido de IPI e regimes especiais de ICMS que exigem domínio profundo da legislação mineira. Empresas do polo petroquímico precisam acompanhar variações de NCM e pauta fiscal do ICMS-ST em matérias-primas que mudam de classificação por ato normativo. Quando esses controles falham, crédito acumula sem gerar benefício de caixa.",
            "p3": "A AC Contabilidade acumulou trinta anos de vivência com os regimes tributários específicos da indústria mineira. Essa bagagem se traduz em capacidade de mapear, em auditoria retroativa de cinco anos, os créditos não aproveitados e quantificar o retorno concreto antes de formalizar qualquer proposta.",
            "p4": "O formato de atendimento se adapta à rotina industrial: videoconferência em qualquer horário ou visita presencial ao escritório de Pará de Minas. Para novos clientes em Betim, a avaliação tributária inicial não tem custo e não exige compromisso de contratação.",
        }
    },
    {
        "name": "Blumenau",
        "path": "/Users/jrios/amanda-cabral-contadora/blumenau-sc/contador-em-blumenau/index.html",
        "h2": "Contabilidade tributária para têxtil de moda e tecnologia em Santa Catarina",
        "data": {
            "p1": "Blumenau reúne o maior parque têxtil da Região Sul e um polo tecnológico com mais de 500 empresas de software, automação industrial e cibersegurança que faturaram bilhões em 2023. A convivência entre teares jacquard de confecção e servidores em nuvem cria obrigações fiscais com lógicas completamente distintas num mesmo município.",
            "p2": "Fábricas de confecção do Vale do Itajaí que adotam regime cumulativo de PIS e COFINS pagam alíquotas menores sobre receita mas abrem mão de crédito sobre insumos. Marcas de moda que licenciam estampas para confeccionistas de outros estados precisam classificar o pagamento como royalty ou serviço, escolha que impacta alíquota efetiva. Empresas de software com contratos de licença recorrente enfrentam controvérsia sobre ISS em operações interestaduais.",
            "p3": "Trinta anos de prática com indústrias de transformação e prestadores de serviços consolidaram uma metodologia para mapear o excedente tributário por atividade antes de propor ajuste de enquadramento.",
            "p4": "Novos clientes de Blumenau recebem avaliação fiscal gratuita por videoconferência. O diagnóstico abrange o regime de tributação em vigor, os direitos creditórios dos últimos cinco exercícios e os pontos de inconsistência identificados na escrituração da empresa.",
        }
    },
]

def validate_against_corpus(text, city_name):
    """Valida se texto passa no gate Jaccard < 0.20 contra todos do corpus."""
    results = []
    all_ok = True
    for name, corp_text in CORPUS.items():
        j = jaccard(text, corp_text)
        status = "OK" if j < 0.20 else "FALHOU"
        if j >= 0.20:
            all_ok = False
        results.append((name, j, status))

    print(f"\n=== Jaccard: {city_name} ===")
    for name, j, status in sorted(results, key=lambda x: -x[1])[:5]:  # Top 5
        print(f"  vs {name:<20} {j:.3f}  {status}")

    if all_ok:
        print(f"  Resultado: OK — pode publicar")
    else:
        print(f"  Resultado: FALHOU — revisar texto")
    return all_ok

def main():
    print("Sistema de atualização de LOCAL CONTEXT por cidade")
    print("=" * 60)

    # Exemplo: processar Betim
    config = cities_config[0]  # Betim
    city_name = config["name"]

    print(f"\nProcessando: {city_name}")

    # Validar Jaccard
    combined_text = " ".join([config["data"]["p1"], config["data"]["p2"], config["data"]["p3"], config["data"]["p4"]])
    valid = validate_against_corpus(combined_text, city_name)

    if valid:
        print(f"  Status: PRONTO para aplicar no HTML")
    else:
        print(f"  Status: REESCREVER antes de aplicar")

if __name__ == "__main__":
    main()
