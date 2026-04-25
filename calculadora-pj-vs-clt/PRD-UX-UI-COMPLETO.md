# PRD — Calculadora CLT vs PJ para Empresas
## Product Requirements Document (UX/UI)

**Versão:** 2.0 | **Data:** 2026-04-24 | **Painel de Experts:** 10 especialistas (PM, UX, UI, CRO, Mobile, Behavioral Economics, IA, SaaS, Growth, Accessibility)

---

## ÍNDICE
1. Personas Primárias
2. Jobs To Be Done
3. Fluxo de Uso Ideal
4. Arquitetura de Inputs
5. Arquitetura de Outputs
6. Estados e Transições
7. Micro-interações Críticas
8. Lead Capture Strategy
9. Mobile UX
10. Funcionalidades (MoSCoW)
11. Copy Crítica
12. Métricas de Sucesso

---

## 1. PERSONAS PRIMÁRIAS

### Persona A: Roberto Ferreira (Proprietário PME de manufatura)
- **Cargo:** Dono, gestão operacional
- **Idade:** 52 anos | **Localização:** Pará de Minas, MG
- **Renda empresa:** R$ 2M–5M/ano | **Equipe:** 8–15 pessoas
- **Dúvida principal:** "Preciso trazer meu gerente de produção como CLT ou negocio como PJ? Qual é o impacto real no fluxo de caixa?"
- **Dado que mais importa ver:** Custo mensal total (CLT), custo de demissão se não der certo, comparação anual
- **Comportamento:** Não lê parágrafos longos. Quer número grande, rápido. Desconfia de fórmulas: "show me the math" implícito.
- **Dispositivo principal:** Desktop (72%), tablet (18%)
- **Gatilho:** Conversa com contador sobre "como formalizar", análise fiscal anual, decisão de expansão.

### Persona B: Marina Silva (Gerente de RH em Tech startup)
- **Cargo:** Gerente de Recursos Humanos
- **Idade:** 32 anos | **Localização:** São Paulo, SP
- **Renda empresa:** Série A/B (R$ 5M–50M/ano) | **Equipe:** 40+ pessoas
- **Dúvida principal:** "Consultores e devs podem ser PJ? A empresa está exposta a risco de vínculo? Qual é a economia real vs CLT?"
- **Dado que mais importa ver:** Diferença percentual (CLT vs PJ), tempo de contrato, risco tributário, comparação anual
- **Comportamento:** Analítica. Quer contexto, comparação, possibilidade de exportar. Confia em numeros com fonte.
- **Dispositivo principal:** Mobile (60%), desktop (40%)
- **Gatilho:** Definição de budgets, contratação de novo time, auditoria de folha.

### Persona C: Amanda Cabral (Prospect contadora)
- **Cargo:** Ela mesma = funil de conversão
- **Idade:** 48 anos | **Localização:** Pará de Minas, MG
- **Objetivo:** Demonstrar expertise, capturar lead, agendar diagnóstico
- **Dúvida:** "Como usar essa calculadora para mostrar ROI de consultoria para meus clientes?"
- **Dado que mais importa:** Form submission, email + whatsapp, tempo de engajamento, conversão para diagnóstico
- **Comportamento:** Quer ver as pessoas usarem a ferramenta, confiar nela, e passar WhatsApp para ela ligar.
- **Dispositivo principal:** Desktop (apresentações) + Mobile (social share)
- **Gatilho:** Social proof, demonstração em reunião, referência em blog/LinkedIn.

---

## 2. JOBS TO BE DO (JTBD)

### Job 1: Roberto (Decisão de contratação)
**When:** Precisa expandir equipe, contratar especialista ou terceirizar
**I want to:** Entender o impacto financeiro real: quanto vou gastar se contratar como CLT vs PJ
**So that:** Posso fazer uma decisão informada sobre estrutura de contratação sem surpresas fiscais

**Pains:**
- Não sabe as taxas exatas (INSS 20%? FGTS é sobre quê?)
- Teme custos de demissão (aviso prévio, multa FGTS)
- Calcula no papel/Excel e fica com dúvida

**Gains:**
- Comparação lado a lado em 30 segundos
- Ver custo anual, não só mensal
- Entender cada encargo (accordion)

---

### Job 2: Marina (Conformidade + benchmark)
**When:** Audita folha de pagamento, define orçamento de RH, contrata novos devs/consultores
**I want to:** Validar se a estrutura PJ de alguns consultores está economizando realmente e se há risco de vínculo
**So that:** Posso defender a decisão em CODIR e ter documentação para compliance (se auditado)

**Pains:**
- Calculadora pode ser enviesada (mostrar só o melhor caso)
- Precisa de source (onde vem o 20% de INSS?)
- Quer poder compartilhar com contador/jurídico

**Gains:**
- Resultado exportável (PDF, link compartilhável)
- Fonte das taxas claramente citada
- Simulação de variações (se salário subir X%, impacto?)

---

### Job 3: Amanda (Lead gen + credibilidade)
**When:** Faz prospecting, atende reunião com cliente potencial, quer demonstrar expertise em contratação
**I want to:** Que o cliente use a calculadora, veja o resultado, e queira conversar mais (diagnóstico)
**So that:** Consigo um novo cliente de consultoria tributária

**Pains:**
- Cliente não entende os encargos, acha a calculadora superficial
- Form capture pode assustar (pede muito)
- Não há CTA clara para agendamento

**Gains:**
- Form minimalista (nome + email + WhatsApp)
- CTA claro: "Agendar diagnóstico com contadora"
- Resultado motiva: "Veja quanto você pode economizar"

---

## 3. FLUXO DE USO IDEAL

### Sequência Completa (entrada até lead)

```
[01] Usuário entra na página
  ↓ Hero section explica o que é
  ↓ Vê 3 badges: "Encargos 2025", "Tempo real", "Demissão incluída"
  ↓ CTA: "Calcular agora" (scroll smooth até calculadora)

[02] Seção Calculadora aparece
  ↓ 2 colunas (CLT | PJ) em desktop, 1 em mobile
  ↓ CLT: Salário bruto (anchor field, foco automático)
  ↓ CLT: Segmento empresa (dropdown, Sistema S)
  ↓ CLT: Benefícios (VR, VT, saúde) — expandable "MAIS OPÇÕES" ou direto?
  ↓ CLT: Checkbox "Incluir provisões 13º/férias"
  ↓ PJ: Honorário mensal (campo secundário)
  ↓ PJ: Tempo contrato (dropdown: 6, 12, 24, 36 meses ou input?)

[03] Clica "Calcular Custo Real"
  ↓ Validação silenciosa (campo obrigatório vazio? erro inline)
  ↓ Animação: resultado aparece com fade-up (.5s)

[04] Resultado exibido (Layer 1)
  ↓ 2 cards (CLT | PJ) com custo mensal total
  ↓ Badge delta: "+ R$ 1.200/mês" ou "- R$ 800/mês" (cor verde se PJ barato, vermelho se CLT barato)
  ↓ Texto contexto: "CLT custa 40% mais ao ano"

[05] Resultado exibido (Layer 2)
  ↓ Card "Diferença anual entre CLT e PJ"
  ↓ Grande valor: "R$ 91.200/ano"
  ↓ Sub: "Se usar CLT: R$ 120k/ano. Se usar PJ: R$ 28.8k/ano"

[06] Encargos detalhados (accordion)
  ↓ Closed by default (não oprime com informação)
  ↓ Header: "Encargos patronais CLT detalhados" + total "R$ 2.000/mês"
  ↓ Click: expand com 5 linhas (INSS, FGTS, Sistema S, 13º, férias)
  ↓ Cada linha mostra: nome + % + valor + tooltip (o que é isso?)

[07] Simulação demissão (accordion)
  ↓ Closed by default
  ↓ Header: "Simulação de demissão sem justa causa" + total "R$ 15.000"
  ↓ Click: expand com 4 linhas (Aviso prévio, Multa FGTS 50%, Férias prop., 13º prop.)

[08] Lead form motiva
  ↓ Fundo dourado (destaque)
  ↓ Headline: "Quer aprofundar essa analise?"
  ↓ Subheadline: "Converse com Amanda Cabral, contadora CRC/MG. Diagnóstico gratuito."
  ↓ 3 campos: Nome | Email | WhatsApp
  ↓ Dropdown: Cargo (Dono, RH, Controller, Jurídico, Outro)
  ↓ CTA verde: "Enviar e agendar com Amanda"

[09] Pós-submissão
  ↓ Success message: "Pronto! Você receberá um WhatsApp em breve."
  ↓ Botão: "Agendar consulta" → link WhatsApp pré-preenchido
  ↓ Ou: mostrar card com "5 coisas que sua empresa pode estar pagando a mais"
```

---

## 4. ARQUITETURA DE INPUTS

### Estrutura Lógica

#### **CLT: Campo Âncora (entrada primária)**
**salarioBruto** (obrigatório)
- **Tipo:** Number input
- **Placeholder:** "ex: 5000"
- **Min:** 1412 (salário mínimo 2025) ✓
- **Step:** 100
- **Inputmode:** numeric
- **Auto-focus:** Sim (entrar na página = foco automático)
- **Validação:** 
  - Campo vazio = mensagem "Preencha o salário" (erro inline, vermelho)
  - Valor < 1412 = "Mínimo é salário mínimo 2025" (warning)
- **Motivo:** Impacto em tudo. Usuário quer preencher este primeiro.
- **Micro:** Ao sair do campo (blur), calcula preview parcial? (V2)

---

#### **CLT: segmentoEmpresa (Sistema S, obrigatório)**
- **Tipo:** Select dropdown
- **Default:** "Indústria (SESI + SENAI + SEBRAE) ~5,8%" (mais comum)
- **Opções:** 6 segmentos (Indústria, Comércio, Serviços/TI, Transporte, Construção, Agronegócio)
- **Valor codificado:** 0.058, 0.055, 0.046, 0.025, 0.025, 0.060
- **Motivo:** Sistema S varia muito. Usuário NÃO sabe que é por segmento.
- **Problema atual:** "Segmento da Empresa (afeta aliquota Sistema S)" — muito técnico.
- **Reescrever para:** "Qual é sua atividade principal?" (menos jargão)
- **Impacto:** +/- R$ 150/mês (significativo)

---

#### **CLT: Benefícios (opcionais, progressive disclosure)**

**Problema diagnosticado:** 
- Usuário vê 3 campos (VR, VT, Saúde) na mesma página.
- Sente-se obrigado a preencher todos.
- Maioria deixa em zero (maior motivo: não oferece esses benefícios).

**Solução - Opção A (RECOMENDADO):**
Manter 3 campos visíveis, mas com copy claro:
```
beneficioVR (Vale-Refeição)
  Label: "Vale-Refeição / Vale-Alimentação (mensal)" 
  Subtext: "(deixe em branco se não oferece)"
  Placeholder: "0"
  Min: 0, Step: 10
```

**Solução - Opção B (V2: Progressive Disclosure):**
Collapsible "Adicionar benefícios?" (closed by default).
- Usuários que não oferecem = não veem.
- Usuários que oferecem = encontram rápido.
- Reduz visual clutter.

**Solução escolhida:** Opção A (menos disruptivo agora, Opção B em v1.1)

**Campos:**
1. **beneficioVR** — Vale-Refeição
   - Min: 0, Step: 10, Default: 0
   
2. **beneficioVT** — Vale-Transporte
   - Min: 0, Step: 10, Default: 0
   - Subtext: "(reembolsável pelo colaborador 6%)"
   - **Problema:** Usuário acha que VT custa 100% para empresa. Real: empresa paga 94%, colaborador desconta 6%.
   - **Fix:** Tooltip: "ℹ Empresa paga 100%, mas colaborador contribui com 6%. Custo líquido: 94%."
   
3. **beneficioSaude** — Plano de Saúde
   - Min: 0, Step: 50, Default: 0
   - Subtext: "(custo mensal para a empresa)"

---

#### **CLT: Provisões (obrigatório com checkbox)**
```
incluirProvisoes (checkbox, checked by default)
  Label: "Incluir provisões mensais"
  Helper text: "Provisionar 13º e férias (recomendado)"
```

**Motivo checkbox é checked:**
- Best practice: empresas DEVEM provisionar.
- Se não provisiona = problema contábil.
- Usuário que descumpre = seu problema, não da calculadora.

**Comportamento:** Se desmarcar, linha "Provisão 13º" + "Provisão Férias" some do accordion.

---

#### **PJ: honorarioPJ (obrigatório)**
```
Tipo: Number input
Placeholder: "ex: 8000"
Min: 0, Step: 100
Inputmode: numeric
Label: "Honorário Mensal do PJ"
Subtext: "(valor pago pela empresa)"
```

**Motivo:** Usuário comparando CLT vs PJ naturalmente quer saber "se eu pagasse X de PJ, quanto sairia?"

**Comportamento:** Se preenchido, calcula imediatamente (sem botão, live).

---

#### **PJ: tempoContrato (espaçamento temporal)**
```
Tipo: Number input (ou select dropdown)
Default: 24 (2 anos)
Min: 1, Max: 120
Step: 1
Label: "Tempo estimado de contrato (meses)"
Subtext: "(para cálculo de custo de demissão)"
```

**Motivo:** Calcula aviso prévio (30 dias + 3 dias/ano). Muito usado em demissão.

**Problema:** Usuário não sabe se preenchimento é obrigatório. Label diz "tempo estimado" (soft).

**Fix em v1.1:** Tornário mais explícito:
- Label: "Se o contrato fosse rescindido, quanto tempo teria durado?" 
- Tooltip: "Usado para calcular multa FGTS e aviso prévio. Se não sabe, use 24 meses (padrão)."

---

### Ordem Ideal dos Campos (Cognitive Load)

**Desktop (2 colunas):**
```
Coluna CLT              |  Coluna PJ
─────────────────────────────────────
Salário bruto ★          |  Honorário PJ ★
Segmento empresa ★       |  Tempo contrato
VR (opcional)            |  [info box]
VT (opcional)            |  
Saúde (opcional)         |
Provisões ☐              |
```

**Mobile (1 coluna):**
Mesmo que desktop, mas stackado verticalmente. Risco: usuário não vê que tem coluna PJ embaixo.

**Fix:** 
- Tabs no mobile: "CLT" | "PJ" (swipeable, sticky tabs no topo após scroll)
- Ou: Accordion "Comparar PJ" (collapsed)
- Recomendado: Tabs (menor barreira cognitiva)

---

### Validação de Inputs

| Campo | Validação | Mensagem | Nível |
|-------|-----------|----------|-------|
| salarioBruto | Vazio | "Preencha o salário bruto" | Error (botão desativado) |
| salarioBruto | < 1412 | "Mínimo é R$ 1.412 (salário mínimo 2025)" | Warning (permite, aviso) |
| segmentoEmpresa | — | (dropdown sempre tem default) | — |
| VR/VT/Saúde | < 0 | (input min="0" previne) | — |
| honorarioPJ | Vazio | "Preencha o honorário PJ para comparar" | Soft (label "ex: 8000") |
| tempoContrato | 0 ou vazio | Use default 24 | Silent (background) |

**Timing:** Validação ao clicar "Calcular", não ao digitar (menos agressivo em mobile).

---

## 5. ARQUITETURA DE OUTPUTS

### Hierarquia Visual (O que aparece primeiro, maior)

```
Resultado (após "Calcular")
├─ LAYER 1 (Impacto imediato, em 3 segundos)
│  ├─ Card CLT: "R$ 6.200/mês" (custo total mensal) [DESTAQUE]
│  └─ Card PJ: "R$ 8.000/mês" com badge delta "PJ é 28% mais caro" [ALERTA]
│
├─ LAYER 2 (Contexto anual, 5 segundos)
│  └─ Card Diferença Anual: "R$ 21.600/ano" + "Se CLT: R$ 74,4k/ano. Se PJ: R$ 96k/ano" [CONTEXTO]
│
├─ LAYER 3 (Detalhes, accordion, não invasivo)
│  ├─ Encargos patronais CLT detalhados [CLOSED]
│  │  ├─ INSS 20% = R$ 1.000
│  │  ├─ FGTS 8% = R$ 400
│  │  ├─ Sistema S 5,8% = R$ 290
│  │  ├─ Provisão 13º 8,33% = R$ 417
│  │  └─ Provisão Férias 11,11% = R$ 555
│  │
│  └─ Simulação demissão [CLOSED]
│     ├─ Aviso prévio = R$ 1.600
│     ├─ Multa FGTS 50% = R$ 4.800
│     ├─ Férias proporcionais = R$ 900
│     └─ 13º proporcionais = R$ 500
│
└─ LAYER 4 (Lead capture, degrau para conversão)
   └─ Form + CTA "Agendar com contadora"
```

---

### Card Layer 1: Custos Mensais (Impacto Visual)

#### **CLT - Resultado Principal**
```
┌─────────────────────────────────────────┐
│ Custo Total CLT (mensal)                │
│ R$ 6.200                      [VALOR]   │
│ Encargos: R$ 1.200            [SUB]     │
│ Benefícios: R$ 500                      │
└─────────────────────────────────────────┘
```

**Problemas diagnosticados:**
1. "Encargos: R$ 1.200 | Benefícios: R$ 500" — usuário não entende se é bom ou ruim.
2. Falta contexto: "R$ 6.200 é muito?" vs salário bruto.

**Fix (v1.1):**
```
┌─────────────────────────────────────────┐
│ Custo Total CLT (mensal)                │
│ R$ 6.200                      [VALOR]   │
│ Encargos: R$ 1.200 (19%)               │
│ Benefícios: R$ 500 (8%)                │
│ ─────────────────────────────────────── │
│ Base (salário bruto): R$ 5.000          │
│ Total adicional: 24% do salário         │
└─────────────────────────────────────────┘
```

**Melhorias:**
- Percentual explícito (19%, 8%)
- "Total adicional: 24%" (resume o custo real)
- Base do cálculo visível

---

#### **PJ - Resultado Secundário (comparável)**
```
┌─────────────────────────────────────────┐
│ Custo Total PJ (mensal)       [BADGE]   │
│ R$ 8.000                      [VALOR]   │
│ Apenas o honorário            [SUB]     │
│ Sem encargos adicionais                 │
└─────────────────────────────────────────┘
```

**Badge Delta (no canto superior direito):**
- **Se CLT < PJ:** Badge GREEN "PJ é 29% mais caro" (alerta positivo para CLT)
- **Se PJ < CLT:** Badge RED "PJ é 29% mais barato" (alerta positivo para PJ)
- **Se iguais:** Badge GREY "Custo equivalente"

**Posicionamento:** Canto superior direito (eye-tracking natural).

**Cores:**
- Verde (#10B981): Bom para CLT (cheaper)
- Vermelho (#EF4444): Bom para PJ (cheaper)
- Cinza (#94A3B8): Neutro (iguais)

---

### Card Layer 2: Diferença Anual (Contextualização)

```
┌─────────────────────────────────────────┐
│ Diferença anual CLT vs PJ               │
│ R$ 21.600                     [VALOR]   │
│ (CLT custa 29% mais ao ano)             │
│ ─────────────────────────────────────── │
│ CLT: R$ 74.400/ano (R$ 6.200 × 12)    │
│ PJ:  R$ 96.000/ano (R$ 8.000 × 12)    │
│ ─────────────────────────────────────── │
│ Economia se optar por PJ: R$ 21.600    │
└─────────────────────────────────────────┘
```

**Motivo:** Usuário pensa em anual, não em mensal. "R$ 21.600 a menos é significativo?"

**Contextualização (em micro):**
- Se diferença > R$ 10k/ano: adicionar emoji 📊 (impacto alto)
- Se diferença < R$ 2k/ano: texto "Diferença baixa" (impacto baixo)

---

### Accordions: O que NÃO aparecer por padrão

**Problema:** Usuário vê "INSS 20%, FGTS 8%, Sistema S 5,8%, Prov. 13º 8,33%, Prov. Férias 11,11%" → overwhelm.

**Solução:** Closed accordions com sumário visível.

#### **Accordion 1: Encargos Patronais CLT Detalhados**

**Header (sempre visível):**
```
Encargos patronais CLT detalhados
Clique para ver o custo de cada obrigação
                              R$ 1.852/mês ↓
```

**Body (onclick, fade-down):**
```
INSS Patronal (20%)
  Base: salário bruto 5.000
  Cálculo: 5.000 × 20%
  Custo: R$ 1.000
  ℹ Empresa paga sobre cada real. Sem teto.

FGTS (8%)
  Base: salário bruto 5.000
  Cálculo: 5.000 × 8%
  Custo: R$ 400
  ℹ Depositado em conta vinculada. Liberado em rescisão.

Sistema S (5,8% — Indústria)
  Base: salário bruto 5.000
  Cálculo: 5.000 × 5,8%
  Custo: R$ 290
  ℹ Varia por setor. Incluir SESI/SENAI, SEBRAE, etc.

Provisão 13º Salário (8,33%)
  Base: salário bruto 5.000
  Cálculo: 5.000 × 8,33%
  Custo: R$ 417
  ℹ Reserva mensal para pagamento dez/jan.

Provisão Férias + 1/3 (11,11%)
  Base: salário bruto 5.000
  Cálculo: 5.000 × 11,11%
  Custo: R$ 555
  ℹ 30 dias férias + 33% acrescido.

TOTAL ENCARGOS: R$ 2.662/mês
```

**Decisão sobre Provisões:**
- Se `incluirProvisoes` = unchecked, omitir últimas 2 linhas (13º e férias).
- Linhas removidas = total muda.

---

#### **Accordion 2: Simulação de Demissão sem Justa Causa**

**Problema:**
- Usuário NÃO quer ver isso (é negativo).
- Mas precisa SABER (é um custo real se dispensar).
- Solução: accordion, collapsed, com aviso no header.

**Header (sempre visível):**
```
Simulação de demissão sem justa causa
Custo estimado se a empresa dispensar o colaborador
                              R$ 7.700 ↓
```

**Body:**
```
Baseado em contrato de 24 meses.

Aviso Prévio
  Mínimo: 30 dias
  + 3 dias por ano completo: 3 anos = 9 dias
  Total dias: 39 dias
  Custo (salário bruto): R$ 1.600
  ℹ Trabalhador cumpre aviso ou empresa paga (indenizado).

Multa FGTS (50% sobre saldo acumulado)
  FGTS acumulado (8% × 24 meses): R$ 9.600
  Multa 50%: R$ 4.800
  ℹ Empresa paga 50%. Colaborador recebe saldo + multa.

Férias Proporcionais + 1/3
  Dias proporcionais de férias: 15 dias
  + 1/3 constitucional: 5 dias
  Total: 20 dias
  Custo (salário diário 5.000/30): R$ 1.200
  ℹ Férias não gozadas do período atual.

13º Proporcional
  Período (24 meses = 2 anos completos): 0 meses
  Custo: R$ 0
  ℹ Se contrato termina no meio do ano, recebe 13º prop.

TOTAL CUSTO DE DEMISSÃO: R$ 7.700
```

**Tooltip interativo (opcional):** Ao passar mouse sobre linha, mostra a fórmula (ex: "30 dias + 3 dias/ano").

---

### O que NÃO mostrar no resultado principal

❌ Detalhes de cálculo (fórmulas)
❌ Campos obrigatórios vs opcionais
❌ Aviso legal "Resultado orientativo"
❌ Dropdown segmento empresa (já aplicado)
❌ Gráficos de pizza / barras (clutter visual)

✅ 2 números grandes (mensal)
✅ 1 número de contexto (anual)
✅ Botão de detalhes (accordion)
✅ CTA para conversar com contador

---

## 6. ESTADOS E TRANSIÇÕES

### Estado Vazio (Zero State)

**Quando:** Página carrega, usuário não preencheu nada.

**Visual:**
```
┌─ Calculadora ──────────────────────┐
│                                    │
│ [Coluna CLT com inputs vazios]    │
│ [Coluna PJ com inputs vazios]     │
│                                    │
│ [Botão "Calcular Custo Real"]     │
│   (habilitado se salário bruto OK) │
│                                    │
│ [Nenhum resultado visível]         │
│                                    │
└────────────────────────────────────┘
```

**Comportamento:**
- Inputs têm `placeholder` ("ex: 5000")
- Nenhum erro visível
- Botão habilitado (incentiva tentativa)

---

### Estado Preenchimento Parcial

**Quando:** Usuário começou a preencher, mas faltam campos obrigatórios.

**Cenário A: Salário bruto vazio, PJ preenchido**
```
┌─ Calculadora ──────────────────────┐
│                                    │
│ [Salário bruto] [VAZIO] ⚠️         │
│ "Preencha o salário bruto"        │
│ [Segmento] [Indústria ✓]          │
│ [VR] [0]                          │
│ ...                               │
│                                    │
│ [Honorário PJ] [8000]             │
│ [Tempo contrato] [24]             │
│                                    │
│ [Botão "Calcular"] (DESATIVADO)   │
│                                    │
└────────────────────────────────────┘
```

**Comportamento:**
- Mensagem de erro inline (vermelha, ícone ⚠️)
- Botão desativado (opacity 0.5, cursor: not-allowed)
- Outras validações silenciosas (não aparecem até submit)

**Cenário B: Salário bruto < salário mínimo**
```
[Salário bruto] [800] ⚠️
"Mínimo é R$ 1.412 (salário mínimo 2025)"
[Botão "Calcular"] (habilitado, mas aviso)
```

**Comportamento:**
- Warning (amarelo), não error (vermelho)
- Botão habilitado (usuário pode ignorar aviso)
- Cálculo segue com valor digitado

---

### Estado Resultado Completo

**Quando:** Usuário clicou "Calcular Custo Real" com dados válidos.

**Transição (0.3s–0.5s):**
1. Botão mostra loading spinner (opcional: "Calculando..." mas é instant, então skip)
2. Resultado aparece com fade-up + stagger animation (cards entram cascata)
3. Scroll automático para resultado? (Depende: desktop não precisa, mobile SIM)

**Layout:**
```
┌─ Resultado Completo ─────────────┐
│                                  │
│ [Card CLT] [Card PJ]   ← LAYER 1 │
│ [Diferença Anual]       ← LAYER 2 │
│ [Accordion Encargos]    ← LAYER 3 │
│ [Accordion Demissão]    ← LAYER 3 │
│                                  │
│ [Form Lead Capture]     ← LAYER 4 │
│                                  │
└──────────────────────────────────┘
```

**Comportamento:**
- Resultado sticky no desktop (segue scroll)? Não, deixa natural.
- Resultado visível 100% em mobile (sem sticky).
- Usuário pode editar inputs acima (não esconde form).
- Re-calcular ao mudar input (live update, v1.1).

---

### Estado Após Lead Capture

**Quando:** Usuário submeteu form com nome, email, WhatsApp.

**Transição:**
1. Form desaparece (fade-out)
2. Success message aparece (fade-in)

**Success Message:**
```
┌─ Sucesso! ───────────────────────┐
│ ✓                                │
│                                  │
│ Recebemos seus dados!            │
│                                  │
│ Amanda Cabral entrará em contato│
│ em breve via WhatsApp para       │
│ aprofundar essa análise.         │
│                                  │
│ [Botão] "Agendar consulta"       │
│         → link WhatsApp          │
│                                  │
│ Tempo médio de resposta:         │
│ 24–48 horas (seg–sex)           │
│                                  │
└──────────────────────────────────┘
```

**Comportamento:**
- Form desaparece completamente (não pode resubmeter 2x)
- Success message mostra contato via WhatsApp
- Botão "Agendar" pré-preenche mensagem: "Olá Amanda, usamos a calculadora CLT vs PJ e gostaria de conversar sobre contratação."
- Após 10s, mostra card adicional: "5 coisas que sua empresa pode estar pagando a mais" (upsell soft)

---

### Tratamento de Inputs Inválidos

| Input | Inválido | Mensagem | Ação |
|-------|----------|----------|------|
| Salário bruto | Vazio | "Preencha o salário bruto" | Erro (botão desativado) |
| Salário bruto | NaN (texto) | "Digite um número válido" | Erro inline |
| Salário bruto | 1000 (< mín) | "Mínimo R$ 1.412" | Aviso (botão ativo) |
| Honorário PJ | Vazio | Silencioso (não calcula PJ) | Sem erro, mostra "Preencha para comparar" |
| Tempo contrato | 0 | Silencioso (usa default 24) | Sem erro |

---

## 7. MICRO-INTERAÇÕES CRÍTICAS

### Feedback ao Digitar (Live Calculation)

**Versão Atual:** Botão "Calcular" (usuário deve clicar)
**Problema:** Friction. Usuário quer ver resultado enquanto digita.

**V1.1 Proposta: Live Calculation**
```
[Salário bruto] [5000] → campo perde foco → resultado atualiza automaticamente
```

**Comportamento:**
- Ao deixar campo (blur), valida e recalcula
- Resultado atualiza sem delay perceptível (< 100ms)
- Sem "Calculando..." message (é instantâneo)
- Botão "Calcular Custo Real" vira "Atualizar Resultado" (secondary button)

**Risco:** Pode confundir usuário que não vê quando cálculo aconteceu.
**Mitigação:** Subtle flash de cor no resultado (1s de glow dourado).

**Implementação recomendada:** Manter botão "Calcular" (v1.0), adicionar live calc em v1.1.

---

### Tooltips de Contexto

**Critério:** Mostrar quando termo é técnico OU usuário pode se confundir.

#### **Tooltip 1: INSS Patronal**
```
Hover sobre "INSS Patronal (20%)" → tooltip aparece:
┌─────────────────────────────────────┐
│ INSS Patronal 20%                  │
│                                     │
│ Contribuição social obrigatória    │
│ que a empresa paga sobre cada      │
│ real do salário do colaborador.    │
│                                     │
│ Não tem teto: pague quanto         │
│ for o salário.                     │
│                                     │
│ Vai para: Tesouro Nacional         │
│ (aposentadoria do colaborador)     │
└─────────────────────────────────────┘
```

**Implementação:**
- Ícone ℹ️ ao lado do termo
- Tooltip em dark mode, com seta apontando termo
- Desaparece ao sair (mouseleave)
- Mobile: tap para toggle (não hover)

#### **Tooltip 2: FGTS**
```
"FGTS (8%)" → tooltip:
Fundo de Garantia do Tempo de Serviço.
Depositado em conta no banco em nome
do colaborador. Liberado em rescisão,
aposentadoria ou saque aniversário.
```

#### **Tooltip 3: Sistema S**
```
"Sistema S (5,8%)" → tooltip:
Contribuições para SESI, SENAI, SESC,
SENAC, SEBRAE, INCRA e outros órgãos
de treinamento e desenvolvimento.
Varia por ramo de atividade (CNAE).
```

#### **Tooltip 4: Multa FGTS**
```
"Multa FGTS (50%)" → tooltip:
Quando empresa rescinde contrato sem
justa causa, paga 50% do FGTS acumulado
como multa. Colaborador recebe 100% do
saldo + 50% de multa.
```

**Implementação:** Usar `<abbr title="">` com CSS ou lib (Popper.js, Tippy.js).

---

### Animação do Resultado (Reveal Pattern)

**Estado inicial:** Resultado oculto (display: none)

**Ao clicar "Calcular":**
```
[Botão "Calcular"] ← click

↓ [0ms] validação passa
↓ [0-300ms] spinner (opcional)
↓ [300-800ms] resultado entra com animação

.calc-result {
  opacity: 0; transform: translateY(20px);
  animation: fadeUp 0.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

@keyframes fadeUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
```

**Cards (stagger):**
```
.result-cards > * {
  animation: fadeUp 0.5s ease forwards;
  animation-delay: calc(150ms * var(--index));
}
```

**Cada card entra em cascata (150ms apart):**
- t=300ms: Card CLT entra
- t=450ms: Card PJ entra
- t=600ms: Diferença Anual entra

**Efeito:** Não é overwhelming, usuário vê resultado revelar gradualmente.

---

### Indicador de Loading

**Necessário?** Não (cálculo é instantâneo JS).

**Se fosse backend:**
```
[Botão "Calcular"] → spinner 
[300ms spinner] → resultado aparece
```

**Decisão:** Skip loading spinner (é muito rápido). Manter animação de entrada.

---

### Comportamento do Accordion

**Default:** Closed
```
├─ Encargos patronais CLT [▼]
│  └─ (body hidden)
│
├─ Simulação demissão [▼]
   └─ (body hidden)
```

**Ao clicar header:**
1. Body aparece (display: none → block)
2. Seta gira 180° (transform rotate)
3. Transição smooth: 0.25s

```
.benefits-section {
  &.open {
    .benefits-header-arrow {
      transform: rotate(180deg);
    }
    .benefits-body {
      display: block;
    }
  }
}
```

**Comportamento:** Todos 2 accordions independentes (usuário pode abrir ambos).

**Mobile:** Tap para toggle (não hover).

---

## 8. LEAD CAPTURE STRATEGY

### Timing Ideal (Quando Mostrar Form)

**Problema diagnosticado:** Form mostra sempre (scroll até ela). Risco: Interrompe fluxo de leitura.

**Opção A (Atual):** Form após accordion demissão (natural, usuário scroll até lá).
**Opção B (V1.1):** Modal popup após 5s de visualização do resultado (agressivo, mas high-conversion).
**Opção C (V1.1):** Sticky button "Agendar" no mobile (botton-fixed).

**Recomendação:** Manter Opção A (v1.0), testar Opção B após 2 semanas (A/B test).

---

### Campos Mínimos Viáveis vs. Ideais

#### **MVP (3 campos):**
```
[Nome] ★
[Email] ★
[WhatsApp] ★
[Botão] "Enviar"
```

**Motivo:** Máxima conversão. Usuário não quer ficar preenchendo.

#### **Ideal (5 campos):**
```
[Nome] ★
[Email] ★
[WhatsApp] ★
[Empresa] (opcional)
[Cargo] (dropdown)
[Botão] "Enviar e agendar com Amanda"
```

**Motivo:** Segmentação (Amanda sabe se é dono, RH, controller = abordagem diferente).

**Decisão v1.0:** MVP (3 campos) + dropdown Cargo.
```
[Nome] ★
[Email] ★
[WhatsApp] ★
[Cargo] (Dono | RH | Controller | Jurídico | Outro)
[Botão] "Enviar"
```

---

### Copy do CTA Principal

**Versão Atual:** "Enviar e agendar com Amanda"

**Problema:** "Agendar" pode soar como "já está marcado" (quando não está).

**Opções:**
1. "Enviar dados → Amanda ligará em breve"
2. "Enviar → Conversaremos via WhatsApp"
3. "Enviar para diagnóstico gratuito"
4. "Enviar e receber proposta" (muito comercial)

**Recomendação:** Opção 2 (mais honesto, menos promessa).

```
[Botão Verde] "Enviar e conversaremos via WhatsApp"
```

**Subtext após botão:**
```
"Amanda Cabral, CRC/MG, entrará em contato em 24–48 horas"
```

---

### O que Oferecer em Troca (Value Exchange)

**Problema:** Form pede dados (contato), usuário quer algo em retorno.

**Opções:**
A) Resultado salvo (PDF para download)
B) Diagnóstico gratuito (consultoria breve)
C) Plano de ação customizado (mais assertivo)
D) E-book "5 erros de contratação" (lead magnet)

**Recomendação:** Opção B (alinha com estratégia Amanda).

**Copy no form:**
```
[Headline]
"Pronto para aprofundar essa análise?"

[Subheadline]
"Converse com Amanda Cabral, contadora CRC/MG. 
Diagnóstico gratuito e sem compromisso. 
Duração típica: 20–30 minutos."

[3 campos]

[Botão]
"Enviar e marcar consulta"
```

---

### Friction vs. Conversion Tradeoff

| Campos | Conversion Rate (Est.) | Friction | Decisão |
|--------|------------------------|----------|---------|
| 2 (Nome, Email) | 12–15% | Baixa | Minimal (não vai) |
| 3 (Nome, Email, WA) | 8–10% | Média | MVP v1.0 ✓ |
| 4 (+ Cargo) | 6–8% | Média-alta | V1.0 ✓ |
| 5 (+ Empresa) | 4–6% | Alta | V1.1 (teste) |

**Escolha:** 4 campos (nome, email, whatsapp, cargo) = bom balanço.

---

## 9. MOBILE UX (375px–480px)

### Layout em 375px (iPhone SE)

#### **Hero Section**
- Font size: clamp() (responsive)
- Button "Calcular agora" full-width (margin: 0 16px)
- Badges empilham verticalmente (grid 1 coluna)

✅ Quebra bem.

#### **Calculadora (Inputs)**

**Problema:** 2 colunas lado a lado em mobile são ilegíveis.

**Solução: Tabs Swipeable**
```
┌─ [CLT] [PJ] ──────────────────┐
│ ●──────●──────                 │
│ Contratacao CLT                │
│                                │
│ [Salário bruto] [5000]        │
│ [Segmento] [dropdown]          │
│ [VR] [0]                       │
│ [VT] [0]                       │
│ [Saúde] [0]                    │
│ [☐ Provisões]                  │
│                                │
│ [Botão "Calcular"]             │
│                                │
│ ← swipe para PJ →              │
└────────────────────────────────┘
```

**Implementação:**
- CSS Grid com gap ou Carousel simple (HTML/CSS, sem JS se possível)
- Indicador de página (·●·) no topo
- Swipe left/right para navegar (touch-friendly)
- Botão "Calcular" **abaixo das abas** (após PJ também)

**Alternativa:** Accordion (simpler)
```
[▼ Contratacao CLT] ← collapsed por padrão
[▲ Contratacao PJ]  ← expandido por padrão
```

**Recomendação:** Accordion é simpler (menos JS). Testes com usuários dirão qual é melhor.

---

#### **Resultado**
```
┌────────────────────────────────┐
│ Custo Total CLT                │
│ R$ 6.200                       │
│ Encargos: R$ 1.200             │
│                                │
│ Custo Total PJ    [+ 29%]      │
│ R$ 8.000                       │
│ Apenas honorário               │
│                                │
│ Diferença anual                │
│ R$ 21.600                      │
│                                │
│ [▼ Encargos detalhados]        │
│ [▼ Simulação demissão]         │
│                                │
│ [Form Lead Capture]            │
└────────────────────────────────┘
```

**Ajustes:**
- Cards stackam 1 coluna (full width - 32px padding)
- Accordion cards pegam 100% width
- Form campos pegam 100% width
- Botão form pega 100% width

✅ Ótimo para mobile.

---

### Teclado Numérico

**Problema:** Números em telefone parecem "texto" ao usuário mobile.

**Solução:**
```html
<input type="number" inputmode="numeric" />
```

✅ Já implementado.

**Teste:** Em iPhone, teclado que aparece deve ser "123" (numérico), não "abc".

---

### Sticky CTA no Mobile

**Problema:** Usuário vê resultado no meio da página, não quer scroll até form.

**Opção A:** Sticky "Agendar com Amanda" no bottom
```
┌─ Page ────────────────────────┐
│                               │
│ [Resultado cards]             │
│ [Accordion 1]                 │
│ [Accordion 2]                 │
│ [Form]                        │
│                               │
└───────────────────────────────┘
┌─ Sticky Bottom ───────────────┐
│ [CTA "Enviar para contadora"] │ ← fixed bottom
└───────────────────────────────┘
```

**Behavior:**
- Aparece após scroll 300px (após resultado)
- Ao clicar, scroll smooth até form
- Ou diretamente submete (se form já preenchido)

**Implementação:** `position: fixed; bottom: 0; width: 100%;`

**Risco:** Oculta content abaixo. Mitigação: padding-bottom na página = espaço para button.

**Decisão:** Adicionar em v1.1 (test).

---

### Comparação de 2 Colunas em Mobile

**Desafio:** Cards CLT | PJ lado a lado não funciona em 375px.

**Soluções:**

**Opção A: Vertical Stack (atual)**
```
[Card CLT]
[Card PJ]
```
Problema: usuário não vê comparação lado a lado.

**Opção B: Swipeable Carousel**
```
┌─ [CLT ●│ PJ ○] ─────────┐
│ Custo Total CLT          │
│ R$ 6.200                 │
│ ← swipe → para ver PJ    │
└──────────────────────────┘
```
Problema: não é óbvio que há 2ª slide.

**Opção C: Tabbed Cards**
```
┌─ [CLT] [PJ] ─────────────┐
│ ◉ CLT ○ PJ                │
│                           │
│ Custo Total CLT           │
│ R$ 6.200                  │
│                           │
│ [Tap para PJ]             │
└───────────────────────────┘
```

**Recomendação:** Opção C (Tabbed). Mais clara que carousel, menos scroll que stack.

---

## 10. FUNCIONALIDADES (MoSCoW)

### MUST HAVE (MVP — v1.0 Release)

- ✅ Campo salário bruto (CLT)
- ✅ Campo segmento empresa (Sistema S)
- ✅ Campos benefícios (VR, VT, Saúde)
- ✅ Checkbox provisões 13º/férias
- ✅ Campo honorário PJ
- ✅ Campo tempo contrato (meses)
- ✅ Botão "Calcular Custo Real"
- ✅ Resultado: 2 cards (CLT | PJ mensal)
- ✅ Resultado: Card diferença anual
- ✅ Accordion: Encargos patronais detalhados
- ✅ Accordion: Simulação demissão
- ✅ Lead form (nome, email, whatsapp, cargo)
- ✅ Success message pós-submissão
- ✅ Validação inputs (salário bruto obrigatório)
- ✅ Responsivo mobile (tabs ou accordion)
- ✅ Schema JSON-LD (WebApplication)

---

### SHOULD HAVE (v1.1 — 2–3 semanas)

- 🟡 Live calculation (atualiza ao sair campo)
- 🟡 Regime tributário da empresa (Simples | LP | LR) — afeta INSS patronal
- 🟡 RAT/FAP (Risco Ambiental do Trabalho) — 1% a 6% por setor
- 🟡 Desoneração da folha (setores específicos: TI, construção)
- 🟡 Modal popup: "Salve seus cálculos" (após 10s visualização resultado)
- 🟡 Botão "Copiar link de resultado" (pré-preenchido na URL)
- 🟡 Tooltips em todos os termos técnicos
- 🟡 Sticky CTA "Agendar" no mobile
- 🟡 A/B test: Form timing (antes vs. depois accordions)
- 🟡 Heat map: quais campos usuário não preenche?

---

### COULD HAVE (v2 — next quarter)

- 💙 Exportar resultado PDF
- 💙 Compartilhar via WhatsApp/Email (pré-preenchido)
- 💙 Terceira via: Contratação intermitente (CLT por projeto)
- 💙 Comparação múltiplos cenários (salário A vs. B)
- 💙 Gráfico visual (pie chart encargos, bar chart anual)
- 💙 Integração com contadores (API para enviar leads)
- 💙 Simulação de impacto de aumento salarial (if salary +10%, impact?)
- 💙 Feedback do usuário embutido ("Isso foi útil?")

---

### WON'T HAVE (Fora do escopo)

- 🚫 Integração com folha de pagamento real
- 🚫 Cálculo de IR pessoa física
- 🚫 Previdência privada / VGBL
- 🚫 Contabilidade complexa (multiestado, exportação)
- 🚫 Dashboard de múltiplas simulações (seria produto diferente)
- 🚫 App mobile nativa (web-first)

---

## 11. COPY CRÍTICA (5 Textos a Reescrever)

### 1. **Atual:** "Segmento da Empresa (afeta aliquota Sistema S)"
**Problema:** "Aliquota Sistema S" é jargão para usuário que não é contador.

**Reescrita:**
```
"Qual é sua atividade principal?"
Subtext: "(afeta contribuições obrigatórias)"
```

**Motivo:**
- Pergunta simples, não técnica
- Subtext explica POR QUÊ (educação leve)
- Usuário não précisa saber "Sistema S"

---

### 2. **Atual:** "No contrato PJ a empresa nao paga INSS patronal, FGTS, 13o salario nem ferias. O risco de reconhecimento de vinculo empregaticio existe se houver subordinacao e exclusividade."

**Problema:** Parágrafo muito denso. "Risco de reconhecimento de vínculo" = linguagem jurídica.

**Reescrita:**
```
Aviso importante: Contrato PJ não gera custo para empresa com INSS, FGTS, 13º ou férias. Mas se a Receita investigar, pode impugnar o contrato se houver:
• Horário fixo (subordinação)
• Exclusividade (proibir outras clientes)
• Benefícios (plano de saúde, VR)

Recomendação: Consultar jurídico antes de contratar PJ.
```

**Motivo:**
- Pontos-chave em bullets (scannable)
- Linguagem simples ("impugnar" em vez de "reconhecimento de vínculo")
- Chamada à ação (consulte jurídico)

---

### 3. **Atual:** "Provisionar 13o e ferias (recomendado)"

**Problema:** Não explica POR QUÊ. Usuário que nunca provisiona acha que está optando.

**Reescrita:**
```
☐ Provisionar 13º e férias obrigadamente
  Sua empresa precisa dessas reservas mensais por lei.
  Se não provisiona: passivo contábil que pode virar multa.
```

**Motivo:**
- "Obrigadamente" (menos soft que "recomendado")
- Explica risco (multa, passivo)
- Usuário quer manter checked

---

### 4. **Atual:** "Resultado orientativo, nao substitui consultoria contabil."

**Problema:** Texto minúsculo no rodapé. Usuário não lê.

**Reescrita:** (Posicionar após botão "Calcular")
```
Os cálculos usam aliquotas INSS patronal, FGTS e Sistema S vigentes em 2025.
Resultado é orientativo. Se sua empresa tem particularidades tributárias 
(regime especial, incentivos fiscais), converse com sua contadora.
```

**Motivo:**
- Mais legível (não em rodapé)
- Explica O QUE é orientativo
- Motiva consulta (já que há variações)

---

### 5. **Atual:** "Clique para ver o custo de cada obrigacao legal"

**Problema:** "Obrigação legal" é genérico. Usuário não sabe se é pra clicar ou ler.

**Reescrita:**
```
"Encargos patronais CLT detalhados"
Subtext: "Clique para ver a fórmula de cada encargo"
```

**Motivo:**
- "Fórmula" é mais concreto (usuário pensa "ah, vou ver como chega em R$ 2.000")
- Menos de jargão ("obrigação")

---

## 12. MÉTRICAS DE SUCESSO

### KPIs Primários (North Star)

#### **KPI 1: Form Submission Rate**
- **Métrica:** % de usuários que chegam até resultado e preenchem form
- **Target v1.0:** 6–8% (baseline: média de calculadoras é 3–5%)
- **Target v1.1:** 10–12% (after optimizations)
- **Como medir:** GA4 event "lead_form_submitted"

#### **KPI 2: Lead Quality (Conversion para Diagnóstico)**
- **Métrica:** % de leads que Amanda marca diagnóstico (whatsapp ou email)
- **Target:** 40–50% (dos leads que submetem form)
- **Como medir:** Integração WA API + CRM manual (Amanda anota)

#### **KPI 3: Cost Per Lead**
- **Métrica:** Custo de publicidade (se houver) / # leads
- **Target:** R$ 50–150 por lead (depende de canal)
- **Como medir:** GA4 + Facebook Ads ROI

---

### KPIs de Engajamento

#### **KPI 4: Time on Page**
- **Métrica:** Tempo médio que usuário fica na página
- **Target:** 3–5 minutos (inclui tempo preenchimento + leitura resultado)
- **Como medir:** GA4 session duration
- **Observação:** Se < 1 min = usuário saiu rápido (problema de UX/copy)

#### **KPI 5: Scroll Depth**
- **Métrica:** % de usuários que scrollam até form
- **Target:** 70%+ (devem ver lead form)
- **Como medir:** GA4 scroll depth event

#### **KPI 6: Accordion Open Rate**
- **Métrica:** % de usuários que abrem accordion "Encargos detalhados"
- **Target:** 30–40% (educação, não crítico)
- **Como medir:** Custom event "accordion_open"

#### **KPI 7: Mobile vs. Desktop Conversion**
- **Métrica:** Form submission rate por device
- **Target:** Desktop 8–10%, Mobile 5–7% (mobile historically lower friction)
- **Como medir:** GA4 segmentation by device

---

### KPIs de Comportamento

#### **KPI 8: Erro de Validação**
- **Métrica:** Quantas vezes usuário clica "Calcular" com campo obrigatório vazio
- **Target:** < 5% (boa copy de erro ou field focus)
- **Como medir:** Custom event "validation_error"
- **Insight:** Se alto = copy de erro não é clara ou campo não é óbvio

#### **KPI 9: Reabrir Calculadora (re-simulation)**
- **Métrica:** % de usuários que modificam input e recalculam
- **Target:** 20–30% (usuário testa cenários)
- **Como medir:** Múltiplos "calculate_click" events por sessão

#### **KPI 10: Form Abandonment**
- **Métrica:** % que clicam em form mas não submetem
- **Target:** < 40% (normal é 50–70% abandonment)
- **Como medir:** GA4 event "form_started" vs "form_submitted"
- **Insight:** Se alto = form é muy larga ou copy não convence

---

### O Que Medir para Saber se Converte

**Método: Funnel Analysis**

```
[100%] Usuários chegam em calculadora
   ↓
[90%] Preenchem salário bruto (engajamento)
   ↓
[75%] Clicam "Calcular" (intent confirmado)
   ↓
[70%] Scrollam até form (awareness de conversão)
   ↓
[8%] Submetem form (lead capturado)
   ↓
[4%] Agendam diagnóstico com Amanda (conversão final)
```

**Teste de sucesso:**
- Semana 1: Baseline (atual)
- Semana 2: Mudança de copy (teste)
- Semana 3: Resultado (compare conversão)

**Exemplo A/B test:**

| Variável | Control | Teste |
|----------|---------|-------|
| Form CTA | "Enviar e agendar com Amanda" | "Enviar e conversaremos via WhatsApp" |
| Expectation | 8% conversion | 10% conversion |
| Winner | — | ← mede após 2 semanas |

---

### Dashboard Ideal (Monitoramento)

```
Calculadora CLT vs PJ — Dashboard

┌─ CONVERSÃO ────────────────────┐
│ Form Submissions (hoje): 24    │
│ Form Submission Rate: 7.2%     │
│ Leads Agendados: 12 (50%)      │
│ CPL (Cost Per Lead): R$ 89     │
└────────────────────────────────┘

┌─ ENGAJAMENTO ──────────────────┐
│ Tempo médio na página: 4m 32s  │
│ Scroll até form: 72%           │
│ Accordion "Encargos" aberto: 34%
│ Erro de validação: 3%          │
└────────────────────────────────┘

┌─ COMPORTAMENTO ────────────────┐
│ Usuários Desktop: 58%          │
│ Usuários Mobile: 42%           │
│ Taxa re-simulação: 28%         │
│ Abandono de form: 32%          │
└────────────────────────────────┘

┌─ TRAFFIC ──────────────────────┐
│ Sessões (hoje): 332            │
│ Usuários novos: 289 (87%)      │
│ Bounce rate: 18%               │
│ Origem: Google Ads (45%)       │
│          Social (30%)           │
│          Direct (25%)           │
└────────────────────────────────┘
```

**Implementação:**
- GA4 com custom events (form_submitted, accordion_open, etc.)
- Looker Studio dashboard (free, integra GA4)
- Sheet manual (Amanda acompanha leads/conversão)

---

## RESUMO EXECUTIVO

### Problemas Diagnosticados
1. **Regime tributário ausente** — Simples Nacional muda INSS (P0)
2. **Multa FGTS incorreta** — Está 40%, deve ser 50% (P0)
3. **Copy técnica demais** — "Aliquota Sistema S" confunde usuário (P1)
4. **RAT/FAP não aparece** — Varia 1%–6% por setor (P1)
5. **Mobile UX confusa** — 2 colunas não funciona em 375px (P1)
6. **Lead form timing** — Aparece tarde (pode perder mobile) (P2)

### Recomendações Prioritárias

**Sprint 1 (v1.0 Release):**
- ✅ Corrigir Multa FGTS (40% → 50%)
- ✅ Reescrever copy técnica (5 pontos identificados)
- ✅ Implementar tabs/accordion mobile (solução escolhida)
- ✅ Adicionar tooltips em termos técnicos
- ✅ Setup GA4 com funnel conversion

**Sprint 2 (v1.1 — 2–3 semanas):**
- 🟡 Adicionar regime tributário (Simples | LP | LR)
- 🟡 Live calculation (atualizar ao sair campo)
- 🟡 RAT/FAP como campo slider/dropdown
- 🟡 Sticky CTA mobile "Agendar"
- 🟡 A/B test: Form copy + timing

**Sprint 3+ (v2):**
- 💙 Exportar PDF
- 💙 Compartilhar resultado
- 💙 Simular aumento salarial
- 💙 Comparação cenários múltiplos

---

**FIM DO PRD**

---

## Apêndice: Guia Rápido para Designers

### Design Tokens Recomendados
- **Cor destaque (resultado):** Dourado (#C9A84C) ou Azul (#3B82F6)
- **Cor erro:** Vermelho (#EF4444)
- **Cor aviso:** Amarelo (#F59E0B)
- **Cor sucesso:** Verde (#10B981)
- **Font corpo:** Inter 400, 500, 600, 700
- **Font display:** Instrument Serif 400 italic (títulos)
- **Spacing:** 8px grid (4px, 8px, 12px, 16px, 24px, 32px)
- **Border radius:** 8px (inputs), 10px (cards), 12px (accordions)
- **Elevation:** Subtle shadow (0 4px 12px rgba(0,0,0,0.08))

### Componentes Reutilizáveis
- **Input numérico:** Com validação inline
- **Select dropdown:** Com ícone customizado
- **Card resultado:** 2 colunas desktop, 1 mobile
- **Accordion:** Header + Body, seta rotativa
- **Form:** 4 campos, botão CTA, mensagem sucesso
- **Tooltip:** Ícone ℹ️ + popup on hover/tap

### Checkpoints de Teste
- ✅ Preenchimento salário bruto = resultado atualiza
- ✅ Mobile 375px: sem overflow horizontal
- ✅ Form submissão = success message
- ✅ Accordion abre/fecha suavemente
- ✅ Botão "Calcular" desativado se salário vazio
- ✅ Cores badge delta (verde/vermelho/cinza)

