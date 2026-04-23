# Léxico Semântico — Contabilidade Tributária

Referência para escrever CONTEXT_LOCAL com variação máxima sem repetição de tokens.
Usar no mínimo 2 sinônimos distintos por conceito entre cidades do mesmo corpus.

---

## 1. ENTIDADE CENTRAL — Escritório / Contador

**Hiperônimo (categoria superior):**
- prestador de serviços profissionais
- escritório de assessoria fiscal

**Hipônimos (variantes específicas):**
- escritório contábil
- consultoria tributária
- assessoria fiscal

**Sinônimos diretos:**
- contador / contadora / contabilista
- escritório / consultório / bureau contábil

**LSI / termos associados (co-ocorrem em documentos do domínio):**
- CRC/MG, CFC, normas NBCPF, eSocial, SPED
- honorários, proposta, contrato de prestação

---

## 2. TRIBUTOS — Campo semântico completo

### ICMS
**Hiperônimo:** imposto sobre circulação
**Sinônimos/variantes:** ICMS-ST, ICMS por substituição, substituição tributária do ICMS, imposto estadual, tributação sobre mercadorias
**Hipônimos:** ICMS diferencial de alíquota (DIFAL), ICMS-DIFAL, pauta fiscal de ICMS
**Holônimos (faz parte de):** carga tributária estadual, obrigações acessórias ao estado
**LSI:** nota fiscal eletrônica, SEFAZ, regime de substituição, contribuinte substituto

### IPI
**Hiperônimo:** tributação federal sobre produtos
**Sinônimos/variantes:** imposto sobre produtos industrializados, tributação industrial federal
**LSI:** TIPI, NCM, nota fiscal de entrada, crédito de IPI, insumo produtivo

### PIS/COFINS
**Hiperônimo:** contribuições sociais federais
**Sinônimos/variantes:** contribuições para financiamento da seguridade, PIS/Pasep, COFINS não cumulativa
**Hipônimos:** PIS monofásico, COFINS concentrada, regime cumulativo vs não cumulativo
**LSI:** alíquota diferenciada, crédito presumido, ressarcimento de PIS/COFINS

### ISS
**Hiperônimo:** tributação municipal sobre serviços
**Sinônimos/variantes:** imposto sobre serviços, ISS fixo, ISS variável, ISSQN
**LSI:** nota fiscal de serviço, lista de serviços LC 116, alíquota municipal

### CSLL / IRPJ
**Hiperônimo:** tributação sobre resultado / lucro
**Sinônimos/variantes:** imposto de renda pessoa jurídica, contribuição social sobre lucro líquido
**LSI:** lucro real, lucro presumido, estimativas mensais, DCTF, ECF

---

## 3. REGIMES TRIBUTÁRIOS

**Hiperônimo:** enquadramento fiscal, modalidade de tributação
**Hipônimos (do mais ao menos favorável por porte):**
- Simples Nacional / Supersimples
- Lucro Presumido / tributação pelo presumido
- Lucro Real / apuração pelo real
- Lucro Arbitrado (raro)

**Sinônimos de "migrar de regime":**
- alterar enquadramento, mudar modalidade, transitar para, reenquadrar, recalibrar regime, ajustar sistemática

**LSI:** faturamento, receita bruta, teto do Simples, opção anual, irretratabilidade

---

## 4. CRÉDITOS TRIBUTÁRIOS — Campo semântico

**Hiperônimo:** direito creditório fiscal, ativo fiscal
**Sinônimos de "crédito acumulado":**
- saldo credor, crédito represado, crédito não aproveitado, crédito estagnado, ativo tributário ocioso
- crédito extemporâneo, escrituração de crédito, aproveitamento de crédito

**Ações sobre créditos (variações verbais):**
- recuperar / resgatar / aproveitar / utilizar / escriturar / compensar / restituir / homologar / habilitar

**LSI:** PER/DCOMP, pedido de restituição, prazo prescricional 5 anos, crédito prescrito, auditoria retroativa

---

## 5. PLANEJAMENTO TRIBUTÁRIO

**Hiperônimo:** gestão fiscal estratégica, inteligência tributária
**Sinônimos:**
- planejamento fiscal, elisão fiscal (legal), otimização tributária, racionalização da carga
- engenharia fiscal, estruturação tributária

**Antônimo (o que o cliente quer evitar):**
- evasão fiscal / sonegação (ilegal — NÃO usar como sinônimo)

**Hipônimos:**
- planejamento de ICMS, planejamento de contribuições, reestruturação societária
- revisão de enquadramento, análise de benefícios fiscais, aproveitamento de incentivos

**LSI:** REFIS, parcelamento, moratória, remissão, benefícios do Estado, ICMS incentivado

---

## 6. PATRIMÔNIO — Campo semântico

**Hiperônimo:** bens e direitos do sócio / da empresa
**Sinônimos de "proteger patrimônio":**
- blindar ativos, segregar bens, resguardar patrimônio, isolar risco, separar pessoa física de jurídica

**Hipônimos:**
- holding patrimonial, holding familiar, sociedade de participação, SPE (Sociedade de Propósito Específico)
- imóveis em pessoa jurídica, participações societárias, doação com reserva de usufruto

**LSI:** planejamento sucessório, ITCMD, doação em vida, antecipação de herança, tag along

---

## 7. EMPRESA / EMPRESÁRIO — Variações

**Hiperônimo:** pessoa jurídica, contribuinte, tomador de serviço
**Hipônimos por porte:**
- MEI, microempresa (ME), empresa de pequeno porte (EPP), média empresa, grande empresa

**Sinônimos de "empresário":**
- empreendedor, gestor, sócio, proprietário, dirigente, titular, CEO (empresas maiores)
- dono do negócio, responsável pela empresa

**Sinônimos de "empresa":**
- negócio, organização, companhia, estabelecimento, firma, empreendimento, unidade produtiva, operação

---

## 8. DIAGNÓSTICO / ANÁLISE — Variações de CTA

**Sinônimos de "diagnóstico tributário gratuito":**
- levantamento fiscal gratuito, avaliação tributária sem custo, análise preliminar sem compromisso
- mapeamento da carga fiscal, revisão tributária inicial, estudo de otimização
- consultoria diagnóstica, triagem tributária, due diligence fiscal

**Sinônimos de "ponto de partida":**
- porta de entrada, primeiro passo, etapa inicial, ponto de início, começo do processo

---

## 9. SETORES ECONÔMICOS — Vocabulário por segmento

| Setor | Termos LSI específicos |
|---|---|
| Metalurgia/Siderurgia | fundição, laminação, lingote, aço, ferro-gusa, ligas metálicas, sucata, IPI sobre insumos |
| Farmacêutico | princípio ativo, medicamento, registro ANVISA, PIS/COFINS monofásico, alíquota zero, insumo farmacêutico |
| Alimentos/Bebidas | ICMS-ST sobre alimentos, pauta de bebidas, substituição tributária alimentícia, alíquota reduzida |
| Têxtil/Vestuário | fio, tecido, confecção, IPI têxtil, drawback, exportação de manufaturados |
| Automotivo | autopeças, montagem, drawback, NCM automotivo, crédito presumido de IPI |
| Construção civil | INSS sobre obra, RRT, deduções de material, ISS sobre empreitada |
| Comércio varejista | substituição tributária de ponta, ICMS diferido, nota fiscal consumidor |
| Serviços | ISS competência, retenção na fonte, IRRF, INSS sobre NFS-e |
| Saúde | imunidade COFINS entidade filantrópica, PIS/COFINS saúde, ISS serviços médicos |
| Agronegócio | Funrural, ITR, crédito presumido PIS/COFINS agroindústria, isenção de IPI |

---

## 10. LOCALIZAÇÃO / ATENDIMENTO — Variações geográficas

**Sinônimos de "atendimento remoto":**
- videoconferência, reunião virtual, chamada de vídeo, atendimento digital, formato online, reunião por plataforma

**Sinônimos de "atendimento presencial":**
- visita ao escritório, reunião presencial, encontro no escritório, atendimento in loco

**Variações de distância:**
- a X km de distância, a Y horas de viagem, acessível pela rodovia X, a menos de Z horas
- na mesma região, na região metropolitana de, no eixo X-Y, conectado por

---

## 11. HOMONÍMIAS — Atenção ao uso

| Palavra | Sentido 1 | Sentido 2 | Risco |
|---|---|---|---|
| crédito | direito fiscal (crédito de ICMS) | financiamento bancário | Evitar ambiguidade — especificar "crédito tributário" |
| imposto | tributo geral | imposição/obrigação | OK — contexto resolve |
| regime | enquadramento fiscal | sistema político | Usar "regime tributário" |
| compensar | abater crédito contra débito | valer a pena | Usar "compensar crédito" |
| restituição | devolução de tributo pago | devolução geral | OK — contexto resolve |

---

## Regra de uso

Ao escrever CONTEXT_LOCAL para uma nova cidade:
1. Escolher **ângulo temático diferente** (ex: se última cidade usou crédito de IPI, próxima usa PIS/COFINS ou ICMS-ST)
2. Usar pelo menos **3 sinônimos distintos** para "escritório/contador", "empresa/empresário" e "crédito/diagnóstico"
3. Ancorar em **2-3 termos LSI do setor dominante** da cidade
4. Evitar os mesmos verbos de p3/p4 das cidades anteriores (ex: "identificar", "acompanhamos", "permite")
5. Calcular Jaccard contra **todo o corpus** antes de publicar
