#!/usr/bin/env node
/**
 * One-time: extract base64 images from index.html into assets/images/
 * and replace data URIs with file paths.
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.join(__dirname, '..');
const htmlPath = path.join(root, 'index.html');

const VIDEO_SLUGS = [
  'anejo-ugc',
  'just-bought-it-hair',
  'garba-ahmedabad',
];

const COLLATERAL_SLUGS = [
  'bulletproof-your-agency',
  'freedom-from-monthly-payments',
  'agency-advocate-podcast',
  'mission-driven-content',
  'designer-humour-series',
  'fall-in-love-at-first-scent',
  'roja-parfums-elixir',
  'somei-yoshino-berdoues',
  'durga-ds-durga',
  'solving-your-buying-needs',
  'verified-resellers',
  'seller-to-buyer',
];

const DATA_URI_RE = /data:image\/(png|jpeg|jpg);base64,([A-Za-z0-9+/=]+)/g;

function writeImage(outPathBase, mime, b64) {
  const buf = Buffer.from(b64, 'base64');
  const dir = path.dirname(outPathBase);
  fs.mkdirSync(dir, { recursive: true });
  const actualExt = mime === 'png' ? 'png' : 'jpg';
  const actualPath = outPathBase.replace(/\.webp$/, `.${actualExt}`);
  fs.writeFileSync(actualPath, buf);
  return actualPath.replace(root + path.sep, '').split(path.sep).join('/');
}

function pathForIndex(i, mime, b64, cache) {
  if (i === 0) {
    return writeImage(path.join(root, 'assets/images/hero.webp'), mime, b64);
  }
  if (i >= 1 && i <= 9) {
    return writeImage(
      path.join(root, 'assets/images/videos', `${VIDEO_SLUGS[i - 1]}.webp`),
      mime,
      b64
    );
  }
  const collPair = Math.floor((i - 10) / 2);
  const slug = COLLATERAL_SLUGS[collPair];
  if (!cache.has(slug)) {
    cache.set(
      slug,
      writeImage(path.join(root, 'assets/images/collateral', `${slug}.webp`), mime, b64)
    );
  }
  return cache.get(slug);
}

let html = fs.readFileSync(htmlPath, 'utf8');
const matches = [...html.matchAll(DATA_URI_RE)];
const cache = new Map();

console.log(`Found ${matches.length} embedded images`);

matches.forEach((m, i) => {
  const full = m[0];
  const relPath = pathForIndex(i, m[1], m[2], cache);
  const idx = html.indexOf(full);
  if (idx === -1) {
    console.error(`Could not find image #${i} to replace`);
    return;
  }
  html = html.slice(0, idx) + relPath + html.slice(idx + full.length);
});

fs.writeFileSync(htmlPath, html);
console.log('Done: images extracted and index.html updated');
