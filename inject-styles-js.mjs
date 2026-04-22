#!/usr/bin/env node

import { readFileSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';

const BASE_DIR = '/Users/jrios/amanda-cabral-contadora';

const CSS_INJECTION = `
        /* === NEW SITE HEADER & FOOTER === */
        .site-header {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background: linear-gradient(to bottom, rgba(15, 20, 25, 0.95), rgba(15, 20, 25, 0.8));
            z-index: 100;
            padding: 16px 0;
            border-bottom: 1px solid rgba(255,255,255,0.08);
            backdrop-filter: blur(8px);
        }

        .site-nav {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 48px;
        }

        .nav-logo {
            font-family: 'Instrument Serif', Georgia, serif;
            font-size: 18px;
            font-weight: 700;
            letter-spacing: 0.02em;
            color: #FFFFFF;
            white-space: nowrap;
        }

        .nav-links {
            display: flex;
            gap: 8px;
            list-style: none;
            flex: 1;
            align-items: center;
        }

        .nav-item {
            position: relative;
        }

        .nav-item > a {
            font-size: 13px;
            font-weight: 500;
            color: #A8B5C6;
            padding: 8px 12px;
            transition: color 0.3s ease;
            display: block;
        }

        .nav-item > a:hover {
            color: #C4A574;
        }

        .nav-trigger {
            font-size: 13px;
            font-weight: 500;
            color: #A8B5C6;
            background: none;
            border: none;
            padding: 8px 12px;
            cursor: pointer;
            transition: color 0.3s ease;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .nav-trigger:hover {
            color: #C4A574;
        }

        .nav-arrow {
            font-size: 10px;
            transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .nav-item.is-open .nav-arrow {
            transform: rotate(180deg);
        }

        .nav-dropdown {
            position: absolute;
            top: calc(100% + 12px);
            left: 0;
            background: #1A2535;
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 4px;
            min-width: 240px;
            padding: 8px 0;
            opacity: 0;
            pointer-events: none;
            transform: translateY(-8px);
            transition: opacity 0.25s, transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
            box-shadow: 0 8px 32px rgba(0,0,0,0.2);
        }

        .nav-item.has-dropdown:hover .nav-dropdown,
        .nav-item.has-dropdown:focus-within .nav-dropdown {
            opacity: 1;
            pointer-events: auto;
            transform: translateY(0);
        }

        .nav-dropdown a {
            display: block;
            padding: 10px 16px;
            font-size: 13px;
            color: #A8B5C6;
            transition: color 0.2s;
        }

        .nav-dropdown a:hover {
            color: #C4A574;
        }

        .dropdown-all {
            border-top: 1px solid rgba(255,255,255,0.04);
            margin-top: 4px;
            padding-top: 10px;
            color: #C4A574 !important;
        }

        .nav-cta {
            display: inline-block;
            padding: 10px 24px;
            background: #C4A574;
            color: #0F1419;
            font-weight: 600;
            font-size: 12px;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            border: none;
            cursor: pointer;
            border-radius: 4px;
            white-space: nowrap;
        }

        .nav-cta:hover {
            transform: translateY(-2px);
            box-shadow: 0 12px 32px rgba(196, 165, 116, 0.2);
        }

        .nav-hamburger {
            display: none;
            flex-direction: column;
            gap: 5px;
            background: none;
            border: none;
            padding: 8px;
            cursor: pointer;
        }

        .nav-hamburger span {
            width: 20px;
            height: 2px;
            background: #FFFFFF;
            border-radius: 2px;
            transition: all 0.3s;
        }

        .mobile-nav {
            position: fixed;
            inset: 0;
            background: #0F1419;
            z-index: 99;
            display: flex;
            flex-direction: column;
            padding: 80px 24px 24px;
            overflow-y: auto;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.3s;
        }

        .mobile-nav.is-open {
            opacity: 1;
            pointer-events: auto;
        }

        .mobile-nav-close {
            position: absolute;
            top: 24px;
            right: 24px;
            background: none;
            border: none;
            color: #FFFFFF;
            font-size: 28px;
            cursor: pointer;
            padding: 4px;
        }

        .mobile-nav a {
            padding: 12px 0;
            font-size: 16px;
            color: #A8B5C6;
            border-bottom: 1px solid rgba(255,255,255,0.04);
        }

        .mobile-nav a:hover {
            color: #C4A574;
        }

        @media (max-width: 900px) {
            .nav-links {
                display: none;
            }

            .nav-cta {
                display: none;
            }

            .nav-hamburger {
                display: flex;
            }
        }

        @media (max-width: 600px) {
            .site-nav {
                padding: 0 16px;
                gap: 24px;
            }

            .nav-logo {
                font-size: 16px;
            }
        }

        /* === FOOTER === */
        .site-footer {
            background: #0F1419;
            border-top: 1px solid rgba(255,255,255,0.08);
            padding: 72px 0 32px;
            margin-top: 80px;
        }

        .footer-inner {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 24px;
        }

        .footer-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 48px;
            margin-bottom: 56px;
        }

        .footer-col {
            display: flex;
            flex-direction: column;
        }

        .footer-heading {
            font-size: 0.65rem;
            font-weight: 700;
            letter-spacing: 0.15em;
            text-transform: uppercase;
            color: #C4A574;
            margin-bottom: 20px;
        }

        .footer-col ul {
            list-style: none;
        }

        .footer-col a {
            display: block;
            font-size: 0.875rem;
            color: #A8B5C6;
            margin-bottom: 10px;
            transition: color 0.2s;
        }

        .footer-col a:hover {
            color: #FFFFFF;
        }

        .footer-brand {
            border-top: 1px solid rgba(255,255,255,0.08);
            padding: 32px 0;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .footer-logo {
            font-family: 'Instrument Serif', Georgia, serif;
            font-size: 1.25rem;
            color: #FFFFFF;
        }

        .footer-cta {
            display: inline-block;
            padding: 12px 28px;
            background: #C4A574;
            color: #0F1419;
            font-weight: 600;
            font-size: 0.8rem;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            cursor: pointer;
            border: none;
        }

        .footer-cta:hover {
            box-shadow: 0 8px 24px rgba(196, 165, 116, 0.2);
        }

        .footer-legal {
            border-top: 1px solid rgba(255,255,255,0.05);
            padding-top: 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 12px;
        }

        .footer-legal p,
        .footer-legal-links a {
            font-size: 0.75rem;
            color: rgba(255,255,255,0.2);
        }

        .footer-legal-links {
            display: flex;
            gap: 20px;
        }

        .footer-legal-links a:hover {
            color: #C4A574;
        }

        @media (max-width: 900px) {
            .footer-grid {
                grid-template-columns: repeat(2, 1fr);
                gap: 32px;
            }
        }

        @media (max-width: 600px) {
            .site-footer {
                padding: 48px 0 24px;
            }

            .footer-inner {
                padding: 0 16px;
            }

            .footer-grid {
                grid-template-columns: 1fr;
                gap: 24px;
            }

            .footer-brand {
                flex-direction: column;
                gap: 20px;
                text-align: center;
            }

            .footer-legal {
                flex-direction: column;
                gap: 12px;
                text-align: center;
            }

            .footer-legal-links {
                flex-wrap: wrap;
                justify-content: center;
            }
        }`;

const JS_INJECTION = `<script>
(function(){
  document.querySelectorAll('.nav-trigger').forEach(btn => {
    btn.addEventListener('click', function(){
      const item = this.closest('.nav-item');
      const expanded = item.classList.toggle('is-open');
      this.setAttribute('aria-expanded', expanded);
      document.querySelectorAll('.nav-item.has-dropdown').forEach(other => {
        if(other !== item){
          other.classList.remove('is-open');
          other.querySelector('.nav-trigger').setAttribute('aria-expanded','false');
        }
      });
    });
  });

  document.addEventListener('click', e => {
    if(!e.target.closest('.has-dropdown')){
      document.querySelectorAll('.nav-item.has-dropdown').forEach(item => {
        item.classList.remove('is-open');
        item.querySelector('.nav-trigger').setAttribute('aria-expanded','false');
      });
    }
  });

  const hamburger = document.getElementById('navHamburger');
  const mobileNav = document.getElementById('mobileNav');
  const mobileClose = document.getElementById('mobileNavClose');

  function openMobile(){
    mobileNav.classList.add('is-open');
    mobileNav.setAttribute('aria-hidden','false');
    hamburger.setAttribute('aria-expanded','true');
    document.body.style.overflow='hidden';
  }
  function closeMobile(){
    mobileNav.classList.remove('is-open');
    mobileNav.setAttribute('aria-hidden','true');
    hamburger.setAttribute('aria-expanded','false');
    document.body.style.overflow='';
  }

  hamburger.addEventListener('click', openMobile);
  mobileClose.addEventListener('click', closeMobile);
  mobileNav.querySelectorAll('a').forEach(a => a.addEventListener('click', closeMobile));
})();
</script>`;

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
];

function injectCSS(filePath) {
  let content = readFileSync(filePath, 'utf-8');

  // Find the closing </style> tag and inject before it
  const styleCloseIdx = content.lastIndexOf('</style>');
  if (styleCloseIdx === -1) return false;

  content = content.slice(0, styleCloseIdx) + CSS_INJECTION + '\n    </style>' + content.slice(styleCloseIdx + 8);
  writeFileSync(filePath, content, 'utf-8');
  return true;
}

function injectJS(filePath) {
  let content = readFileSync(filePath, 'utf-8');

  // Inject before closing </body> tag
  const bodyCloseIdx = content.lastIndexOf('</body>');
  if (bodyCloseIdx === -1) return false;

  content = content.slice(0, bodyCloseIdx) + '\n' + JS_INJECTION + '\n' + content.slice(bodyCloseIdx);
  writeFileSync(filePath, content, 'utf-8');
  return true;
}

console.log('💉 Injetando CSS e JS...\n');

filesToUpdate.forEach(file => {
  const filePath = join(BASE_DIR, file);
  try {
    const cssOk = injectCSS(filePath);
    const jsOk = injectJS(filePath);

    if (cssOk && jsOk) {
      console.log(`✓ ${file}`);
    } else {
      console.warn(`⚠ ${file} — CSS: ${cssOk ? 'OK' : 'SKIP'}, JS: ${jsOk ? 'OK' : 'SKIP'}`);
    }
  } catch (e) {
    console.error(`✗ ${file} — ${e.message}`);
  }
});

console.log('\n✅ Concluído!');
