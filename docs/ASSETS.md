# Assets guide

Image files live under `assets/images/`. Do not embed large base64 strings in `index.html`.

## Folder layout

```
assets/images/
├── hero.jpg              # Hero portrait (+ hero.webp)
├── videos/               # Video grid posters (9:16 friendly)
│   ├── distillery-district.jpg
│   ├── distillery-district-2.jpg
│   ├── tamasha.jpg
│   ├── anejo-ugc.jpg
│   ├── oro.jpg
│   ├── oro-2.jpg
│   ├── oro-3.jpg
│   ├── just-bought-it-hair.jpg
│   └── garba-ahmedabad.jpg
├── blog/                 # Writing section thumbnails (from article og:image)
│   ├── influencer-marketing-strategies.png
│   ├── data-driven-social-media.jpeg
│   ├── ultimate-guide-freelancer.png
│   ├── start-agency-guide.png
│   ├── sales-funnel-guide.png
│   └── agency-freelancer-tools.jpeg
└── collateral/           # Square-ish design work thumbs
    ├── bulletproof-your-agency.jpg
    ├── freedom-from-monthly-payments.jpg
    └── ... (12 files total)
```

## Naming rules

- Lowercase kebab-case: `my-project-name.jpg`
- Match slug in `index.html` paths exactly
- Prefer `.webp` for smaller size; update `src` extensions if you change format

## Quality targets

| Asset | Suggested size | Notes |
|-------|----------------|-------|
| Hero | 1200–1600px wide | Portrait; optimize to &lt; 300 KB if possible |
| Video poster | 800–1200px wide | 9:16 crop; JPEG 80% or WebP |
| Collateral thumb | 800–1200px square | Used in grid and lightbox |
| Blog card thumb | 800×400px (2:1) | Writing section; swap `.svg` for `.jpg` / `.webp` when you have hero images |

## Video poster workflow

1. Add the Vimeo ID and slug to `scripts/fetch-vimeo-thumbnails.py` and `scripts/generate-video-clusters.py`.
2. Run `python3 scripts/fetch-vimeo-thumbnails.py` to pull **960×540** thumbnails from Vimeo.
3. Run `npm run optimize:images` to resize/compress JPEGs and generate `.webp` siblings.
4. Run `python3 scripts/wrap-webp-picture.py` after adding new `<img>` tags (wraps with `<picture>` if `.webp` exists).
5. Reference in the matching `.video-item` (or regenerate clusters HTML via `scripts/generate-video-clusters.py`).

## Blog thumbnail workflow

Thumbnails are pulled from each article’s `og:image` on ClientJoy and saved under `assets/images/blog/`. To refresh after a post update:

1. Open the article URL and read `og:image` from the page source (or use a link preview debugger).
2. Download the image to `assets/images/blog/{slug}.{png|jpeg}`.
3. Update the matching `.blog-card-img img` `src` (and `width`/`height` if the aspect ratio changed) in `index.html`.

## Collateral workflow

1. Save full-resolution export to `assets/images/collateral/{slug}.jpg`.
2. Update both thumbnail `src` and `openLightbox('...')` first argument on the card.

## Extract script

If images were pasted as base64 again:

```bash
node scripts/extract-images.mjs
```

This writes files and replaces URIs in `index.html` in document order (hero → 9 videos → 12 collateral pairs).

## When you change X, also update Y

| Change | Update |
|--------|--------|
| New filename | All `src` and `openLightbox` references |
| New video slug | [SITE-GUIDE.md](SITE-GUIDE.md) video grid section |
| Format switch (jpg → webp) | Every path in `index.html` |

## Related docs

- [SITE-GUIDE.md](SITE-GUIDE.md)
- [PORTFOLIO-BEST-PRACTICES.md](PORTFOLIO-BEST-PRACTICES.md)
