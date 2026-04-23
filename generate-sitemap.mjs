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

  // Minas Gerais — silos de cidade
  ['/para-de-minas-mg',                                              '0.8', 'monthly'],
  ['/para-de-minas-mg/escritorio-de-contabilidade-em-para-de-minas', '0.7', 'monthly'],
  ['/sete-lagoas-mg',                                                '0.7', 'monthly'],
  ['/sete-lagoas-mg/contabilidade-industrial-em-sete-lagoas',        '0.7', 'monthly'],
  ['/montes-claros-mg',                                              '0.7', 'monthly'],
  ['/montes-claros-mg/contador-especializado-industrias-montes-claros','0.7','monthly'],
  ['/uberaba-mg',                                                    '0.7', 'monthly'],
  ['/uberaba-mg/consultoria-tributaria-industrias-uberaba',          '0.7', 'monthly'],
  ['/uberlandia-mg',                                                 '0.7', 'monthly'],
  ['/uberlandia-mg/escritorio-contabil-industrial-uberlandia',       '0.7', 'monthly'],
  ['/betim-mg',                                                      '0.7', 'monthly'],
  ['/betim-mg/contabilidade-planejamento-tributario-betim',          '0.7', 'monthly'],
  ['/pocos-de-caldas-mg',                                            '0.7', 'monthly'],
  ['/pocos-de-caldas-mg/escritorio-contabil-pocos-de-caldas',        '0.7', 'monthly'],

  // São Paulo — silos de cidade
  ['/sorocaba-sp',                                                   '0.7', 'monthly'],
  ['/sorocaba-sp/contador-industrias-sorocaba',                      '0.7', 'monthly'],
  ['/guarulhos-sp',                                                  '0.7', 'monthly'],
  ['/guarulhos-sp/escritorio-contabilidade-industrial-guarulhos',    '0.7', 'monthly'],
  ['/osasco-sp',                                                     '0.7', 'monthly'],
  ['/osasco-sp/contabilidade-especializada-industrias-osasco',       '0.7', 'monthly'],
  ['/ribeirao-preto-sp',                                             '0.7', 'monthly'],
  ['/ribeirao-preto-sp/planejamento-tributario-industrial-ribeirao-preto','0.7','monthly'],
  ['/piracicaba-sp',                                                 '0.7', 'monthly'],
  ['/piracicaba-sp/contador-tributarista-industrias-piracicaba',     '0.7', 'monthly'],
  ['/campinas-sp',                                                   '0.7', 'monthly'],
  ['/campinas-sp/consultoria-contabil-industrial-campinas',          '0.7', 'monthly'],

  // Sul — silos de cidade
  ['/curitiba-pr',                                                   '0.7', 'monthly'],
  ['/curitiba-pr/escritorio-contabilidade-industrias-curitiba',      '0.7', 'monthly'],
  ['/caxias-do-sul-rs',                                              '0.7', 'monthly'],
  ['/caxias-do-sul-rs/contabilidade-tributaria-industrial-caxias-do-sul','0.7','monthly'],
  ['/blumenau-sc',                                                   '0.7', 'monthly'],
  ['/blumenau-sc/contador-especialista-industrias-blumenau',         '0.7', 'monthly'],
  ['/joinville-sc',                                                  '0.7', 'monthly'],
  ['/joinville-sc/gestao-contabil-tributaria-industrias-joinville',  '0.7', 'monthly'],

  // Nordeste — silos de cidade
  ['/fortaleza-ce',                                                  '0.7', 'monthly'],
  ['/fortaleza-ce/contabilidade-industrial-remota-fortaleza',        '0.7', 'monthly'],
  ['/joao-pessoa-pb',                                                '0.7', 'monthly'],
  ['/joao-pessoa-pb/contador-industrial-atendimento-digital-joao-pessoa','0.7','monthly'],
  ['/salvador-ba',                                                   '0.7', 'monthly'],
  ['/salvador-ba/escritorio-contabilidade-industrial-salvador',      '0.7', 'monthly'],
  ['/feira-de-santana-ba',                                           '0.7', 'monthly'],
  ['/feira-de-santana-ba/consultoria-tributaria-industrias-feira-de-santana','0.7','monthly'],
  ['/recife-pe',                                                     '0.7', 'monthly'],
  ['/recife-pe/contabilidade-recuperacao-creditos-industrias-recife', '0.7', 'monthly'],

  // Norte
  ['/manaus-am',                                                     '0.7', 'monthly'],
  ['/manaus-am/contador-industrias-zona-franca-manaus',              '0.7', 'monthly'],

  // Centro-Oeste
  ['/goiania-go',                                                    '0.7', 'monthly'],
  ['/goiania-go/escritorio-contabilidade-tributaria-goiania',        '0.7', 'monthly'],

  // Rio de Janeiro
  ['/rio-de-janeiro-rj',                                             '0.7', 'monthly'],
  ['/rio-de-janeiro-rj/contabilidade-industrial-rio-de-janeiro',     '0.7', 'monthly'],

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
