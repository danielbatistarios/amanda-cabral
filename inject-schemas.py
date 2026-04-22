#!/usr/bin/env python3
"""
Injeta schema JSON-LD em todas as páginas de serviço da Amanda Cabral.
Execução: python3 inject-schemas.py
"""

import json
import re
import os

BASE_URL = "https://amcabralblindagem.com.br"
ORG_ID   = f"{BASE_URL}/#organization"
SITE_ID  = f"{BASE_URL}/#website"

OG_IMAGE = f"{BASE_URL}/assets/og-image.webp"

PAGES = [
    {
        "file": "planejamento-tributario.html",
        "slug": "planejamento-tributario",
        "name": "Planejamento Tributário — Estratégia Completa para Pagar Menos Imposto",
        "service_name": "Planejamento Tributário",
        "service_type": "Planejamento Tributário",
        "service_wikidata": "https://www.wikidata.org/wiki/Q232156",
        "description": "Planejamento tributário especializado para empresas em MG. Análise do regime tributário ideal, aproveitamento de incentivos fiscais e adequação à reforma tributária 2026.",
        "breadcrumb": [
            {"position": 1, "name": "Início", "item": BASE_URL + "/"},
            {"position": 2, "name": "Planejamento Tributário", "item": BASE_URL + "/planejamento-tributario/"}
        ],
        "faqs": [
            ("O que é planejamento tributário?",
             "Planejamento tributário é o processo de análise e estruturação fiscal da empresa para reduzir legalmente a carga tributária, escolhendo o regime ideal e aproveitando todos os incentivos disponíveis."),
            ("Qual o regime tributário ideal para empresas?",
             "Depende do faturamento, margem de lucro e tipo de atividade. Simples Nacional, Lucro Presumido e Lucro Real têm vantagens distintas. A AM Cabral analisa o cenário completo antes de recomendar."),
            ("Quais incentivos fiscais existem em MG para empresas?",
             "Minas Gerais oferece incentivos de ICMS para diversos segmentos industriais e comerciais. A AM Cabral mapeia todos os benefícios aplicáveis ao perfil da sua empresa."),
            ("Como a reforma tributária afeta minha empresa?",
             "A reforma tributária unifica PIS, COFINS, IPI, ICMS e ISS em novos tributos (CBS, IBS e IS). A transição ocorre entre 2026 e 2033. Planejamento antecipado garante menor impacto."),
        ]
    },
    {
        "file": "recuperacao-creditos-tributarios.html",
        "slug": "recuperacao-creditos-tributarios",
        "name": "Recuperação de Créditos Tributários — R$ 12M Já Recuperados",
        "service_name": "Recuperação de Créditos Tributários",
        "service_type": "Recuperação de Créditos Fiscais",
        "service_wikidata": None,
        "description": "Auditoria retroativa de até 5 anos para recuperar créditos de ICMS, IPI e PIS/COFINS não aproveitados. Média de R$ 180 mil por cliente. Processo 100% administrativo.",
        "breadcrumb": [
            {"position": 1, "name": "Início", "item": BASE_URL + "/"},
            {"position": 2, "name": "Recuperação de Créditos", "item": BASE_URL + "/recuperacao-creditos-tributarios/"}
        ],
        "faqs": [
            ("Como funciona a recuperação de créditos tributários?",
             "A AM Cabral realiza auditoria retroativa de até 5 anos nos registros fiscais da empresa, identificando créditos de ICMS, IPI e PIS/COFINS pagos a mais ou não aproveitados, e solicita a compensação junto à Receita Federal ou SEFAZ."),
            ("Quais tributos podem ser recuperados?",
             "ICMS, IPI, PIS, COFINS, IRPJ e CSLL pago indevidamente ou a maior. Também créditos de ICMS na entrada de mercadorias e insumos utilizados na produção."),
            ("Minha empresa provavelmente tem créditos perdidos?",
             "8 em cada 10 empresas têm créditos não aproveitados. Quanto maior o volume de compras e operações, maior a probabilidade. O diagnóstico gratuito da AM Cabral identifica o potencial exato."),
            ("A recuperação é judicial ou administrativa?",
             "Prioritariamente administrativa, via pedido de compensação ou restituição junto à Receita Federal e SEFAZ. Mais rápido, sem custas judiciais e com menor risco."),
        ]
    },
    {
        "file": "consultoria-tributaria.html",
        "slug": "consultoria-tributaria",
        "name": "Consultoria Tributária e Compliance Fiscal para Empresas",
        "service_name": "Consultoria Tributária e Compliance Fiscal",
        "service_type": "Consultoria Tributária",
        "service_wikidata": "https://www.wikidata.org/wiki/Q12913062",
        "description": "Consultoria tributária especializada e gestão de compliance fiscal para empresas em MG. Obrigações acessórias, adequação à reforma tributária e segurança fiscal.",
        "breadcrumb": [
            {"position": 1, "name": "Início", "item": BASE_URL + "/"},
            {"position": 2, "name": "Consultoria Tributária", "item": BASE_URL + "/consultoria-tributaria/"}
        ],
        "faqs": [
            ("O que é consultoria tributária e compliance fiscal?",
             "Consultoria tributária é o acompanhamento especializado das decisões fiscais da empresa. Compliance fiscal garante que todas as obrigações tributárias sejam cumpridas corretamente, evitando autuações e multas."),
            ("Quais obrigações acessórias a AM Cabral gerencia?",
             "SPED Fiscal, SPED Contábil, ECF, EFD-Reinf, EFD-Contribuições, DCTF, DIRF, RAIS, e todas as obrigações estaduais (GIA-MG, DAPI). A AM Cabral cuida do calendário fiscal completo."),
            ("A AM Cabral ajuda na preparação para a reforma tributária?",
             "Sim. A reforma tributária altera profundamente o sistema fiscal brasileiro a partir de 2026. A AM Cabral mapeia os impactos para cada empresa e prepara a transição com planejamento antecipado."),
            ("Quanto custa a consultoria tributária?",
             "O custo varia conforme o porte da empresa e a complexidade das operações. A AM Cabral oferece diagnóstico gratuito para estimar o investimento e o retorno esperado."),
        ]
    },
    {
        "file": "gestao-contabil-industrial.html",
        "slug": "gestao-contabil-industrial",
        "name": "Gestão Contábil Estratégica para Empresas — Inteligência de Gestão",
        "service_name": "Gestão Contábil Estratégica",
        "service_type": "Gestão Contábil",
        "service_wikidata": "https://www.wikidata.org/wiki/Q318193",
        "description": "Gestão contábil estratégica para empresas em MG. Relatórios gerenciais, dashboard financeiro, departamento pessoal e acompanhamento mensal com foco em resultado.",
        "breadcrumb": [
            {"position": 1, "name": "Início", "item": BASE_URL + "/"},
            {"position": 2, "name": "Gestão Contábil", "item": BASE_URL + "/gestao-contabil-industrial/"}
        ],
        "faqs": [
            ("O que é gestão contábil estratégica para empresas?",
             "É a contabilidade além do registro: relatórios gerenciais que orientam decisões, análise de margem, fluxo de caixa e indicadores de desempenho integrados à gestão do negócio."),
            ("Qual a diferença entre contabilidade operacional e estratégica?",
             "Contabilidade operacional registra o que aconteceu. Contabilidade estratégica transforma esses dados em inteligência para decisões de preço, investimento e crescimento."),
            ("A AM Cabral cuida do departamento pessoal e folha de pagamento?",
             "Sim. A AM Cabral gerencia folha de pagamento, admissões, demissões, férias, 13º salário e todas as obrigações trabalhistas, com segurança jurídica e agilidade."),
            ("Como funciona o relatório gerencial da AM Cabral?",
             "Mensalmente, a empresa recebe um dashboard com DRE, fluxo de caixa, indicadores tributários e alertas de oportunidade. Reunião de análise inclusa para clientes no plano estratégico."),
        ]
    },
    {
        "file": "holding-patrimonial.html",
        "slug": "holding-patrimonial",
        "name": "Constituição de Holding Patrimonial e Familiar — Proteja Seu Patrimônio",
        "service_name": "Holding Patrimonial e Familiar",
        "service_type": "Planejamento Patrimonial",
        "service_wikidata": None,
        "description": "Estruturação de holdings patrimoniais e familiares em MG. Proteção de bens, redução de impostos sobre aluguéis, planejamento sucessório sem inventário judicial.",
        "breadcrumb": [
            {"position": 1, "name": "Início", "item": BASE_URL + "/"},
            {"position": 2, "name": "Holding Patrimonial", "item": BASE_URL + "/holding-patrimonial/"}
        ],
        "faqs": [
            ("O que é holding patrimonial?",
             "Holding patrimonial é uma empresa criada exclusivamente para administrar bens — imóveis, investimentos, participações societárias. Os bens saem do CPF do dono e passam para o CNPJ da holding, reduzindo impostos e protegendo o patrimônio."),
            ("Holding é só para quem é rico?",
             "Não. Qualquer pessoa física com imóveis, aluguéis ou bens que queira reduzir impostos (de 27,5% para ~8,4% sobre aluguéis) e simplificar a sucessão pode se beneficiar de uma holding."),
            ("Qual a diferença entre holding e testamento?",
             "O testamento é um documento de vontade que passa pelo inventário judicial, podendo durar anos. A holding transfere o patrimônio via contrato social, sem inventário, de forma mais rápida e barata."),
            ("Quanto custa constituir uma holding?",
             "O custo envolve honorários do contador, do advogado e eventuais taxas cartoriais. A AM Cabral faz a análise de viabilidade gratuita para verificar se a economia tributária justifica o investimento."),
        ]
    },
]

# Schema extra para faq.html — FAQPage standalone
FAQ_PAGE = {
    "file": "faq.html",
    "slug": "faq",
    "name": "Perguntas Frequentes — Amanda Cabral Contadora",
    "description": "Dúvidas frequentes sobre contabilidade, planejamento tributário e recuperação de créditos para empresas em Minas Gerais.",
    "breadcrumb": [
        {"position": 1, "name": "Início", "item": BASE_URL + "/"},
        {"position": 2, "name": "Perguntas Frequentes", "item": BASE_URL + "/faq/"}
    ],
}

# Schema para bio.html / author.html — Person
PERSON_PAGES = ["author.html", "bio.html"]


def build_service_schema(p):
    page_id = f"{BASE_URL}/{p['slug']}/#webpage"
    breadcrumb_id = f"{BASE_URL}/{p['slug']}/#breadcrumb"
    service_id = f"{BASE_URL}/{p['slug']}/#service"

    service_node = {
        "@type": "Service",
        "@id": service_id,
        "name": p["service_name"],
        "serviceType": p["service_type"],
        "provider": {"@id": ORG_ID},
        "url": f"{BASE_URL}/{p['slug']}/",
        "description": p["description"],
        "areaServed": [
            {"@type": "City", "name": "Para de Minas", "sameAs": "https://www.wikidata.org/wiki/Q2913906"},
            {"@type": "City", "name": "Belo Horizonte", "sameAs": "https://www.wikidata.org/wiki/Q601"},
            {"@type": "State", "name": "Minas Gerais", "sameAs": "https://www.wikidata.org/wiki/Q1061"}
        ],
        "availableLanguage": {"@language": "pt-BR"},
    }
    if p.get("service_wikidata"):
        service_node["sameAs"] = p["service_wikidata"]

    webpage_node = {
        "@type": "WebPage",
        "@id": page_id,
        "url": f"{BASE_URL}/{p['slug']}/",
        "name": p["name"],
        "description": p["description"],
        "isPartOf": {"@id": SITE_ID},
        "publisher": {"@id": ORG_ID},
        "breadcrumb": {"@id": breadcrumb_id},
        "mainEntity": {"@id": service_id},
        "inLanguage": "pt-BR",
    }

    breadcrumb_node = {
        "@type": "BreadcrumbList",
        "@id": breadcrumb_id,
        "itemListElement": [
            {"@type": "ListItem", "position": item["position"], "name": item["name"], "item": item["item"]}
            for item in p["breadcrumb"]
        ]
    }

    faq_node = {
        "@type": "FAQPage",
        "@id": f"{BASE_URL}/{p['slug']}/#faqpage",
        "about": {"@id": service_id},
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a}
            }
            for q, a in p["faqs"]
        ]
    }

    return {
        "@context": "https://schema.org",
        "@graph": [service_node, webpage_node, breadcrumb_node, faq_node]
    }


def build_faq_page_schema():
    page_id = f"{BASE_URL}/faq/#webpage"
    breadcrumb_id = f"{BASE_URL}/faq/#breadcrumb"
    return {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebPage",
                "@id": page_id,
                "url": f"{BASE_URL}/faq/",
                "name": FAQ_PAGE["name"],
                "description": FAQ_PAGE["description"],
                "isPartOf": {"@id": SITE_ID},
                "publisher": {"@id": ORG_ID},
                "breadcrumb": {"@id": breadcrumb_id},
                "inLanguage": "pt-BR",
            },
            {
                "@type": "BreadcrumbList",
                "@id": breadcrumb_id,
                "itemListElement": [
                    {"@type": "ListItem", "position": item["position"], "name": item["name"], "item": item["item"]}
                    for item in FAQ_PAGE["breadcrumb"]
                ]
            }
        ]
    }


def build_person_schema(file):
    slug = "sobre" if "author" in file or "bio" in file else file.replace(".html", "")
    page_id = f"{BASE_URL}/{slug}/#webpage"
    breadcrumb_id = f"{BASE_URL}/{slug}/#breadcrumb"
    person_id = f"{BASE_URL}/#person-amanda-silva"
    return {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebPage",
                "@id": page_id,
                "url": f"{BASE_URL}/{slug}/",
                "name": "Amanda Cabral de Oliveira — Contadora Especialista em Tributação",
                "description": "Conheça Amanda Cabral de Oliveira, contadora especialista em tributação empresarial, sócia da AC Contabilidade e Consultoria em Pará de Minas, MG.",
                "isPartOf": {"@id": SITE_ID},
                "publisher": {"@id": ORG_ID},
                "mainEntity": {"@id": person_id},
                "breadcrumb": {"@id": breadcrumb_id},
                "inLanguage": "pt-BR",
            },
            {
                "@type": "BreadcrumbList",
                "@id": breadcrumb_id,
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Início", "item": BASE_URL + "/"},
                    {"@type": "ListItem", "position": 2, "name": "Sobre Amanda", "item": f"{BASE_URL}/{slug}/"}
                ]
            }
        ]
    }


OG_META = f"""    <meta property="og:image" content="{OG_IMAGE}">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">"""


def inject_schema(filepath, schema_dict):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    schema_tag = f'\n    <!-- Schema Markup — JSON-LD @graph -->\n    <script type="application/ld+json">\n    {json.dumps(schema_dict, ensure_ascii=False, indent=2)}\n    </script>'

    # Remover schema antigo se existir
    content = re.sub(
        r'\s*<!-- Schema[^>]*-->.*?<script type="application/ld\+json">.*?</script>',
        '', content, flags=re.DOTALL
    )

    # Adicionar og:image se não existir
    if 'og:image' not in content:
        content = content.replace(
            '<link rel="preconnect" href="https://fonts.googleapis.com">',
            OG_META + '\n    <link rel="preconnect" href="https://fonts.googleapis.com">'
        )

    # Inserir schema antes de </head>
    content = content.replace('</head>', schema_tag + '\n</head>')

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ {os.path.basename(filepath)}")


base = '/Users/jrios/amanda-cabral-contadora/'

# Páginas de serviço
for p in PAGES:
    schema = build_service_schema(p)
    inject_schema(base + p["file"], schema)

# FAQ standalone
inject_schema(base + "faq.html", build_faq_page_schema())

# Páginas de pessoa
for f in PERSON_PAGES:
    inject_schema(base + f, build_person_schema(f))

print("\n✅ Todos os schemas injetados com sucesso!")
print(f"Total: {len(PAGES) + 1 + len(PERSON_PAGES)} páginas atualizadas")
