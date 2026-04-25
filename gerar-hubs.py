#!/usr/bin/env python3
"""Gera hub de cidade a partir do template Sete Lagoas."""
import os, re, json

BASE = "/Users/jrios/amanda-cabral-contadora"
TEMPLATE = os.path.join(BASE, "sete-lagoas-mg/index.html")

with open(TEMPLATE, encoding="utf-8") as f:
    TPL = f.read()

CITIES = [
  {
    "slug": "betim-mg",
    "name": "Betim",
    "name_ac": "Betim",
    "state": "MG",
    "uf": "mg",
    "preposition": "em",
    "foto_file": "betim-cidade.jpg",
    "foto_alt": "Centro de Betim/MG",
    "foto_figcaption": "Betim, polo petroquímico e automotivo de Minas Gerais.",
    "loader_phrase": "Cada empresa em Betim tem um perfil tributário único",
    "title": "Serviços Contábeis em Betim | AM Cabral Contabilidade",
    "meta_desc": "Escritório de contabilidade em Betim/MG. Polo petroquímico, automotivo e industrial: cada setor exige tributação especializada. Planejamento tributário, holding e recuperação de créditos.",
    "og_desc": "Contabilidade especializada por setor em Betim/MG. Petroquímica, automotivo, comércio e indústria. Diagnóstico tributário gratuito.",
    "canonical": "https://amcabralblindagem.com.br/betim-mg/",
    "breadcrumb_name": "Betim",
    "hero_h1": 'Serviços Contábeis em <span style="color:var(--dourado)">Betim</span>: cada empresa tem um perfil tributário diferente',
    "hero_sub": 'Polo petroquímico, automotivo e industrial: cada setor de <a href="https://pt.wikipedia.org/wiki/Betim" target="_blank" rel="noopener" class="wiki-link">Betim</a> tem tributos próprios que o contador genérico ignora. A AM Cabral entrega contabilidade feita para o seu setor. Diagnóstico tributário gratuito.',
    "wiki_url": "https://pt.wikipedia.org/wiki/Betim",
    "marquee_city": "Betim, MG",
    "marquee_destaque": "Polo Petroquímico Betim",
    "authority_h2": 'Contabilidade especializada por setor para empresas de <a href="https://pt.wikipedia.org/wiki/Betim" target="_blank" rel="noopener" class="wiki-link">Betim</a>',
    "authority_p1": "Betim não é uma cidade com um único perfil empresarial. É um dos maiores polos petroquímicos do Brasil, com a Refinaria Gabriel Passos (Regap) e toda a cadeia de fornecedores. É um polo automotivo com montadoras e sistemistas. É um centro comercial e industrial diversificado.",
    "authority_p2": "Cada um desses setores tem uma estrutura tributária diferente. <strong>Petroquímica e refinamento operam com créditos de ICMS e IPI sobre insumos industriais.</strong> Automotivo tem ICMS-ST em toda a cadeia de peças. Comércio varejista tem oportunidades de migração de regime que reduzem carga em até 8 pontos percentuais. Construtoras acessam RET com IRPJ de 1%.",
    "authority_p3": "Um contador genérico não conhece essas especificidades. <strong>A AM Cabral foi constituída justamente para empresas que precisam de mais do que declaração em dia.</strong> Atendemos Betim remotamente com a mesma profundidade dos nossos clientes presenciais em Pará de Minas.",
    "stats4": "4 setores com especialização",
    "card1_title": "Contabilidade em Betim",
    "card1_desc": "Contabilidade completa para empresas de Betim: DRE, fluxo de caixa, departamento pessoal e obrigações acessórias. Atendimento remoto com profundidade de quem conhece o polo petroquímico e automotivo.",
    "card2_title": "Contador Especializado em Holding em Betim",
    "card2_desc": "Para empresários de Betim que construíram patrimônio ao longo dos anos. A holding separa pessoa física da jurídica, reduz imposto sobre aluguel de 27,5% para 8,4% e organiza a sucessão familiar.",
    "card3_title": "Contador para Fábricas &amp; Indústrias em Betim",
    "card3_desc": "Petroquímica, automotivo e indústrias diversas de Betim têm estruturas tributárias distintas. Créditos de ICMS-ST, IPI sobre insumos e SPED Industrial precisam de especialista, não de um genérico.",
    "card4_title": "Trocar de Contador em Betim",
    "card4_desc": "Trocar de contador parece complicado, mas não precisa ser. A AM Cabral faz toda a migração: busca de documentos, transferência de obrigações e diagnóstico de pendências sem interrupção da sua contabilidade.",
    "card3_bullets": ["ICMS-ST, IPI e PIS/COFINS por atividade industrial", "Créditos extemporâneos de 5 anos", "Preparação para reforma tributária 2026"],
    "amanda_h2": "Contadora tributária para empresas de Betim: Amanda Cabral de Oliveira, CRC/MG Ativo",
    "amanda_quote": '"Betim tem setores com tributação completamente distinta. Petroquímica, automotivo, comércio e construção civil não podem compartilhar o mesmo contador genérico. Cada setor exige especialização diferente, e é exatamente isso que entregamos."',
    "setores": ["Petroquímica e Refinamento", "Polo Automotivo", "Indústria Diversificada", "Comércio Varejista", "Construtoras e Incorporadoras", "Serviços Profissionais", "Holding Patrimonial", "MEI em Crescimento"],
    "cases": [
      {"pill": "Recuperação de Créditos", "title": "Fornecedor do polo automotivo em MG", "stat": "R$ 240 mil", "label": "recuperados em créditos", "detail": "ICMS-ST sobre peças e componentes não aproveitados pelo contador anterior. Auditoria retroativa de 5 anos. Processo via compensação, sem litígio."},
      {"pill": "Planejamento Tributário", "title": "Prestadora de serviços industriais em Betim", "stat": "R$ 120 mil/ano", "label": "de economia tributária", "detail": "Migração do Simples Nacional para o Lucro Presumido. Regime de estimativa corrigido para o perfil da empresa. Redução imediata na carga efetiva."},
      {"pill": "Holding Patrimonial", "title": "Empresário do setor comercial em Betim", "stat": "R$ 85 mil/ano", "label": "de redução no IRPF", "detail": "Constituição de holding familiar. Tributação de aluguel reduzida de 27,5% para 8,4%. Sucessão organizada sem inventário."},
    ],
    "depo": [
      {"quote": "\"A Amanda identificou R$ 240 mil em crédito de ICMS-ST que meu contador anterior nunca tinha mencionado. O processo foi completamente legal e a Amanda conduziu tudo sem precisar da minha intervenção no dia a dia.\"", "role": "Sócio", "empresa": "Fornecedor automotivo, Betim/MG"},
      {"quote": "\"A migração do Simples para o Lucro Presumido foi a decisão certa. A Amanda fez o diagnóstico gratuito, mostrou o número exato antes de eu decidir, e a economia de R$ 120 mil anuais já pagou o investimento várias vezes.\"", "role": "Diretor", "empresa": "Prestadora industrial, Betim/MG"},
      {"quote": "\"A holding resolveu dois problemas de uma vez: reduziu meu imposto de renda sobre os aluguéis e organizou a herança para os meus filhos. A Amanda cuidou de todo o processo.\"", "role": "Proprietário", "empresa": "Empresário, Betim/MG"},
    ],
    "faq": [
      {"q": "Como funciona a contabilidade para indústrias petroquímicas em Betim?", "a": "Indústrias petroquímicas e fornecedores da cadeia em Betim operam com créditos de IPI sobre insumos industriais e ICMS sobre operações intermunicipais. A maioria tem créditos não aproveitados nesses tributos. Fazemos auditoria retroativa de 5 anos e identificamos o que pode ser compensado ou restituído."},
      {"q": "Fornecedores do polo automotivo de Betim têm tributação especial?", "a": "Sim. Fornecedores de peças e componentes automotivos em Betim operam com ICMS-ST em toda a cadeia. Créditos extemporâneos são comuns quando o contador anterior não mapeou corretamente o fluxo de substituição tributária."},
      {"q": "Qual a diferença de contabilidade para comércio, indústria e serviços em Betim?", "a": "Cada setor tem obrigações e oportunidades distintas. Indústrias têm ICMS-ST e IPI. Comércio varejista pode migrar do Simples para o Lucro Presumido. Construtoras têm RET com IRPJ de 1%. A AM Cabral atende todos esses perfis em Betim remotamente."},
      {"q": "Quanto custa o diagnóstico tributário gratuito?", "a": "O diagnóstico é gratuito e dura cerca de 30 minutos por videoconferência. Ao final, você recebe um relatório com créditos que podem ser recuperados, riscos fiscais identificados e oportunidades de redução de carga. Sem compromisso de contratação."},
      {"q": "Posso trocar de contador sem perder documentos ou histórico?", "a": "Sim. A troca de contador não interrompe a operação da empresa. Assumimos a transferência de todos os documentos e dados do contador anterior. Em geral, o processo leva entre 15 e 30 dias. Para Betim, o atendimento é 100% remoto por videoconferência."},
    ],
    "coverage": [
      {"title": "Polo Industrial", "items": ["Regap e cadeia petroquímica", "Polo automotivo Fiat/sistemistas", "Distrito Industrial I e II", "Indústrias do eixo BR-381", "Metalurgia e fundição"]},
      {"title": "Eixo Comercial", "items": ["Centro de Betim", "Contagem/Betim (divisa)", "Av. Amazonas", "Shopping Contagem/Betim", "Nova Betim"]},
      {"title": "Demais Bairros", "items": ["Citrolândia", "PTB", "Jardim das Oliveiras", "Ressaca", "Todo o município"]},
    ],
    "local_intro": 'Betim tem <strong>mais de 25.000 empresas ativas</strong> e um PIB de aproximadamente R$ 30 bilhões, fortemente industrial. A cidade abriga a Refinaria Gabriel Passos (Regap) e é um dos principais polos automotivos do Brasil. Informações sobre abertura de empresas estão disponíveis na <a href="https://www.jucemg.mg.gov.br/" target="_blank" rel="noopener">JUCEMG</a>.',
    "local_p1": "Para indústrias petroquímicas e fornecedores automotivos, a estrutura tributária envolve <strong>ICMS-ST sobre peças e insumos</strong>, créditos de IPI e obrigações do <strong>SPED Industrial</strong>. Para comércio varejista, a migração entre Simples Nacional e Lucro Presumido pode representar até 8 pontos de diferença na carga efetiva.",
    "local_p2": "Construtoras e incorporadoras de Betim acessam o <strong>RET</strong> com IRPJ de 1% sobre receitas da incorporação. MEIs que prestam serviços para o polo industrial precisam de CNAE correto e enquadramento adequado. A AM Cabral atua com todos esses perfis por atendimento 100% remoto.",
    "local_toggle_text": "Ver mais sobre a economia de Betim",
    "location_h2": "Escritório em Pará de Minas. <em>Atendimento remoto em Betim.</em>",
    "location_atend": "Atendemos empresas de Betim 100% por videoconferência e plataforma digital. Sem necessidade de deslocamento para o cliente.",
    "footer_atend": "100% remoto por videoconferência<br>Segunda a sexta, 8h às 18h",
  },
  {
    "slug": "montes-claros-mg",
    "name": "Montes Claros",
    "name_ac": "Montes Claros",
    "state": "MG",
    "uf": "mg",
    "preposition": "em",
    "foto_file": "montes-claros-cidade.jpg",
    "foto_alt": "Centro de Montes Claros/MG",
    "foto_figcaption": "Montes Claros, maior cidade do Norte de Minas e polo regional.",
    "loader_phrase": "Norte de Minas merece contabilidade que conhece o Norte de Minas",
    "title": "Serviços Contábeis em Montes Claros | AM Cabral Contabilidade",
    "meta_desc": "Escritório de contabilidade em Montes Claros/MG. Polo têxtil, agroindustrial e comercial do Norte de Minas: contabilidade por setor. Planejamento tributário e holding.",
    "og_desc": "Contabilidade especializada para empresas de Montes Claros/MG. Têxtil, agroindustrial, comércio e serviços. Diagnóstico tributário gratuito.",
    "canonical": "https://amcabralblindagem.com.br/montes-claros-mg/",
    "breadcrumb_name": "Montes Claros",
    "hero_h1": 'Serviços Contábeis em <span style="color:var(--dourado)">Montes Claros</span>: Norte de Minas tem tributação própria',
    "hero_sub": 'Polo têxtil, agroindustrial e maior cidade do Norte de Minas: cada setor de <a href="https://pt.wikipedia.org/wiki/Montes_Claros" target="_blank" rel="noopener" class="wiki-link">Montes Claros</a> tem tributos específicos que o contador genérico ignora. A AM Cabral entrega contabilidade feita para o seu setor. Diagnóstico tributário gratuito.',
    "wiki_url": "https://pt.wikipedia.org/wiki/Montes_Claros",
    "marquee_city": "Montes Claros, MG",
    "marquee_destaque": "Norte de Minas Gerais",
    "authority_h2": 'Contabilidade especializada por setor para empresas de <a href="https://pt.wikipedia.org/wiki/Montes_Claros" target="_blank" rel="noopener" class="wiki-link">Montes Claros</a>',
    "authority_p1": "Montes Claros é a maior cidade do Norte de Minas e polo regional de serviços, comércio e indústria. Abriga um dos maiores polos têxteis do estado, além de agroindústria, frigoríficos e distribuição atacadista para toda a região.",
    "authority_p2": "Cada setor tem uma estrutura tributária diferente. <strong>Têxtil e confecções operam com ICMS-ST sobre fios e tecidos e com créditos de IPI.</strong> Agroindústria tem tributação específica sobre produtos do campo e beneficiamento. Comércio atacadista tem regimes próprios de ICMS e oportunidades de migração. Construtoras acessam RET com IRPJ de 1%.",
    "authority_p3": "Um contador genérico não conhece essas especificidades. <strong>A AM Cabral atende Montes Claros remotamente com a mesma profundidade dos nossos clientes presenciais em Pará de Minas.</strong>",
    "stats4": "4 setores com especialização",
    "card1_title": "Contabilidade em Montes Claros",
    "card1_desc": "Contabilidade completa para empresas de Montes Claros: DRE, fluxo de caixa, departamento pessoal e obrigações acessórias. Atendimento remoto com profundidade de quem conhece o polo do Norte de Minas.",
    "card2_title": "Contador Especializado em Holding em Montes Claros",
    "card2_desc": "Para empresários de Montes Claros que construíram patrimônio ao longo dos anos. A holding separa pessoa física da jurídica, reduz imposto sobre aluguel de 27,5% para 8,4% e organiza a sucessão familiar.",
    "card3_title": "Contador para Fábricas &amp; Indústrias em Montes Claros",
    "card3_desc": "Têxtil, agroindústria e indústrias diversas de Montes Claros têm estruturas tributárias distintas. ICMS-ST, IPI sobre insumos e regimes específicos do agro precisam de especialista setorial.",
    "card4_title": "Trocar de Contador em Montes Claros",
    "card4_desc": "Trocar de contador parece complicado, mas não precisa ser. A AM Cabral faz toda a migração: busca de documentos, transferência de obrigações e diagnóstico de pendências sem interrupção da sua contabilidade.",
    "card3_bullets": ["ICMS-ST e IPI para têxtil e agroindústria", "Regimes específicos do agronegócio", "Preparação para reforma tributária 2026"],
    "amanda_h2": "Contadora tributária para empresas de Montes Claros: Amanda Cabral de Oliveira, CRC/MG Ativo",
    "amanda_quote": '"Montes Claros tem setores com tributação completamente distinta. Têxtil, agroindústria, comércio e construção civil não podem compartilhar o mesmo contador genérico. Cada setor exige especialização diferente, e é exatamente isso que entregamos."',
    "setores": ["Têxtil e Confecções", "Agroindústria e Frigoríficos", "Comércio Atacadista", "Comércio Varejista", "Construtoras e Incorporadoras", "Serviços de Saúde", "Holding Patrimonial", "MEI em Crescimento"],
    "cases": [
      {"pill": "Recuperação de Créditos", "title": "Indústria têxtil no Norte de Minas", "stat": "R$ 210 mil", "label": "recuperados em créditos", "detail": "ICMS-ST sobre fios e tecidos não aproveitados pelo contador anterior. Auditoria retroativa de 5 anos. Processo via compensação, sem litígio."},
      {"pill": "Planejamento Tributário", "title": "Distribuidora atacadista em Montes Claros", "stat": "R$ 145 mil/ano", "label": "de economia tributária", "detail": "Migração do Simples Nacional para o Lucro Presumido. Regime de ICMS corrigido para o perfil de distribuição regional. Redução imediata na carga efetiva."},
      {"pill": "Holding Patrimonial", "title": "Empresário do setor de serviços de saúde", "stat": "R$ 90 mil/ano", "label": "de redução no IRPF", "detail": "Constituição de holding familiar. Tributação de aluguel reduzida de 27,5% para 8,4%. Sucessão organizada sem necessidade de inventário."},
    ],
    "depo": [
      {"quote": "\"A Amanda identificou R$ 210 mil em crédito de ICMS-ST que meu contador anterior nunca tinha mencionado. Trabalho com têxtil há 15 anos e nunca tinha aproveitado esses créditos corretamente.\"", "role": "Sócio", "empresa": "Indústria têxtil, Norte de Minas"},
      {"quote": "\"A migração do Simples para o Lucro Presumido foi a decisão certa para a nossa distribuidora. O diagnóstico da Amanda mostrou o número exato antes de decidir.\"", "role": "Diretor", "empresa": "Distribuidora atacadista, Montes Claros"},
      {"quote": "\"A holding organizou meu patrimônio e reduziu o imposto sobre os aluguéis. A Amanda cuida de tudo remotamente e nunca precisei ir até Pará de Minas.\"", "role": "Proprietário", "empresa": "Empresário, Montes Claros/MG"},
    ],
    "faq": [
      {"q": "Como funciona a contabilidade para indústrias têxteis em Montes Claros?", "a": "Têxtil e confecções operam com ICMS-ST sobre fios e tecidos e com créditos de IPI sobre insumos industriais. Muitas indústrias em Montes Claros têm créditos não aproveitados. Fazemos auditoria retroativa de 5 anos e identificamos o que pode ser compensado ou restituído."},
      {"q": "Empresas do agronegócio de Montes Claros têm regime tributário especial?", "a": "Sim. Agroindústria, frigoríficos e beneficiamento de produtos do campo têm tributação específica: ICMS com alíquotas reduzidas, isenções e créditos extemporâneos. A estrutura varia por produto e destino da mercadoria."},
      {"q": "Qual a diferença de contabilidade para comércio, indústria e serviços em Montes Claros?", "a": "Cada setor tem obrigações e oportunidades distintas. Indústrias têm ICMS-ST e IPI. Comércio atacadista tem regimes específicos de ICMS. Serviços de saúde têm ISSQN próprio. Construtoras acessam RET com IRPJ de 1%. A AM Cabral atende todos em Montes Claros remotamente."},
      {"q": "Quanto custa o diagnóstico tributário gratuito?", "a": "O diagnóstico é gratuito e dura cerca de 30 minutos por videoconferência. Ao final, você recebe um relatório com créditos que podem ser recuperados, riscos fiscais e oportunidades de redução de carga. Sem compromisso."},
      {"q": "Posso trocar de contador sem perder documentos ou histórico?", "a": "Sim. Assumimos a transferência de todos os documentos e dados do contador anterior. O processo leva entre 15 e 30 dias. Para Montes Claros, o atendimento é 100% remoto por videoconferência."},
    ],
    "coverage": [
      {"title": "Polo Industrial", "items": ["Distrito Industrial I e II", "Polo Têxtil e Confecções", "Agroindústria e Frigoríficos", "Distribuidoras regionais", "Indústrias do eixo BR-135"]},
      {"title": "Eixo Comercial", "items": ["Centro (Av. Mestra Zezé)", "Montes Claros Shopping", "Bairro Ibituruna", "Av. Deputado Esteves Rodrigues", "Major Prates"]},
      {"title": "Demais Bairros", "items": ["Morada do Parque", "Santa Cecília", "Jardim Panorâmico", "Vila Oliveira", "Todo o município"]},
    ],
    "local_intro": 'Montes Claros tem <strong>mais de 35.000 empresas ativas</strong> e um PIB de aproximadamente R$ 13 bilhões. É o maior polo regional do Norte de Minas, com destaque para têxtil, agroindústria, comércio atacadista e serviços de saúde. Informações sobre abertura de empresas estão disponíveis na <a href="https://www.jucemg.mg.gov.br/" target="_blank" rel="noopener">JUCEMG</a>.',
    "local_p1": "Para indústrias têxteis e confecções, a estrutura tributária envolve <strong>ICMS-ST sobre fios e tecidos</strong>, créditos de IPI sobre insumos e obrigações do <strong>SPED Industrial</strong>. Para agroindústria, o foco é nos regimes especiais de ICMS e nos créditos extemporâneos do agronegócio.",
    "local_p2": "Comércio atacadista de Montes Claros tem regimes específicos de ICMS para distribuição regional. Construtoras acessam o <strong>RET</strong> com IRPJ de 1%. A AM Cabral atua com todos esses perfis por atendimento 100% remoto, sem necessidade de deslocamento.",
    "local_toggle_text": "Ver mais sobre a economia de Montes Claros",
    "location_h2": "Escritório em Pará de Minas. <em>Atendimento remoto em Montes Claros.</em>",
    "location_atend": "Atendemos empresas de Montes Claros 100% por videoconferência e plataforma digital. Sem necessidade de deslocamento para o cliente.",
    "footer_atend": "100% remoto por videoconferência<br>Segunda a sexta, 8h às 18h",
  },
  {
    "slug": "pocos-de-caldas-mg",
    "name": "Poços de Caldas",
    "name_ac": "Poços de Caldas",
    "state": "MG",
    "uf": "mg",
    "preposition": "em",
    "foto_file": "pocos-de-caldas-cidade.jpg",
    "foto_alt": "Centro de Poços de Caldas/MG",
    "foto_figcaption": "Poços de Caldas, polo turístico e industrial do Sul de Minas.",
    "loader_phrase": "Turismo e indústria em Poços de Caldas exigem contabilidades diferentes",
    "title": "Serviços Contábeis em Poços de Caldas | AM Cabral Contabilidade",
    "meta_desc": "Escritório de contabilidade em Poços de Caldas/MG. Polo turístico, mineração e industrial do Sul de Minas: cada setor exige tributação especializada. Planejamento tributário e holding.",
    "og_desc": "Contabilidade especializada para empresas de Poços de Caldas/MG. Turismo, mineração, indústria e comércio. Diagnóstico tributário gratuito.",
    "canonical": "https://amcabralblindagem.com.br/pocos-de-caldas-mg/",
    "breadcrumb_name": "Poços de Caldas",
    "hero_h1": 'Serviços Contábeis em <span style="color:var(--dourado)">Poços de Caldas</span>: turismo e indústria exigem contabilidades diferentes',
    "hero_sub": 'Polo turístico, mineração e industrial do Sul de Minas: cada setor de <a href="https://pt.wikipedia.org/wiki/Po%C3%A7os_de_Caldas" target="_blank" rel="noopener" class="wiki-link">Poços de Caldas</a> tem tributos específicos que o contador genérico ignora. A AM Cabral entrega contabilidade feita para o seu setor. Diagnóstico tributário gratuito.',
    "wiki_url": "https://pt.wikipedia.org/wiki/Po%C3%A7os_de_Caldas",
    "marquee_city": "Poços de Caldas, MG",
    "marquee_destaque": "Sul de Minas Gerais",
    "authority_h2": 'Contabilidade especializada por setor para empresas de <a href="https://pt.wikipedia.org/wiki/Po%C3%A7os_de_Caldas" target="_blank" rel="noopener" class="wiki-link">Poços de Caldas</a>',
    "authority_p1": "Poços de Caldas tem um perfil econômico diverso: polo turístico com hotéis e serviços, mineração de bauxita e alumínio, indústria química e cerâmica. Cada um desses setores tem tributação completamente diferente.",
    "authority_p2": "<strong>Mineração e beneficiamento de minério têm CFEM, ICMS específico e créditos de IPI.</strong> Turismo e hotelaria têm ISSQN municipal e tributação de serviços distinta. Indústria química opera com regimes especiais de IPI. Comércio varejista tem oportunidades de migração de regime tributário.",
    "authority_p3": "Um contador genérico não conhece essas especificidades. <strong>A AM Cabral atende Poços de Caldas remotamente com a mesma profundidade dos nossos clientes presenciais em Pará de Minas.</strong>",
    "stats4": "4 setores com especialização",
    "card1_title": "Contabilidade em Poços de Caldas",
    "card1_desc": "Contabilidade completa para empresas de Poços de Caldas: DRE, fluxo de caixa, departamento pessoal e obrigações acessórias. Atendimento remoto com profundidade de quem conhece o Sul de Minas.",
    "card2_title": "Contador Especializado em Holding em Poços de Caldas",
    "card2_desc": "Para empresários de Poços de Caldas que construíram patrimônio ao longo dos anos. A holding separa pessoa física da jurídica, reduz imposto sobre aluguel de 27,5% para 8,4% e organiza a sucessão familiar.",
    "card3_title": "Contador para Fábricas &amp; Indústrias em Poços de Caldas",
    "card3_desc": "Mineração, química e cerâmica de Poços de Caldas têm tributação específica que o contador genérico não conhece. CFEM, ICMS sobre minério e créditos de IPI precisam de especialista setorial.",
    "card4_title": "Trocar de Contador em Poços de Caldas",
    "card4_desc": "Trocar de contador parece complicado, mas não precisa ser. A AM Cabral faz toda a migração: busca de documentos, transferência de obrigações e diagnóstico de pendências sem interrupção da sua contabilidade.",
    "card3_bullets": ["CFEM, ICMS e IPI para mineração", "Regimes especiais de indústria química", "Preparação para reforma tributária 2026"],
    "amanda_h2": "Contadora tributária para empresas de Poços de Caldas: Amanda Cabral de Oliveira, CRC/MG Ativo",
    "amanda_quote": '"Poços de Caldas tem setores com tributação completamente distinta. Mineração, turismo, indústria e comércio não podem compartilhar o mesmo contador genérico. Cada setor exige especialização diferente, e é exatamente isso que entregamos."',
    "setores": ["Mineração de Bauxita e Alumínio", "Turismo e Hotelaria", "Indústria Química", "Cerâmica e Porcelana", "Comércio Varejista", "Serviços Profissionais", "Holding Patrimonial", "MEI em Crescimento"],
    "cases": [
      {"pill": "Recuperação de Créditos", "title": "Empresa de mineração no Sul de Minas", "stat": "R$ 195 mil", "label": "recuperados em créditos", "detail": "ICMS sobre saída de minério e créditos de IPI sobre insumos industriais não aproveitados. Auditoria retroativa de 5 anos."},
      {"pill": "Planejamento Tributário", "title": "Hotel e pousada em Poços de Caldas", "stat": "R$ 110 mil/ano", "label": "de economia tributária", "detail": "Regime tributário ajustado para hotelaria. ISS municipal e IRPJ corrigidos para o perfil de faturamento. Redução imediata na carga efetiva."},
      {"pill": "Holding Patrimonial", "title": "Empresário do setor de turismo", "stat": "R$ 78 mil/ano", "label": "de redução no IRPF", "detail": "Constituição de holding familiar com imóveis turísticos. Tributação de aluguel reduzida de 27,5% para 8,4%. Sucessão organizada."},
    ],
    "depo": [
      {"quote": "\"Trabalho com mineração há 20 anos e nunca tinha aproveitado os créditos de ICMS corretamente. A Amanda identificou R$ 195 mil que estavam na mesa.\"", "role": "Sócio", "empresa": "Empresa de mineração, Sul de Minas"},
      {"quote": "\"A Amanda ajustou o regime tributário do nosso hotel e economizamos R$ 110 mil no ano. O processo foi 100% remoto e sem burocracia.\"", "role": "Diretor", "empresa": "Hotelaria, Poços de Caldas"},
      {"quote": "\"A holding organizou meu patrimônio e reduziu o imposto sobre os aluguéis dos imóveis turísticos. Processo simples e transparente.\"", "role": "Proprietário", "empresa": "Empresário turismo, Poços de Caldas"},
    ],
    "faq": [
      {"q": "Como funciona a contabilidade para mineração em Poços de Caldas?", "a": "Mineração e beneficiamento de bauxita e alumínio têm CFEM (royalties), ICMS específico sobre saída de minério e créditos de IPI sobre insumos industriais. A maioria das empresas tem créditos não aproveitados. Auditoria retroativa de 5 anos identifica o que pode ser compensado."},
      {"q": "Empresas de turismo e hotelaria de Poços de Caldas têm tributação especial?", "a": "Sim. Hotelaria e turismo têm ISSQN municipal com alíquotas específicas e ISS retido na fonte em alguns casos. O regime de IRPJ e CSLL pode variar conforme o faturamento e a atividade. O diagnóstico identifica o regime ideal para cada empresa do setor."},
      {"q": "Qual a diferença de contabilidade para mineração, turismo e comércio em Poços de Caldas?", "a": "Cada setor tem obrigações e oportunidades distintas. Mineração tem CFEM e ICMS específico. Turismo e hotelaria têm ISSQN municipal. Comércio varejista pode migrar de regime. A AM Cabral atende todos remotamente."},
      {"q": "Quanto custa o diagnóstico tributário gratuito?", "a": "O diagnóstico é gratuito, dura cerca de 30 minutos por videoconferência e resulta em um relatório com créditos recuperáveis, riscos fiscais e oportunidades de redução. Sem compromisso de contratação."},
      {"q": "Posso trocar de contador sem perder documentos ou histórico?", "a": "Sim. Assumimos a transferência de todos os documentos em até 30 dias. O atendimento para Poços de Caldas é 100% remoto por videoconferência."},
    ],
    "coverage": [
      {"title": "Polo Industrial/Mineração", "items": ["CBA (Companhia Brasileira de Alumínio)", "Indústria química e cerâmica", "Mineradoras da região", "Distrito Industrial", "Fornecedores e sistemistas"]},
      {"title": "Eixo Comercial/Turístico", "items": ["Centro Histórico", "Praça Pedro Sanches", "Thermas Palace e entorno", "Av. João Pinheiro", "Serra de São Domingos"]},
      {"title": "Demais Bairros", "items": ["Jardim São José", "Vila Verde", "Santa Rosália", "Residencial das Agulhas", "Todo o município"]},
    ],
    "local_intro": 'Poços de Caldas tem <strong>mais de 18.000 empresas ativas</strong> e um PIB de aproximadamente R$ 8 bilhões, com destaque para mineração, indústria e turismo. É referência em alumínio e bauxita no Brasil. Informações sobre abertura de empresas estão disponíveis na <a href="https://www.jucemg.mg.gov.br/" target="_blank" rel="noopener">JUCEMG</a>.',
    "local_p1": "Para mineração e beneficiamento, a estrutura tributária envolve <strong>CFEM, ICMS sobre saída de minério</strong> e créditos de IPI. Para turismo e hotelaria, o foco é no <strong>ISSQN municipal</strong> e nos regimes de IRPJ por atividade.",
    "local_p2": "Comércio varejista pode ter redução significativa de carga com migração de regime. Construtoras acessam o <strong>RET</strong> com IRPJ de 1%. A AM Cabral atua com todos esses perfis por atendimento 100% remoto.",
    "local_toggle_text": "Ver mais sobre a economia de Poços de Caldas",
    "location_h2": "Escritório em Pará de Minas. <em>Atendimento remoto em Poços de Caldas.</em>",
    "location_atend": "Atendemos empresas de Poços de Caldas 100% por videoconferência e plataforma digital. Sem necessidade de deslocamento para o cliente.",
    "footer_atend": "100% remoto por videoconferência<br>Segunda a sexta, 8h às 18h",
  },
  {
    "slug": "uberaba-mg",
    "name": "Uberaba",
    "name_ac": "Uberaba",
    "state": "MG",
    "uf": "mg",
    "preposition": "em",
    "foto_file": "uberaba-cidade.jpg",
    "foto_alt": "Centro de Uberaba/MG",
    "foto_figcaption": "Uberaba, capital do agronegócio e polo universitário do Triângulo Mineiro.",
    "loader_phrase": "Agronegócio e serviços em Uberaba exigem contabilidades diferentes",
    "title": "Serviços Contábeis em Uberaba | AM Cabral Contabilidade",
    "meta_desc": "Escritório de contabilidade em Uberaba/MG. Polo do agronegócio, frigoríficos e serviços do Triângulo Mineiro: cada setor com tributação especializada. Planejamento e holding.",
    "og_desc": "Contabilidade especializada para empresas de Uberaba/MG. Agronegócio, frigoríficos, comércio e serviços. Diagnóstico tributário gratuito.",
    "canonical": "https://amcabralblindagem.com.br/uberaba-mg/",
    "breadcrumb_name": "Uberaba",
    "hero_h1": 'Serviços Contábeis em <span style="color:var(--dourado)">Uberaba</span>: agronegócio e serviços têm tributação completamente diferente',
    "hero_sub": 'Capital do agronegócio e polo universitário do Triângulo Mineiro: cada setor de <a href="https://pt.wikipedia.org/wiki/Uberaba" target="_blank" rel="noopener" class="wiki-link">Uberaba</a> tem tributos específicos que o contador genérico ignora. A AM Cabral entrega contabilidade feita para o seu setor. Diagnóstico tributário gratuito.',
    "wiki_url": "https://pt.wikipedia.org/wiki/Uberaba",
    "marquee_city": "Uberaba, MG",
    "marquee_destaque": "Triângulo Mineiro",
    "authority_h2": 'Contabilidade especializada por setor para empresas de <a href="https://pt.wikipedia.org/wiki/Uberaba" target="_blank" rel="noopener" class="wiki-link">Uberaba</a>',
    "authority_p1": "Uberaba é a capital brasileira do zebu e um dos maiores polos do agronegócio do país. Frigoríficos, cooperativas, trading de grãos e toda a cadeia do campo têm tributação completamente diferente de comércio e serviços.",
    "authority_p2": "<strong>Frigoríficos e processamento de proteína animal têm créditos de ICMS específicos e PIS/COFINS monofásico.</strong> Cooperativas têm tributação própria sobre sobras e distribuição. Comércio atacadista tem regimes específicos de ICMS. Setor de saúde e educação têm ISSQN municipal.",
    "authority_p3": "Um contador genérico não conhece essas especificidades. <strong>A AM Cabral atende Uberaba remotamente com a mesma profundidade dos nossos clientes presenciais em Pará de Minas.</strong>",
    "stats4": "4 setores com especialização",
    "card1_title": "Contabilidade em Uberaba",
    "card1_desc": "Contabilidade completa para empresas de Uberaba: DRE, fluxo de caixa, departamento pessoal e obrigações acessórias. Atendimento remoto com profundidade de quem conhece o Triângulo Mineiro.",
    "card2_title": "Contador Especializado em Holding em Uberaba",
    "card2_desc": "Para empresários de Uberaba que construíram patrimônio ao longo dos anos. A holding separa pessoa física da jurídica, reduz imposto sobre aluguel de 27,5% para 8,4% e organiza a sucessão familiar.",
    "card3_title": "Contador para Fábricas &amp; Indústrias em Uberaba",
    "card3_desc": "Frigoríficos, beneficiamento agro e indústrias do Triângulo têm tributação específica que o contador genérico não conhece. PIS/COFINS monofásico, ICMS do agro e créditos extemporâneos precisam de especialista.",
    "card4_title": "Trocar de Contador em Uberaba",
    "card4_desc": "Trocar de contador parece complicado, mas não precisa ser. A AM Cabral faz toda a migração: busca de documentos, transferência de obrigações e diagnóstico de pendências sem interrupção da sua contabilidade.",
    "card3_bullets": ["PIS/COFINS monofásico para frigoríficos", "ICMS específico do agronegócio", "Preparação para reforma tributária 2026"],
    "amanda_h2": "Contadora tributária para empresas de Uberaba: Amanda Cabral de Oliveira, CRC/MG Ativo",
    "amanda_quote": '"Uberaba tem setores com tributação completamente distinta. Frigoríficos, agronegócio, comércio e serviços não podem compartilhar o mesmo contador genérico. Cada setor exige especialização diferente, e é exatamente isso que entregamos."',
    "setores": ["Frigoríficos e Proteína Animal", "Cooperativas Agropecuárias", "Trading de Grãos", "Comércio Atacadista", "Saúde e Educação", "Construtoras", "Holding Patrimonial", "MEI em Crescimento"],
    "cases": [
      {"pill": "Recuperação de Créditos", "title": "Frigorífico no Triângulo Mineiro", "stat": "R$ 310 mil", "label": "recuperados em créditos", "detail": "PIS/COFINS monofásico sobre proteína animal não aproveitados pelo contador anterior. Auditoria retroativa de 5 anos. Processo via compensação."},
      {"pill": "Planejamento Tributário", "title": "Cooperativa agropecuária em Uberaba", "stat": "R$ 185 mil/ano", "label": "de economia tributária", "detail": "Regime tributário ajustado para o modelo de cooperativa. Distribuição de sobras e tributação específica corrigidos. Redução recorrente na carga efetiva."},
      {"pill": "Holding Patrimonial", "title": "Produtor rural e empresário em Uberaba", "stat": "R$ 105 mil/ano", "label": "de redução no IRPF", "detail": "Constituição de holding rural e familiar. Tributação de aluguel e arrendamento reduzida. Sucessão organizada sem inventário."},
    ],
    "depo": [
      {"quote": "\"Trabalho com frigorífico há 12 anos e nunca tinha aproveitado o PIS/COFINS monofásico corretamente. A Amanda identificou R$ 310 mil que estavam na mesa.\"", "role": "Sócio", "empresa": "Frigorífico, Triângulo Mineiro"},
      {"quote": "\"A Amanda ajustou a tributação da nossa cooperativa e economizamos R$ 185 mil no ano. Processo 100% remoto e sem complicação.\"", "role": "Presidente", "empresa": "Cooperativa agropecuária, Uberaba"},
      {"quote": "\"A holding rural organizou meu patrimônio e reduziu o imposto sobre arrendamentos. Amanda conhece o agronegócio de verdade.\"", "role": "Proprietário", "empresa": "Produtor rural, Uberaba/MG"},
    ],
    "faq": [
      {"q": "Como funciona a contabilidade para frigoríficos em Uberaba?", "a": "Frigoríficos e processamento de proteína animal têm PIS/COFINS monofásico e créditos específicos de ICMS na cadeia de proteína. Muitas empresas têm créditos não aproveitados que podem ser recuperados em auditoria retroativa de 5 anos."},
      {"q": "Cooperativas agropecuárias de Uberaba têm regime tributário especial?", "a": "Sim. Cooperativas têm tributação própria: sobras distribuídas aos cooperados têm tratamento diferente de lucro. O ato cooperativo não integra a base de cálculo do IRPJ e CSLL, e o ICMS nas operações entre cooperado e cooperativa tem alíquota específica."},
      {"q": "Qual a diferença de contabilidade para agronegócio, comércio e serviços em Uberaba?", "a": "Cada setor tem obrigações e oportunidades distintas. Frigoríficos e agro têm PIS/COFINS monofásico e ICMS específico. Comércio atacadista tem regimes de ICMS para distribuição regional. Serviços de saúde e educação têm ISSQN municipal. A AM Cabral atende todos remotamente."},
      {"q": "Quanto custa o diagnóstico tributário gratuito?", "a": "O diagnóstico é gratuito, dura cerca de 30 minutos por videoconferência e resulta em um relatório com créditos recuperáveis, riscos fiscais e oportunidades de redução. Sem compromisso."},
      {"q": "Posso trocar de contador sem perder documentos ou histórico?", "a": "Sim. Assumimos a transferência de todos os documentos em até 30 dias. O atendimento para Uberaba é 100% remoto por videoconferência."},
    ],
    "coverage": [
      {"title": "Polo Agroindustrial", "items": ["Frigoríficos e abatedouros", "Cooperativas agropecuárias", "Trading de grãos e insumos", "Eixo BR-050 e BR-262", "Agroindústria e processamento"]},
      {"title": "Eixo Comercial/Serviços", "items": ["Centro (Av. Getúlio Vargas)", "Bairro Fabrício", "Shopping Uberaba", "Av. Leopoldino de Oliveira", "Parque das Gameleiras"]},
      {"title": "Demais Bairros", "items": ["Abadia", "Nossa Senhora Aparecida", "Jardim das Rosas", "Mercês", "Todo o município"]},
    ],
    "local_intro": 'Uberaba tem <strong>mais de 30.000 empresas ativas</strong> e um PIB de aproximadamente R$ 15 bilhões, fortemente ancorado no agronegócio, frigoríficos e serviços. É a capital brasileira do zebu e sede de grandes cooperativas. Informações sobre abertura de empresas estão disponíveis na <a href="https://www.jucemg.mg.gov.br/" target="_blank" rel="noopener">JUCEMG</a>.',
    "local_p1": "Para frigoríficos e processamento de proteína, a estrutura tributária envolve <strong>PIS/COFINS monofásico</strong> e créditos de ICMS na cadeia. Para cooperativas, o foco é no <strong>ato cooperativo</strong> e na tributação específica de sobras e distribuição.",
    "local_p2": "Comércio atacadista tem regimes de ICMS para distribuição regional do Triângulo. Construtoras acessam o <strong>RET</strong> com IRPJ de 1%. A AM Cabral atua com todos esses perfis por atendimento 100% remoto.",
    "local_toggle_text": "Ver mais sobre a economia de Uberaba",
    "location_h2": "Escritório em Pará de Minas. <em>Atendimento remoto em Uberaba.</em>",
    "location_atend": "Atendemos empresas de Uberaba 100% por videoconferência e plataforma digital. Sem necessidade de deslocamento para o cliente.",
    "footer_atend": "100% remoto por videoconferência<br>Segunda a sexta, 8h às 18h",
  },
  {
    "slug": "uberlandia-mg",
    "name": "Uberlândia",
    "name_ac": "Uberlandia",
    "state": "MG",
    "uf": "mg",
    "preposition": "em",
    "foto_file": "uberlandia-cidade.jpg",
    "foto_alt": "Centro de Uberlândia/MG",
    "foto_figcaption": "Uberlândia, polo de logística e comércio atacadista do Brasil.",
    "loader_phrase": "Atacado e logística em Uberlândia exigem contabilidade especializada",
    "title": "Serviços Contábeis em Uberlândia | AM Cabral Contabilidade",
    "meta_desc": "Escritório de contabilidade em Uberlândia/MG. Polo de atacado, logística e indústria do Triângulo Mineiro: cada setor com tributação especializada. Planejamento e holding.",
    "og_desc": "Contabilidade especializada para empresas de Uberlândia/MG. Atacado, logística, indústria e serviços. Diagnóstico tributário gratuito.",
    "canonical": "https://amcabralblindagem.com.br/uberlandia-mg/",
    "breadcrumb_name": "Uberlândia",
    "hero_h1": 'Serviços Contábeis em <span style="color:var(--dourado)">Uberlândia</span>: atacado, logística e indústria têm tributação completamente diferente',
    "hero_sub": 'Polo de comércio atacadista e logística do Brasil: cada setor de <a href="https://pt.wikipedia.org/wiki/Uberl%C3%A2ndia" target="_blank" rel="noopener" class="wiki-link">Uberlândia</a> tem tributos específicos que o contador genérico ignora. A AM Cabral entrega contabilidade feita para o seu setor. Diagnóstico tributário gratuito.',
    "wiki_url": "https://pt.wikipedia.org/wiki/Uberl%C3%A2ndia",
    "marquee_city": "Uberlândia, MG",
    "marquee_destaque": "Polo Atacadista do Brasil",
    "authority_h2": 'Contabilidade especializada por setor para empresas de <a href="https://pt.wikipedia.org/wiki/Uberl%C3%A2ndia" target="_blank" rel="noopener" class="wiki-link">Uberlândia</a>',
    "authority_p1": "Uberlândia é o maior polo de comércio atacadista e distribuição do interior do Brasil. Distribuidoras, transportadoras, indústrias e prestadores de serviços têm tributação completamente diferente entre si.",
    "authority_p2": "<strong>Comércio atacadista tem regimes específicos de ICMS para distribuição interestadual.</strong> Transportadoras têm ICMS sobre frete com alíquotas específicas e créditos de diesel. Indústria diversificada tem ICMS-ST e IPI. Serviços de tecnologia têm ISSQN municipal variável.",
    "authority_p3": "Um contador genérico não conhece essas especificidades. <strong>A AM Cabral atende Uberlândia remotamente com a mesma profundidade dos nossos clientes presenciais em Pará de Minas.</strong>",
    "stats4": "4 setores com especialização",
    "card1_title": "Contabilidade em Uberlândia",
    "card1_desc": "Contabilidade completa para empresas de Uberlândia: DRE, fluxo de caixa, departamento pessoal e obrigações acessórias. Atendimento remoto com profundidade de quem conhece o polo atacadista.",
    "card2_title": "Contador Especializado em Holding em Uberlândia",
    "card2_desc": "Para empresários de Uberlândia que construíram patrimônio ao longo dos anos. A holding separa pessoa física da jurídica, reduz imposto sobre aluguel de 27,5% para 8,4% e organiza a sucessão familiar.",
    "card3_title": "Contador para Fábricas &amp; Indústrias em Uberlândia",
    "card3_desc": "Atacadistas, transportadoras e indústrias de Uberlândia têm tributação específica. ICMS interestadual, crédito de diesel e regimes específicos de distribuição precisam de especialista setorial.",
    "card4_title": "Trocar de Contador em Uberlândia",
    "card4_desc": "Trocar de contador parece complicado, mas não precisa ser. A AM Cabral faz toda a migração: busca de documentos, transferência de obrigações e diagnóstico de pendências sem interrupção da sua contabilidade.",
    "card3_bullets": ["ICMS interestadual para atacadistas", "Crédito de diesel e ICMS para transportadoras", "Preparação para reforma tributária 2026"],
    "amanda_h2": "Contadora tributária para empresas de Uberlândia: Amanda Cabral de Oliveira, CRC/MG Ativo",
    "amanda_quote": '"Uberlândia tem setores com tributação completamente distinta. Atacado, logística, indústria e serviços não podem compartilhar o mesmo contador genérico. Cada setor exige especialização diferente, e é exatamente isso que entregamos."',
    "setores": ["Comércio Atacadista", "Transportadoras e Logística", "Indústria Diversificada", "Tecnologia e Software", "Saúde e Clínicas", "Construtoras", "Holding Patrimonial", "MEI em Crescimento"],
    "cases": [
      {"pill": "Recuperação de Créditos", "title": "Distribuidora atacadista em Uberlândia", "stat": "R$ 290 mil", "label": "recuperados em créditos", "detail": "ICMS interestadual com alíquotas incorretas aplicadas pelo contador anterior. Auditoria retroativa de 5 anos. Recuperação via compensação."},
      {"pill": "Planejamento Tributário", "title": "Transportadora no Triângulo Mineiro", "stat": "R$ 155 mil/ano", "label": "de economia tributária", "detail": "Regime de ICMS sobre frete corrigido. Créditos de diesel mapeados e aproveitados. Redução recorrente na carga efetiva."},
      {"pill": "Holding Patrimonial", "title": "Empresário do setor atacadista", "stat": "R$ 95 mil/ano", "label": "de redução no IRPF", "detail": "Constituição de holding familiar. Tributação de aluguel reduzida de 27,5% para 8,4%. Sucessão organizada sem inventário."},
    ],
    "depo": [
      {"quote": "\"A Amanda identificou R$ 290 mil em crédito de ICMS interestadual que minha distribuidora pagava a mais há anos. Processo legal e conduzido sem precisar da minha intervenção diária.\"", "role": "Sócio", "empresa": "Distribuidora atacadista, Uberlândia"},
      {"quote": "\"Nosso ICMS sobre frete estava errado. A Amanda corrigiu o regime e economizamos R$ 155 mil no primeiro ano. Atendimento 100% remoto e eficiente.\"", "role": "Diretor", "empresa": "Transportadora, Triângulo Mineiro"},
      {"quote": "\"A holding resolveu a tributação dos meus aluguéis e organizou a sucessão. Amanda conhece o setor atacadista de Uberlândia de verdade.\"", "role": "Proprietário", "empresa": "Empresário, Uberlândia/MG"},
    ],
    "faq": [
      {"q": "Como funciona a contabilidade para distribuidoras atacadistas em Uberlândia?", "a": "Distribuidoras atacadistas têm regimes específicos de ICMS para operações interestaduais, com créditos e débitos que variam por estado de destino. Erros nessa estrutura são comuns e podem resultar em créditos não aproveitados ou autuações. Auditoria de 5 anos identifica o potencial de recuperação."},
      {"q": "Transportadoras de Uberlândia têm tributação especial?", "a": "Sim. Transportadoras têm ICMS sobre prestação de serviço de frete com alíquotas específicas por modal e destino. Além disso, há crédito de ICMS embutido no diesel que muitas empresas não aproveitam. O diagnóstico tributário mapeia o potencial de cada empresa."},
      {"q": "Qual a diferença de contabilidade para atacado, indústria e serviços em Uberlândia?", "a": "Atacadistas têm ICMS interestadual. Indústrias têm ICMS-ST e IPI. Serviços de tecnologia têm ISSQN variável por município. Cada setor exige estratégia diferente. A AM Cabral atende todos remotamente de Uberlândia."},
      {"q": "Quanto custa o diagnóstico tributário gratuito?", "a": "O diagnóstico é gratuito, dura cerca de 30 minutos por videoconferência e resulta em relatório com créditos recuperáveis, riscos e oportunidades. Sem compromisso de contratação."},
      {"q": "Posso trocar de contador sem perder documentos ou histórico?", "a": "Sim. Assumimos a transferência de todos os documentos em até 30 dias. O atendimento para Uberlândia é 100% remoto por videoconferência."},
    ],
    "coverage": [
      {"title": "Polo Atacadista/Logístico", "items": ["DAIA (Distrito Agroindustrial)", "Centro de distribuição BR-050/BR-365", "Porto Seco do Triângulo", "Hubs logísticos e transportadoras", "Indústrias do eixo norte"]},
      {"title": "Eixo Comercial/Serviços", "items": ["Centro (Av. Afonso Pena)", "Bairro Santa Mônica", "Shopping Uberlândia Center", "Av. Rondon Pacheco", "Bairro Tibery"]},
      {"title": "Demais Bairros", "items": ["Saraiva", "Jardim Canaã", "Morada da Colina", "Pampulha", "Todo o município"]},
    ],
    "local_intro": 'Uberlândia tem <strong>mais de 70.000 empresas ativas</strong> e um PIB de aproximadamente R$ 35 bilhões. É o maior polo de comércio atacadista e logística do interior do Brasil, com forte presença industrial e de serviços. Informações sobre abertura de empresas estão disponíveis na <a href="https://www.jucemg.mg.gov.br/" target="_blank" rel="noopener">JUCEMG</a>.',
    "local_p1": "Para distribuidoras atacadistas, a estrutura tributária envolve <strong>ICMS interestadual</strong> com créditos e débitos por estado. Para transportadoras, o foco é no <strong>ICMS sobre frete</strong> e nos créditos de diesel.",
    "local_p2": "Serviços de tecnologia têm ISSQN variável por município de destino do serviço. Construtoras acessam o <strong>RET</strong> com IRPJ de 1%. A AM Cabral atua com todos esses perfis por atendimento 100% remoto.",
    "local_toggle_text": "Ver mais sobre a economia de Uberlândia",
    "location_h2": "Escritório em Pará de Minas. <em>Atendimento remoto em Uberlândia.</em>",
    "location_atend": "Atendemos empresas de Uberlândia 100% por videoconferência e plataforma digital. Sem necessidade de deslocamento para o cliente.",
    "footer_atend": "100% remoto por videoconferência<br>Segunda a sexta, 8h às 18h",
  },
  {
    "slug": "campinas-sp",
    "name": "Campinas",
    "name_ac": "Campinas",
    "state": "SP",
    "uf": "sp",
    "preposition": "em",
    "foto_file": "campinas-cidade.jpg",
    "foto_alt": "Centro de Campinas/SP",
    "foto_figcaption": "Campinas, polo de tecnologia e indústria do interior de São Paulo.",
    "loader_phrase": "Tecnologia e indústria em Campinas exigem contabilidades diferentes",
    "title": "Serviços Contábeis em Campinas | AM Cabral Contabilidade",
    "meta_desc": "Escritório de contabilidade em Campinas/SP. Polo de tecnologia, indústria e serviços do interior paulista: cada setor com tributação especializada. Planejamento tributário e holding.",
    "og_desc": "Contabilidade especializada para empresas de Campinas/SP. Tecnologia, indústria, comércio e serviços. Diagnóstico tributário gratuito.",
    "canonical": "https://amcabralblindagem.com.br/campinas-sp/",
    "breadcrumb_name": "Campinas",
    "hero_h1": 'Serviços Contábeis em <span style="color:var(--dourado)">Campinas</span>: tecnologia, indústria e serviços têm tributação completamente diferente',
    "hero_sub": 'Polo de tecnologia e indústria do interior de São Paulo: cada setor de <a href="https://pt.wikipedia.org/wiki/Campinas" target="_blank" rel="noopener" class="wiki-link">Campinas</a> tem tributos específicos que o contador genérico ignora. A AM Cabral entrega contabilidade feita para o seu setor. Diagnóstico tributário gratuito.',
    "wiki_url": "https://pt.wikipedia.org/wiki/Campinas",
    "marquee_city": "Campinas, SP",
    "marquee_destaque": "Polo Tecnológico Campinas",
    "authority_h2": 'Contabilidade especializada por setor para empresas de <a href="https://pt.wikipedia.org/wiki/Campinas" target="_blank" rel="noopener" class="wiki-link">Campinas</a>',
    "authority_p1": "Campinas é um dos maiores polos tecnológicos e industriais do Brasil. Empresas de software, hardware, indústria de alta tecnologia, saúde e serviços avançados convivem com comércio e construção civil.",
    "authority_p2": "<strong>Empresas de tecnologia têm ISS variável por município e benefícios fiscais específicos.</strong> Indústrias de alta tecnologia têm ICMS-ST e IPI com regimes específicos. Saúde e educação têm tributação própria. Comércio varejista tem oportunidades de migração de regime.",
    "authority_p3": "Um contador genérico não conhece essas especificidades. <strong>A AM Cabral atende Campinas remotamente com a mesma profundidade dos nossos clientes presenciais em Pará de Minas.</strong>",
    "stats4": "4 setores com especialização",
    "card1_title": "Contabilidade em Campinas",
    "card1_desc": "Contabilidade completa para empresas de Campinas: DRE, fluxo de caixa, departamento pessoal e obrigações acessórias. Atendimento remoto com profundidade de quem conhece o polo tecnológico.",
    "card2_title": "Contador Especializado em Holding em Campinas",
    "card2_desc": "Para empresários de Campinas que construíram patrimônio ao longo dos anos. A holding separa pessoa física da jurídica, reduz imposto sobre aluguel de 27,5% para 8,4% e organiza a sucessão familiar.",
    "card3_title": "Contador para Fábricas &amp; Indústrias em Campinas",
    "card3_desc": "Indústrias de alta tecnologia, farmacêutica e de alimentos de Campinas têm tributação específica. ICMS-ST, IPI e benefícios fiscais do polo tecnológico precisam de especialista.",
    "card4_title": "Trocar de Contador em Campinas",
    "card4_desc": "Trocar de contador parece complicado, mas não precisa ser. A AM Cabral faz toda a migração: busca de documentos, transferência de obrigações e diagnóstico de pendências sem interrupção da sua contabilidade.",
    "card3_bullets": ["ICMS-ST e IPI para indústria tech", "Benefícios fiscais do polo tecnológico", "Preparação para reforma tributária 2026"],
    "amanda_h2": "Contadora tributária para empresas de Campinas: Amanda Cabral de Oliveira, CRC/MG Ativo",
    "amanda_quote": '"Campinas tem setores com tributação completamente distinta. Tecnologia, indústria, comércio e serviços não podem compartilhar o mesmo contador genérico. Cada setor exige especialização diferente, e é exatamente isso que entregamos."',
    "setores": ["Tecnologia e Software", "Indústria de Alta Tecnologia", "Farmacêutica e Saúde", "Comércio Varejista", "Serviços Avançados", "Construtoras", "Holding Patrimonial", "MEI em Crescimento"],
    "cases": [
      {"pill": "Recuperação de Créditos", "title": "Indústria de alimentos em Campinas/SP", "stat": "R$ 260 mil", "label": "recuperados em créditos", "detail": "PIS/COFINS monofásico sobre insumos alimentícios não aproveitados pelo contador anterior. Auditoria retroativa de 5 anos."},
      {"pill": "Planejamento Tributário", "title": "Empresa de tecnologia em Campinas", "stat": "R$ 130 mil/ano", "label": "de economia tributária", "detail": "Enquadramento em regime tributário adequado para empresa de software. ISS e IRPJ corrigidos para o perfil de faturamento."},
      {"pill": "Holding Patrimonial", "title": "Empresário do setor industrial", "stat": "R$ 88 mil/ano", "label": "de redução no IRPF", "detail": "Constituição de holding familiar. Tributação de aluguel reduzida de 27,5% para 8,4%. Sucessão organizada sem inventário."},
    ],
    "depo": [
      {"quote": "\"A Amanda identificou R$ 260 mil em crédito de PIS/COFINS que minha indústria pagava a mais. Processo conduzido 100% remotamente, sem burocracia.\"", "role": "Sócio", "empresa": "Indústria de alimentos, Campinas/SP"},
      {"quote": "\"Nossa empresa de tecnologia precisava de um contador que entendesse ISS e regimes específicos de software. A Amanda corrigiu tudo e economizamos R$ 130 mil.\"", "role": "CEO", "empresa": "Empresa tech, Campinas/SP"},
      {"quote": "\"A holding resolveu a tributação dos meus aluguéis e organizou a herança. Amanda atende Campinas com a mesma qualidade de quem está presencialmente.\"", "role": "Proprietário", "empresa": "Empresário, Campinas/SP"},
    ],
    "faq": [
      {"q": "Como funciona a contabilidade para empresas de tecnologia em Campinas?", "a": "Empresas de tecnologia e software em Campinas têm ISS variável conforme o município de prestação do serviço, com alíquotas de 2% a 5%. Além disso, há benefícios fiscais específicos para empresas do polo tecnológico. O regime entre Simples Nacional, Lucro Presumido e Lucro Real impacta diretamente o ISS e o PIS/COFINS."},
      {"q": "Indústrias farmacêuticas e de alimentos de Campinas têm tributação especial?", "a": "Sim. Indústrias farmacêuticas operam com substituição tributária de ICMS e PIS/COFINS monofásico. Indústrias de alimentos têm regimes de PIS/COFINS monofásico sobre itens específicos. Créditos extemporâneos são comuns quando o contador anterior não mapeou corretamente."},
      {"q": "Qual a diferença de contabilidade para tecnologia, indústria e serviços em Campinas?", "a": "Tecnologia tem ISS específico. Indústria tem ICMS-ST e IPI. Serviços de saúde têm ISSQN. Comércio varejista pode migrar de regime. A AM Cabral atende todos remotamente."},
      {"q": "Quanto custa o diagnóstico tributário gratuito?", "a": "O diagnóstico é gratuito, dura cerca de 30 minutos por videoconferência e resulta em relatório com créditos recuperáveis, riscos e oportunidades. Sem compromisso."},
      {"q": "Posso trocar de contador sem perder documentos ou histórico?", "a": "Sim. Assumimos a transferência de todos os documentos em até 30 dias. O atendimento para Campinas é 100% remoto por videoconferência."},
    ],
    "coverage": [
      {"title": "Polo Tecnológico/Industrial", "items": ["Techno Park (polo tech)", "Distrito Industrial de Campinas", "Farmacêutica e alimentos Anhanguera", "Indústrias do eixo SP-065", "Parque Científico UNICAMP"]},
      {"title": "Eixo Comercial/Serviços", "items": ["Centro (Largo do Rosário)", "Bairro Cambuí", "Shopping Iguatemi Campinas", "Av. José de Souza Campos", "Barão Geraldo"]},
      {"title": "Demais Bairros", "items": ["Taquaral", "Mansões Santo Antônio", "Jardim Guarani", "Nova Campinas", "Todo o município"]},
    ],
    "local_intro": 'Campinas tem <strong>mais de 90.000 empresas ativas</strong> e um PIB de aproximadamente R$ 90 bilhões. É um dos maiores polos tecnológicos e industriais do Brasil, com destaque para tecnologia, farmacêutica, alimentos e serviços avançados. Informações sobre abertura de empresas estão disponíveis na <a href="https://www.jucei.sp.gov.br/" target="_blank" rel="noopener">JUCESP</a>.',
    "local_p1": "Para empresas de tecnologia, a estrutura tributária envolve <strong>ISS variável por município</strong> e benefícios fiscais específicos do polo. Para indústrias farmacêuticas e de alimentos, o foco é no <strong>PIS/COFINS monofásico</strong> e no ICMS-ST.",
    "local_p2": "Comércio varejista pode ter redução significativa de carga com migração de regime. Construtoras acessam o <strong>RET</strong> com IRPJ de 1%. A AM Cabral atua com todos esses perfis por atendimento 100% remoto.",
    "local_toggle_text": "Ver mais sobre a economia de Campinas",
    "location_h2": "Escritório em Pará de Minas. <em>Atendimento remoto em Campinas.</em>",
    "location_atend": "Atendemos empresas de Campinas 100% por videoconferência e plataforma digital. Sem necessidade de deslocamento para o cliente.",
    "footer_atend": "100% remoto por videoconferência<br>Segunda a sexta, 8h às 18h",
  },
  {
    "slug": "guarulhos-sp",
    "name": "Guarulhos",
    "name_ac": "Guarulhos",
    "state": "SP",
    "uf": "sp",
    "preposition": "em",
    "foto_file": "guarulhos-cidade.jpg",
    "foto_alt": "Centro de Guarulhos/SP",
    "foto_figcaption": "Guarulhos, polo logístico e industrial da Grande São Paulo.",
    "loader_phrase": "Logística e indústria em Guarulhos exigem contabilidades diferentes",
    "title": "Serviços Contábeis em Guarulhos | AM Cabral Contabilidade",
    "meta_desc": "Escritório de contabilidade em Guarulhos/SP. Polo logístico, industrial e de serviços da Grande SP: cada setor com tributação especializada. Planejamento tributário e holding.",
    "og_desc": "Contabilidade especializada para empresas de Guarulhos/SP. Logística, indústria, comércio e serviços. Diagnóstico tributário gratuito.",
    "canonical": "https://amcabralblindagem.com.br/guarulhos-sp/",
    "breadcrumb_name": "Guarulhos",
    "hero_h1": 'Serviços Contábeis em <span style="color:var(--dourado)">Guarulhos</span>: logística, indústria e comércio têm tributação completamente diferente',
    "hero_sub": 'Polo logístico e industrial da Grande São Paulo: cada setor de <a href="https://pt.wikipedia.org/wiki/Guarulhos" target="_blank" rel="noopener" class="wiki-link">Guarulhos</a> tem tributos específicos que o contador genérico ignora. A AM Cabral entrega contabilidade feita para o seu setor. Diagnóstico tributário gratuito.',
    "wiki_url": "https://pt.wikipedia.org/wiki/Guarulhos",
    "marquee_city": "Guarulhos, SP",
    "marquee_destaque": "Polo Logístico Guarulhos",
    "authority_h2": 'Contabilidade especializada por setor para empresas de <a href="https://pt.wikipedia.org/wiki/Guarulhos" target="_blank" rel="noopener" class="wiki-link">Guarulhos</a>',
    "authority_p1": "Guarulhos é o segundo maior município de São Paulo e um dos maiores polos logísticos e industriais do Brasil. Sua localização próxima ao Aeroporto Internacional e às principais rodovias atrai transportadoras, distribuidoras e indústrias de toda cadeia produtiva.",
    "authority_p2": "<strong>Transportadoras e operadores logísticos têm ICMS sobre frete com alíquotas específicas e créditos de diesel.</strong> Indústrias têm ICMS-ST e IPI. Comércio importador tem regimes aduaneiros e tributação específica de importação. Serviços têm ISSQN municipal.",
    "authority_p3": "Um contador genérico não conhece essas especificidades. <strong>A AM Cabral atende Guarulhos remotamente com a mesma profundidade dos nossos clientes presenciais em Pará de Minas.</strong>",
    "stats4": "4 setores com especialização",
    "card1_title": "Contabilidade em Guarulhos",
    "card1_desc": "Contabilidade completa para empresas de Guarulhos: DRE, fluxo de caixa, departamento pessoal e obrigações acessórias. Atendimento remoto com profundidade de quem conhece o polo logístico.",
    "card2_title": "Contador Especializado em Holding em Guarulhos",
    "card2_desc": "Para empresários de Guarulhos que construíram patrimônio ao longo dos anos. A holding separa pessoa física da jurídica, reduz imposto sobre aluguel de 27,5% para 8,4% e organiza a sucessão familiar.",
    "card3_title": "Contador para Fábricas &amp; Indústrias em Guarulhos",
    "card3_desc": "Indústrias e operadores logísticos de Guarulhos têm tributação específica. ICMS sobre frete, crédito de diesel e regimes aduaneiros precisam de especialista setorial.",
    "card4_title": "Trocar de Contador em Guarulhos",
    "card4_desc": "Trocar de contador parece complicado, mas não precisa ser. A AM Cabral faz toda a migração: busca de documentos, transferência de obrigações e diagnóstico de pendências sem interrupção da sua contabilidade.",
    "card3_bullets": ["ICMS sobre frete e crédito de diesel", "Regimes aduaneiros e importação", "Preparação para reforma tributária 2026"],
    "amanda_h2": "Contadora tributária para empresas de Guarulhos: Amanda Cabral de Oliveira, CRC/MG Ativo",
    "amanda_quote": '"Guarulhos tem setores com tributação completamente distinta. Logística, indústria, comércio e serviços não podem compartilhar o mesmo contador genérico. Cada setor exige especialização diferente, e é exatamente isso que entregamos."',
    "setores": ["Transportadoras e Logística", "Comércio Importador", "Indústria Diversificada", "Distribuição Atacadista", "Serviços Profissionais", "Construtoras", "Holding Patrimonial", "MEI em Crescimento"],
    "cases": [
      {"pill": "Recuperação de Créditos", "title": "Transportadora na Grande São Paulo", "stat": "R$ 220 mil", "label": "recuperados em créditos", "detail": "ICMS embutido no diesel não aproveitado e alíquotas de frete incorretas. Auditoria retroativa de 5 anos. Recuperação via compensação."},
      {"pill": "Planejamento Tributário", "title": "Distribuidora importadora em Guarulhos", "stat": "R$ 175 mil/ano", "label": "de economia tributária", "detail": "Regime tributário ajustado para importação e distribuição. ICMS e PIS/COFINS corrigidos para o perfil de operações. Redução imediata na carga efetiva."},
      {"pill": "Holding Patrimonial", "title": "Empresário do setor logístico", "stat": "R$ 92 mil/ano", "label": "de redução no IRPF", "detail": "Constituição de holding familiar. Tributação de aluguel reduzida de 27,5% para 8,4%. Sucessão organizada sem inventário."},
    ],
    "depo": [
      {"quote": "\"A Amanda encontrou R$ 220 mil em créditos de ICMS de diesel que nunca tinham sido aproveitados. Processo conduzido remotamente, sem precisar ir até o escritório.\"", "role": "Sócio", "empresa": "Transportadora, Grande São Paulo"},
      {"quote": "\"Nossa importadora precisava de um contador que entendesse regimes aduaneiros. A Amanda corrigiu o regime e economizamos R$ 175 mil no primeiro ano.\"", "role": "Diretor", "empresa": "Importadora, Guarulhos/SP"},
      {"quote": "\"A holding resolveu a tributação dos meus imóveis e organizou a herança de forma simples. Recomendo para qualquer empresário em Guarulhos.\"", "role": "Proprietário", "empresa": "Empresário, Guarulhos/SP"},
    ],
    "faq": [
      {"q": "Como funciona a contabilidade para transportadoras em Guarulhos?", "a": "Transportadoras têm ICMS sobre prestação de serviço de frete com alíquotas específicas por modal e destino. Há também crédito de ICMS embutido no diesel que muitas empresas não aproveitam. A auditoria retroativa de 5 anos mapeia o potencial de recuperação."},
      {"q": "Empresas de importação e comércio exterior de Guarulhos têm tributação especial?", "a": "Sim. Importadores têm II, IPI, PIS/COFINS-Importação e ICMS na entrada, com regimes específicos conforme o produto e o destino. O Drawback, o Recof e outros regimes aduaneiros especiais reduzem significativamente a carga para exportadores."},
      {"q": "Qual a diferença de contabilidade para logística, indústria e serviços em Guarulhos?", "a": "Logística tem ICMS sobre frete. Indústria tem ICMS-ST e IPI. Comércio importador tem regimes aduaneiros. Serviços têm ISSQN. Cada setor exige estratégia diferente. A AM Cabral atende todos remotamente."},
      {"q": "Quanto custa o diagnóstico tributário gratuito?", "a": "O diagnóstico é gratuito, dura cerca de 30 minutos por videoconferência e resulta em relatório com créditos recuperáveis, riscos e oportunidades. Sem compromisso."},
      {"q": "Posso trocar de contador sem perder documentos ou histórico?", "a": "Sim. Assumimos a transferência de todos os documentos em até 30 dias. O atendimento para Guarulhos é 100% remoto por videoconferência."},
    ],
    "coverage": [
      {"title": "Polo Logístico/Industrial", "items": ["Aeroporto Internacional de GRU", "Polo Industrial de Guarulhos", "Hub logístico Rodovia Dutra", "Condomínios logísticos SP-55", "Distribuidoras e atacadistas"]},
      {"title": "Eixo Comercial/Serviços", "items": ["Centro de Guarulhos", "Bairro Macedo", "Shopping Bonsucesso", "Av. Guarulhos", "Bairro Jardim Tranquilidade"]},
      {"title": "Demais Bairros", "items": ["Cumbica", "Ponte Grande", "Vila Galvão", "Jardim São João", "Todo o município"]},
    ],
    "local_intro": 'Guarulhos tem <strong>mais de 60.000 empresas ativas</strong> e um PIB de aproximadamente R$ 55 bilhões. É o segundo maior município de SP e um dos maiores polos logísticos do Brasil, com destaque para transportadoras, importação e indústria. Informações sobre abertura de empresas estão disponíveis na <a href="https://www.jucei.sp.gov.br/" target="_blank" rel="noopener">JUCESP</a>.',
    "local_p1": "Para transportadoras e operadores logísticos, a estrutura tributária envolve <strong>ICMS sobre frete</strong> com alíquotas por modal e créditos de diesel. Para importadores, o foco é nos <strong>regimes aduaneiros especiais</strong> que reduzem a carga na entrada.",
    "local_p2": "Comércio varejista pode ter redução com migração de regime. Construtoras acessam o <strong>RET</strong> com IRPJ de 1%. A AM Cabral atua com todos esses perfis por atendimento 100% remoto.",
    "local_toggle_text": "Ver mais sobre a economia de Guarulhos",
    "location_h2": "Escritório em Pará de Minas. <em>Atendimento remoto em Guarulhos.</em>",
    "location_atend": "Atendemos empresas de Guarulhos 100% por videoconferência e plataforma digital. Sem necessidade de deslocamento para o cliente.",
    "footer_atend": "100% remoto por videoconferência<br>Segunda a sexta, 8h às 18h",
  },
  {
    "slug": "osasco-sp",
    "name": "Osasco",
    "name_ac": "Osasco",
    "state": "SP",
    "uf": "sp",
    "preposition": "em",
    "foto_file": "osasco-cidade.jpg",
    "foto_alt": "Centro de Osasco/SP",
    "foto_figcaption": "Osasco, polo financeiro e industrial da Grande São Paulo.",
    "loader_phrase": "Finanças e indústria em Osasco exigem contabilidades diferentes",
    "title": "Serviços Contábeis em Osasco | AM Cabral Contabilidade",
    "meta_desc": "Escritório de contabilidade em Osasco/SP. Polo financeiro, industrial e de serviços da Grande SP: cada setor com tributação especializada. Planejamento tributário e holding.",
    "og_desc": "Contabilidade especializada para empresas de Osasco/SP. Financeiro, indústria, comércio e serviços. Diagnóstico tributário gratuito.",
    "canonical": "https://amcabralblindagem.com.br/osasco-sp/",
    "breadcrumb_name": "Osasco",
    "hero_h1": 'Serviços Contábeis em <span style="color:var(--dourado)">Osasco</span>: financeiro, indústria e serviços têm tributação completamente diferente',
    "hero_sub": 'Polo financeiro e industrial da Grande São Paulo: cada setor de <a href="https://pt.wikipedia.org/wiki/Osasco" target="_blank" rel="noopener" class="wiki-link">Osasco</a> tem tributos específicos que o contador genérico ignora. A AM Cabral entrega contabilidade feita para o seu setor. Diagnóstico tributário gratuito.',
    "wiki_url": "https://pt.wikipedia.org/wiki/Osasco",
    "marquee_city": "Osasco, SP",
    "marquee_destaque": "Polo Financeiro Osasco",
    "authority_h2": 'Contabilidade especializada por setor para empresas de <a href="https://pt.wikipedia.org/wiki/Osasco" target="_blank" rel="noopener" class="wiki-link">Osasco</a>',
    "authority_p1": "Osasco é o terceiro maior polo financeiro do Brasil, atrás de São Paulo e Rio de Janeiro. Bancos, financeiras, fintechs e seguradoras convivem com um forte setor industrial e comercial.",
    "authority_p2": "<strong>Serviços financeiros têm tributação específica: IOF, PIS/COFINS sobre receitas financeiras e CSLL com alíquota diferenciada.</strong> Indústrias têm ICMS-ST e IPI. Comércio varejista tem oportunidades de migração de regime. Serviços de saúde têm ISSQN municipal.",
    "authority_p3": "Um contador genérico não conhece essas especificidades. <strong>A AM Cabral atende Osasco remotamente com a mesma profundidade dos nossos clientes presenciais em Pará de Minas.</strong>",
    "stats4": "4 setores com especialização",
    "card1_title": "Contabilidade em Osasco",
    "card1_desc": "Contabilidade completa para empresas de Osasco: DRE, fluxo de caixa, departamento pessoal e obrigações acessórias. Atendimento remoto com profundidade de quem conhece o polo financeiro.",
    "card2_title": "Contador Especializado em Holding em Osasco",
    "card2_desc": "Para empresários de Osasco que construíram patrimônio ao longo dos anos. A holding separa pessoa física da jurídica, reduz imposto sobre aluguel de 27,5% para 8,4% e organiza a sucessão familiar.",
    "card3_title": "Contador para Fábricas &amp; Indústrias em Osasco",
    "card3_desc": "Indústrias e prestadores de serviços financeiros de Osasco têm tributação específica. ICMS-ST, IPI e tributação financeira precisam de especialista que conheça cada setor.",
    "card4_title": "Trocar de Contador em Osasco",
    "card4_desc": "Trocar de contador parece complicado, mas não precisa ser. A AM Cabral faz toda a migração: busca de documentos, transferência de obrigações e diagnóstico de pendências sem interrupção da sua contabilidade.",
    "card3_bullets": ["ICMS-ST e IPI para indústria", "PIS/COFINS e CSLL para serviços financeiros", "Preparação para reforma tributária 2026"],
    "amanda_h2": "Contadora tributária para empresas de Osasco: Amanda Cabral de Oliveira, CRC/MG Ativo",
    "amanda_quote": '"Osasco tem setores com tributação completamente distinta. Financeiro, indústria, comércio e serviços não podem compartilhar o mesmo contador genérico. Cada setor exige especialização diferente, e é exatamente isso que entregamos."',
    "setores": ["Serviços Financeiros e Fintechs", "Indústria Diversificada", "Comércio Varejista", "Saúde e Clínicas", "Seguradoras", "Construtoras", "Holding Patrimonial", "MEI em Crescimento"],
    "cases": [
      {"pill": "Recuperação de Créditos", "title": "Indústria de plásticos em Osasco/SP", "stat": "R$ 230 mil", "label": "recuperados em créditos", "detail": "ICMS-ST sobre insumos plásticos e créditos de IPI não aproveitados. Auditoria retroativa de 5 anos. Recuperação via compensação."},
      {"pill": "Planejamento Tributário", "title": "Prestadora de serviços financeiros", "stat": "R$ 160 mil/ano", "label": "de economia tributária", "detail": "Regime tributário ajustado para fintech. PIS/COFINS e CSLL corrigidos conforme atividade financeira específica."},
      {"pill": "Holding Patrimonial", "title": "Empresário do setor industrial em Osasco", "stat": "R$ 86 mil/ano", "label": "de redução no IRPF", "detail": "Constituição de holding familiar. Tributação de aluguel reduzida de 27,5% para 8,4%. Sucessão organizada."},
    ],
    "depo": [
      {"quote": "\"A Amanda encontrou R$ 230 mil em créditos de ICMS-ST que a indústria nunca tinha aproveitado. Processo 100% remoto e conduzido sem interrupção da operação.\"", "role": "Sócio", "empresa": "Indústria de plásticos, Osasco/SP"},
      {"quote": "\"Nossa fintech precisava de um contador que entendesse PIS/COFINS sobre receitas financeiras. A Amanda ajustou o regime e economizamos R$ 160 mil.\"", "role": "CEO", "empresa": "Fintech, Osasco/SP"},
      {"quote": "\"A holding resolveu a tributação dos meus imóveis e organizou a herança. Processo simples e transparente, 100% remoto.\"", "role": "Proprietário", "empresa": "Empresário, Osasco/SP"},
    ],
    "faq": [
      {"q": "Como funciona a contabilidade para fintechs e serviços financeiros em Osasco?", "a": "Fintechs e empresas de serviços financeiros têm PIS/COFINS calculado sobre receitas financeiras com alíquota de 0,65%/4% (Lucro Real) ou 3%/0,65% (Presumido). A CSLL tem alíquota de 15% para instituições financeiras, diferente dos 9% de empresas comuns. O regime escolhido impacta diretamente a carga total."},
      {"q": "Indústrias de Osasco têm tributação especial?", "a": "Indústrias em Osasco operam com ICMS-ST e IPI sobre os produtos fabricados. Créditos extemporâneos são comuns quando o contador anterior não mapeou corretamente os insumos industriais. Auditoria de 5 anos identifica o potencial de recuperação."},
      {"q": "Qual a diferença de contabilidade para financeiro, indústria e comércio em Osasco?", "a": "Financeiro tem PIS/COFINS e CSLL diferenciados. Indústria tem ICMS-ST e IPI. Comércio pode migrar de regime. Serviços têm ISSQN. A AM Cabral atende todos remotamente."},
      {"q": "Quanto custa o diagnóstico tributário gratuito?", "a": "O diagnóstico é gratuito, dura cerca de 30 minutos e resulta em relatório com créditos recuperáveis e oportunidades. Sem compromisso."},
      {"q": "Posso trocar de contador sem perder documentos ou histórico?", "a": "Sim. Assumimos a transferência de todos os documentos em até 30 dias. O atendimento para Osasco é 100% remoto por videoconferência."},
    ],
    "coverage": [
      {"title": "Polo Financeiro/Industrial", "items": ["Centro Empresarial de Osasco", "Polo Industrial Ayrton Senna", "Fintechs e financeiras Rua Antônio Agu", "Indústrias do eixo SP-270", "Distribuidoras e atacadistas"]},
      {"title": "Eixo Comercial/Serviços", "items": ["Centro de Osasco", "Bairro Presidente Altino", "Shopping Pátio Osasco", "Av. dos Autonomistas", "Bairro Quitaúna"]},
      {"title": "Demais Bairros", "items": ["Jardim D'Abril", "Vila Yara", "Baronesa", "Bonfim", "Todo o município"]},
    ],
    "local_intro": 'Osasco tem <strong>mais de 50.000 empresas ativas</strong> e um PIB de aproximadamente R$ 50 bilhões. É o terceiro maior polo financeiro do Brasil, com forte presença de bancos, fintechs, indústria e comércio. Informações sobre abertura de empresas na <a href="https://www.jucei.sp.gov.br/" target="_blank" rel="noopener">JUCESP</a>.',
    "local_p1": "Para serviços financeiros, a estrutura tributária envolve <strong>PIS/COFINS diferenciado</strong> e CSLL com alíquota de 15%. Para indústrias, o foco é no <strong>ICMS-ST e IPI</strong> sobre insumos e produtos.",
    "local_p2": "Comércio varejista pode ter redução com migração de regime. Construtoras acessam o <strong>RET</strong> com IRPJ de 1%. A AM Cabral atua com todos esses perfis por atendimento 100% remoto.",
    "local_toggle_text": "Ver mais sobre a economia de Osasco",
    "location_h2": "Escritório em Pará de Minas. <em>Atendimento remoto em Osasco.</em>",
    "location_atend": "Atendemos empresas de Osasco 100% por videoconferência e plataforma digital. Sem necessidade de deslocamento para o cliente.",
    "footer_atend": "100% remoto por videoconferência<br>Segunda a sexta, 8h às 18h",
  },
  {
    "slug": "piracicaba-sp",
    "name": "Piracicaba",
    "name_ac": "Piracicaba",
    "state": "SP",
    "uf": "sp",
    "preposition": "em",
    "foto_file": "piracicaba-cidade.jpg",
    "foto_alt": "Centro de Piracicaba/SP",
    "foto_figcaption": "Piracicaba, polo sucroalcooleiro e industrial do interior paulista.",
    "loader_phrase": "Sucroalcooleiro e indústria em Piracicaba exigem contabilidades diferentes",
    "title": "Serviços Contábeis em Piracicaba | AM Cabral Contabilidade",
    "meta_desc": "Escritório de contabilidade em Piracicaba/SP. Polo sucroalcooleiro, metalúrgico e universitário do interior paulista: cada setor com tributação especializada.",
    "og_desc": "Contabilidade especializada para empresas de Piracicaba/SP. Sucroalcooleiro, metalurgia, comércio e serviços. Diagnóstico tributário gratuito.",
    "canonical": "https://amcabralblindagem.com.br/piracicaba-sp/",
    "breadcrumb_name": "Piracicaba",
    "hero_h1": 'Serviços Contábeis em <span style="color:var(--dourado)">Piracicaba</span>: sucroalcooleiro, metalurgia e serviços têm tributação completamente diferente',
    "hero_sub": 'Polo sucroalcooleiro e metalúrgico do interior de São Paulo: cada setor de <a href="https://pt.wikipedia.org/wiki/Piracicaba" target="_blank" rel="noopener" class="wiki-link">Piracicaba</a> tem tributos específicos que o contador genérico ignora. A AM Cabral entrega contabilidade feita para o seu setor. Diagnóstico tributário gratuito.',
    "wiki_url": "https://pt.wikipedia.org/wiki/Piracicaba",
    "marquee_city": "Piracicaba, SP",
    "marquee_destaque": "Polo Sucroalcooleiro Piracicaba",
    "authority_h2": 'Contabilidade especializada por setor para empresas de <a href="https://pt.wikipedia.org/wiki/Piracicaba" target="_blank" rel="noopener" class="wiki-link">Piracicaba</a>',
    "authority_p1": "Piracicaba é um dos maiores polos sucroalcooleiros do mundo, sede de usinas, fornecedores de cana e toda a cadeia do etanol e açúcar. Metalurgia, fabricação de equipamentos agrícolas e comércio completam o perfil econômico da cidade.",
    "authority_p2": "<strong>Usinas e fornecedores do sucroalcooleiro têm ICMS sobre açúcar e etanol com alíquotas específicas.</strong> Metalurgia e fabricação de equipamentos têm ICMS-ST e IPI. Serviços de tecnologia agrícola têm ISS próprio. Comércio varejista tem oportunidades de migração de regime.",
    "authority_p3": "Um contador genérico não conhece essas especificidades. <strong>A AM Cabral atende Piracicaba remotamente com a mesma profundidade dos nossos clientes presenciais em Pará de Minas.</strong>",
    "stats4": "4 setores com especialização",
    "card1_title": "Contabilidade em Piracicaba",
    "card1_desc": "Contabilidade completa para empresas de Piracicaba: DRE, fluxo de caixa, departamento pessoal e obrigações acessórias. Atendimento remoto com profundidade de quem conhece o polo sucroalcooleiro.",
    "card2_title": "Contador Especializado em Holding em Piracicaba",
    "card2_desc": "Para empresários de Piracicaba que construíram patrimônio ao longo dos anos. A holding separa pessoa física da jurídica, reduz imposto sobre aluguel de 27,5% para 8,4% e organiza a sucessão familiar.",
    "card3_title": "Contador para Fábricas &amp; Indústrias em Piracicaba",
    "card3_desc": "Usinas, metalurgia e fabricantes de equipamentos agrícolas de Piracicaba têm tributação específica. ICMS sobre açúcar e etanol, IPI sobre máquinas e créditos extemporâneos precisam de especialista.",
    "card4_title": "Trocar de Contador em Piracicaba",
    "card4_desc": "Trocar de contador parece complicado, mas não precisa ser. A AM Cabral faz toda a migração: busca de documentos, transferência de obrigações e diagnóstico de pendências sem interrupção da sua contabilidade.",
    "card3_bullets": ["ICMS sobre açúcar, etanol e cana", "IPI para máquinas e equipamentos agrícolas", "Preparação para reforma tributária 2026"],
    "amanda_h2": "Contadora tributária para empresas de Piracicaba: Amanda Cabral de Oliveira, CRC/MG Ativo",
    "amanda_quote": '"Piracicaba tem setores com tributação completamente distinta. Sucroalcooleiro, metalurgia, comércio e serviços não podem compartilhar o mesmo contador genérico. Cada setor exige especialização diferente, e é exatamente isso que entregamos."',
    "setores": ["Sucroalcooleiro e Usinas", "Fornecedores de Cana", "Metalurgia e Fundição", "Equipamentos Agrícolas", "Comércio Varejista", "Serviços Profissionais", "Holding Patrimonial", "MEI em Crescimento"],
    "cases": [
      {"pill": "Recuperação de Créditos", "title": "Fornecedor do polo sucroalcooleiro em SP", "stat": "R$ 250 mil", "label": "recuperados em créditos", "detail": "ICMS sobre saída de açúcar e etanol com alíquotas incorretas. Auditoria retroativa de 5 anos. Recuperação via compensação."},
      {"pill": "Planejamento Tributário", "title": "Metalúrgica em Piracicaba/SP", "stat": "R$ 140 mil/ano", "label": "de economia tributária", "detail": "Créditos de ICMS-ST sobre insumos metálicos e IPI sobre produtos exportados não aproveitados. Redução imediata na carga efetiva."},
      {"pill": "Holding Patrimonial", "title": "Empresário do setor agroindustrial", "stat": "R$ 82 mil/ano", "label": "de redução no IRPF", "detail": "Constituição de holding rural e familiar. Tributação de aluguel e arrendamento rural reduzida. Sucessão organizada."},
    ],
    "depo": [
      {"quote": "\"A Amanda identificou R$ 250 mil em créditos de ICMS sobre açúcar que estavam errados. Processo 100% remoto, sem interrupção da nossa operação na usina.\"", "role": "Gestor Fiscal", "empresa": "Polo sucroalcooleiro, SP"},
      {"quote": "\"Nossa metalúrgica nunca tinha aproveitado os créditos de ICMS-ST corretamente. A Amanda encontrou R$ 140 mil de economia anual.\"", "role": "Sócio", "empresa": "Metalúrgica, Piracicaba/SP"},
      {"quote": "\"A holding organizou meu patrimônio rural e reduziu o imposto sobre os arrendamentos. Amanda conhece o agronegócio de verdade.\"", "role": "Proprietário", "empresa": "Produtor rural, Piracicaba/SP"},
    ],
    "faq": [
      {"q": "Como funciona a contabilidade para o polo sucroalcooleiro em Piracicaba?", "a": "Usinas e fornecedores do sucroalcooleiro têm ICMS sobre saída de açúcar e etanol com alíquotas específicas por produto e destino. Além disso, há créditos de PIS/COFINS sobre insumos da produção e regimes específicos de exportação de açúcar. Auditoria retroativa de 5 anos identifica créditos não aproveitados."},
      {"q": "Metalúrgicas e fabricantes de equipamentos de Piracicaba têm tributação especial?", "a": "Sim. Metalurgia e fabricação de máquinas agrícolas operam com ICMS-ST sobre insumos e IPI sobre os produtos fabricados. Exportações de máquinas e equipamentos têm benefícios fiscais específicos que precisam ser corretamente estruturados."},
      {"q": "Qual a diferença de contabilidade para sucroalcooleiro, metalurgia e comércio em Piracicaba?", "a": "Sucroalcooleiro tem ICMS específico sobre açúcar e etanol. Metalurgia tem ICMS-ST e IPI. Comércio pode migrar de regime. Serviços têm ISSQN. A AM Cabral atende todos remotamente."},
      {"q": "Quanto custa o diagnóstico tributário gratuito?", "a": "O diagnóstico é gratuito, dura cerca de 30 minutos e resulta em relatório com créditos recuperáveis e oportunidades. Sem compromisso."},
      {"q": "Posso trocar de contador sem perder documentos ou histórico?", "a": "Sim. Assumimos a transferência de todos os documentos em até 30 dias. O atendimento para Piracicaba é 100% remoto por videoconferência."},
    ],
    "coverage": [
      {"title": "Polo Sucroalcooleiro/Industrial", "items": ["Usinas da região de Piracicaba", "Fornecedores de cana-de-açúcar", "Distrito Industrial I e II", "Fabricantes de equipamentos agrícolas", "Metalurgia e fundição"]},
      {"title": "Eixo Comercial/Universitário", "items": ["Centro (Av. Independência)", "ESALQ/USP e entorno", "Shopping Piracicaba", "Av. Armando Salles de Oliveira", "Bairro Alto"]},
      {"title": "Demais Bairros", "items": ["Monte Líbano", "Castelinho", "Jardim Elite", "São Dimas", "Todo o município"]},
    ],
    "local_intro": 'Piracicaba tem <strong>mais de 25.000 empresas ativas</strong> e um PIB de aproximadamente R$ 25 bilhões. É um dos maiores polos sucroalcooleiros do mundo, com forte presença de metalurgia e equipamentos agrícolas. Informações sobre abertura de empresas na <a href="https://www.jucei.sp.gov.br/" target="_blank" rel="noopener">JUCESP</a>.',
    "local_p1": "Para o polo sucroalcooleiro, a estrutura tributária envolve <strong>ICMS específico sobre açúcar e etanol</strong> e créditos de PIS/COFINS. Para metalurgia, o foco é no <strong>ICMS-ST sobre insumos</strong> e no IPI sobre produtos.",
    "local_p2": "Comércio varejista pode ter redução com migração de regime. Construtoras acessam o <strong>RET</strong> com IRPJ de 1%. A AM Cabral atua com todos esses perfis por atendimento 100% remoto.",
    "local_toggle_text": "Ver mais sobre a economia de Piracicaba",
    "location_h2": "Escritório em Pará de Minas. <em>Atendimento remoto em Piracicaba.</em>",
    "location_atend": "Atendemos empresas de Piracicaba 100% por videoconferência e plataforma digital. Sem necessidade de deslocamento para o cliente.",
    "footer_atend": "100% remoto por videoconferência<br>Segunda a sexta, 8h às 18h",
  },
  {
    "slug": "ribeirao-preto-sp",
    "name": "Ribeirão Preto",
    "name_ac": "Ribeirao Preto",
    "state": "SP",
    "uf": "sp",
    "preposition": "em",
    "foto_file": "ribeirao-preto-cidade.jpg",
    "foto_alt": "Centro de Ribeirão Preto/SP",
    "foto_figcaption": "Ribeirão Preto, capital do agronegócio e polo de saúde do interior paulista.",
    "loader_phrase": "Agronegócio e saúde em Ribeirão Preto exigem contabilidades diferentes",
    "title": "Serviços Contábeis em Ribeirão Preto | AM Cabral Contabilidade",
    "meta_desc": "Escritório de contabilidade em Ribeirão Preto/SP. Polo do agronegócio, saúde e serviços do interior paulista: cada setor com tributação especializada.",
    "og_desc": "Contabilidade especializada para empresas de Ribeirão Preto/SP. Agronegócio, saúde, comércio e serviços. Diagnóstico tributário gratuito.",
    "canonical": "https://amcabralblindagem.com.br/ribeirao-preto-sp/",
    "breadcrumb_name": "Ribeirão Preto",
    "hero_h1": 'Serviços Contábeis em <span style="color:var(--dourado)">Ribeirão Preto</span>: agronegócio, saúde e serviços têm tributação completamente diferente',
    "hero_sub": 'Capital do agronegócio e polo de saúde do interior paulista: cada setor de <a href="https://pt.wikipedia.org/wiki/Ribeir%C3%A3o_Preto" target="_blank" rel="noopener" class="wiki-link">Ribeirão Preto</a> tem tributos específicos que o contador genérico ignora. A AM Cabral entrega contabilidade feita para o seu setor.',
    "wiki_url": "https://pt.wikipedia.org/wiki/Ribeir%C3%A3o_Preto",
    "marquee_city": "Ribeirão Preto, SP",
    "marquee_destaque": "Polo de Saúde Ribeirão Preto",
    "authority_h2": 'Contabilidade especializada por setor para empresas de <a href="https://pt.wikipedia.org/wiki/Ribeir%C3%A3o_Preto" target="_blank" rel="noopener" class="wiki-link">Ribeirão Preto</a>',
    "authority_p1": "Ribeirão Preto é chamada de a California brasileira. É polo do agronegócio, com usinas de cana, trading de grãos e toda a cadeia do campo. É também um dos maiores polos de saúde do Brasil, com hospitais, clínicas e indústria farmacêutica.",
    "authority_p2": "<strong>Agronegócio e usinas têm ICMS específico sobre açúcar, etanol e grãos.</strong> Saúde e clínicas têm ISSQN municipal com alíquotas específicas e tributação de serviços médicos. Comércio atacadista tem regimes específicos de ICMS. Serviços financeiros têm PIS/COFINS diferenciado.",
    "authority_p3": "Um contador genérico não conhece essas especificidades. <strong>A AM Cabral atende Ribeirão Preto remotamente com a mesma profundidade dos nossos clientes presenciais em Pará de Minas.</strong>",
    "stats4": "4 setores com especialização",
    "card1_title": "Contabilidade em Ribeirão Preto",
    "card1_desc": "Contabilidade completa para empresas de Ribeirão Preto: DRE, fluxo de caixa, departamento pessoal e obrigações acessórias. Atendimento remoto com profundidade de quem conhece o polo do agronegócio.",
    "card2_title": "Contador Especializado em Holding em Ribeirão Preto",
    "card2_desc": "Para empresários de Ribeirão Preto que construíram patrimônio ao longo dos anos. A holding separa pessoa física da jurídica, reduz imposto sobre aluguel de 27,5% para 8,4% e organiza a sucessão familiar.",
    "card3_title": "Contador para Fábricas &amp; Indústrias em Ribeirão Preto",
    "card3_desc": "Usinas, indústria farmacêutica e fabricantes de Ribeirão Preto têm tributação específica. ICMS sobre açúcar e etanol, PIS/COFINS monofásico farmacêutico e créditos extemporâneos precisam de especialista.",
    "card4_title": "Trocar de Contador em Ribeirão Preto",
    "card4_desc": "Trocar de contador parece complicado, mas não precisa ser. A AM Cabral faz toda a migração: busca de documentos, transferência de obrigações e diagnóstico de pendências sem interrupção da sua contabilidade.",
    "card3_bullets": ["ICMS sobre açúcar, etanol e grãos", "PIS/COFINS monofásico farmacêutico", "Preparação para reforma tributária 2026"],
    "amanda_h2": "Contadora tributária para empresas de Ribeirão Preto: Amanda Cabral de Oliveira, CRC/MG Ativo",
    "amanda_quote": '"Ribeirão Preto tem setores com tributação completamente distinta. Agronegócio, saúde, comércio e serviços não podem compartilhar o mesmo contador genérico. Cada setor exige especialização diferente, e é exatamente isso que entregamos."',
    "setores": ["Usinas e Sucroalcooleiro", "Trading de Grãos", "Saúde e Clínicas", "Indústria Farmacêutica", "Comércio Atacadista", "Serviços Profissionais", "Holding Patrimonial", "MEI em Crescimento"],
    "cases": [
      {"pill": "Recuperação de Créditos", "title": "Usina sucroalcooleira no interior de SP", "stat": "R$ 320 mil", "label": "recuperados em créditos", "detail": "ICMS sobre saída de açúcar com alíquotas incorretas e créditos de etanol não aproveitados. Auditoria retroativa de 5 anos."},
      {"pill": "Planejamento Tributário", "title": "Clínica médica em Ribeirão Preto", "stat": "R$ 118 mil/ano", "label": "de economia tributária", "detail": "ISSQN e IRPJ corrigidos para o perfil de clínica especializada. Regime tributário ajustado para serviços médicos com mais de um sócio."},
      {"pill": "Holding Patrimonial", "title": "Médico com imóveis em Ribeirão Preto", "stat": "R$ 96 mil/ano", "label": "de redução no IRPF", "detail": "Constituição de holding com imóveis urbanos e rurais. Tributação de aluguel reduzida de 27,5% para 8,4%."},
    ],
    "depo": [
      {"quote": "\"A Amanda identificou R$ 320 mil em créditos de ICMS sobre açúcar que estavam com alíquotas erradas. Processo conduzido 100% remotamente.\"", "role": "Gestor Fiscal", "empresa": "Usina, interior de SP"},
      {"quote": "\"Nossa clínica precisava de um contador que entendesse ISSQN médico e tributação de sociedades de saúde. A Amanda corrigiu e economizamos R$ 118 mil.\"", "role": "Diretor", "empresa": "Clínica médica, Ribeirão Preto"},
      {"quote": "\"A holding com os meus imóveis reduziu o IRPF de 27,5% para 8,4% e ainda organizou a herança. Recomendo para qualquer médico ou empresário da saúde.\"", "role": "Médico", "empresa": "Ribeirão Preto/SP"},
    ],
    "faq": [
      {"q": "Como funciona a contabilidade para usinas e o sucroalcooleiro em Ribeirão Preto?", "a": "Usinas e fornecedores do sucroalcooleiro têm ICMS específico sobre saída de açúcar e etanol, com alíquotas que variam por destino e produto. Créditos de PIS/COFINS sobre insumos e benefícios fiscais de exportação também precisam ser corretamente estruturados."},
      {"q": "Clínicas médicas e hospitais de Ribeirão Preto têm tributação especial?", "a": "Sim. Serviços médicos têm ISSQN municipal com alíquotas de 2% a 5% conforme o tipo de serviço. Sociedades de profissionais de saúde têm ISS fixo por sócio em alguns municípios. O regime entre Simples Nacional, Lucro Presumido e Lucro Real impacta diretamente o IRPJ e CSLL."},
      {"q": "Qual a diferença de contabilidade para agronegócio, saúde e comércio em Ribeirão Preto?", "a": "Agronegócio tem ICMS específico. Saúde tem ISSQN. Comércio atacadista tem regimes de ICMS interestadual. Cada setor exige estratégia diferente. A AM Cabral atende todos remotamente."},
      {"q": "Quanto custa o diagnóstico tributário gratuito?", "a": "O diagnóstico é gratuito, dura 30 minutos por videoconferência e resulta em relatório com créditos recuperáveis e oportunidades. Sem compromisso."},
      {"q": "Posso trocar de contador sem perder documentos ou histórico?", "a": "Sim. Assumimos a transferência de todos os documentos em até 30 dias. O atendimento para Ribeirão Preto é 100% remoto por videoconferência."},
    ],
    "coverage": [
      {"title": "Polo Agroindustrial", "items": ["Usinas da região de Ribeirão Preto", "Trading e cooperativas de grãos", "Indústria farmacêutica (Anel Viário)", "Distribuidoras atacadistas", "Eixo SP-330 e SP-333"]},
      {"title": "Eixo Saúde/Serviços", "items": ["Hospital das Clínicas FMRP-USP", "Av. Costábile Romano", "Bairro Higienópolis", "Shopping Santa Úrsula", "Av. Presidente Vargas"]},
      {"title": "Demais Bairros", "items": ["Jardim Sumaré", "Nova Aliança", "Ribeirânia", "Parque Industrial Lagoinha", "Todo o município"]},
    ],
    "local_intro": 'Ribeirão Preto tem <strong>mais de 50.000 empresas ativas</strong> e um PIB de aproximadamente R$ 45 bilhões. É a capital brasileira do agronegócio moderno e um dos maiores polos de saúde do país. Informações sobre abertura de empresas na <a href="https://www.jucei.sp.gov.br/" target="_blank" rel="noopener">JUCESP</a>.',
    "local_p1": "Para o polo sucroalcooleiro, a estrutura tributária envolve <strong>ICMS específico sobre açúcar e etanol</strong>. Para saúde e clínicas, o foco é no <strong>ISSQN municipal</strong> e na tributação de sociedades de profissionais.",
    "local_p2": "Comércio atacadista tem regimes específicos de ICMS interestadual. Construtoras acessam o <strong>RET</strong> com IRPJ de 1%. A AM Cabral atua com todos esses perfis por atendimento 100% remoto.",
    "local_toggle_text": "Ver mais sobre a economia de Ribeirão Preto",
    "location_h2": "Escritório em Pará de Minas. <em>Atendimento remoto em Ribeirão Preto.</em>",
    "location_atend": "Atendemos empresas de Ribeirão Preto 100% por videoconferência e plataforma digital. Sem necessidade de deslocamento para o cliente.",
    "footer_atend": "100% remoto por videoconferência<br>Segunda a sexta, 8h às 18h",
  },
  {
    "slug": "sorocaba-sp",
    "name": "Sorocaba",
    "name_ac": "Sorocaba",
    "state": "SP",
    "uf": "sp",
    "preposition": "em",
    "foto_file": "sorocaba-cidade.jpg",
    "foto_alt": "Centro de Sorocaba/SP",
    "foto_figcaption": "Sorocaba, polo industrial e logístico do interior paulista.",
    "loader_phrase": "Indústria e logística em Sorocaba exigem contabilidades diferentes",
    "title": "Serviços Contábeis em Sorocaba | AM Cabral Contabilidade",
    "meta_desc": "Escritório de contabilidade em Sorocaba/SP. Polo industrial, logístico e de serviços do interior paulista: cada setor com tributação especializada.",
    "og_desc": "Contabilidade especializada para empresas de Sorocaba/SP. Indústria, logística, comércio e serviços. Diagnóstico tributário gratuito.",
    "canonical": "https://amcabralblindagem.com.br/sorocaba-sp/",
    "breadcrumb_name": "Sorocaba",
    "hero_h1": 'Serviços Contábeis em <span style="color:var(--dourado)">Sorocaba</span>: indústria, logística e serviços têm tributação completamente diferente',
    "hero_sub": 'Polo industrial e logístico do interior de São Paulo: cada setor de <a href="https://pt.wikipedia.org/wiki/Sorocaba" target="_blank" rel="noopener" class="wiki-link">Sorocaba</a> tem tributos específicos que o contador genérico ignora. A AM Cabral entrega contabilidade feita para o seu setor.',
    "wiki_url": "https://pt.wikipedia.org/wiki/Sorocaba",
    "marquee_city": "Sorocaba, SP",
    "marquee_destaque": "Polo Industrial Sorocaba",
    "authority_h2": 'Contabilidade especializada por setor para empresas de <a href="https://pt.wikipedia.org/wiki/Sorocaba" target="_blank" rel="noopener" class="wiki-link">Sorocaba</a>',
    "authority_p1": "Sorocaba é um dos maiores polos industriais do interior de São Paulo. Indústrias têxteis, metalúrgicas, de borracha e equipamentos convivem com um forte setor logístico e comercial. É a Manchester paulista.",
    "authority_p2": "<strong>Têxtil e confecções têm ICMS-ST sobre fios e tecidos e créditos de IPI.</strong> Metalurgia e borracha têm ICMS-ST e IPI específicos. Logística tem ICMS sobre frete. Comércio varejista tem oportunidades de migração de regime.",
    "authority_p3": "Um contador genérico não conhece essas especificidades. <strong>A AM Cabral atende Sorocaba remotamente com a mesma profundidade dos nossos clientes presenciais em Pará de Minas.</strong>",
    "stats4": "4 setores com especialização",
    "card1_title": "Contabilidade em Sorocaba",
    "card1_desc": "Contabilidade completa para empresas de Sorocaba: DRE, fluxo de caixa, departamento pessoal e obrigações acessórias. Atendimento remoto com profundidade de quem conhece a Manchester paulista.",
    "card2_title": "Contador Especializado em Holding em Sorocaba",
    "card2_desc": "Para empresários de Sorocaba que construíram patrimônio ao longo dos anos. A holding separa pessoa física da jurídica, reduz imposto sobre aluguel de 27,5% para 8,4% e organiza a sucessão familiar.",
    "card3_title": "Contador para Fábricas &amp; Indústrias em Sorocaba",
    "card3_desc": "Têxtil, metalurgia e borracha de Sorocaba têm tributação específica. ICMS-ST sobre fios e tecidos, IPI sobre produtos industriais e créditos extemporâneos precisam de especialista.",
    "card4_title": "Trocar de Contador em Sorocaba",
    "card4_desc": "Trocar de contador parece complicado, mas não precisa ser. A AM Cabral faz toda a migração: busca de documentos, transferência de obrigações e diagnóstico de pendências sem interrupção da sua contabilidade.",
    "card3_bullets": ["ICMS-ST para têxtil, metalurgia e borracha", "IPI sobre produtos industriais", "Preparação para reforma tributária 2026"],
    "amanda_h2": "Contadora tributária para empresas de Sorocaba: Amanda Cabral de Oliveira, CRC/MG Ativo",
    "amanda_quote": '"Sorocaba tem setores com tributação completamente distinta. Têxtil, metalurgia, logística e comércio não podem compartilhar o mesmo contador genérico. Cada setor exige especialização diferente, e é exatamente isso que entregamos."',
    "setores": ["Têxtil e Confecções", "Metalurgia e Borracha", "Equipamentos Industriais", "Transportadoras e Logística", "Comércio Varejista", "Construtoras", "Holding Patrimonial", "MEI em Crescimento"],
    "cases": [
      {"pill": "Recuperação de Créditos", "title": "Indústria têxtil no interior de SP", "stat": "R$ 235 mil", "label": "recuperados em créditos", "detail": "ICMS-ST sobre fios e tecidos não aproveitados pelo contador anterior. Auditoria retroativa de 5 anos."},
      {"pill": "Planejamento Tributário", "title": "Metalúrgica em Sorocaba/SP", "stat": "R$ 138 mil/ano", "label": "de economia tributária", "detail": "Créditos de ICMS-ST sobre insumos metálicos e migração para regime de Lucro Presumido. Redução imediata na carga efetiva."},
      {"pill": "Holding Patrimonial", "title": "Empresário do polo industrial", "stat": "R$ 84 mil/ano", "label": "de redução no IRPF", "detail": "Constituição de holding familiar. Tributação de aluguel reduzida de 27,5% para 8,4%. Sucessão organizada."},
    ],
    "depo": [
      {"quote": "\"A Amanda identificou R$ 235 mil em créditos de ICMS-ST que nossa têxtil nunca tinha aproveitado. Processo 100% remoto e sem complicação.\"", "role": "Sócio", "empresa": "Indústria têxtil, Sorocaba/SP"},
      {"quote": "\"Nossa metalúrgica economizou R$ 138 mil com a migração de regime que a Amanda recomendou. O diagnóstico foi gratuito e o retorno foi imediato.\"", "role": "Diretor", "empresa": "Metalúrgica, Sorocaba/SP"},
      {"quote": "\"A holding organizou meu patrimônio e reduziu o imposto sobre os aluguéis. Amanda atende Sorocaba com a mesma qualidade de quem está presencialmente.\"", "role": "Proprietário", "empresa": "Empresário, Sorocaba/SP"},
    ],
    "faq": [
      {"q": "Como funciona a contabilidade para indústrias têxteis em Sorocaba?", "a": "Têxtil e confecções operam com ICMS-ST sobre fios e tecidos e com créditos de IPI sobre insumos industriais. Muitas indústrias em Sorocaba têm créditos não aproveitados nesses tributos. Auditoria retroativa de 5 anos identifica o potencial de recuperação."},
      {"q": "Indústrias de borracha e metalurgia de Sorocaba têm tributação especial?", "a": "Sim. Metalurgia e borracha têm ICMS-ST específico por produto e IPI sobre os bens fabricados. A estrutura de créditos e débitos varia conforme o produto final e o destino. Erros nessa estrutura são comuns e representam créditos não aproveitados."},
      {"q": "Qual a diferença de contabilidade para têxtil, metalurgia e logística em Sorocaba?", "a": "Têxtil tem ICMS-ST sobre fios. Metalurgia tem ICMS-ST e IPI. Logística tem ICMS sobre frete. Comércio pode migrar de regime. A AM Cabral atende todos remotamente."},
      {"q": "Quanto custa o diagnóstico tributário gratuito?", "a": "O diagnóstico é gratuito, dura 30 minutos e resulta em relatório com créditos recuperáveis e oportunidades. Sem compromisso."},
      {"q": "Posso trocar de contador sem perder documentos ou histórico?", "a": "Sim. Assumimos a transferência de todos os documentos em até 30 dias. O atendimento para Sorocaba é 100% remoto por videoconferência."},
    ],
    "coverage": [
      {"title": "Polo Industrial", "items": ["Distrito Industrial de Sorocaba", "Polo Têxtil Av. Dom Aguirre", "Metalurgia e borracha BR-162", "Equipamentos industriais", "Eixo Rodovia Raposo Tavares"]},
      {"title": "Eixo Comercial/Serviços", "items": ["Centro (Largo São Bento)", "Parque Campolim", "Shopping Iguatemi Sorocaba", "Av. Dom Lúcio", "Bairro Jardim Faculdade"]},
      {"title": "Demais Bairros", "items": ["Wanel Ville", "Éden", "Aparecidinha", "Cajuru do Sul", "Todo o município"]},
    ],
    "local_intro": 'Sorocaba tem <strong>mais de 35.000 empresas ativas</strong> e um PIB de aproximadamente R$ 30 bilhões. É um dos maiores polos industriais do interior paulista, com destaque para têxtil, metalurgia, borracha e logística. Informações sobre abertura de empresas na <a href="https://www.jucei.sp.gov.br/" target="_blank" rel="noopener">JUCESP</a>.',
    "local_p1": "Para têxtil e confecções, a estrutura tributária envolve <strong>ICMS-ST sobre fios e tecidos</strong> e créditos de IPI. Para metalurgia e borracha, o foco é no <strong>ICMS-ST e IPI</strong> por produto.",
    "local_p2": "Logística tem ICMS sobre frete. Comércio varejista pode ter redução com migração de regime. A AM Cabral atua com todos esses perfis por atendimento 100% remoto.",
    "local_toggle_text": "Ver mais sobre a economia de Sorocaba",
    "location_h2": "Escritório em Pará de Minas. <em>Atendimento remoto em Sorocaba.</em>",
    "location_atend": "Atendemos empresas de Sorocaba 100% por videoconferência e plataforma digital. Sem necessidade de deslocamento para o cliente.",
    "footer_atend": "100% remoto por videoconferência<br>Segunda a sexta, 8h às 18h",
  },
  {
    "slug": "rio-de-janeiro-rj",
    "name": "Rio de Janeiro",
    "name_ac": "Rio de Janeiro",
    "state": "RJ",
    "uf": "rj",
    "preposition": "no",
    "foto_file": "rio-de-janeiro-cidade.jpg",
    "foto_alt": "Vista do Rio de Janeiro/RJ",
    "foto_figcaption": "Rio de Janeiro, polo de petróleo, turismo e serviços financeiros.",
    "loader_phrase": "Petróleo e turismo no Rio de Janeiro exigem contabilidades diferentes",
    "title": "Serviços Contábeis no Rio de Janeiro | AM Cabral Contabilidade",
    "meta_desc": "Escritório de contabilidade no Rio de Janeiro/RJ. Petróleo e gás, turismo, serviços financeiros: cada setor com tributação especializada. Planejamento tributário e holding.",
    "og_desc": "Contabilidade especializada para empresas do Rio de Janeiro/RJ. Petróleo, turismo, finanças e serviços. Diagnóstico tributário gratuito.",
    "canonical": "https://amcabralblindagem.com.br/rio-de-janeiro-rj/",
    "breadcrumb_name": "Rio de Janeiro",
    "hero_h1": 'Serviços Contábeis <span style="color:var(--dourado)">no Rio de Janeiro</span>: petróleo, turismo e finanças têm tributação completamente diferente',
    "hero_sub": 'Polo de petróleo e gás, turismo e serviços financeiros: cada setor do <a href="https://pt.wikipedia.org/wiki/Rio_de_Janeiro_(cidade)" target="_blank" rel="noopener" class="wiki-link">Rio de Janeiro</a> tem tributos específicos que o contador genérico ignora. A AM Cabral entrega contabilidade feita para o seu setor.',
    "wiki_url": "https://pt.wikipedia.org/wiki/Rio_de_Janeiro_(cidade)",
    "marquee_city": "Rio de Janeiro, RJ",
    "marquee_destaque": "Polo Petróleo e Gás RJ",
    "authority_h2": 'Contabilidade especializada por setor para empresas do <a href="https://pt.wikipedia.org/wiki/Rio_de_Janeiro_(cidade)" target="_blank" rel="noopener" class="wiki-link">Rio de Janeiro</a>',
    "authority_p1": "O Rio de Janeiro concentra o polo de petróleo e gás do Brasil (Petrobras e toda a cadeia de fornecedores), um dos maiores mercados de turismo e hotelaria do mundo e um setor financeiro relevante com bancos, fundos e gestoras.",
    "authority_p2": "<strong>Petróleo e gás têm royalties, participações especiais e ICMS específico sobre combustíveis.</strong> Turismo e hotelaria têm ISSQN municipal com alíquotas específicas. Serviços financeiros têm PIS/COFINS e CSLL diferenciados. Comércio e serviços têm ISSQN municipal do Rio.",
    "authority_p3": "Um contador genérico não conhece essas especificidades. <strong>A AM Cabral atende o Rio de Janeiro remotamente com a mesma profundidade dos nossos clientes presenciais em Pará de Minas.</strong>",
    "stats4": "4 setores com especialização",
    "card1_title": "Contabilidade no Rio de Janeiro",
    "card1_desc": "Contabilidade completa para empresas do Rio de Janeiro: DRE, fluxo de caixa, departamento pessoal e obrigações acessórias. Atendimento remoto com profundidade de quem conhece os setores cariocas.",
    "card2_title": "Contador Especializado em Holding no Rio de Janeiro",
    "card2_desc": "Para empresários do Rio de Janeiro que construíram patrimônio ao longo dos anos. A holding separa pessoa física da jurídica, reduz imposto sobre aluguel de 27,5% para 8,4% e organiza a sucessão familiar.",
    "card3_title": "Contador para Fábricas &amp; Indústrias no Rio de Janeiro",
    "card3_desc": "Petróleo, gás e indústria naval do Rio têm tributação específica. Royalties, participações especiais e ICMS sobre combustíveis precisam de especialista que conheça o setor.",
    "card4_title": "Trocar de Contador no Rio de Janeiro",
    "card4_desc": "Trocar de contador parece complicado, mas não precisa ser. A AM Cabral faz toda a migração: busca de documentos, transferência de obrigações e diagnóstico de pendências sem interrupção da sua contabilidade.",
    "card3_bullets": ["Royalties e participações especiais O&G", "ICMS sobre combustíveis", "Preparação para reforma tributária 2026"],
    "amanda_h2": "Contadora tributária para empresas do Rio de Janeiro: Amanda Cabral de Oliveira, CRC/MG Ativo",
    "amanda_quote": '"O Rio de Janeiro tem setores com tributação completamente distinta. Petróleo, turismo, finanças e serviços não podem compartilhar o mesmo contador genérico. Cada setor exige especialização diferente, e é exatamente isso que entregamos."',
    "setores": ["Petróleo e Gás", "Turismo e Hotelaria", "Serviços Financeiros", "Indústria Naval", "Comércio Varejista", "Serviços Profissionais", "Holding Patrimonial", "MEI em Crescimento"],
    "cases": [
      {"pill": "Recuperação de Créditos", "title": "Fornecedor da cadeia de O&G no RJ", "stat": "R$ 340 mil", "label": "recuperados em créditos", "detail": "ICMS sobre saída de equipamentos para o setor de petróleo com alíquotas incorretas. Auditoria retroativa de 5 anos."},
      {"pill": "Planejamento Tributário", "title": "Hotel boutique no Rio de Janeiro", "stat": "R$ 125 mil/ano", "label": "de economia tributária", "detail": "ISSQN e IRPJ corrigidos para o perfil de hotelaria boutique. Regime tributário ajustado para o mix de serviços."},
      {"pill": "Holding Patrimonial", "title": "Empresário com imóveis no RJ", "stat": "R$ 112 mil/ano", "label": "de redução no IRPF", "detail": "Constituição de holding com imóveis na Zona Sul e Barra. Tributação de aluguel reduzida de 27,5% para 8,4%."},
    ],
    "depo": [
      {"quote": "\"Nossa empresa fornece equipamentos para o setor de petróleo e a Amanda identificou R$ 340 mil em créditos de ICMS que estavam errados. Processo 100% remoto.\"", "role": "Sócio", "empresa": "Fornecedor O&G, Rio de Janeiro"},
      {"quote": "\"A Amanda ajustou o regime tributário do nosso hotel e economizamos R$ 125 mil no ano. Atendimento remoto de altíssima qualidade.\"", "role": "Proprietário", "empresa": "Hotel boutique, Rio de Janeiro/RJ"},
      {"quote": "\"A holding com os imóveis na Zona Sul reduziu meu IRPF e organizou a herança. Amanda conhece o mercado imobiliário do Rio de Janeiro.\"", "role": "Investidor", "empresa": "Rio de Janeiro/RJ"},
    ],
    "faq": [
      {"q": "Como funciona a contabilidade para empresas fornecedoras de petróleo e gás no Rio de Janeiro?", "a": "Fornecedores da cadeia de O&G têm ICMS sobre saída de equipamentos e serviços com alíquotas específicas para o setor. Além disso, há créditos de PIS/COFINS sobre insumos e regimes de importação temporária que precisam ser corretamente estruturados."},
      {"q": "Hotéis e empresas de turismo do Rio de Janeiro têm tributação especial?", "a": "Sim. Hotelaria tem ISSQN municipal com alíquotas de 2% a 5% conforme o tipo de serviço. Pacotes turísticos com hospedagem e serviço têm base de cálculo específica. O regime entre Simples, Presumido e Real impacta diretamente a carga total."},
      {"q": "Qual a diferença de contabilidade para petróleo, turismo e serviços no Rio de Janeiro?", "a": "Petróleo tem royalties e ICMS específico. Turismo tem ISSQN. Serviços financeiros têm PIS/COFINS diferenciado. Comércio pode migrar de regime. A AM Cabral atende todos remotamente."},
      {"q": "Quanto custa o diagnóstico tributário gratuito?", "a": "O diagnóstico é gratuito, dura 30 minutos e resulta em relatório com créditos recuperáveis e oportunidades. Sem compromisso."},
      {"q": "Posso trocar de contador sem perder documentos ou histórico?", "a": "Sim. Assumimos a transferência de todos os documentos em até 30 dias. O atendimento para o Rio de Janeiro é 100% remoto por videoconferência."},
    ],
    "coverage": [
      {"title": "Polo Petróleo/Industrial", "items": ["Petrobras e cadeia O&G", "Ilha do Governador (indústria)", "Santa Cruz e Sepetiba", "Zona Portuária do Rio", "Indústria Naval"]},
      {"title": "Eixo Comercial/Turístico", "items": ["Zona Sul (Ipanema/Leblon)", "Barra da Tijuca", "Centro Financeiro", "Botafogo e Flamengo", "Rua do Ouvidor"]},
      {"title": "Demais Regiões", "items": ["Zona Norte", "Méier e subúrbios", "Jacarepaguá", "Campo Grande", "Todo o município"]},
    ],
    "local_intro": 'O Rio de Janeiro tem <strong>mais de 120.000 empresas ativas</strong> e um PIB de aproximadamente R$ 350 bilhões. É o polo de petróleo e gás do Brasil, com forte presença de turismo, serviços financeiros e indústria. Informações sobre abertura de empresas na <a href="https://www.jucerja.rj.gov.br/" target="_blank" rel="noopener">JUCERJA</a>.',
    "local_p1": "Para fornecedores de petróleo e gás, a estrutura tributária envolve <strong>ICMS sobre equipamentos e serviços O&G</strong> e créditos de PIS/COFINS. Para turismo e hotelaria, o foco é no <strong>ISSQN municipal</strong> e na estrutura de pacotes.",
    "local_p2": "Serviços financeiros têm PIS/COFINS e CSLL diferenciados. Construtoras acessam o <strong>RET</strong> com IRPJ de 1%. A AM Cabral atua com todos esses perfis por atendimento 100% remoto.",
    "local_toggle_text": "Ver mais sobre a economia do Rio de Janeiro",
    "location_h2": "Escritório em Pará de Minas. <em>Atendimento remoto no Rio de Janeiro.</em>",
    "location_atend": "Atendemos empresas do Rio de Janeiro 100% por videoconferência e plataforma digital. Sem necessidade de deslocamento para o cliente.",
    "footer_atend": "100% remoto por videoconferência<br>Segunda a sexta, 8h às 18h",
  },
  {
    "slug": "goiania-go",
    "name": "Goiânia",
    "name_ac": "Goiania",
    "state": "GO",
    "uf": "go",
    "preposition": "em",
    "foto_file": "goiania-cidade.jpg",
    "foto_alt": "Centro de Goiânia/GO",
    "foto_figcaption": "Goiânia, polo do agronegócio, saúde e serviços do Centro-Oeste.",
    "loader_phrase": "Agronegócio e saúde em Goiânia exigem contabilidades diferentes",
    "title": "Serviços Contábeis em Goiânia | AM Cabral Contabilidade",
    "meta_desc": "Escritório de contabilidade em Goiânia/GO. Polo do agronegócio, saúde e serviços do Centro-Oeste: cada setor com tributação especializada.",
    "og_desc": "Contabilidade especializada para empresas de Goiânia/GO. Agronegócio, saúde, comércio e serviços. Diagnóstico tributário gratuito.",
    "canonical": "https://amcabralblindagem.com.br/goiania-go/",
    "breadcrumb_name": "Goiânia",
    "hero_h1": 'Serviços Contábeis em <span style="color:var(--dourado)">Goiânia</span>: agronegócio, saúde e comércio têm tributação completamente diferente',
    "hero_sub": 'Polo do agronegócio, saúde e serviços do Centro-Oeste: cada setor de <a href="https://pt.wikipedia.org/wiki/Goi%C3%A2nia" target="_blank" rel="noopener" class="wiki-link">Goiânia</a> tem tributos específicos que o contador genérico ignora. A AM Cabral entrega contabilidade feita para o seu setor.',
    "wiki_url": "https://pt.wikipedia.org/wiki/Goi%C3%A2nia",
    "marquee_city": "Goiânia, GO",
    "marquee_destaque": "Centro-Oeste Agronegócio",
    "authority_h2": 'Contabilidade especializada por setor para empresas de <a href="https://pt.wikipedia.org/wiki/Goi%C3%A2nia" target="_blank" rel="noopener" class="wiki-link">Goiânia</a>',
    "authority_p1": "Goiânia é a capital do agronegócio do Centro-Oeste, com frigoríficos, tradings de grãos e toda a cadeia do campo. É também um dos maiores polos de saúde do Brasil, com hospitais, clínicas e indústria farmacêutica. Comércio atacadista regional e serviços completam o perfil da cidade.",
    "authority_p2": "<strong>Frigoríficos e agroindústria têm PIS/COFINS monofásico e ICMS específico sobre proteína animal.</strong> Saúde e clínicas têm ISSQN municipal com alíquotas específicas. Comércio atacadista tem regimes de ICMS para distribuição regional. Construtoras acessam RET com IRPJ de 1%.",
    "authority_p3": "Um contador genérico não conhece essas especificidades. <strong>A AM Cabral atende Goiânia remotamente com a mesma profundidade dos nossos clientes presenciais em Pará de Minas.</strong>",
    "stats4": "4 setores com especialização",
    "card1_title": "Contabilidade em Goiânia",
    "card1_desc": "Contabilidade completa para empresas de Goiânia: DRE, fluxo de caixa, departamento pessoal e obrigações acessórias. Atendimento remoto com profundidade de quem conhece o polo do Centro-Oeste.",
    "card2_title": "Contador Especializado em Holding em Goiânia",
    "card2_desc": "Para empresários de Goiânia que construíram patrimônio ao longo dos anos. A holding separa pessoa física da jurídica, reduz imposto sobre aluguel de 27,5% para 8,4% e organiza a sucessão familiar.",
    "card3_title": "Contador para Fábricas &amp; Indústrias em Goiânia",
    "card3_desc": "Frigoríficos, indústria farmacêutica e agroindústria de Goiânia têm tributação específica. PIS/COFINS monofásico, ICMS do agro e créditos extemporâneos precisam de especialista.",
    "card4_title": "Trocar de Contador em Goiânia",
    "card4_desc": "Trocar de contador parece complicado, mas não precisa ser. A AM Cabral faz toda a migração: busca de documentos, transferência de obrigações e diagnóstico de pendências sem interrupção da sua contabilidade.",
    "card3_bullets": ["PIS/COFINS monofásico para frigoríficos", "ICMS específico do agronegócio GO", "Preparação para reforma tributária 2026"],
    "amanda_h2": "Contadora tributária para empresas de Goiânia: Amanda Cabral de Oliveira, CRC/MG Ativo",
    "amanda_quote": '"Goiânia tem setores com tributação completamente distinta. Frigoríficos, saúde, comércio e serviços não podem compartilhar o mesmo contador genérico. Cada setor exige especialização diferente, e é exatamente isso que entregamos."',
    "setores": ["Frigoríficos e Agroindústria", "Trading de Grãos", "Saúde e Clínicas", "Comércio Atacadista", "Serviços Profissionais", "Construtoras", "Holding Patrimonial", "MEI em Crescimento"],
    "cases": [
      {"pill": "Recuperação de Créditos", "title": "Frigorífico no Centro-Oeste", "stat": "R$ 295 mil", "label": "recuperados em créditos", "detail": "PIS/COFINS monofásico sobre proteína animal não aproveitados pelo contador anterior. Auditoria retroativa de 5 anos."},
      {"pill": "Planejamento Tributário", "title": "Clínica de especialidades em Goiânia", "stat": "R$ 122 mil/ano", "label": "de economia tributária", "detail": "ISSQN e IRPJ corrigidos para o perfil de clínica com múltiplos sócios. Regime tributário ajustado para serviços médicos."},
      {"pill": "Holding Patrimonial", "title": "Empresário do agronegócio em GO", "stat": "R$ 108 mil/ano", "label": "de redução no IRPF", "detail": "Constituição de holding rural e familiar. Tributação de aluguel e arrendamento reduzida. Sucessão organizada."},
    ],
    "depo": [
      {"quote": "\"A Amanda encontrou R$ 295 mil em créditos de PIS/COFINS que nosso frigorífico nunca tinha aproveitado. Processo 100% remoto e eficiente.\"", "role": "Sócio", "empresa": "Frigorífico, Centro-Oeste"},
      {"quote": "\"Nossa clínica precisava de um contador que entendesse ISSQN médico em Goiânia. A Amanda corrigiu e economizamos R$ 122 mil por ano.\"", "role": "Diretor Médico", "empresa": "Clínica, Goiânia/GO"},
      {"quote": "\"A holding rural organizou meu patrimônio e reduziu o imposto sobre os arrendamentos. Amanda conhece o agronegócio goiano de verdade.\"", "role": "Produtor Rural", "empresa": "Goiânia/GO"},
    ],
    "faq": [
      {"q": "Como funciona a contabilidade para frigoríficos e agroindústria em Goiânia?", "a": "Frigoríficos e processamento de proteína animal têm PIS/COFINS monofásico e créditos específicos de ICMS na cadeia de proteína. O ICMS de Goiás tem alíquotas específicas para saída de proteína animal. Auditoria retroativa de 5 anos mapeia os créditos não aproveitados."},
      {"q": "Clínicas médicas de Goiânia têm tributação especial?", "a": "Sim. Serviços médicos têm ISSQN municipal com alíquotas específicas em Goiânia. Sociedades de profissionais de saúde podem ter ISS fixo por sócio. O regime entre Simples, Presumido e Real impacta diretamente o IRPJ e a CSLL."},
      {"q": "Qual a diferença de contabilidade para agronegócio, saúde e comércio em Goiânia?", "a": "Agronegócio tem PIS/COFINS monofásico e ICMS específico. Saúde tem ISSQN municipal. Comércio atacadista tem regimes de ICMS interestadual. A AM Cabral atende todos remotamente."},
      {"q": "Quanto custa o diagnóstico tributário gratuito?", "a": "O diagnóstico é gratuito, dura 30 minutos e resulta em relatório com créditos recuperáveis e oportunidades. Sem compromisso."},
      {"q": "Posso trocar de contador sem perder documentos ou histórico?", "a": "Sim. Assumimos a transferência de todos os documentos em até 30 dias. O atendimento para Goiânia é 100% remoto por videoconferência."},
    ],
    "coverage": [
      {"title": "Polo Agroindustrial", "items": ["Frigoríficos e abatedouros", "Trading e cooperativas de grãos", "Indústria farmacêutica", "Eixo BR-060 e BR-153", "Distribuidoras regionais"]},
      {"title": "Eixo Comercial/Saúde", "items": ["Setor Bueno (clínicas)", "Setor Oeste (hospitais)", "Av. T-63 e T-7", "Flamboyant e entorno", "Bairro Jardim Goiás"]},
      {"title": "Demais Regiões", "items": ["Aparecida de Goiânia", "Trindade", "Nerópolis", "Senador Canedo", "Todo o município"]},
    ],
    "local_intro": 'Goiânia tem <strong>mais de 80.000 empresas ativas</strong> e um PIB de aproximadamente R$ 80 bilhões. É o polo do agronegócio do Centro-Oeste, com forte presença de frigoríficos, saúde e comércio atacadista. Informações sobre abertura de empresas na <a href="https://www.juceg.go.gov.br/" target="_blank" rel="noopener">JUCEG</a>.',
    "local_p1": "Para frigoríficos e agroindústria, a estrutura tributária envolve <strong>PIS/COFINS monofásico</strong> e ICMS específico de Goiás sobre proteína animal. Para saúde e clínicas, o foco é no <strong>ISSQN municipal</strong> e na tributação de sociedades de profissionais.",
    "local_p2": "Comércio atacadista tem regimes de ICMS interestadual para distribuição regional do Centro-Oeste. Construtoras acessam o <strong>RET</strong> com IRPJ de 1%. A AM Cabral atua com todos esses perfis por atendimento 100% remoto.",
    "local_toggle_text": "Ver mais sobre a economia de Goiânia",
    "location_h2": "Escritório em Pará de Minas. <em>Atendimento remoto em Goiânia.</em>",
    "location_atend": "Atendemos empresas de Goiânia 100% por videoconferência e plataforma digital. Sem necessidade de deslocamento para o cliente.",
    "footer_atend": "100% remoto por videoconferência<br>Segunda a sexta, 8h às 18h",
  },
]

def build_cases_html(cases):
    html = ""
    for i, c in enumerate(cases, 1):
        html += f"""
      <div class="case-card reveal d{i}">
        <div class="case-pill">{c['pill']}</div>
        <div class="case-title">{c['title']}</div>
        <div class="case-stat">{c['stat']}</div>
        <div class="case-stat-label">{c['label']}</div>
        <p class="case-detail">{c['detail']}</p>
      </div>"""
    return html

def build_depo_html(depos):
    html = ""
    for i, d in enumerate(depos, 1):
        html += f"""
      <div class="depo-card reveal d{i}">
        <div class="depo-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <blockquote class="depo-quote">
          <p>{d['quote']}</p>
          <footer><cite><span class="depo-role">{d['role']}</span> &mdash; {d['empresa']}</cite></footer>
        </blockquote>
      </div>"""
    return html

def build_faq_html(faqs):
    html = ""
    for f in faqs:
        html += f"""
      <div class="faq-item">
        <h3 class="faq-q" role="button" tabindex="0" aria-expanded="false">
          {f['q']}
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14"/><path d="M5 12h14"/></svg>
        </h3>
        <div class="faq-a"><p>{f['a']}</p></div>
      </div>"""
    return html

def build_coverage_html(coverage):
    html = ""
    for col in coverage:
        items_html = "".join(f"<li>{it}</li>" for it in col['items'])
        html += f"""
      <div class="coverage-col">
        <h3>{col['title']}</h3>
        <ul>{items_html}</ul>
      </div>"""
    return html

def build_setores_html(setores):
    items = "".join(f'<span class="setores-item">{s}</span><span class="setores-sep">&middot;</span>' for s in setores)
    return items + items  # duplicate for seamless loop

def build_html(c):
    html = TPL

    # Meta / title
    html = html.replace("Serviços Contábeis em Sete Lagoas | AM Cabral Contabilidade", c['title'])
    html = html.replace(
        "Escritório de contabilidade em Sete Lagoas/MG. Cada setor paga imposto diferente: siderurgia, farmacêutico, comércio, construção. Planejamento tributário, recuperação de créditos, holding patrimonial.",
        c['meta_desc']
    )
    html = html.replace(
        "Contabilidade especializada por setor em Sete Lagoas/MG. Siderurgia, farmacêutico, comércio, construção civil e MEI. Diagnóstico tributário gratuito.",
        c['og_desc']
    )
    html = html.replace("https://amcabralblindagem.com.br/sete-lagoas-mg/", c['canonical'], 4)
    html = html.replace("Serviços Contábeis em Sete Lagoas | AM Cabral Contabilidade", c['title'])

    # Schema breadcrumb
    html = html.replace(
        '{ "@type": "ListItem", "position": 3, "name": "Sete Lagoas", "item": "https://amcabralblindagem.com.br/sete-lagoas-mg/" }',
        f'{{ "@type": "ListItem", "position": 3, "name": "{c["breadcrumb_name"]}", "item": "{c["canonical"]}" }}'
    )
    html = html.replace(
        '"name": "Serviços Contábeis em Sete Lagoas | AM Cabral Contabilidade"',
        f'"name": "{c["title"]}"'
    )
    html = html.replace(
        '"description": "Contabilidade especializada por setor em Sete Lagoas/MG: siderurgia, farmacêutico, comércio, construção civil e MEI para ME."',
        f'"description": "{c["meta_desc"]}"'
    )

    # Loader phrase
    html = html.replace(
        "Cada setor paga imposto diferente merece contabilidade diferente",
        c['loader_phrase']
    )
    # Also update the toggle text that references sete lagoas
    html = html.replace(
        "localToggle.childNodes[0].textContent = open\n      ? 'Ver menos '\n      : 'Ver mais sobre a economia de Sete Lagoas ';",
        f"localToggle.childNodes[0].textContent = open\n      ? 'Ver menos '\n      : '{c['local_toggle_text']} ';"
    )

    # Hero
    html = html.replace(
        'Serviços Contábeis em <span style="color:var(--dourado)">Sete Lagoas</span>: cada setor paga imposto diferente',
        c['hero_h1']
    )
    html = html.replace(
        'Siderurgia, farmácia, comércio, construtoras e MEI em crescimento: cada um tem tributos próprios e créditos que o contador genérico ignora. Em <a href="https://pt.wikipedia.org/wiki/Sete_Lagoas" target="_blank" rel="noopener" class="wiki-link">Sete Lagoas</a>, a AM Cabral entrega contabilidade feita para o seu setor. Diagnóstico tributário gratuito.',
        c['hero_sub']
    )

    # Image paths
    img_slug = c['foto_file']
    img_slug_webp = img_slug.replace('.jpg', '.webp').replace('.jpeg', '.webp')
    html = html.replace('srcset="sete-lagoas-lagoa-paulino.webp"', f'srcset="{img_slug_webp}"')
    html = html.replace('src="sete-lagoas-lagoa-paulino.jpg"', f'src="{img_slug}"')
    html = html.replace(
        'alt="Gruta Rei do Mato, Sete Lagoas/MG — AM Cabral Contabilidade atende empresas na cidade"',
        f'alt="{c["foto_alt"]} — AM Cabral Contabilidade atende empresas na cidade"'
    )
    html = html.replace(
        'alt="Gruta Rei do Mato, Sete Lagoas/MG"',
        f'alt="{c["foto_alt"]}"'
    )
    html = html.replace(
        'Gruta Rei do Mato, Sete Lagoas. Cidade com polo siderúrgico, farmácia e comércio ativo.',
        c['foto_figcaption']
    )

    # Marquee credentials (template has encoded entities)
    html = html.replace("Polo Sider&#250;rgico Sete Lagoas", c['marquee_destaque'])
    html = html.replace("Sete Lagoas, MG", c['marquee_city'])

    # Breadcrumb nav
    html = html.replace(
        '<li aria-current="page">Sete Lagoas</li>',
        f'<li aria-current="page">{c["breadcrumb_name"]}</li>'
    )

    # Authority section
    html = html.replace(
        'Contabilidade especializada por setor para empresas de <a href="https://pt.wikipedia.org/wiki/Sete_Lagoas" target="_blank" rel="noopener" class="wiki-link">Sete Lagoas</a>',
        c['authority_h2']
    )
    html = html.replace(
        "Sete Lagoas n&#227;o &#233; uma cidade com um &#250;nico perfil empresarial. &#201; um polo sider&#250;rgico com ferro-gusa e fundi&#231;&#227;o. &#201; um hub farmac&#234;utico com distribuidoras e ind&#250;strias. &#201; um centro comercial com varejistas de todos os portes. &#201; uma cidade de construtoras e de profissionais liberais.",
        c['authority_p1']
    )
    html = html.replace(
        "Cada um desses setores tem uma estrutura tribut&#225;ria diferente. <strong>Siderurgia opera com ICMS-ST sobre sucata e IPI sobre produtos fundidos.</strong> Farm&#225;cia trabalha com PIS/COFINS monof&#225;sico e cr&#233;ditos extemporâneos. Com&#233;rcio varejista tem oportunidades de migra&#231;&#227;o de regime que reduzem carga em at&#233; 8 pontos percentuais. Construtoras acessam RET com IRPJ de 1%.",
        c['authority_p2']
    )
    html = html.replace(
        "Um contador gen&#233;rico n&#227;o conhece essas especificidades. <strong>A AM Cabral foi constitu&#237;da justamente para empresas que precisam de mais do que declara&#231;&#227;o em dia.</strong> Atendemos Sete Lagoas remotamente com a mesma profundidade que os nossos clientes presenciais em Par&#225; de Minas.",
        c['authority_p3']
    )

    # Numbers 4th stat
    html = html.replace(
        '<div class="numbers-val">5</div>\n        <div class="numbers-label">setores com especialização</div>',
        f'<div class="numbers-val">4</div>\n        <div class="numbers-label">{c["stats4"]}</div>'
    )

    # Services hub heading
    html = html.replace(
        '<div class="sec-label lt" style="text-align:center;">Serviços Contábeis em Sete Lagoas</div>',
        f'<div class="sec-label lt" style="text-align:center;">Serviços Contábeis {c["preposition"]} {c["name"]}</div>'
    )
    html = html.replace(
        '<h2 class="sec-h lt" style="text-align:center;margin-bottom:0;">Contabilidade especializada para empresas de Sete Lagoas</h2>',
        f'<h2 class="sec-h lt" style="text-align:center;margin-bottom:0;">Contabilidade especializada para empresas {c["preposition"]} {c["name"]}</h2>'
    )
    html = html.replace(
        '<p class="services-hub-sub">Quatro áreas de atuação, todas adaptadas ao perfil tributário de Sete Lagoas: siderurgia e fundição, distribuição farmacêutica, comércio varejista e construtoras.</p>',
        f'<p class="services-hub-sub">Quatro áreas de atuação, adaptadas ao perfil tributário {c["preposition"]} {c["name"]}.</p>'
    )

    # Cards
    html = html.replace("Contabilidade em Sete Lagoas</h3>", f'{c["card1_title"]}</h3>')
    html = html.replace(
        "Contabilidade completa para empresas de Sete Lagoas: DRE, fluxo de caixa, departamento pessoal e obriga&#231;&#245;es acess&#243;rias. Atendimento remoto com profundidade de quem conhece os setores da cidade.",
        c['card1_desc']
    )
    html = html.replace("Contador Especializado em Holding em Sete Lagoas</h3>", f'{c["card2_title"]}</h3>')
    html = html.replace(
        "Para empres&#225;rios de Sete Lagoas que constru&#237;ram patrim&#244;nio ao longo dos anos. A holding separa pessoa f&#237;sica da jur&#237;dica, reduz imposto sobre aluguel de 27,5% para 8,4% e organiza a sucess&#227;o familiar.",
        c['card2_desc']
    )
    html = html.replace("Contador para F&#225;bricas &amp; Ind&#250;strias em Sete Lagoas</h3>", f'{c["card3_title"]}</h3>')
    html = html.replace(
        "Siderurgia paga ICMS-ST diferente de com&#233;rcio varejista. Farm&#225;cia tem PIS/COFINS monof&#225;sico. Ind&#250;strias de Sete Lagoas precisam de contador que conhe&#231;a o setor, n&#227;o de um gen&#233;rico que aplica a mesma f&#243;rmula para todos.",
        c['card3_desc']
    )
    # card3 bullets
    b = c['card3_bullets']
    html = html.replace(
        "<li>ICMS-ST, IPI e PIS/COFINS por atividade industrial</li>\n          <li>Recupera&#231;&#227;o de cr&#233;ditos extemporâneos</li>\n          <li>Prepara&#231;&#227;o para reforma tribut&#225;ria 2026</li>",
        f"<li>{b[0]}</li>\n          <li>{b[1]}</li>\n          <li>{b[2]}</li>"
    )
    html = html.replace("Trocar de Contador em Sete Lagoas</h3>", f'{c["card4_title"]}</h3>')
    html = html.replace(
        "Trocar de contador parece complicado, mas n&#227;o precisa ser. A AM Cabral faz toda a migra&#231;&#227;o: busca de documentos, transfer&#234;ncia de obriga&#231;&#245;es e diagn&#243;stico de pend&#234;ncias sem interrup&#231;&#227;o da sua contabilidade.",
        c['card4_desc']
    )

    # Amanda CTA
    html = html.replace(
        "Contadora tribut&#225;ria para empresas de Sete Lagoas: Amanda Cabral de Oliveira, CRC/MG Ativo",
        c['amanda_h2']
    )
    html = html.replace(
        '"Sete Lagoas tem setores com tributação completamente distinta. Siderurgia, farmácia, comércio e construção civil não podem compartilhar o mesmo contador genérico. Cada setor exige especialização diferente, e é exatamente isso que entregamos."',
        c['amanda_quote']
    )
    html = html.replace(
        'alt="Amanda Cabral de Oliveira, CRC/MG Ativo, contadora especialista em tributação para empresas de Sete Lagoas"',
        f'alt="Amanda Cabral de Oliveira, CRC/MG Ativo, contadora especialista em tributação para empresas {c["preposition"]} {c["name"]}"'
    )

    # Setores marquee
    old_setores_track = """    <span class="setores-item">Siderurgia e Fundição</span><span class="setores-sep">&middot;</span>
    <span class="setores-item">Distribuição Farmacêutica</span><span class="setores-sep">&middot;</span>
    <span class="setores-item">Comércio Varejista</span><span class="setores-sep">&middot;</span>
    <span class="setores-item">Construtoras e Incorporadoras</span><span class="setores-sep">&middot;</span>
    <span class="setores-item">Indústria de Laticínios</span><span class="setores-sep">&middot;</span>
    <span class="setores-item">Clínicas e Consultórios</span><span class="setores-sep">&middot;</span>
    <span class="setores-item">Serviços Profissionais</span><span class="setores-sep">&middot;</span>
    <span class="setores-item">Holding Patrimonial</span><span class="setores-sep">&middot;</span>
    <span class="setores-item">MEI em Crescimento</span><span class="setores-sep">&middot;</span>
    <!-- duplicate for seamless loop -->
    <span class="setores-item">Siderurgia e Fundição</span><span class="setores-sep">&middot;</span>
    <span class="setores-item">Distribuição Farmacêutica</span><span class="setores-sep">&middot;</span>
    <span class="setores-item">Comércio Varejista</span><span class="setores-sep">&middot;</span>
    <span class="setores-item">Construtoras e Incorporadoras</span><span class="setores-sep">&middot;</span>
    <span class="setores-item">Indústria de Laticínios</span><span class="setores-sep">&middot;</span>
    <span class="setores-item">Clínicas e Consultórios</span><span class="setores-sep">&middot;</span>
    <span class="setores-item">Serviços Profissionais</span><span class="setores-sep">&middot;</span>
    <span class="setores-item">Holding Patrimonial</span><span class="setores-sep">&middot;</span>
    <span class="setores-item">MEI em Crescimento</span><span class="setores-sep">&middot;</span>"""
    new_setores_track = "    " + build_setores_html(c['setores'])
    html = html.replace(old_setores_track, new_setores_track)

    # Setores h2
    html = html.replace(
        "Setores atendidos pelo escrit&#243;rio de contabilidade em Sete Lagoas",
        f"Setores atendidos pelo escritório de contabilidade {c['preposition']} {c['name']}"
    )

    # Cases section
    old_cases_head = """    <div class="sec-label lt reveal" style="text-align:center;">Resultados Reais</div>
    <h2 class="sec-h lt reveal" style="text-align:center;margin-bottom:0;">Resultados para empresas do perfil de Sete Lagoas</h2>
    <div class="cases-grid">
      <div class="case-card reveal d1">
        <div class="case-pill">Recuperação de Créditos</div>
        <div class="case-title">Empresa siderúrgica com operações em MG</div>
        <div class="case-stat">R$ 280 mil</div>
        <div class="case-stat-label">recuperados em créditos</div>
        <p class="case-detail">ICMS-ST sobre sucata e ferro-gusa não aproveitados pelo contador anterior. Auditoria retroativa de 5 anos. Cliente desde 2021. Processo via compensação, sem litígio.</p>
      </div>
      <div class="case-card reveal d2">
        <div class="case-pill">Planejamento Tributário</div>
        <div class="case-title">Indústria de laticínios em Minas Gerais</div>
        <div class="case-stat">R$ 165 mil/ano</div>
        <div class="case-stat-label">de economia tributária</div>
        <p class="case-detail">PIS/COFINS monofásico sobre insumos não estava sendo aproveitado corretamente. Correção do regime com redução recorrente na carga efetiva. Parceria desde 2020.</p>
      </div>
      <div class="case-card reveal d3">
        <div class="case-pill">Regime de Estimativa</div>
        <div class="case-title">Comércio varejista com múltiplas filiais</div>
        <div class="case-stat">R$ 98 mil/ano</div>
        <div class="case-stat-label">de redução tributária</div>
        <p class="case-detail">Migração do Simples Nacional para Lucro Presumido. Regime de estimativa corrigido para o perfil de faturamento da empresa. Cliente desde 2022. Redução imediata na carga efetiva.</p>
      </div>
    </div>"""
    new_cases_head = f"""    <div class="sec-label lt reveal" style="text-align:center;">Resultados Reais</div>
    <h2 class="sec-h lt reveal" style="text-align:center;margin-bottom:0;">Resultados para empresas do perfil {c['preposition']} {c['name']}</h2>
    <div class="cases-grid">{build_cases_html(c['cases'])}
    </div>"""
    html = html.replace(old_cases_head, new_cases_head)

    # Depoimentos
    old_depo_head = """    <div class="sec-label on-lt reveal" style="text-align:center;">Depoimentos</div>
    <h2 class="sec-h on-lt reveal" style="text-align:center;margin-bottom:0;">O que dizem empresários do setor industrial</h2>
    <div class="depoimentos-grid">
      <div class="depo-card reveal d1">
        <div class="depo-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <blockquote class="depo-quote">
          <p>&#8220;A Amanda identificou R$ 280 mil em crédito de ICMS-ST que meu contador anterior nunca tinha mencionado. O processo foi completamente legal e a Amanda conduziu tudo sem precisar da minha intervenção no dia a dia.&#8221;</p>
          <footer><cite><span class="depo-role">Sócio</span> &mdash; Empresa siderúrgica, Minas Gerais</cite></footer>
        </blockquote>
      </div>
      <div class="depo-card reveal d2">
        <div class="depo-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <blockquote class="depo-quote">
          <p>&#8220;Trabalhamos com PIS/COFINS monofásico e nenhum contador nosso tinha aproveitado os créditos corretamente. A AM Cabral encontrou R$ 165 mil por ano de economia que estávamos deixando na mesa.&#8221;</p>
          <footer><cite><span class="depo-role">Proprietário</span> &mdash; Indústria de laticínios, MG</cite></footer>
        </blockquote>
      </div>
      <div class="depo-card reveal d3">
        <div class="depo-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <blockquote class="depo-quote">
          <p>&#8220;A migração do Simples para o Lucro Presumido foi a decisão certa. A Amanda fez o diagnóstico gratuito, mostrou o número exato antes de eu decidir, e a economia de R$ 98 mil anuais já pagou o investimento várias vezes.&#8221;</p>
          <footer><cite><span class="depo-role">Diretora</span> &mdash; Comércio varejista, Minas Gerais</cite></footer>
        </blockquote>
      </div>
    </div>"""
    new_depo_head = f"""    <div class="sec-label on-lt reveal" style="text-align:center;">Depoimentos</div>
    <h2 class="sec-h on-lt reveal" style="text-align:center;margin-bottom:0;">O que dizem empresários {c['preposition']} {c['name']}</h2>
    <div class="depoimentos-grid">{build_depo_html(c['depo'])}
    </div>"""
    html = html.replace(old_depo_head, new_depo_head)

    # FAQ heading
    html = html.replace(
        "Perguntas frequentes sobre contabilidade em Sete Lagoas",
        f"Perguntas frequentes sobre contabilidade {c['preposition']} {c['name']}"
    )
    # FAQ items — replace the whole list
    old_faq_list = """      <div class="faq-item">
        <h3 class="faq-q" role="button" tabindex="0" aria-expanded="false">
          Como funciona a contabilidade para indústrias siderúrgicas em Sete Lagoas?
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14"/><path d="M5 12h14"/></svg>
        </h3>
        <div class="faq-a"><p>Siderurgia e fundição operam com ICMS-ST sobre sucata e ferro-gusa e com créditos de IPI sobre insumos industriais. A maioria das indústrias em Sete Lagoas tem créditos não aproveitados nesses tributos. Fazemos auditoria retroativa de 5 anos e identificamos o que pode ser compensado ou restituído. O processo é completamente legal e não interrompe a operação.</p></div>
      </div>
      <div class="faq-item">
        <h3 class="faq-q" role="button" tabindex="0" aria-expanded="false">
          Empresas farmacêuticas de Sete Lagoas têm regime tributário especial?
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14"/><path d="M5 12h14"/></svg>
        </h3>
        <div class="faq-a"><p>Sim. Distribuidoras e indústrias farmacêuticas em Sete Lagoas operam com substituição tributária de ICMS e PIS/COFINS monofásico, o que cria oportunidades específicas de crédito extemporâneo. O diagnóstico tributário identifica o regime correto e os créditos recuperáveis para cada empresa do setor.</p></div>
      </div>
      <div class="faq-item">
        <h3 class="faq-q" role="button" tabindex="0" aria-expanded="false">
          Qual a diferença de contabilidade para comércio, indústria e serviços em Sete Lagoas?
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14"/><path d="M5 12h14"/></svg>
        </h3>
        <div class="faq-a"><p>Cada setor tem obrigações e oportunidades distintas. Indústrias siderúrgicas e farmacêuticas lidam com ICMS-ST e IPI. Comércio varejista pode migrar do Simples Nacional para o Lucro Presumido e reduzir carga. Construtoras têm RET com IRPJ de 1% e ISS variável. Profissionais de saúde e serviços têm ISSQN próprio. A AM Cabral atende todos esses perfis em Sete Lagoas.</p></div>
      </div>
      <div class="faq-item">
        <h3 class="faq-q" role="button" tabindex="0" aria-expanded="false">
          Quanto custa o diagnóstico tributário gratuito?
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14"/><path d="M5 12h14"/></svg>
        </h3>
        <div class="faq-a"><p>O diagnóstico é gratuito e dura cerca de 30 minutos por videoconferência. Ao final, você recebe um relatório com o que encontramos: créditos que podem ser recuperados, riscos fiscais identificados e oportunidades de redução de carga. Sem compromisso de contratação.</p></div>
      </div>
      <div class="faq-item">
        <h3 class="faq-q" role="button" tabindex="0" aria-expanded="false">
          Construtoras de Sete Lagoas têm regime especial de tributação?
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14"/><path d="M5 12h14"/></svg>
        </h3>
        <div class="faq-a"><p>Sim. Construtoras e incorporadoras podem optar pelo RET (Regime Especial de Tributação) com IRPJ de 1% sobre as receitas mensais das incorporações. Esse regime é vantajoso para empreendimentos enquadrados no Minha Casa Minha Vida e para incorporações de médio e alto padrão. O ISS em Sete Lagoas também tem alíquotas específicas por tipo de obra que precisam ser verificadas caso a caso.</p></div>
      </div>
      <div class="faq-item">
        <h3 class="faq-q" role="button" tabindex="0" aria-expanded="false">
          Como a reforma tributária impacta empresas de Sete Lagoas?
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14"/><path d="M5 12h14"/></svg>
        </h3>
        <div class="faq-a"><p>A transição para IBS e CBS impacta setores de forma diferente. Indústrias siderúrgicas perdem parte do ICMS-ST e ganham créditos na cadeia do IBS. Distribuição farmacêutica passa do PIS/COFINS monofásico para um modelo de crédito integral. Comércio varejista pode ter aumento ou redução de carga conforme a aliquota de referência do setor. O mapeamento prévio é essencial para não ser surpreendido na transição.</p></div>
      </div>
      <div class="faq-item">
        <h3 class="faq-q" role="button" tabindex="0" aria-expanded="false">
          Posso trocar de contador sem perder documentos ou histórico?
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14"/><path d="M5 12h14"/></svg>
        </h3>
        <div class="faq-a"><p>Sim. A troca de contador não interrompe a operação da empresa. Assumimos a transferência de todos os documentos e dados do contador anterior. Em geral, o processo leva entre 15 e 30 dias e é completamente transparente. Para Sete Lagoas, o atendimento é 100% remoto por videoconferência e plataforma digital.</p></div>
      </div>"""
    new_faq_list = build_faq_html(c['faq'])
    html = html.replace(old_faq_list, new_faq_list)

    # Local presence heading
    html = html.replace("Onde Atuamos em Sete Lagoas", f"Onde Atuamos {c['preposition']} {c['name']}")
    html = html.replace(
        "Contabilidade especializada para cada setor e polo da cidade",
        f"Contabilidade especializada para cada setor {c['preposition']} {c['name']}"
    )
    # Coverage grid
    old_coverage = """      <div class="coverage-col">
        <h3>Polo Industrial</h3>
        <ul>
          <li>Distrito Industrial I (siderurgia)</li>
          <li>Distrito Industrial II (fundição)</li>
          <li>Polo Metalúrgico BR-040</li>
          <li>Indústrias de ferro-gusa e lamineis</li>
          <li>Distribuição farmacêutica</li>
        </ul>
      </div>
      <div class="coverage-col">
        <h3>Eixo Comercial</h3>
        <ul>
          <li>Centro (Av. Presidente Vargas)</li>
          <li>Rua Antônio Olinto</li>
          <li>Bairro Santa Luzia</li>
          <li>Avenida Comércio</li>
          <li>Nova Suissa</li>
        </ul>
      </div>
      <div class="coverage-col">
        <h3>Demais Bairros</h3>
        <ul>
          <li>Santo Antônio</li>
          <li>Belo Vale</li>
          <li>Jardim Cambuí</li>
          <li>Vargem Grande</li>
          <li>Todo o município</li>
        </ul>
      </div>"""
    new_coverage = build_coverage_html(c['coverage'])
    html = html.replace(old_coverage, new_coverage)

    # Local prose (template uses HTML entities)
    # Find and replace local_intro block
    import re as _re
    local_intro_pat = _re.compile(
        r'Sete Lagoas tem <strong>mais de 30\.000 empresas ativas</strong>.*?</a>\.',
        _re.DOTALL
    )
    html = local_intro_pat.sub(c['local_intro'], html, count=1)

    local_p1_pat = _re.compile(
        r'Para ind&#250;strias sider&#250;rgicas.*?carga efetiva\.',
        _re.DOTALL
    )
    html = local_p1_pat.sub(c['local_p1'], html, count=1)

    local_p2_pat = _re.compile(
        r'Construtoras e incorporadoras podem.*?por tipo de obra que precisam ser verificadas caso a caso\.',
        _re.DOTALL
    )
    html = local_p2_pat.sub(c['local_p2'], html, count=1)

    html = html.replace(
        "Ver mais sobre a economia de Sete Lagoas",
        c['local_toggle_text']
    )

    # Location section (encoded entities)
    html = html.replace(
        "Escrit&#243;rio em Par&#225; de Minas. <em>Atendimento remoto em Sete Lagoas.</em>",
        c['location_h2']
    )
    html = html.replace(
        "Atendemos empresas de Sete Lagoas 100% por videoconfer&#234;ncia e plataforma digital. Sem necessidade de deslocamento para o cliente.",
        c['location_atend']
    )
    html = html.replace(
        '<div class="location-card-label">Atendimento Sete Lagoas</div>',
        f'<div class="location-card-label">Atendimento {c["name"]}</div>'
    )
    html = html.replace(
        "100% remoto por videoconfer&#234;ncia<br>Segunda a sexta, 8h &#224;s 18h",
        c['footer_atend']
    )

    # Footer cities - update the self-referencing city
    html = html.replace(
        '<li><a href="/sete-lagoas-mg/">Sete Lagoas</a></li>',
        f'<li><a href="/{c["slug"]}/">{c["name"]}</a></li>'
    )

    # Breadcrumb JSON-LD id
    html = html.replace(
        '"@id": "https://amcabralblindagem.com.br/sete-lagoas-mg/#breadcrumb"',
        f'"@id": "{c["canonical"]}#breadcrumb"'
    )
    html = html.replace(
        '"breadcrumb": { "@id": "https://amcabralblindagem.com.br/sete-lagoas-mg/#breadcrumb" }',
        f'"breadcrumb": {{ "@id": "{c["canonical"]}#breadcrumb" }}'
    )

    # Replace Wikipedia link with correct city
    html = html.replace(
        'href="https://pt.wikipedia.org/wiki/Sete_Lagoas"',
        f'href="{c["wiki_url"]}"'
    )

    # Replace schema @id sete-lagoas-mg with correct slug
    html = html.replace(
        '"https://amcabralblindagem.com.br/sete-lagoas-mg/#servicos"',
        f'"{c["canonical"]}#servicos"'
    )
    html = html.replace(
        '"https://amcabralblindagem.com.br/sete-lagoas-mg/#faq"',
        f'"{c["canonical"]}#faq"'
    )
    html = html.replace(
        '"https://amcabralblindagem.com.br/sete-lagoas-mg/escritorio-de-contabilidade-sete-lagoas/"',
        f'"{c["canonical"]}escritorio-de-contabilidade/"'
    )

    # Header mega-menu link (sete-lagoas specific LP)
    html = html.replace(
        'href="/sete-lagoas-mg/escritorio-de-contabilidade-sete-lagoas/"',
        f'href="/{c["slug"]}/escritorio-de-contabilidade/"'
    )

    # Final pass: replace any remaining "Sete Lagoas" references (plain text)
    # This catches schema markup, FAQ items, comments, etc.
    html = html.replace("Sete Lagoas", c['name'])

    return html


for city in CITIES:
    slug = city['slug']
    out_dir = os.path.join(BASE, slug)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "index.html")
    content = build_html(city)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✓ {slug}/index.html")

print("\nDone. 13 hubs gerados.")
