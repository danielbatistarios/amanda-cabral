#!/usr/bin/env python3
"""
Header/Footer Rollout — Amanda Cabral
======================================
Uso:
    1. Suba o servidor local:  python3 server.py   (ou: python3 -m http.server 8000)
    2. Edite header/footer/mega-menu na index.html
    3. Rode este script:       python3 apply-header-footer.py
    4. Commit + push:          git add -A && git commit -m "chore: rollout header/footer"

O script lê o header, mega-menu, hdr-mob, footer e script de animação direto do
localhost:8000 (a home) e propaga para todas as páginas ativas.
"""
import re, os, urllib.request

BASE = os.path.dirname(os.path.abspath(__file__))

# ── Fetch source from localhost ──────────────────────────────────────────────
print('Buscando http://localhost:8000 ...')
try:
    content = urllib.request.urlopen('http://localhost:8000').read().decode('utf-8')
except Exception as e:
    print(f'ERRO: não consegui conectar em localhost:8000 — {e}')
    print('Suba o servidor antes de rodar este script.')
    exit(1)

# ── Extract CSS block (HEADER section to end of <style>) ────────────────────
style_start = content.find('<style>') + len('<style>')
style_end   = content.find('</style>')
style_content = content[style_start:style_end]
hdr_section   = style_content.find('HEADER / MEGA-MENU')
comment_start = style_content.rfind('/*', 0, hdr_section)
HEADER_CSS    = style_content[comment_start:]

# ── Extract HTML blocks ──────────────────────────────────────────────────────
hdr_html_start = content.find('<header id="hdr">')
hdr_html_end   = content.find('</header>', hdr_html_start) + len('</header>')
HEADER_HTML    = content[hdr_html_start:hdr_html_end]

mob_start  = content.find('<div id="hdr-mob">')
MEGA_HTML  = content[hdr_html_end:mob_start]   # mega panels between header and hdr-mob

# hdr-mob: count divs to find full closing tag
pos = mob_start + len('<div id="hdr-mob">')
depth = 1
while depth > 0 and pos < len(content):
    next_open  = content.find('<div', pos)
    next_close = content.find('</div>', pos)
    if next_close == -1:
        break
    if next_open != -1 and next_open < next_close:
        depth += 1
        pos = next_open + 4
    else:
        depth -= 1
        pos = next_close + 6
MOB_HTML = content[mob_start:pos]

ftr_start   = content.find('<footer class="site-footer">')
ftr_end     = content.find('</footer>', ftr_start) + len('</footer>')
FOOTER_HTML = content[ftr_start:ftr_end]

# Mega-menu script
pos2 = pos
SCRIPT_HTML = ''
while True:
    s = content.find('<script>', pos2)
    if s == -1:
        break
    e = content.find('</script>', s) + len('</script>')
    chunk = content[s:min(s + 300, e)]
    if 'hdrTimer' in chunk or 'MEGA-MENU' in chunk:
        SCRIPT_HTML = content[s:e]
        break
    pos2 = e

# ── Pages to update ──────────────────────────────────────────────────────────
PAGES = [
    '404.html', 'author.html', 'bio.html',
    'blog/index.html', 'blog/o-que-e-ibs-e-cbs/index.html',
    'casos-de-sucesso/index.html', 'cidades-atendidas/index.html',
    'contabilidade-para-de-minas/index.html', 'fale-com-especialista/index.html',
    'faq-amcabralblindagem.html', 'index.html',
    'nossos-servicos/consultoria-tributaria/index.html',
    'nossos-servicos/gestao-contabil/index.html',
    'nossos-servicos/holding-patrimonial/index.html',
    'nossos-servicos/planejamento-tributario/index.html',
    'nossos-servicos/recuperacao-creditos-tributarios/index.html',
    'para-de-minas-mg/escritorio-de-contabilidade/index.html',
    'politica-de-cookies/index.html', 'politica-de-privacidade/index.html',
    'sobre-amcabral-blindagem/index.html', 'termos-de-uso/index.html',
]


LEGACY_VARS_BLOCK = """  /* legacy template vars */
  --blue-900: #060E1A;
  --blue-700: #0F2137;
  --white: #FFFFFF;
  --gold: #C9A84C;
  --accent-gold: #C4A574;
  --accent-light: #60A5FA;
  --silver: #94A3B8;
  --dark-hero: #0F1419;
  --text: #1E293B;
  --text-muted: #64748B;
  --border: #E2E8F0;
  --font-body: 'Inter', system-ui, sans-serif;
  --font-display: 'Instrument Serif', Georgia, serif;
  --ease: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);"""


def ensure_legacy_vars(c):
    """Inject missing legacy CSS vars into :root so header CSS works on all pages."""
    if '/* legacy template vars */' in c:
        return c
    root_start = c.find(':root {')
    if root_start == -1:
        root_start = c.find(':root{')
    if root_start == -1:
        return c
    pos = c.find('{', root_start) + 1
    depth = 1
    while depth > 0 and pos < len(c):
        nc = c.find('}', pos)
        no = c.find('{', pos)
        if nc == -1:
            break
        if no != -1 and no < nc:
            depth += 1; pos = no + 1
        else:
            depth -= 1; pos = nc + 1
    close_brace = pos - 1
    return c[:close_brace] + '\n' + LEGACY_VARS_BLOCK + '\n' + c[close_brace:]


def fix_image_paths(html, is_subdirectory):
    if is_subdirectory:
        html = html.replace('src="amanda-sobre.webp"', 'src="/amanda-sobre.webp"')
    return html


def remove_old_hdr_css(style_content):
    marker = 'HEADER / MEGA-MENU'
    pos = style_content.find(marker)
    if pos == -1:
        pos = style_content.find('#hdr {')
        if pos == -1:
            pos = style_content.find('#hdr{')
    if pos == -1:
        return style_content
    comment_start = style_content.rfind('/*', 0, pos)
    if comment_start == -1:
        comment_start = pos
    return style_content[:comment_start].rstrip()


def process_page(rel):
    path = os.path.join(BASE, rel)
    if not os.path.exists(path):
        print(f'  SKIP (não encontrado): {rel}')
        return False

    original = open(path, encoding='utf-8').read()
    c = original
    is_sub = rel.count('/') > 0

    mega_html = fix_image_paths(MEGA_HTML, is_sub)
    c = ensure_legacy_vars(c)

    # 1. CSS: inject/replace header CSS in <style> block
    style_s = c.find('<style>')
    style_e = c.find('</style>')
    if style_s != -1 and style_e != -1:
        inner       = c[style_s + len('<style>'):style_e]
        inner_clean = remove_old_hdr_css(inner)
        new_inner   = inner_clean + '\n\n' + HEADER_CSS
        c = c[:style_s + len('<style>')] + new_inner + c[style_e:]
    else:
        inject = f'<style>\n{HEADER_CSS}\n</style>'
        c = c.replace('</head>', inject + '\n</head>', 1)

    # 2. Remove existing mega + hdr-mob blocks
    for panel_id in ['mega-sobre', 'mega-servicos', 'mega-blog']:
        start_tag = f'<div class="hdr-mega" id="{panel_id}">'
        p = c.find(start_tag)
        if p != -1:
            pos = p + len(start_tag)
            depth = 1
            while depth > 0 and pos < len(c):
                no = c.find('<div', pos)
                nc = c.find('</div>', pos)
                if nc == -1:
                    break
                if no != -1 and no < nc:
                    depth += 1; pos = no + 4
                else:
                    depth -= 1; pos = nc + 6
            c = c[:p] + c[pos:]

    # Remove hdr-mob (div or nav tag)
    for mob_tag in ['<div id="hdr-mob">', '<nav id="hdr-mob">']:
        close_tag = '</div>' if mob_tag.startswith('<div') else '</nav>'
        mob_s = c.find(mob_tag)
        if mob_s != -1:
            pos = mob_s + len(mob_tag)
            depth = 1
            open_tag_name = mob_tag[1:4]  # 'div' or 'nav'
            while depth > 0 and pos < len(c):
                no = c.find(f'<{open_tag_name}', pos)
                nc = c.find(close_tag, pos)
                if nc == -1:
                    break
                if no != -1 and no < nc:
                    depth += 1; pos = no + len(open_tag_name) + 1
                else:
                    depth -= 1; pos = nc + len(close_tag)
            c = c[:mob_s] + c[pos:]

    # 3. Replace <header> block
    hdr_s = c.find('<header')
    if hdr_s != -1:
        hdr_e = c.find('</header>', hdr_s) + len('</header>')
        replacement = HEADER_HTML + '\n\n' + mega_html + '\n\n' + MOB_HTML
        c = c[:hdr_s] + replacement + c[hdr_e:]
    else:
        body_tag = c.find('<body')
        if body_tag != -1:
            body_end = c.find('>', body_tag) + 1
            replacement = '\n' + HEADER_HTML + '\n\n' + mega_html + '\n\n' + MOB_HTML + '\n'
            c = c[:body_end] + replacement + c[body_end:]

    # 4. Replace <footer class="site-footer"> (remove all, inject once)
    while True:
        ftr_s = c.find('<footer class="site-footer">')
        if ftr_s == -1:
            break
        ftr_e = c.find('</footer>', ftr_s) + len('</footer>')
        c = c[:ftr_s] + c[ftr_e:]

    body_close = c.rfind('</body>')
    if body_close != -1:
        c = c[:body_close] + '\n' + FOOTER_HTML + '\n' + c[body_close:]
    else:
        c += '\n' + FOOTER_HTML

    # 5. Replace/inject mega-menu script
    if SCRIPT_HTML:
        while True:
            s = c.rfind('<script>')
            if s == -1:
                break
            e = c.find('</script>', s) + len('</script>')
            chunk = c[s:min(s + 400, e)]
            if 'hdrTimer' in chunk or 'hdr-hamburger' in chunk or 'closeAll' in chunk:
                c = c[:s] + c[e:]
                break
            else:
                break
        body_close2 = c.rfind('</body>')
        if body_close2 != -1:
            c = c[:body_close2] + '\n' + SCRIPT_HTML + '\n' + c[body_close2:]

    changed = c != original
    if changed:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(c)
    print(f'  {"ATUALIZADO" if changed else "sem mudança"}: {rel}')
    return changed


# ── Run ──────────────────────────────────────────────────────────────────────
print()
print('=== Header/Footer Rollout — Amanda Cabral ===')
print(f'Páginas: {len(PAGES)}')
print()

updated = 0
for rel in PAGES:
    changed = process_page(rel)
    if changed:
        updated += 1

print()
print(f'Concluído. {updated}/{len(PAGES)} páginas atualizadas.')
if updated > 0:
    print()
    print('Próximos passos:')
    print('  git add -A')
    print('  git commit -m "chore: rollout header/footer global"')
    print('  git push origin main')
