"""
Adiciona marquees de autoridade e serviços + cross-link section + cross pattern CTA
a todas as 5 LPs de serviço da Amanda.
Executar APÓS os agents criarem os arquivos.
"""
import os

LP_FILES = [
    'gestao-contabil-industrial.html',
    'recuperacao-creditos-tributarios.html',
    'holding-patrimonial.html',
    'planejamento-tributario.html',
    'consultoria-tributaria.html',
]

MARQUEE_CREDENCIAIS = '''
<!-- MARQUEE CREDENCIAIS -->
<div style="overflow:hidden;padding:14px 0;position:relative;border-top:1px solid rgba(255,255,255,.04);border-bottom:1px solid rgba(255,255,255,.04);background:#060E1A">
  <div style="position:absolute;top:0;bottom:0;left:0;width:80px;z-index:2;background:linear-gradient(90deg,#060E1A,transparent)"></div>
  <div style="position:absolute;top:0;bottom:0;right:0;width:80px;z-index:2;background:linear-gradient(-90deg,#060E1A,transparent)"></div>
  <div class="mq-cred">
    <span class="mqi"><span class="mqd"></span>CRC/MG Ativo</span>
    <span class="mqi"><span class="mqd"></span>30 Anos de Experiência</span>
    <span class="mqi"><span class="mqd"></span>Especialista ICMS/IPI</span>
    <span class="mqi"><span class="mqd"></span>Pós em Direito Tributário</span>
    <span class="mqi"><span class="mqd"></span>Membro IBPT</span>
    <span class="mqi"><span class="mqd"></span>120+ Indústrias Atendidas</span>
    <span class="mqi"><span class="mqd"></span>R$ 12M+ Recuperados</span>
    <span class="mqi"><span class="mqd"></span>Pará de Minas · MG</span>
    <span class="mqi"><span class="mqd"></span>CRC/MG Ativo</span>
    <span class="mqi"><span class="mqd"></span>30 Anos de Experiência</span>
    <span class="mqi"><span class="mqd"></span>Especialista ICMS/IPI</span>
    <span class="mqi"><span class="mqd"></span>Pós em Direito Tributário</span>
    <span class="mqi"><span class="mqd"></span>Membro IBPT</span>
    <span class="mqi"><span class="mqd"></span>120+ Indústrias Atendidas</span>
    <span class="mqi"><span class="mqd"></span>R$ 12M+ Recuperados</span>
    <span class="mqi"><span class="mqd"></span>Pará de Minas · MG</span>
  </div>
</div>
'''

MARQUEE_GOLD = '''
<!-- MARQUEE GOLD SERVIÇOS -->
<div style="overflow:hidden;padding:12px 0;position:relative;background:#C9A84C">
  <div style="position:absolute;top:0;bottom:0;left:0;width:80px;z-index:2;background:linear-gradient(90deg,#C9A84C,transparent)"></div>
  <div style="position:absolute;top:0;bottom:0;right:0;width:80px;z-index:2;background:linear-gradient(-90deg,#C9A84C,transparent)"></div>
  <div class="mq-gold">
    <span class="mqgi"><span class="mqgd"></span>Gestão Contábil Estratégica</span>
    <span class="mqgi"><span class="mqgd"></span>Recuperação de Créditos Tributários</span>
    <span class="mqgi"><span class="mqgd"></span>Holding Patrimonial e Familiar</span>
    <span class="mqgi"><span class="mqgd"></span>Planejamento Tributário</span>
    <span class="mqgi"><span class="mqgd"></span>Consultoria Tributária</span>
    <span class="mqgi"><span class="mqgd"></span>Compliance Fiscal</span>
    <span class="mqgi"><span class="mqgd"></span>ICMS · IPI · PIS/COFINS</span>
    <span class="mqgi"><span class="mqgd"></span>Incentivos Fiscais MG</span>
    <span class="mqgi"><span class="mqgd"></span>Gestão Contábil Estratégica</span>
    <span class="mqgi"><span class="mqgd"></span>Recuperação de Créditos Tributários</span>
    <span class="mqgi"><span class="mqgd"></span>Holding Patrimonial e Familiar</span>
    <span class="mqgi"><span class="mqgd"></span>Planejamento Tributário</span>
    <span class="mqgi"><span class="mqgd"></span>Consultoria Tributária</span>
    <span class="mqgi"><span class="mqgd"></span>Compliance Fiscal</span>
    <span class="mqgi"><span class="mqgd"></span>ICMS · IPI · PIS/COFINS</span>
    <span class="mqgi"><span class="mqgd"></span>Incentivos Fiscais MG</span>
  </div>
</div>
'''

MARQUEE_CSS = '''
/* === MARQUEES === */
.mq-cred{display:flex;gap:36px;animation:mqc 28s linear infinite;width:max-content}
.mq-cred:hover{animation-play-state:paused}
@keyframes mqc{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}
.mqi{display:flex;align-items:center;gap:10px;font-size:11px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:rgba(255,255,255,.25);white-space:nowrap}
.mqd{width:4px;height:4px;border-radius:50%;background:#3B82F6;opacity:.5}
.mq-gold{display:flex;gap:36px;animation:mqg 32s linear infinite;width:max-content}
.mq-gold:hover{animation-play-state:paused}
@keyframes mqg{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}
.mqgi{display:flex;align-items:center;gap:10px;font-size:12px;font-weight:700;letter-spacing:.04em;color:#060E1A;white-space:nowrap}
.mqgd{width:5px;height:5px;border-radius:50%;background:#060E1A;opacity:.2}
'''

CROSS_LINKS = {
    'gestao-contabil-industrial.html': [
        ('Recuperação de Créditos Tributários', '/recuperacao-creditos-tributarios/', '#38BDF8', 'PIS/COFINS, ICMS, IPI — até 5 anos retroativos'),
        ('Holding Patrimonial e Familiar', '/constituicao-de-holding-patrimonial-e-familiar/', '#C9A84C', 'Proteja seu patrimônio e planeje a sucessão'),
        ('Planejamento Tributário', '/planejamento-tributario-industrial/', '#60A5FA', 'Regime ideal, incentivos MG, elisão fiscal'),
        ('Consultoria Tributária', '/consultoria-tributaria/', '#94A3B8', 'Compliance fiscal e preparação reforma 2026'),
    ],
    'recuperacao-creditos-tributarios.html': [
        ('Gestão Contábil Estratégica', '/gestao-contabil-industrial/', '#3B82F6', 'Balanços, DRE, custos, folha — visão estratégica'),
        ('Holding Patrimonial e Familiar', '/constituicao-de-holding-patrimonial-e-familiar/', '#C9A84C', 'Proteja seu patrimônio e planeje a sucessão'),
        ('Planejamento Tributário', '/planejamento-tributario-industrial/', '#60A5FA', 'Regime ideal, incentivos MG, elisão fiscal'),
        ('Consultoria Tributária', '/consultoria-tributaria/', '#94A3B8', 'Compliance fiscal e preparação reforma 2026'),
    ],
    'holding-patrimonial.html': [
        ('Gestão Contábil Estratégica', '/gestao-contabil-industrial/', '#3B82F6', 'Balanços, DRE, custos, folha — visão estratégica'),
        ('Recuperação de Créditos Tributários', '/recuperacao-creditos-tributarios/', '#38BDF8', 'PIS/COFINS, ICMS, IPI — até 5 anos retroativos'),
        ('Planejamento Tributário', '/planejamento-tributario-industrial/', '#60A5FA', 'Regime ideal, incentivos MG, elisão fiscal'),
        ('Consultoria Tributária', '/consultoria-tributaria/', '#94A3B8', 'Compliance fiscal e preparação reforma 2026'),
    ],
    'planejamento-tributario.html': [
        ('Gestão Contábil Estratégica', '/gestao-contabil-industrial/', '#3B82F6', 'Balanços, DRE, custos, folha — visão estratégica'),
        ('Recuperação de Créditos Tributários', '/recuperacao-creditos-tributarios/', '#38BDF8', 'PIS/COFINS, ICMS, IPI — até 5 anos retroativos'),
        ('Holding Patrimonial e Familiar', '/constituicao-de-holding-patrimonial-e-familiar/', '#C9A84C', 'Proteja seu patrimônio e planeje a sucessão'),
        ('Consultoria Tributária', '/consultoria-tributaria/', '#94A3B8', 'Compliance fiscal e preparação reforma 2026'),
    ],
    'consultoria-tributaria.html': [
        ('Gestão Contábil Estratégica', '/gestao-contabil-industrial/', '#3B82F6', 'Balanços, DRE, custos, folha — visão estratégica'),
        ('Recuperação de Créditos Tributários', '/recuperacao-creditos-tributarios/', '#38BDF8', 'PIS/COFINS, ICMS, IPI — até 5 anos retroativos'),
        ('Holding Patrimonial e Familiar', '/constituicao-de-holding-patrimonial-e-familiar/', '#C9A84C', 'Proteja seu patrimônio e planeje a sucessão'),
        ('Planejamento Tributário', '/planejamento-tributario-industrial/', '#60A5FA', 'Regime ideal, incentivos MG, elisão fiscal'),
    ],
}

CROSS_PATTERN = 'background-image:url("data:image/svg+xml,%3Csvg width=\'60\' height=\'60\' viewBox=\'0 0 60 60\' xmlns=\'http://www.w3.org/2000/svg\'%3E%3Cg fill=\'none\' fill-rule=\'evenodd\'%3E%3Cg fill=\'%23ffffff\' fill-opacity=\'0.04\'%3E%3Cpath d=\'M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z\'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E")'

BASE = '/Users/jrios/amanda-cabral-contadora'

for fname in LP_FILES:
    fpath = os.path.join(BASE, fname)
    if not os.path.exists(fpath):
        print(f"⏭️  {fname} — não encontrado (agent ainda rodando?)")
        continue

    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    changes = 0

    # 1. Add marquee CSS before </style>
    if '.mq-cred' not in html and '</style>' in html:
        html = html.replace('</style>', MARQUEE_CSS + '</style>', 1)
        changes += 1

    # 2. Add marquee credenciais after hero </section>
    if 'mq-cred' not in html:
        # Find first </section> after hero
        hero_end = html.find('</section>', html.find('id="hero"') if 'id="hero"' in html else 0)
        if hero_end == -1:
            # Try finding first </section> in body
            hero_end = html.find('</section>', html.find('<body'))
        if hero_end > 0:
            insert_pos = hero_end + len('</section>')
            html = html[:insert_pos] + '\n' + MARQUEE_CREDENCIAIS + html[insert_pos:]
            changes += 1

    # 3. Add marquee gold before CTA final
    if 'mq-gold' not in html:
        cta_pos = html.find('id="cta-final"')
        if cta_pos == -1:
            cta_pos = html.find('class="cta-final"')
        if cta_pos > 0:
            # Find the <section before this
            section_start = html.rfind('<section', 0, cta_pos)
            if section_start > 0:
                html = html[:section_start] + MARQUEE_GOLD + '\n\n' + html[section_start:]
                changes += 1

    # 4. Add cross-link section before FAQ
    if 'OUTROS SERVIÇOS' not in html and fname in CROSS_LINKS:
        links = CROSS_LINKS[fname]
        cards_html = ''
        for title, href, color, desc in links:
            cards_html += f'''
      <a href="{href}" class="xlink-card reveal" style="border-left:3px solid {color}">
        <div class="xlink-title">{title}</div>
        <div class="xlink-desc">{desc}</div>
        <span class="xlink-arrow" style="color:{color}">→</span>
      </a>'''

        xlink_section = f'''
<!-- OUTROS SERVIÇOS -->
<section class="light sec-pad" id="outros-servicos" style="background:var(--paper,#F1F5F9)">
  <div class="container" style="text-align:center">
    <div class="reveal">
      <div class="sec-label" style="color:#3B82F6;font-size:11px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;margin-bottom:12px">OUTROS SERVIÇOS</div>
      <h2 style="font-size:clamp(1.4rem,3vw,1.875rem);font-weight:800;color:#060E1A;line-height:1.25">Conheça também nossos <em style="font-style:italic;color:#3B82F6">outros serviços</em></h2>
    </div>
    <div class="xlink-grid" style="display:grid;grid-template-columns:repeat(2,1fr);gap:16px;margin-top:40px;text-align:left">
{cards_html}
    </div>
  </div>
</section>
'''
        # Insert before FAQ section
        faq_pos = html.find('id="faq"')
        if faq_pos > 0:
            section_start = html.rfind('<section', 0, faq_pos)
            if section_start > 0:
                html = html[:section_start] + xlink_section + '\n' + html[section_start:]
                changes += 1

    # 5. Add cross-link CSS if not present
    if '.xlink-card' not in html and '</style>' in html:
        xlink_css = '''
/* Cross-link cards */
.xlink-card{display:flex;align-items:center;gap:12px;background:#fff;border:1.5px solid #E2E8F0;border-radius:12px;padding:20px;transition:border-color .25s,box-shadow .25s,transform .25s;color:inherit}
.xlink-card:hover{box-shadow:0 4px 16px rgba(0,0,0,.06);transform:translateY(-2px)}
.xlink-title{font-size:15px;font-weight:700;color:#060E1A;flex:1}
.xlink-desc{font-size:13px;color:#94A3B8;flex:2}
.xlink-arrow{font-size:18px;font-weight:700;flex-shrink:0}
@media(max-width:768px){.xlink-grid{grid-template-columns:1fr!important}.xlink-desc{display:none}}
'''
        html = html.replace('</style>', xlink_css + '</style>', 1)
        changes += 1

    # 6. Add cross pattern to CTA final if missing
    if CROSS_PATTERN not in html and 'cta-final' in html:
        # Try to find cta-final CSS and add background-image
        if '.cta-final{' in html or '.cta-final {' in html:
            for pattern in ['.cta-final{', '.cta-final {']:
                if pattern in html:
                    pos = html.find(pattern)
                    brace = html.find('{', pos)
                    html = html[:brace+1] + CROSS_PATTERN + ';' + html[brace+1:]
                    changes += 1
                    break

    # 7. Fix hero CTA mobile size
    if 'hero-cta' in html and '@media' not in html.split('hero-cta')[1][:200]:
        # This is harder to do generically, skip if complex
        pass

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"✅ {fname} — {changes} mudanças aplicadas")

print("\n🎯 Script concluído. Execute o upload para deploy.")
