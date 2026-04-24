import { minify } from 'html-minifier-terser';
import postcss from 'postcss';
import cssnano from 'cssnano';
import { readFileSync, writeFileSync, mkdirSync, copyFileSync, existsSync } from 'fs';
import { join } from 'path';

const ROOT = new URL('.', import.meta.url).pathname;
const DIST = join(ROOT, 'dist');

mkdirSync(DIST, { recursive: true });
mkdirSync(join(DIST, 'assets'), { recursive: true });
mkdirSync(join(DIST, 'assets', 'fonts'), { recursive: true });

// Minify HTML
const html = readFileSync(join(ROOT, 'index.html'), 'utf8');
const minHtml = await minify(html, {
  collapseWhitespace: true,
  removeComments: true,
  removeRedundantAttributes: true,
  removeScriptTypeAttributes: true,
  removeStyleLinkTypeAttributes: true,
  useShortDoctype: true,
  minifyCSS: true,
  minifyJS: { compress: true, mangle: true },
  decodeEntities: false,
});
writeFileSync(join(DIST, 'index.html'), minHtml);
const htmlRatio = ((1 - minHtml.length / html.length) * 100).toFixed(1);
console.log(`HTML: ${(html.length/1024).toFixed(0)}KB → ${(minHtml.length/1024).toFixed(0)}KB (${htmlRatio}% reduction)`);

// Minify CSS files
const cssFiles = ['assets/styles.css', 'mobile-patch.css'];
for (const cssFile of cssFiles) {
  const src = join(ROOT, cssFile);
  if (!existsSync(src)) continue;
  const css = readFileSync(src, 'utf8');
  const result = await postcss([cssnano({ preset: 'default' })]).process(css, { from: src });
  const dest = join(DIST, cssFile);
  mkdirSync(join(DIST, cssFile.split('/').slice(0, -1).join('/')), { recursive: true });
  writeFileSync(dest, result.css);
  const ratio = ((1 - result.css.length / css.length) * 100).toFixed(1);
  console.log(`${cssFile}: ${(css.length/1024).toFixed(0)}KB → ${(result.css.length/1024).toFixed(0)}KB (${ratio}% reduction)`);
}

// Copy static assets (fonts, images, headers)
const staticFiles = [
  'assets/fonts',
  '_headers',
  '_redirects',
  'amanda-hero.webp',
  'amanda-hero.jpg',
  'amanda-hero-mobile.webp',
  'amanda-hero-mobile.jpg',
  'favicon.ico',
  'favicon.png',
  'bg-cta.webp',
  'img-servicos-contabeis.webp',
  'img-servicos-contabeis.jpg',
  'img-blog.webp',
  'img-blog.jpg',
  'blog-reforma-tributaria.webp',
  'blog-icms-industrias.webp',
  'blog-holding-patrimonial.webp',
  'avatar-ricardo.webp',
  'avatar-patricia.webp',
  'avatar-carlos.webp',
];

import { readdirSync, statSync } from 'fs';

function copyDir(src, dest) {
  if (!existsSync(src)) return;
  mkdirSync(dest, { recursive: true });
  for (const entry of readdirSync(src)) {
    const s = join(src, entry);
    const d = join(dest, entry);
    if (statSync(s).isDirectory()) copyDir(s, d);
    else { copyFileSync(s, d); }
  }
}

for (const f of staticFiles) {
  const src = join(ROOT, f);
  const dest = join(DIST, f);
  if (!existsSync(src)) continue;
  if (statSync(src).isDirectory()) {
    copyDir(src, dest);
    console.log(`Copied dir: ${f}`);
  } else {
    mkdirSync(join(dest, '..'), { recursive: true });
    copyFileSync(src, dest);
  }
}

console.log(`\nDist ready at: ${DIST}`);
