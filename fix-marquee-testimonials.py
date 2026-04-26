#!/usr/bin/env python3
"""
Fix marquee items and testimonials in Poços de Caldas LPs.
"""

import re
from pathlib import Path
import html

# Marquee items for each LP type (with HTML entities for accents)
MARQUEE_ITEMS_BY_TYPE = {
    "holding": [
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
    ],
    "fabricas": [
        "Cerâmica Técnica",
        "Mineração de Alumínio",
        "Alumina",
        "Processamento Mineral",
        "Refratários",
        "Óxidos Especiais",
        "P&D Industrial",
        "Conformidade Ambiental",
        "IPI e ICMS",
        "Inteligência Tributária"
    ],
    "trocar": [
        "Hotelaria",
        "Restaurantes",
        "Turismo Termal",
        "Comércio Varejista",
        "Laboratórios",
        "Serviços Profissionais",
        "Gastronomia",
        "Saúde",
        "Educação",
        "Turismo"
    ]
}

# Testimonials
TESTIMONIALS_BY_TYPE = {
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

def encode_marquee_item(text):
    """Encode marquee item with HTML entities."""
    return html.escape(text).replace('á', '&aacute;').replace('é', '&eacute;').replace('í', '&iacute;').replace('ó', '&oacute;').replace('ú', '&uacute;').replace('ã', '&atilde;')

def build_marquee_html(items):
    """Build full marquee HTML with duplicated items."""
    marquee_html = ""
    for item in items:
        encoded = encode_marquee_item(item)
        marquee_html += f'      <span class="marquee-item">{encoded}<span class="sep"></span></span>\n'

    # Duplicate for infinite loop effect
    for item in items:
        encoded = encode_marquee_item(item)
        marquee_html += f'      <span class="marquee-item">{encoded}<span class="sep"></span></span>\n'

    return marquee_html.rstrip()

def build_testimonial_html(testimonials):
    """Build testimonials section HTML."""
    html_out = ""
    for i, test in enumerate(testimonials):
        initial = test['name'].split()[0][0].upper()
        avatar_class = f"avatar-{i+1}"
        html_out += f"""        <div class="dep-card">
          <div class="dep-stars">★★★★★</div>
          <p class="dep-text">"{test['text']}"</p>
          <div class="dep-author">
            <div class="dep-avatar">{initial}</div>
            <div class="dep-info">
              <strong>{test['name']}</strong>
              <span>{test['role']}</span>
            </div>
          </div>
        </div>
"""
    return html_out.rstrip()

def fix_file(filepath, lp_type):
    """Fix marquee and testimonials in a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix marquee
    marquee_items = MARQUEE_ITEMS_BY_TYPE[lp_type]
    new_marquee_html = build_marquee_html(marquee_items)

    # Find marquee section and replace
    marquee_pattern = r'<section class="marquee-section" aria-hidden="true">\s*<div class="marquee-track">.*?</div>\s*</section>'
    new_marquee_section = f'''<section class="marquee-section" aria-hidden="true">
    <div class="marquee-track">
{new_marquee_html}
    </div>
  </section>'''

    content = re.sub(marquee_pattern, new_marquee_section, content, flags=re.DOTALL)

    # Fix testimonials (assuming they exist in a depoimentos section)
    testimonials = TESTIMONIALS_BY_TYPE[lp_type]
    new_testimonial_html = build_testimonial_html(testimonials)

    # Find depoimentos grid and replace
    testimonial_pattern = r'<div class="dep-grid">.*?</div>\s*</div>\s*</section>\s*<!-- PROCESSO'
    new_testimonial_section = f'''<div class="dep-grid">
{new_testimonial_html}
        </div>
      </div>
    </section>

  <!-- PROCESSO'''

    content = re.sub(testimonial_pattern, new_testimonial_section, content, flags=re.DOTALL)

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return True

def main():
    base_path = "/Users/jrios/amanda-cabral-contadora/pocos-de-caldas-mg"

    files_to_fix = {
        "holding": f"{base_path}/contador-especializado-em-holding/index.html",
        "fabricas": f"{base_path}/contador-para-fabricas-e-industrias/index.html",
        "trocar": f"{base_path}/trocar-de-contador/index.html"
    }

    print("Fixing marquee and testimonials...")
    print("=" * 80)

    for lp_type, filepath in files_to_fix.items():
        try:
            fix_file(filepath, lp_type)
            print(f"✓ {lp_type}: Fixed marquee and testimonials")
        except Exception as e:
            print(f"✗ {lp_type}: Error - {e}")

    print("=" * 80)
    print("Done")

if __name__ == "__main__":
    main()
