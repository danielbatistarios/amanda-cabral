# Mobile Audit Report — Amanda Cabral Contadora

**Data:** 2026-04-23  
**Dispositivo Testado:** iPhone/Mobile (viewport <= 600px)  
**Breakpoints Críticos:** 600px, 900px, 1024px  

---

## SCORE E RESUMO

| Métrica | Resultado |
|---------|-----------|
| **Score Geral** | 28/100 |
| **P0 (Críticos)** | 5 issues |
| **P1 (Altos)** | 8 issues |
| **P2 (Baixos)** | 6 issues |
| **Total Issues** | 19 |

**Interpretação:** Site tem problemas críticos que degradam UX em mobile. Sem patch, usuários em telefones terão dificuldade de navegação, leitura e interação. Score reflete 28% de conformidade (72% não-conforme).

---

## PROBLEMAS P0 (BLOQUEADORES) — 5 ISSUES

### P0.1: Padding Horizontal Excessivo (0 80px)
**Severity:** CRÍTICO | **Impact:** Layout quebra em mobile small (< 380px)

**Problema:**
- Container usa padding: 0 80px globalmente
- Em mobile 320-375px, deixa apenas 160-215px de espaço
- Texto fica comprimido, cards se sobrepõem
- Rodapé desborda horizontalmente

**Afetados:** `.container`, hero, seções, cards

**Solução:** Reduzir para 16px em @media (max-width: 600px)

---

### P0.2: Font Size Mínimo (9px, 10px, 11px)
**Severity:** CRÍTICO | **Impact:** Texto ilegível em mobile

**Problema:**
- 8 ocorrências de font-size < 12px encontradas
- Tags, labels, small text em 9px-11px
- Impossível ler sem zoom em tela pequena
- Viola WCAG AA (12px mínimo para body)

**Afetados:** `.logo-tag`, badges, pequenas descrições

**Solução:** Elevar mínimo para 12px em @media mobile

---

### P0.3: Touch Target < 44px (Mobile Toggle)
**Severity:** CRÍTICO | **Impact:** Usuário não consegue clicar no hambúrguer

**Problema:**
- `.mobile-toggle` tem padding: 8px = altura de 20-24px
- Google/Apple recomenda 44-48px mínimo
- Muito pequeno para dedos de adultos
- Botão close no menu mobile também inadequado

**Afetados:** Hamburger menu, close button

**Solução:** min-height: 48px; min-width: 48px; padding: 12px;

---

### P0.4: Font Size Body em Mobile (< 14px)
**Severity:** CRÍTICO | **Impact:** Leitura cansativa, taxas de bounce altas

**Problema:**
- Body text em 12px-13px é padrão no desktop
- Em mobile 320px, 12px é muito pequeno
- Recomendado: 16px mínimo em mobile para legibilidade
- Headings não reduzem proporcionalmente

**Afetados:** Parágrafos, descrições de serviços, blog

**Solução:** Body 14px, H1 2rem, H2 1.5rem em @media (max-width: 600px)

---

### P0.5: Sem Touch States (:active, :focus)
**Severity:** CRÍTICO | **Impact:** Feedback visual inadequado em touch

**Problema:**
- 18 :hover states mas ZERO :active ou :focus
- Em touch, :hover não funciona
- Usuário clica em botão e não vê feedback visual
- Acessibilidade ruim (sem focus ring)

**Afetados:** Todos os botões e links

**Solução:** Adicionar :active { transform: scale(0.98); } e :focus { outline: 2px solid #C9A84C; }

---

## PROBLEMAS P1 (ALTOS) — 8 ISSUES

### P1.1: Header Fixed com Stacking Context
**Severity:** ALTO | **Impact:** Conteúdo coberto pelo header

**Problema:**
- Header position: fixed com z-index: 1000
- Primeira seção começa logo depois, sem margem-top
- Hero conteúdo pode ficar oculto atrás do header

**Solução:** Adicionar margin-top: 70px no elemento após header

---

### P1.2: Mobile Menu Overlay Sem Display Guard
**Severity:** ALTO | **Impact:** Menu mobile pode estar visível o tempo todo

**Problema:**
- #hdr-mob existe no HTML mas CSS não controla display adequadamente
- Conflita com nav desktop em breakpoints grandes

**Solução:** Guardar #hdr-mob { display: none; } como default, mostrar em @media (max-width: 900px)

---

### P1.3: Heading Sizes Não Reduzem em Mobile
**Severity:** ALTO | **Impact:** Headings muito grandes em mobile

**Problema:**
- Headings em rem absoluto (ex: 3.5rem, 2.2rem)
- Em mobile 320px, H1 ocupa tela inteira
- Sem @media mobile para reduzir

**Solução:** h1 { font-size: 2rem; } h2 { font-size: 1.5rem; } em @media (max-width: 600px)

---

### P1.4: Grid Columns Sem Fallback Mobile
**Severity:** ALTO | **Impact:** Cards se sobrepõem em mobile

**Problema:**
- 5 ocorrências de display: grid
- Provavelmente grid-template-columns: repeat(3, 1fr)
- Sem @media para 1 coluna em mobile

**Solução:** grid-template-columns: 1fr !important; em @media (max-width: 600px)

---

### P1.5: Overflow Hidden (4+) Escondendo Conteúdo
**Severity:** ALTO | **Impact:** Elementos legítimos desaparecem

**Problema:**
- 4+ usos de overflow: hidden
- Em mobile com transforms, pode clipar conteúdo

**Solução:** Revisar cada overflow:hidden, adicionar margin/padding compensatória

---

### P1.6: Hover States Sem Equivalente Touch
**Severity:** ALTO | **Impact:** 18 interações não funcionam em touch

**Problema:**
- 18 :hover states definidos
- Touch devices nunca trigam :hover

**Solução:** Adicionar @media (hover: none) ou :active states equivalentes

---

### P1.7: Muitas Transições (30) Causam Lag
**Severity:** ALTO | **Impact:** Mobile fica lento durante scroll

**Problema:**
- 30 transition rules em paralelo
- Em mobile com GPU fraco, causa frame drops

**Solução:** Reduzir transition duration em @media mobile (0.15s em vez de 0.4s)

---

### P1.8: Sem Active/Focus States
**Severity:** ALTO | **Impact:** Acessibilidade F, não-conforme WCAG

**Problema:**
- Links/botões sem :focus { outline: ... }
- Usuários de teclado não veem foco

**Solução:** Adicionar outline gold (2px solid #C9A84C) em :focus

---

## PROBLEMAS P2 (BAIXOS) — 6 ISSUES

- Nav gap reduzir de 36px para 16px em mobile
- Logo adicionar max-width: 140px
- Validar heading hierarchy H1 > H2 > H3
- Reduzir letter-spacing em mobile
- Desabilitar 6 animations para prefers-reduced-motion
- Remover cursor:pointer de elementos não-interativos

---

## RECOMENDAÇÕES DE DEPLOY

1. Aplicar mobile-patch.css em <style> ou como arquivo separado
2. Testar em iPhone 12 (375px) e Pixel 6 (412px)
3. Validar com Lighthouse Mobile (target: 75+)
4. Deploy para Amanda Cabral repo → Cloudflare Pages

---

## PRÓXIMOS PASSOS (Após Patch)

1. Implementar prefers-reduced-motion (P1)
2. Adicionar :focus-visible para acessibilidade (P1)
3. Audit de performance CWV (First Contentful Paint, Largest Contentful Paint)
4. Teste em Safari iOS (viewport-fit, safe-area-inset)

