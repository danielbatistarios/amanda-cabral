#!/usr/bin/env node

import { readFileSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';

const BASE_DIR = '/Users/jrios/amanda-cabral-contadora';

const NEW_HEADER = `<header class="site-header" id="siteHeader">
  <nav class="site-nav" aria-label="Navegação principal">
    <a href="/" class="nav-logo">AM Cabral</a>

    <ul class="nav-links" id="navLinks">
      <!-- Dropdown: Serviços -->
      <li class="nav-item has-dropdown">
        <button class="nav-trigger" aria-expanded="false" aria-haspopup="true">
          Serviços <span class="nav-arrow" aria-hidden="true">▼</span>
        </button>
        <div class="nav-dropdown" role="menu">
          <a href="/gestao-contabil-para-industrias/" role="menuitem">Gestão Contábil Estratégica</a>
          <a href="/recuperacao-de-creditos-tributarios/" role="menuitem">Recuperação de Créditos</a>
          <a href="/holding-patrimonial-e-familiar/" role="menuitem">Holding Patrimonial e Familiar</a>
          <a href="/planejamento-tributario/" role="menuitem">Planejamento Tributário</a>
          <a href="/consultoria-tributaria/" role="menuitem">Consultoria Tributária</a>
          <a href="/servicos/" class="dropdown-all" role="menuitem">Ver todos os serviços →</a>
        </div>
      </li>

      <!-- Link direto -->
      <li class="nav-item"><a href="/reforma-tributaria/">Reforma Tributária</a></li>
      <li class="nav-item"><a href="/blog/">Blog</a></li>

      <!-- Dropdown: Sobre -->
      <li class="nav-item has-dropdown">
        <button class="nav-trigger" aria-expanded="false" aria-haspopup="true">
          Sobre <span class="nav-arrow" aria-hidden="true">▼</span>
        </button>
        <div class="nav-dropdown" role="menu">
          <a href="/sobre/" role="menuitem">Amanda Silva</a>
          <a href="/casos-de-sucesso/" role="menuitem">Casos de Sucesso</a>
          <a href="/depoimentos/" role="menuitem">Depoimentos</a>
        </div>
      </li>

      <li class="nav-item"><a href="/contato/">Contato</a></li>
    </ul>

    <!-- CTA -->
    <a href="/diagnostico-gratuito/" class="nav-cta">Diagnóstico Gratuito</a>

    <!-- Hamburger mobile -->
    <button class="nav-hamburger" id="navHamburger" aria-label="Abrir menu" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
  </nav>
</header>

<!-- Mobile overlay -->
<div class="mobile-nav" id="mobileNav" aria-hidden="true">
  <button class="mobile-nav-close" id="mobileNavClose" aria-label="Fechar menu">✕</button>
  <a href="/gestao-contabil-para-industrias/">Gestão Contábil Estratégica</a>
  <a href="/recuperacao-de-creditos-tributarios/">Recuperação de Créditos</a>
  <a href="/holding-patrimonial-e-familiar/">Holding Patrimonial e Familiar</a>
  <a href="/planejamento-tributario/">Planejamento Tributário</a>
  <a href="/consultoria-tributaria/">Consultoria Tributária</a>
  <a href="/servicos/">Ver todos os serviços</a>
  <a href="/reforma-tributaria/">Reforma Tributária</a>
  <a href="/blog/">Blog</a>
  <a href="/sobre/">Amanda Silva</a>
  <a href="/casos-de-sucesso/">Casos de Sucesso</a>
  <a href="/depoimentos/">Depoimentos</a>
  <a href="/contato/">Contato</a>
  <a href="/diagnostico-gratuito/" style="color: var(--accent-gold); margin-top: 20px; font-weight: 600;">Diagnóstico Gratuito</a>
</div>`;

const NEW_FOOTER = `<footer class="site-footer">
  <div class="footer-inner">
    <div class="footer-grid">
      <!-- Col 1: A Empresa -->
      <div class="footer-col">
        <h3 class="footer-heading">A Empresa</h3>
        <ul>
          <li><a href="/sobre/">Sobre Amanda Silva</a></li>
          <li><a href="/casos-de-sucesso/">Casos de Sucesso</a></li>
          <li><a href="/depoimentos/">Depoimentos</a></li>
          <li><a href="/faq/">FAQ</a></li>
          <li><a href="/contato/">Contato</a></li>
        </ul>
      </div>

      <!-- Col 2: Serviços -->
      <div class="footer-col">
        <h3 class="footer-heading">Serviços</h3>
        <ul>
          <li><a href="/gestao-contabil-para-industrias/">Gestão Contábil Estratégica</a></li>
          <li><a href="/recuperacao-de-creditos-tributarios/">Recuperação de Créditos</a></li>
          <li><a href="/holding-patrimonial-e-familiar/">Holding Patrimonial e Familiar</a></li>
          <li><a href="/planejamento-tributario/">Planejamento Tributário</a></li>
          <li><a href="/consultoria-tributaria/">Consultoria Tributária</a></li>
        </ul>
      </div>

      <!-- Col 3: Conteúdo -->
      <div class="footer-col">
        <h3 class="footer-heading">Conteúdo</h3>
        <ul>
          <li><a href="/blog/">Blog</a></li>
          <li><a href="/reforma-tributaria/">Reforma Tributária</a></li>
          <li><a href="/faq/">FAQ</a></li>
        </ul>
      </div>

      <!-- Col 4: Regiões -->
      <div class="footer-col">
        <h3 class="footer-heading">Regiões Atendidas</h3>
        <ul>
          <li><a href="/contabilidade-industrial-belo-horizonte/">Belo Horizonte</a></li>
          <li><a href="/contabilidade-industrial-sao-paulo/">São Paulo</a></li>
          <li><a href="/contabilidade-industrial-rio-de-janeiro/">Rio de Janeiro</a></li>
          <li><a href="/contabilidade-industrial-vale-do-aco/">Vale do Aço</a></li>
          <li><a href="/regioes-atendidas/">Ver todas →</a></li>
        </ul>
      </div>
    </div>

    <!-- Separador + Logo + CTA -->
    <div class="footer-brand">
      <a href="/" class="footer-logo">AM Cabral</a>
      <a href="/diagnostico-gratuito/" class="footer-cta">Diagnóstico Gratuito</a>
    </div>

    <!-- Barra legal -->
    <div class="footer-legal">
      <p>© 2026 Amanda Silva Cabral Contabilidade. CRC/MG ativo.</p>
      <div class="footer-legal-links">
        <a href="/politica-de-privacidade/">Política de Privacidade</a>
        <a href="/politica-de-cookies/">Política de Cookies</a>
        <a href="/termos-de-uso/">Termos de Uso</a>
      </div>
    </div>
  </div>
</footer>`;

const filesToUpdate = [
  'author.html',
  'bio.html',
  'consultoria-tributaria.html',
  'faq.html',
  'gestao-contabil-industrial.html',
  'holding-patrimonial.html',
  'home-v2-modern.html',
  'home-v3.html',
  'planejamento-tributario.html',
  'recuperacao-creditos-tributarios.html',
  'servicos.html',
  'teste-dourado.html',
  'calculadora-pj-vs-clt/index.html',
];

function replaceHeaderFooter(filePath) {
  let content = readFileSync(filePath, 'utf-8');

  // Replace header - look for <header ... </header> or similar pattern
  const headerRegex = /<header[^>]*>[\s\S]*?<\/header>/;
  content = content.replace(headerRegex, NEW_HEADER);

  // Replace footer - look for <footer ... </footer>
  const footerRegex = /<footer[^>]*>[\s\S]*?<\/footer>/;
  content = content.replace(footerRegex, NEW_FOOTER);

  writeFileSync(filePath, content, 'utf-8');
}

console.log('🔄 Aplicando novo header/footer...\n');

filesToUpdate.forEach(file => {
  const filePath = join(BASE_DIR, file);
  try {
    replaceHeaderFooter(filePath);
    console.log(`✓ ${file}`);
  } catch (e) {
    console.error(`✗ ${file} — ${e.message}`);
  }
});

console.log('\n✅ Concluído!');
