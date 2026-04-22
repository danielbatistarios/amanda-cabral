/**
 * upload-amanda.mjs — CabralHanani site → Cloudflare R2
 * Usage: node upload-amanda.mjs
 */

import { AwsClient } from 'aws4fetch';
import { readFileSync, existsSync } from 'node:fs';
import { join } from 'node:path';

const ACCOUNT_ID = '842561b03363b0ab3a35556ff728f9fe';
const ACCESS_KEY = '9b8005782e2f6ebd197768fabe1e07c2';
const SECRET_KEY = '05bafb847199adb9b99d6e3631541995be399d7e621a5132512837ed45832093';
const ENDPOINT   = `https://${ACCOUNT_ID}.r2.cloudflarestorage.com`;
const BUCKET     = 'pages';
const BASE_DIR   = '/Users/jrios/amanda-cabral-contadora';

const FILES = [
  { local: 'index.html',        r2Key: 'amanda/index.html',        contentType: 'text/html; charset=utf-8' },
  { local: 'bio.html',          r2Key: 'amanda/bio.html',          contentType: 'text/html; charset=utf-8' },
  { local: 'author.html',       r2Key: 'amanda/author/index.html', contentType: 'text/html; charset=utf-8' },
  { local: 'faq.html',          r2Key: 'amanda/faq-amcabralblindagem/index.html', contentType: 'text/html; charset=utf-8' },
  { local: 'servicos.html',     r2Key: 'amanda/servicos/index.html', contentType: 'text/html; charset=utf-8' },
  { local: 'gestao-contabil-industrial.html', r2Key: 'amanda/gestao-contabil-industrial/index.html', contentType: 'text/html; charset=utf-8' },
  { local: 'recuperacao-creditos-tributarios.html', r2Key: 'amanda/recuperacao-creditos-tributarios/index.html', contentType: 'text/html; charset=utf-8' },
  { local: 'holding-patrimonial.html', r2Key: 'amanda/constituicao-de-holding-patrimonial-e-familiar/index.html', contentType: 'text/html; charset=utf-8' },
  { local: 'planejamento-tributario.html', r2Key: 'amanda/planejamento-tributario-industrial/index.html', contentType: 'text/html; charset=utf-8' },
  { local: 'consultoria-tributaria.html', r2Key: 'amanda/consultoria-tributaria/index.html', contentType: 'text/html; charset=utf-8' },
  { local: 'home-v2.html', r2Key: 'amanda/home-v2.html', contentType: 'text/html; charset=utf-8' },
  { local: 'home-v3.html', r2Key: 'amanda/home-v3.html', contentType: 'text/html; charset=utf-8' },
  { local: 'amanda-cabral.jpg', r2Key: 'amanda/amanda-cabral.jpg', contentType: 'image/jpeg' },
  { local: 'amanda-cabral-foto.jpg', r2Key: 'amanda/amanda-cabral-foto.jpg', contentType: 'image/jpeg' },
];

const client = new AwsClient({
  accessKeyId: ACCESS_KEY,
  secretAccessKey: SECRET_KEY,
  service: 's3',
  region: 'auto',
});

async function upload(localPath, r2Key, contentType) {
  const url = `${ENDPOINT}/${BUCKET}/${r2Key}`;
  const content = readFileSync(localPath);
  const res = await client.fetch(url, {
    method: 'PUT',
    body: content,
    headers: { 'Content-Type': contentType, 'Content-Length': String(content.length) },
  });
  if (!res.ok) throw new Error(`HTTP ${res.status}: ${await res.text()}`);
  return url;
}

async function main() {
  console.log(`📦 Bucket: ${BUCKET}\n`);
  for (const f of FILES) {
    const path = join(BASE_DIR, f.local);
    if (!existsSync(path)) { console.warn(`⚠️  ${f.local} não encontrado`); continue; }
    process.stdout.write(`⬆️  ${f.local} → ${f.r2Key} ... `);
    try {
      await upload(path, f.r2Key, f.contentType);
      console.log('✓');
    } catch (e) { console.error(`✗ ${e.message}`); }
  }
  console.log(`\n✅ URL: https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/amanda/index.html`);
}

main().catch(e => { console.error(e); process.exit(1); });
