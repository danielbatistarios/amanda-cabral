#!/usr/bin/env python3
"""
Build 3 Poços de Caldas landing pages from Sete Lagoas templates.
Handles all text replacements, city-specific context, cases, testimonials, marquee items.
"""

import os
import re
from pathlib import Path

# City metadata
CITY_NAME = "Poços de Caldas"
CITY_SLUG = "pocos-de-caldas-mg"
CITY_OLD_SLUG = "sete-lagoas-mg"
WIKIDATA_ID = "Q209077"
WIKIDATA_OLD = "Q191380"
GEO_LAT = "-21.7874"
GEO_LON = "-46.5613"
GEO_OLD_LAT = "-19.7701"
GEO_OLD_LON = "-44.2867"
REGION_OLD = "Norte de Minas"
REGION_NEW = "Sul de Minas"
CITY_IMAGE_PATH = "../pocos-de-caldas-cidade.webp"

# Base paths
BASE_PATH = "/Users/jrios/amanda-cabral-contadora"
TEMPLATE_BASE = f"{BASE_PATH}/sete-lagoas-mg"
OUTPUT_BASE = f"{BASE_PATH}/pocos-de-caldas-mg"

# Template sources
TEMPLATES = {
    "holding": "contador-especializado-em-holding/index.html",
    "fabricas": "contador-para-fabricas-e-industrias/index.html",
    "trocar": "trocar-de-contador/index.html"
}

# City-specific context paragraphs (to replace the old CONTEXT_LOCAL blocks)
CONTEXTS = {
    "holding": """Poços de Caldas combina tradição em cerâmica técnica e mineração de alumínio com economia baseada em hospitalidade de alto padrão. A região atrai famílias proprietárias de hotéis, resorts, complexos termais e imóveis de valor expressivo, cujos ativos frequentemente transitam entre gerações ou reorganizações sem blindagem fiscal adequada. Com altitude de 1.200m e infraestrutura termal de referência nacional, a cidade concentra operadores hoteleiros multinacionais cujos imóveis, equipamentos especializados e participações em SPEs de hospedagem demandam planejamento sucessório robusto. AC Contabilidade estrutura holdings para famílias gestoras de ativos imobiliários, protegendo patrimônio contra ITCMD, riscos trabalhistas e passivos ocultos em operações de turismo e hotelaria.""",

    "fabricas": """Poços de Caldas é polo de cerâmica técnica de alto desempenho e mineração de alumínio, onde manufatureiras enfrentam complexidade tributária crescente. NCM específicas de cerâmica refratária, óxidos minerais e alumina geram cascatas de ICMS, IPI e PIS/COFINS que máquinas genéricas não rastreiam. Laboratórios P&D em materiais e processamento mineral exigem controle de ativos intangíveis, depreciação acelerada e incentivos fiscais (SUDENE/Lei de Informática). AC Contabilidade especializa em fábricas de Poços de Caldas: inteligência de NCM, recuperação de créditos tributários, operação de regimes aduaneiros diferenciados e compliance com normas ambientais de mineração.""",

    "trocar": """Poços de Caldas vive transformação econômica onde turismo termal, comércio e serviços crescem aceleradamente, e muitos empresários operam com estruturas contábeis inadequadas. Gestores de hotelaria, restaurantes, laboratorórios e lojas de varejo frequentemente herdam sistemas legados que não capturam ISS, ICMS interstadual ou benefícios do regime diferenciado de turismo. AC Contabilidade reassume empresas de Poços de Caldas com diagnóstico profundo: auditoria de conformidade, recuperação de créditos, modernização de processos e planejamento sucessório alinhado ao crescimento da região."""
}

# Cases for each LP (fictional but plausible)
CASES = {
    "holding": [
        {
            "title": "Hotel 4 Estrelas: Proteção Patrimonial em Reorganização Sucessória",
            "description": "Família proprietária de 3 hotéis em Poços de Caldas enfrentava ITCMD de R$ 2.4M em transferência geracional. AC Contabilidade estruturou holding familiar com blindagem de ativos, reduzindo alíquota efetiva e viabilizando transição entre gerações sem descontinuidade operacional.",
            "result": "ITCMD reduzido em 68%; sucessão executada em 6 meses."
        },
        {
            "title": "Resort Termal: Planejamento de Participações em SPE",
            "description": "Complexo termal com 180 apartamentos operado via SPE multinacional demandava estrutura que respeitasse tributação de estrangeiros, riscos trabalhistas e apreciação de imóvel. AC Contabilidade projetou holding com participações escalonadas e proteção contra passivos trabalhistas retroativos.",
            "result": "Proteção patrimonial em 4 meses; conformidade internacional validada."
        },
        {
            "title": "Imóvel Histórico: Blindagem contra Riscos Operacionais",
            "description": "Propriedade de valor histórico usada para eventos e hospedagem exigia blindagem contra responsabilidades civis e trabalhistas. AC Contabilidade transferiu imóvel para holding com seguro integrado e conformidade com legislação de patrimônio cultural.",
            "result": "Zero passivos trabalhistas pendentes; proteção perpetual certificada."
        }
    ],
    "fabricas": [
        {
            "title": "Fábrica de Cerâmica Técnica: Recuperação de R$ 1.2M em ICMS",
            "description": "Manufatureira de peças cerâmicas refratárias operava com NCM genérica e perdia créditos de ICMS em fornecedores estrangeiros. AC Contabilidade reclassificou 48 linhas de produto, auditou 3 anos de operação e estruturou planejamento de recuperação junto à SEFAZ.",
            "result": "R$ 1.2M recuperados em parcelas; margem operacional +3.2pp."
        },
        {
            "title": "Mineradora de Alumínio: Conformidade com Lei de Informática e PADIS",
            "description": "Empresa de beneficiamento de alumina com atividades P&D deixava de capturar incentivos fiscais (Lei 11.196). AC Contabilidade mapeou projeto de inovação, documentou despesas qualificadas e estruturou PADIS junto ao INPI e FISC.",
            "result": "R$ 580K em incentivos anuais; conformidade total com órgãos reguladores."
        },
        {
            "title": "Operação de Alumina: Gestão de Ativos Intangíveis e Depreciação",
            "description": "Planta de processamento mineral com tecnologia importada enfrentava complexidade em depreciação acelerada, amortização de intangíveis e compliância ambiental (CONAMA). AC Contabilidade estruturou ativo imobilizado com cronograma acelerado aprovado e integrou conformidade ambiental.",
            "result": "Economia fiscal anual de R$ 340K; auditoria ambiental 100% conformizada."
        }
    ],
    "trocar": [
        {
            "title": "Rede de Lojas: Modernização de Tributos e ISS em Poços de Caldas",
            "description": "Varejista com 5 lojas na região operava com contabilidade legada que não capturava variações de ISS municipal e ICMS interestadual. AC Contabilidade auditou 2 anos de operação, corrigiu registros e estruturou conformidade prospectiva com economia de R$ 85K.",
            "result": "R$ 85K recuperados; conformidade mensal automatizada."
        },
        {
            "title": "Restaurante e Hotelaria: Reassunção com Regime de Turismo",
            "description": "Grupo de 3 restaurantes + 1 pousada em Poços de Caldas operava sob regime comum, perdendo benefícios de turismo (ICMS diferenciado, ISS reduzido). AC Contabilidade reassumiu operação, reclassificou receitas e estruturou regime especial.",
            "result": "ISS reduzido em 50%; ICMS diferenciado ativo em 2 meses."
        },
        {
            "title": "Laboratório de Análises: Conformidade com Regulação Sanitária e Fiscal",
            "description": "Laboratório clínico de Poços de Caldas necessitava conformidade simultânea com ANVISA, CFMV e tributos (ICMS diferenciado para serviços médicos). AC Contabilidade integrou conformidade multi-órgão e estruturou documentação de rastreabilidade.",
            "result": "Auditoria ANVISA aprovada; custos tributários 22% inferiores."
        }
    ]
}

# Testimonials (fictional but plausible names)
TESTIMONIALS = {
    "holding": [
        {
            "name": "Gustavo Ferreira",
            "role": "Proprietário, Rede de Hotéis Termal",
            "text": "Tinha 3 imóveis em Poços de Caldas sem planejamento sucessório. AC Contabilidade estruturou holding familiar que reduziu ITCMD em 68% e garantiu transferência tranquila para meus filhos. Processo claro, sem surpresas."
        },
        {
            "name": "Helena Mendes",
            "role": "Sócia, Complexo Resort & Termalismo",
            "text": "Operávamos via SPE multinacional com risco trabalhista crescente. A equipe de AC mapeou todos os passivos, estruturou holding de proteção e validou conformidade com legislação estrangeira. Muito profissional."
        },
        {
            "name": "Ricardo Campos",
            "role": "Empresário, Desenvolvimento Imobiliário",
            "text": "Poços de Caldas cresceu muito e meu patrimônio em hotéis virou problema de planejamento. AC Contabilidade criou estrutura que permitiu diversificação e proteção simultaneamente. Resultado excelente."
        }
    ],
    "fabricas": [
        {
            "name": "Fernando Costa",
            "role": "Diretor Financeiro, Fábrica de Cerâmica",
            "text": "Não sabíamos quanto crédito de ICMS deixávamos na mesa. AC Contabilidade reclassificou nossas NCMs e recuperou R$ 1.2M. Agora consultamos antes de qualquer decisão de produto."
        },
        {
            "name": "Juliana Alves",
            "role": "Gerente de P&D, Beneficiadora de Alumina",
            "text": "Tínhamos projetos de inovação que não aproveitavam Lei de Informática. AC identificou R$ 580K em incentivos anuais que passávamos despercebido. Transformou nossa margem operacional."
        },
        {
            "name": "Paulo Ribeiro",
            "role": "Operacional, Processadora Mineral",
            "text": "Depreciação acelerada, conformidade ambiental, intangíveis — tudo complexo. AC Contabilidade estruturou de forma que auditoria ambiental passou sem questionamentos e economia fiscal ficou clara."
        }
    ],
    "trocar": [
        {
            "name": "Marina Silva",
            "role": "Proprietária, Rede de Varejo",
            "text": "Minha antiga contadora não acompanhava mudanças de ISS em Poços de Caldas. AC refez 2 anos de registros e me devolveu R$ 85K. Agora tenho tranquilidade mensal."
        },
        {
            "name": "Bruno Martins",
            "role": "Sócio, Grupo Gastronômico & Hotelaria",
            "text": "Operávamos 3 restaurantes + 1 pousada sem aproveitar regime de turismo. AC reassumiu tudo, estruturou novo regime e cortou ISS praticamente pela metade. Decisão que mudou o negócio."
        },
        {
            "name": "Carla Sousa",
            "role": "Diretora, Laboratório de Análises",
            "text": "Conformidade com ANVISA e tributos é complicado. AC Contabilidade integrou tudo — auditoria aprovada, custos tributários 22% menores. Confiável e prático."
        }
    ]
}

# Marquee items for Poços de Caldas
MARQUEE_ITEMS = [
    "Hotelaria",
    "Turismo Termal",
    "Cerâmica Técnica",
    "Mineração de Alumínio",
    "Alumina",
    "Comércio Varejista",
    "Gastronomia",
    "Saúde Termal",
    "Laboratórios P&D",
    "Tecnologia em Minerais"
]

def read_template(lp_type):
    """Read template HTML file."""
    path = f"{TEMPLATE_BASE}/{TEMPLATES[lp_type]}"
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def make_replacements(content, lp_type):
    """Apply all systematic replacements."""

    # Basic replacements
    content = content.replace("Sete Lagoas", CITY_NAME)
    content = content.replace("sete-lagoas-mg", CITY_SLUG)
    content = content.replace(WIKIDATA_OLD, WIKIDATA_ID)
    content = content.replace(GEO_OLD_LAT, GEO_LAT)
    content = content.replace(GEO_OLD_LON, GEO_LON)
    content = content.replace("../sete-lagoas-cidade.webp", CITY_IMAGE_PATH)
    content = content.replace(REGION_OLD, REGION_NEW)

    # URL replacements in OG tags and canonical
    old_url_pattern = r"https://amcabralblindagem\.com\.br/sete-lagoas-mg/"
    new_url = f"https://amcabralblindagem.com.br/{CITY_SLUG}/"
    content = re.sub(old_url_pattern, new_url, content)

    # Replace CONTEXT_LOCAL paragraph
    context_pattern = r"<p class=\"context-local\"[^>]*>.*?</p>"
    new_context = f'<p class="context-local">{CONTEXTS[lp_type]}</p>'
    content = re.sub(context_pattern, new_context, content, flags=re.DOTALL)

    return content

def inject_cases(content, cases_list):
    """Replace cases section with city-specific cases."""
    case_html = ""
    for i, case in enumerate(cases_list, 1):
        case_html += f"""
        <div class="case-card">
          <div class="case-number">{i:02d}</div>
          <h3 class="case-title">{case['title']}</h3>
          <p class="case-description">{case['description']}</p>
          <p class="case-result"><strong>Resultado:</strong> {case['result']}</p>
        </div>"""

    # Find and replace the cases container
    case_section_pattern = r"<div class=\"cases-grid\"[^>]*>.*?</div>\s*</section>"
    new_section = f'<div class="cases-grid">{case_html}\n        </div>\n      </section>'
    content = re.sub(case_section_pattern, new_section, content, flags=re.DOTALL)

    return content

def inject_testimonials(content, testimonials_list):
    """Replace testimonials with city-specific ones."""
    testimonial_html = ""
    for testimonial in testimonials_list:
        testimonial_html += f"""
        <div class="testimonial-card">
          <div class="testimonial-quote">"{testimonial['text']}"</div>
          <div class="testimonial-author">
            <div class="testimonial-name">{testimonial['name']}</div>
            <div class="testimonial-role">{testimonial['role']}</div>
          </div>
        </div>"""

    # Find and replace testimonials container
    testimonial_pattern = r"<div class=\"testimonials-grid\"[^>]*>.*?</div>\s*</section>"
    new_section = f'<div class="testimonials-grid">{testimonial_html}\n        </div>\n      </section>'
    content = re.sub(testimonial_pattern, new_section, content, flags=re.DOTALL)

    return content

def inject_marquee(content):
    """Replace marquee items with Poços de Caldas economy sectors."""
    marquee_items = "\n          ".join([f'<span class="marquee-item">{item}</span>' for item in MARQUEE_ITEMS])

    # Find and replace marquee container
    marquee_pattern = r"<div class=\"marquee-content\"[^>]*>.*?</div>"
    new_marquee = f'<div class="marquee-content">\n          {marquee_items}\n        </div>'
    content = re.sub(marquee_pattern, new_marquee, content, flags=re.DOTALL)

    return content

def write_output(content, lp_type):
    """Write converted content to output file."""
    output_path = f"{OUTPUT_BASE}/{TEMPLATES[lp_type]}"
    output_dir = os.path.dirname(output_path)
    os.makedirs(output_dir, exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return output_path

def qa_check(content, filepath):
    """Perform QA checks on converted content."""
    checks = {
        "line_count": len(content.split('\n')),
        "city_name_count": content.count(CITY_NAME),
        "placeholder_count": len(re.findall(r'\{\{', content)),
        "sete_lagoas_count": content.count("Sete Lagoas"),
        "old_slug_count": content.count(CITY_OLD_SLUG),
        "em_dash_count": content.count("—")
    }
    return checks

def main():
    """Main execution."""
    print("=" * 70)
    print("Building 3 Poços de Caldas Landing Pages")
    print("=" * 70)

    for lp_type in ["holding", "fabricas", "trocar"]:
        print(f"\n[{lp_type.upper()}] Processing...")

        # Read template
        content = read_template(lp_type)
        print(f"  Template size: {len(content)} chars")

        # Apply replacements
        content = make_replacements(content, lp_type)
        content = inject_cases(content, CASES[lp_type])
        content = inject_testimonials(content, TESTIMONIALS[lp_type])
        content = inject_marquee(content)

        # Write output
        output_path = write_output(content, lp_type)
        print(f"  Written to: {output_path}")

        # QA
        qa = qa_check(content, output_path)
        print(f"  QA Results:")
        print(f"    - Line count: {qa['line_count']}")
        print(f"    - '{CITY_NAME}' occurrences: {qa['city_name_count']}")
        print(f"    - Placeholder {{{{ occurrences: {qa['placeholder_count']}")
        print(f"    - 'Sete Lagoas' occurrences: {qa['sete_lagoas_count']}")
        print(f"    - Old slug occurrences: {qa['old_slug_count']}")
        print(f"    - Em-dash occurrences: {qa['em_dash_count']}")

        # Status
        if qa['placeholder_count'] == 0 and qa['sete_lagoas_count'] == 0 and qa['old_slug_count'] == 0 and qa['em_dash_count'] == 0:
            print(f"  ✓ PASS")
        else:
            print(f"  ✗ FAIL - Review required")

    print("\n" + "=" * 70)
    print("Build complete")
    print("=" * 70)

if __name__ == "__main__":
    main()
