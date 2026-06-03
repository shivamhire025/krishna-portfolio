# Portfolio best practices

Guidelines for maintaining Krishna Thakkar’s portfolio: content, design, performance, and accessibility.

## Content hierarchy

1. **Hero** — Name, role, one-line value prop, primary CTA (work), secondary (LinkedIn).
2. **Proof** — Video grid and work cards (show, don’t only tell).
3. **Depth** — Services, collateral, writing samples.
4. **Contact** — Clear next step (LinkedIn, availability).

Keep section labels consistent (`section-label` + `section-title` pattern).

## Visual design

- Use existing CSS variables (`--cream`, `--terracotta`, `--deep`, etc.); avoid one-off hex colors in inline styles.
- Headlines: Playfair Display. Body: DM Sans.
- Maintain generous whitespace on desktop; use `--space-gutter` on phone instead of cramming content.
- Motion: subtle hover lifts; respect `prefers-reduced-motion`.

## Imagery

- Real project frames beat generic stock.
- Compress before upload (see [ASSETS.md](ASSETS.md)).
- Always set meaningful `alt` text on `<img>`.
- Use `loading="lazy"` on below-the-fold images (already applied on videos and collateral).

## Video

- Host on Vimeo; embed in-site via modal (see [SITE-GUIDE.md](SITE-GUIDE.md)).
- Posters should match the actual grade and framing of the piece.
- Allow embedding on the live domain in Vimeo settings.
- Keep videos short-form context in labels (client / project name).

## Performance

- Keep `index.html` lean — assets in files, not base64.
- Limit custom font weights to what is used (currently 300, 400, 500, 700, 900).
- Avoid adding heavy libraries for a static portfolio.
- Test Lighthouse on mobile after large image swaps.

## Accessibility

- Minimum **44×44px** touch targets on phone (`--touch-min`).
- Keyboard: Escape closes lightbox and mobile menu.
- `aria-expanded` on hamburger; `aria-controls="nav-menu"`.
- Sufficient contrast: deep text on cream backgrounds (existing palette passes for body text).
- Do not rely on color alone for links — use underline or arrow on CTAs where needed.

## Mobile UX

Follow [MOBILE-STANDARDS.md](MOBILE-STANDARDS.md) for breakpoints. Never hide navigation on phone without a menu alternative.

## SEO and sharing (lightweight)

- Descriptive `<title>` and section headings (`h1` once in hero, `h2` in sections).
- `theme-color` matches brand background.
- LinkedIn is the primary outbound professional link.

## Changelog discipline

Document user-visible changes in [CHANGELOG.md](../CHANGELOG.md):

- **Added** — features
- **Changed** — behavior or design shifts
- **Fixed** — bugs

Link to the relevant doc when changing standards.

## When you change X, also update Y

| Change | Update |
|--------|--------|
| New brand color | `:root` tokens, spot-check contrast, CHANGELOG |
| New content section | MOBILE-STANDARDS grid table, SITE-GUIDE architecture |
| Performance work | Note in CHANGELOG; ASSETS if compression rules change |

## Related docs

- [MOBILE-STANDARDS.md](MOBILE-STANDARDS.md)
- [SITE-GUIDE.md](SITE-GUIDE.md)
- [ASSETS.md](ASSETS.md)
