#!/usr/bin/env node

import { readFileSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';

const BASE_DIR = '/Users/jrios/amanda-cabral-contadora';

const filesToUpdate = [
  'author.html',
  'bio.html',
  'consultoria-tributaria.html',
  'faq.html',
  'gestao-contabil-industrial.html',
  'holding-patrimonial.html',
  'home-v2-modern.html',
  'home-v3.html',
  'index.html',
  'planejamento-tributario.html',
  'recuperacao-creditos-tributarios.html',
  'servicos.html',
  'teste-dourado.html',
];

console.log('🔄 Enhancing mobile-nav with visibility delay...\n');

filesToUpdate.forEach(file => {
  const filePath = join(BASE_DIR, file);
  try {
    let content = readFileSync(filePath, 'utf-8');

    // Check if it already has the enhanced version
    if (content.includes('visibility: hidden;') && content.includes('visibility 0.3s')) {
      console.log(`⊗ ${file} — already enhanced`);
      return;
    }

    // Replace the old mobile-nav CSS
    const oldPattern = /\.mobile-nav\s*{\s*position:\s*fixed;\s*inset:\s*0;[^}]*?transition:\s*opacity\s*0\.3s;/s;
    const newCSS = `.mobile-nav {
      position: fixed;
      inset: 0;
      background: var(--dark-hero);
      z-index: 99;
      display: flex;
      flex-direction: column;
      padding: 80px 24px 24px;
      overflow-y: auto;
      opacity: 0;
      visibility: hidden;
      pointer-events: none;
      transition: opacity 0.3s ease, visibility 0.3s;`;

    if (oldPattern.test(content)) {
      content = content.replace(oldPattern, newCSS);

      // Also update the .is-open state
      const openPattern = /\.mobile-nav\.is-open\s*{\s*opacity:\s*1;[^}]*?pointer-events:\s*auto;/s;
      const newOpen = `.mobile-nav.is-open {
      opacity: 1;
      visibility: visible;
      pointer-events: auto;`;

      content = content.replace(openPattern, newOpen);
      writeFileSync(filePath, content, 'utf-8');
      console.log(`✓ ${file}`);
    } else {
      console.log(`⚠ ${file} — pattern not found, skipping`);
    }
  } catch (e) {
    console.error(`✗ ${file} — ${e.message}`);
  }
});

console.log('\n✅ Done!');
