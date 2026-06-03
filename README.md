# Krishna Thakkar — Portfolio

A single-page portfolio for social media strategy, video work, and brand storytelling. Built as static HTML with no build step.

## Quick start

```bash
cd "Krishna Portfolio"
python3 -m http.server 8080
```

Open [http://localhost:8080](http://localhost:8080).

## Project structure

```
Krishna Portfolio/
├── index.html              # All markup, styles, and scripts
├── assets/images/          # Hero, video posters, collateral
├── scripts/
│   └── extract-images.mjs  # One-time base64 → files extractor
├── docs/                   # Standards and how-to guides
├── CHANGELOG.md
└── README.md
```

## Documentation

Start at [docs/README.md](docs/README.md).

| Doc | What it covers |
|-----|----------------|
| [MOBILE-STANDARDS.md](docs/MOBILE-STANDARDS.md) | Breakpoints, spacing tokens, touch targets, testing |
| [SITE-GUIDE.md](docs/SITE-GUIDE.md) | How the site works and how to edit content |
| [ASSETS.md](docs/ASSETS.md) | Image naming and folders |
| [PORTFOLIO-BEST-PRACTICES.md](docs/PORTFOLIO-BEST-PRACTICES.md) | Design, performance, and content guidelines |

## Deploy

Upload the entire folder to any static host (Netlify, Vercel, GitHub Pages, etc.). Ensure `assets/` is deployed alongside `index.html`.

For Vimeo embeds on production, allow embedding for your live domain in each video’s Vimeo settings.

## Related

- [CHANGELOG.md](CHANGELOG.md) — version history
