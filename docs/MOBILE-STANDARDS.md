# Mobile standards

Single source of truth for responsive behavior. CSS tokens live in `index.html` `:root`; rules are in the `/* --- Responsive --- */` block at the bottom of the stylesheet.

## Breakpoint tokens

| Token | Value | Typical devices | Primary layout changes |
|-------|-------|-----------------|------------------------|
| `--bp-xs` | 380px | iPhone SE, narrow Android | Single-column collateral; smaller hero type |
| `--bp-sm` | 600px | Most phones | Hamburger nav, 1-col grids, full-width CTAs |
| `--bp-md` | 768px | Large phones, small tablets | 2-col collateral; smaller marquee |
| `--bp-lg` | 900px | Tablets, small laptops | Stacked hero; 2-col video grid |
| `--bp-xl` | 1200px | Desktop | Optional wider section gutters |

Media queries use **max-width** (mobile-first overrides):

```css
@media (max-width: 900px) { /* --bp-lg */ }
@media (max-width: 768px) { /* --bp-md */ }
@media (max-width: 600px) { /* --bp-sm */ }
@media (max-width: 380px) { /* --bp-xs */ }
```

## Spacing and touch tokens

| Token | Value | Use |
|-------|-------|-----|
| `--space-section` | 7rem | Desktop vertical section padding |
| `--space-section-sm` | 4rem | Phone vertical section padding |
| `--space-gutter` | 1.25rem | Phone horizontal padding |
| `--touch-min` | 44px | Minimum tap target (WCAG 2.5.5) |

Apply `--touch-min` to: `.nav-toggle`, `.nav-link` (mobile panel), `.filter-btn`, video play control (52px, already compliant).

## Component rules by breakpoint

### Navigation

| Viewport | Behavior |
|----------|----------|
| > 600px | Horizontal links in header |
| ≤ 600px | Hamburger opens right drawer; backdrop closes; Escape closes; link click scrolls + closes |

**Colors:** Scroll state uses class `nav-scrolled` on `<nav>` (not inline styles). On phones, drawer links always use `var(--deep)` on `var(--cream)` so they stay readable when the header bar turns pink after scroll. When the menu is open, the header bar resets to cream with dark logo and toggle bars.

Safe areas: `env(safe-area-inset-top)` on nav and drawer; `safe-area-inset-*` on lightbox close button.

### Hero

| Viewport | Behavior |
|----------|----------|
| ≤ 900px | Single column; image block 50vh |
| ≤ 600px | Image 45vh; stacked full-width buttons; hide scroll hint and side float text |

### Grids

| Component | ≤ 900px | ≤ 600px | ≤ 380px |
|-----------|---------|---------|---------|
| Services / work / blog | 2 columns | 1 column | 1 column |
| Video clusters | Horizontal scroll row per cluster | Same; narrower cards (~58vw) |
| Collateral | auto-fill | 2 columns | 1 column |

### Lightbox / Vimeo modal

| Viewport | Behavior |
|----------|----------|
| ≤ 600px | Video wrapper full viewport width; square corners; close button respects safe area |

### Motion

`prefers-reduced-motion: reduce` disables marquee animation, smooth scroll, reveal transitions, and drawer slide transition.

## Testing checklist

Test in Chrome DevTools device mode **and** at least one real phone when possible.

| Width | Checked | Notes |
|-------|---------|-------|
| 375px | Yes | Hamburger opens/closes; all 7 nav targets scroll correctly; no horizontal scroll |
| 390px | Yes | Video modal full width; close button tappable |
| 430px | Yes | Collateral 2-col; filters wrap; posters load |

### Per feature

- [x] Hamburger: open, backdrop close, Escape, navigate to section closes menu
- [x] Drawer nav links readable after scrolling (dark text on cream panel)
- [x] No horizontal overflow on home, videos, collateral, contact
- [x] Video clusters scroll horizontally; inline play works
- [x] Work filter buttons meet touch size
- [x] Collateral lightbox opens image
- [x] Reduced motion: marquee static when OS setting enabled

### Regression on desktop

- [x] Nav links visible without hamburger above 600px
- [x] Hero two-column layout from 901px up
- [x] Video clusters horizontal scroll on all breakpoints

## When you change X, also update Y

| Change | Update |
|--------|--------|
| New breakpoint | `:root` in `index.html`, this file’s tables, `CHANGELOG.md` |
| Nav behavior | `index.html` HTML/CSS/JS, testing table above |
| Component layout at a width | Matching `@media` block comment (`/* --bp-sm */`) |

## Related docs

- [SITE-GUIDE.md](SITE-GUIDE.md) — nav and lightbox JavaScript
- [PORTFOLIO-BEST-PRACTICES.md](PORTFOLIO-BEST-PRACTICES.md) — performance and accessibility
- [../CHANGELOG.md](../CHANGELOG.md)
