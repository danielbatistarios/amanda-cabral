/**
 * Gera sitemap.xml para amcabralblindagem.com.br
 * - Páginas existentes: lastmod = data de modificação real do arquivo
 * - Páginas futuras (ainda não criadas): lastmod = data de hoje
 *
 * Uso: node generate-sitemap.mjs
 * Depois: commitar sitemap.xml no GitHub
 */

import { statSync, existsSync, writeFileSync } from 'fs'
import { join } from 'path'

const BASE_URL = 'https://amcabralblindagem.com.br'
const ROOT = new URL('.', import.meta.url).pathname
const TODAY = new Date().toISOString().split('T')[0]

// Mapeia slug → caminho relativo do arquivo HTML
function slugToFile(slug) {
  if (slug === '/') return 'index.html'
  const bare = slug.replace(/^\/|\/$/g, '')
  // Tenta slug/index.html primeiro, depois slug.html
  const asFolder = join(ROOT, bare, 'index.html')
  if (existsSync(asFolder)) return join(bare, 'index.html')
  const asFile = join(ROOT, bare + '.html')
  if (existsSync(asFile)) return bare + '.html'
  return null
}

function lastmod(slug) {
  const rel = slugToFile(slug)
  if (!rel) return TODAY
  try {
    const mtime = statSync(join(ROOT, rel)).mtime
    return mtime.toISOString().split('T')[0]
  } catch {
    return TODAY
  }
}

// Definição completa das páginas
// [slug, priority, changefreq]
const pages = [
  // Core
  ['/',                                          '1.0', 'weekly'],
  ['/sobre-amcabral-blindagem',                  '0.6', 'monthly'],
  ['/bio',                                       '0.6', 'monthly'],
  ['/casos-de-sucesso',                          '0.6', 'monthly'],
  ['/casos-de-sucesso/metalurgica',              '0.6', 'monthly'],
  ['/faq-amcabralblindagem',                     '0.6', 'monthly'],
  ['/fale-com-especialista',                     '0.6', 'monthly'],

  // Serviços
  ['/nossos-servicos',                                          '0.8', 'monthly'],
  ['/nossos-servicos/gestao-contabil',                          '0.7', 'monthly'],
  ['/nossos-servicos/recuperacao-creditos-tributarios',         '0.7', 'monthly'],
  ['/nossos-servicos/holding-patrimonial',                      '0.7', 'monthly'],
  ['/nossos-servicos/planejamento-tributario',                  '0.7', 'monthly'],
  ['/nossos-servicos/consultoria-tributaria',                   '0.7', 'monthly'],

  // Hub de cidades
  ['/cidades-atendidas',                                              '0.8', 'monthly'],

  // ── MINAS GERAIS ──────────────────────────────────────────────────────────

  // Pará de Minas — SEDE (conjunto completo: contador + abertura + holding + planejamento + recuperação)
  ['/para-de-minas-mg',                                                          '0.8', 'monthly'],
  ['/para-de-minas-mg/escritorio-de-contabilidade-em-para-de-minas',             '0.8', 'monthly'],
  ['/para-de-minas-mg/abertura-de-empresa-para-de-minas',                        '0.7', 'monthly'],
  ['/para-de-minas-mg/holding-patrimonial-para-de-minas',                        '0.7', 'monthly'],
  ['/para-de-minas-mg/planejamento-tributario-para-de-minas',                    '0.7', 'monthly'],
  ['/para-de-minas-mg/recuperacao-creditos-tributarios-para-de-minas',           '0.7', 'monthly'],
  ['/para-de-minas-mg/contador-especializado-em-holding',                        '0.7', 'monthly'],
  ['/para-de-minas-mg/contador-para-fabricas-e-industrias',                      '0.7', 'monthly'],
  ['/para-de-minas-mg/trocar-de-contador',                                       '0.7', 'monthly'],

  // Uberlândia — polo industrial grande (contador + abertura + holding + planejamento + recuperação)
  ['/uberlandia-mg',                                                              '0.7', 'monthly'],
  ['/uberlandia-mg/contador-em-uberlandia',                                       '0.7', 'monthly'],
  ['/uberlandia-mg/abertura-de-empresa-uberlandia',                               '0.7', 'monthly'],
  ['/uberlandia-mg/holding-patrimonial-uberlandia',                               '0.7', 'monthly'],
  ['/uberlandia-mg/planejamento-tributario-uberlandia',                           '0.7', 'monthly'],
  ['/uberlandia-mg/recuperacao-creditos-tributarios-uberlandia',                  '0.7', 'monthly'],

  // Betim — polo industrial (contador + abertura + recuperação)
  ['/betim-mg',                                                                   '0.7', 'monthly'],
  ['/betim-mg/contador-em-betim',                                                 '0.7', 'monthly'],
  ['/betim-mg/abertura-de-empresa-betim',                                         '0.7', 'monthly'],
  ['/betim-mg/recuperacao-creditos-tributarios-betim',                            '0.7', 'monthly'],

  // Sete Lagoas — polo industrial (contador + abertura + recuperação)
  ['/sete-lagoas-mg',                                                             '0.7', 'monthly'],
  ['/sete-lagoas-mg/contador-em-sete-lagoas',                                     '0.7', 'monthly'],
  ['/sete-lagoas-mg/abertura-de-empresa-sete-lagoas',                             '0.7', 'monthly'],
  ['/sete-lagoas-mg/recuperacao-creditos-tributarios-sete-lagoas',                '0.7', 'monthly'],

  // Montes Claros — polo regional (contador + abertura)
  ['/montes-claros-mg',                                                           '0.7', 'monthly'],
  ['/montes-claros-mg/contador-em-montes-claros',                                 '0.7', 'monthly'],
  ['/montes-claros-mg/abertura-de-empresa-montes-claros',                         '0.7', 'monthly'],

  // Uberaba — polo regional (contador + abertura)
  ['/uberaba-mg',                                                                 '0.7', 'monthly'],
  ['/uberaba-mg/contador-em-uberaba',                                             '0.7', 'monthly'],
  ['/uberaba-mg/abertura-de-empresa-uberaba',                                     '0.7', 'monthly'],

  // Poços de Caldas — 1 LP
  ['/pocos-de-caldas-mg',                                                         '0.7', 'monthly'],
  ['/pocos-de-caldas-mg/contador-em-pocos-de-caldas',                             '0.7', 'monthly'],

  // ── SÃO PAULO ──────────────────────────────────────────────────────────────

  // Campinas — polo industrial grande (contador + abertura + holding + planejamento + recuperação)
  ['/campinas-sp',                                                                '0.7', 'monthly'],
  ['/campinas-sp/contador-em-campinas',                                           '0.7', 'monthly'],
  ['/campinas-sp/abertura-de-empresa-campinas',                                   '0.7', 'monthly'],
  ['/campinas-sp/holding-patrimonial-campinas',                                   '0.7', 'monthly'],
  ['/campinas-sp/planejamento-tributario-campinas',                               '0.7', 'monthly'],
  ['/campinas-sp/recuperacao-creditos-tributarios-campinas',                      '0.7', 'monthly'],

  // Sorocaba — polo industrial (contador + abertura + recuperação)
  ['/sorocaba-sp',                                                                '0.7', 'monthly'],
  ['/sorocaba-sp/contador-em-sorocaba',                                           '0.7', 'monthly'],
  ['/sorocaba-sp/abertura-de-empresa-sorocaba',                                   '0.7', 'monthly'],
  ['/sorocaba-sp/recuperacao-creditos-tributarios-sorocaba',                      '0.7', 'monthly'],

  // Guarulhos — polo industrial (contador + abertura + recuperação)
  ['/guarulhos-sp',                                                               '0.7', 'monthly'],
  ['/guarulhos-sp/contador-em-guarulhos',                                         '0.7', 'monthly'],
  ['/guarulhos-sp/abertura-de-empresa-guarulhos',                                 '0.7', 'monthly'],
  ['/guarulhos-sp/recuperacao-creditos-tributarios-guarulhos',                    '0.7', 'monthly'],

  // Ribeirão Preto — polo regional (contador + abertura + holding)
  ['/ribeirao-preto-sp',                                                          '0.7', 'monthly'],
  ['/ribeirao-preto-sp/contador-em-ribeirao-preto',                               '0.7', 'monthly'],
  ['/ribeirao-preto-sp/abertura-de-empresa-ribeirao-preto',                       '0.7', 'monthly'],
  ['/ribeirao-preto-sp/holding-patrimonial-ribeirao-preto',                       '0.7', 'monthly'],

  // Piracicaba — polo industrial (contador + abertura)
  ['/piracicaba-sp',                                                              '0.7', 'monthly'],
  ['/piracicaba-sp/contador-em-piracicaba',                                       '0.7', 'monthly'],
  ['/piracicaba-sp/abertura-de-empresa-piracicaba',                               '0.7', 'monthly'],

  // Osasco — polo industrial (contador + abertura)
  ['/osasco-sp',                                                                  '0.7', 'monthly'],
  ['/osasco-sp/contador-em-osasco',                                               '0.7', 'monthly'],
  ['/osasco-sp/abertura-de-empresa-osasco',                                       '0.7', 'monthly'],

  // ── SUL ───────────────────────────────────────────────────────────────────

  // Curitiba — polo industrial grande (contador + abertura + holding + planejamento + recuperação)
  ['/curitiba-pr',                                                                '0.7', 'monthly'],
  ['/curitiba-pr/contador-em-curitiba',                                           '0.7', 'monthly'],
  ['/curitiba-pr/abertura-de-empresa-curitiba',                                   '0.7', 'monthly'],
  ['/curitiba-pr/holding-patrimonial-curitiba',                                   '0.7', 'monthly'],
  ['/curitiba-pr/planejamento-tributario-curitiba',                               '0.7', 'monthly'],
  ['/curitiba-pr/recuperacao-creditos-tributarios-curitiba',                      '0.7', 'monthly'],

  // Joinville — polo industrial (contador + abertura + recuperação)
  ['/joinville-sc',                                                               '0.7', 'monthly'],
  ['/joinville-sc/contador-em-joinville',                                         '0.7', 'monthly'],
  ['/joinville-sc/abertura-de-empresa-joinville',                                 '0.7', 'monthly'],
  ['/joinville-sc/recuperacao-creditos-tributarios-joinville',                    '0.7', 'monthly'],

  // Caxias do Sul — polo industrial (contador + abertura + recuperação)
  ['/caxias-do-sul-rs',                                                           '0.7', 'monthly'],
  ['/caxias-do-sul-rs/contador-em-caxias-do-sul',                                 '0.7', 'monthly'],
  ['/caxias-do-sul-rs/abertura-de-empresa-caxias-do-sul',                         '0.7', 'monthly'],
  ['/caxias-do-sul-rs/recuperacao-creditos-tributarios-caxias-do-sul',            '0.7', 'monthly'],

  // Blumenau — polo regional (contador + abertura)
  ['/blumenau-sc',                                                                '0.7', 'monthly'],
  ['/blumenau-sc/contador-em-blumenau',                                           '0.7', 'monthly'],
  ['/blumenau-sc/abertura-de-empresa-blumenau',                                   '0.7', 'monthly'],

  // ── NORDESTE ──────────────────────────────────────────────────────────────

  // Recife — polo regional grande (contador + abertura + recuperação)
  ['/recife-pe',                                                                  '0.7', 'monthly'],
  ['/recife-pe/contador-em-recife',                                               '0.7', 'monthly'],
  ['/recife-pe/abertura-de-empresa-recife',                                       '0.7', 'monthly'],
  ['/recife-pe/recuperacao-creditos-tributarios-recife',                          '0.7', 'monthly'],

  // Fortaleza — polo regional grande (contador + abertura)
  ['/fortaleza-ce',                                                               '0.7', 'monthly'],
  ['/fortaleza-ce/contador-em-fortaleza',                                         '0.7', 'monthly'],
  ['/fortaleza-ce/abertura-de-empresa-fortaleza',                                 '0.7', 'monthly'],

  // Salvador — polo regional (contador + abertura)
  ['/salvador-ba',                                                                '0.7', 'monthly'],
  ['/salvador-ba/contador-em-salvador',                                           '0.7', 'monthly'],
  ['/salvador-ba/abertura-de-empresa-salvador',                                   '0.7', 'monthly'],

  // Feira de Santana — 1 LP
  ['/feira-de-santana-ba',                                                        '0.7', 'monthly'],
  ['/feira-de-santana-ba/contador-em-feira-de-santana',                           '0.7', 'monthly'],

  // João Pessoa — 1 LP
  ['/joao-pessoa-pb',                                                             '0.7', 'monthly'],
  ['/joao-pessoa-pb/contador-em-joao-pessoa',                                     '0.7', 'monthly'],

  // ── NORTE ─────────────────────────────────────────────────────────────────

  // Manaus — polo industrial Zona Franca (contador + abertura)
  ['/manaus-am',                                                                  '0.7', 'monthly'],
  ['/manaus-am/contador-em-manaus',                                               '0.7', 'monthly'],
  ['/manaus-am/abertura-de-empresa-manaus',                                       '0.7', 'monthly'],

  // ── CENTRO-OESTE ──────────────────────────────────────────────────────────

  // Goiânia — polo regional (contador + abertura)
  ['/goiania-go',                                                                 '0.7', 'monthly'],
  ['/goiania-go/contador-em-goiania',                                             '0.7', 'monthly'],
  ['/goiania-go/abertura-de-empresa-goiania',                                     '0.7', 'monthly'],

  // ── RIO DE JANEIRO ────────────────────────────────────────────────────────

  // Rio de Janeiro — polo grande (contador + abertura + holding + planejamento)
  ['/rio-de-janeiro-rj',                                                          '0.7', 'monthly'],
  ['/rio-de-janeiro-rj/contador-em-rio-de-janeiro',                               '0.7', 'monthly'],
  ['/rio-de-janeiro-rj/abertura-de-empresa-rio-de-janeiro',                       '0.7', 'monthly'],
  ['/rio-de-janeiro-rj/holding-patrimonial-rio-de-janeiro',                       '0.7', 'monthly'],
  ['/rio-de-janeiro-rj/planejamento-tributario-rio-de-janeiro',                   '0.7', 'monthly'],

  // Cluster Holding / Patrimônio
  ['/cib-cadastro-imovel-brasileiro',            '0.7', 'monthly'],
  ['/empresa-rica-dono-pobre',                   '0.7', 'monthly'],
  ['/como-montar-holding-patrimonial',           '0.7', 'monthly'],
  ['/holding-imobiliaria-reforma-tributaria',    '0.7', 'monthly'],
  ['/holding-vs-pessoa-fisica-imoveis',          '0.7', 'monthly'],
  ['/planejamento-sucessorio-empresarial',       '0.7', 'monthly'],
  ['/protecao-patrimonial-empresa',              '0.7', 'monthly'],
  ['/tributacao-aluguel-temporada-airbnb',       '0.7', 'monthly'],
  ['/holding-diagnostico-imoveis',               '0.7', 'monthly'],

  // Cluster Reforma Tributária
  ['/reforma-tributaria-industria',              '0.7', 'monthly'],
  ['/reavaliacao-imoveis-reforma-tributaria',    '0.7', 'monthly'],
  ['/reforma-tributaria-saude',                  '0.7', 'monthly'],
  ['/reforma-tributaria-aluguel',                '0.7', 'monthly'],
  ['/reforma-tributaria-simples-nacional',       '0.7', 'monthly'],

  // Cluster Planejamento Industrial
  ['/planejamento-tributario-industrial',        '0.7', 'monthly'],
  ['/incentivos-fiscais-minas-gerais',           '0.7', 'monthly'],

  // Cluster Setorial
  ['/tributacao-industria-alimentos',            '0.7', 'monthly'],
  ['/tributacao-industria-farmaceutica',         '0.7', 'monthly'],
  ['/tributacao-industria-metalmecanica',        '0.7', 'monthly'],

  // Materiais
  ['/materiais/diagnostico-sucessao-familiar',   '0.6', 'monthly'],

  // Blog hub
  ['/blog',                                      '0.8', 'weekly'],

  // Blog — Holding / Patrimônio
  ['/blog/dividendos-reforma-tributaria-2026',   '0.8', 'monthly'],
  ['/blog/como-proteger-patrimonio-empresarial', '0.8', 'monthly'],
  ['/blog/patrimonio-sem-protecao-2026',         '0.8', 'monthly'],
  ['/blog/itcmd-minas-gerais-herdeiros',         '0.8', 'monthly'],
  ['/blog/holding-vs-testamento',                '0.8', 'monthly'],
  ['/blog/reforma-tributaria-holdings',          '0.8', 'monthly'],
  ['/blog/holding-familiar-vs-imobiliaria',      '0.8', 'monthly'],
  ['/blog/contadora-ou-advogado-holding',        '0.8', 'monthly'],
  ['/blog/aluguel-nao-declarado-cib',            '0.8', 'monthly'],
  ['/blog/tributacao-aluguel-2026-mudancas',     '0.8', 'monthly'],

  // Blog — Reforma Tributária Indústria
  ['/blog/o-que-e-ibs-cbs',                     '0.8', 'monthly'],
  ['/blog/lc-214-lei-complementar',              '0.8', 'monthly'],
  ['/blog/ec-132-2023-reforma',                  '0.8', 'monthly'],
  ['/blog/cronograma-transicao',                 '0.8', 'monthly'],
  ['/blog/split-payment-industria',              '0.8', 'monthly'],
  ['/blog/nao-cumulatividade-ibs',               '0.8', 'monthly'],
  ['/blog/imposto-seletivo',                     '0.8', 'monthly'],
  ['/blog/iva-dual-brasil',                      '0.8', 'monthly'],
  ['/blog/apuracao-assistida',                   '0.8', 'monthly'],
  ['/blog/regime-de-caixa-empresas-industriais', '0.8', 'monthly'],
  ['/blog/margem-industrial-encolhe',            '0.8', 'monthly'],
  ['/blog/industrias-mg-pagam-icms-a-mais',      '0.8', 'monthly'],

  // Blog — Planejamento Tributário Industrial
  ['/blog/regime-tributario-industria',          '0.8', 'monthly'],
  ['/blog/lucro-real-vs-presumido',              '0.8', 'monthly'],
  ['/blog/elisao-fiscal-industria',              '0.8', 'monthly'],
  ['/blog/checklist-planejamento',               '0.8', 'monthly'],
  ['/blog/sinais-sair-simples-nacional-industria','0.8', 'monthly'],
  ['/blog/simples-nacional-mito-protecao-reforma','0.8', 'monthly'],
  ['/blog/lc-214-artigo-por-artigo-industria',   '0.8', 'monthly'],
  ['/blog/panorama-tributario-industria-mg',     '0.8', 'monthly'],

  // Blog — Recuperação de Créditos
  ['/blog/como-recuperar-credito',               '0.8', 'monthly'],
  ['/blog/credito-pis-cofins',                   '0.8', 'monthly'],
  ['/blog/revisao-creditos-icms',                '0.8', 'monthly'],
  ['/blog/prescricao-credito',                   '0.8', 'monthly'],
  ['/blog/restituicao-tributos',                 '0.8', 'monthly'],
  ['/blog/creditos-perdidos-industria-5-anos',   '0.8', 'monthly'],

  // Blog — Incentivos / Regime Especial MG
  ['/blog/ttd-icms-minas-gerais',               '0.8', 'monthly'],
  ['/blog/regime-especial-mg-industria',         '0.8', 'monthly'],

  // Blog — Empresa Familiar / Sucessão
  ['/blog/empresa-familiar-segunda-geracao',     '0.8', 'monthly'],
  ['/blog/governanca-familiar-industria',        '0.8', 'monthly'],
  ['/blog/acordo-socios-empresa-familiar',       '0.8', 'monthly'],

  // Legais
  ['/termos-de-uso',                             '0.3', 'yearly'],
  ['/politica-de-privacidade',                   '0.3', 'yearly'],
  ['/politica-de-cookies',                       '0.3', 'yearly'],
]

function buildXml() {
  const entries = pages.map(([slug, priority, changefreq]) => {
    const loc = `${BASE_URL}${slug}`
    const lm = lastmod(slug)
    return `  <url>
    <loc>${loc}</loc>
    <lastmod>${lm}</lastmod>
    <changefreq>${changefreq}</changefreq>
    <priority>${priority}</priority>
  </url>`
  })

  return `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${entries.join('\n')}
</urlset>`
}

const xml = buildXml()
writeFileSync(join(ROOT, 'sitemap.xml'), xml, 'utf8')

const existing = pages.filter(([slug]) => slugToFile(slug) !== null).length
const missing = pages.length - existing
console.log(`sitemap.xml gerado: ${pages.length} URLs`)
console.log(`  - ${existing} com lastmod real (arquivo existente)`)
console.log(`  - ${missing} com lastmod hoje (página ainda não criada)`)
