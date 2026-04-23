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

  // Cidades
  ['/cidades-atendidas',                         '0.8', 'monthly'],
  ['/contabilidade-para-de-minas',               '0.7', 'monthly'],
  ['/contabilidade-sete-lagoas',                 '0.7', 'monthly'],
  ['/contabilidade-montes-claros',               '0.7', 'monthly'],
  ['/contador-uberaba',                          '0.7', 'monthly'],
  ['/contador-uberlandia',                       '0.7', 'monthly'],
  ['/contador-pocos-de-caldas',                  '0.7', 'monthly'],
  ['/contador-betim',                            '0.7', 'monthly'],
  ['/contador-curitiba',                         '0.7', 'monthly'],
  ['/contador-sorocaba',                         '0.7', 'monthly'],
  ['/contador-guarulhos',                        '0.7', 'monthly'],
  ['/contador-manaus',                           '0.7', 'monthly'],
  ['/contador-osasco',                           '0.7', 'monthly'],
  ['/contador-caxias-do-sul',                    '0.7', 'monthly'],
  ['/contador-fortaleza',                        '0.7', 'monthly'],
  ['/contador-goiania',                          '0.7', 'monthly'],
  ['/contador-joao-pessoa',                      '0.7', 'monthly'],
  ['/contador-ribeirao-preto',                   '0.7', 'monthly'],
  ['/contador-salvador',                         '0.7', 'monthly'],
  ['/contador-blumenau',                         '0.7', 'monthly'],
  ['/contador-feira-de-santana',                 '0.7', 'monthly'],
  ['/contador-piracicaba',                       '0.7', 'monthly'],
  ['/contador-recife',                           '0.7', 'monthly'],
  ['/contador-rio-de-janeiro',                   '0.7', 'monthly'],
  ['/contador-joinville',                        '0.7', 'monthly'],
  ['/contador-campinas',                         '0.7', 'monthly'],

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
