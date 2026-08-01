# Mobile standards

Single source of truth for responsive behavior. CSS tokens live in `index.html` `:root`; rules are in the `/* --- Responsive --- */` block at the bottom of the stylesheet.

## Breakpoint tokens

| Token | Value | Typical devices | Primary layout changes |
|-------|-------|-----------------|------------------------|
| `--bp-xs` | 380px | iPhone SE, narrow Android | Single-column collateral; smaller hero type |
| `--bp-sm` | 600px | Most phones | 1-col grids, full-width CTAs, tighter section spacing |
| `--bp-md` | 768px | Large phones, small tablets | Hamburger nav; 2-col collateral; smaller marquee |
| `--bp-lg` | 900px | Tablets, small laptops | Stacked hero; 2-col service/work grids |
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

Apply `--touch-min` to: `.nav-toggle`, `.nav-link` (drawer, ≤768px), `.btn`, `.filter-btn`, `.work-card-link`, video play control (52px, already compliant).

## Component rules by breakpoint

### Navigation

| Viewport | Behavior |
|----------|----------|
| > 768px | Horizontal links in header |
| ≤ 768px | Hamburger opens right drawer; backdrop closes; Escape closes; link click scrolls + closes |

**Colors:** Scroll state uses class `nav-scrolled` on `<nav>` (not inline styles). Drawer links are `<button class="nav-link">` with full-width tap rows. When the menu is open, the header bar is forced cream with burgundy logo/toggle (including over the dark hero) so controls stay visible.

Safe areas: `env(safe-area-inset-top)` on nav and drawer; `safe-area-inset-*` on lightbox / orbit-focus close; footer bottom inset.

**Scroll:** `html { scroll-padding-top: 5rem }`. Drawer navigations use instant `scrollIntoView` after overflow unlock (smooth scroll is unreliable right after closing the drawer on mobile).

### Hero / videos

| Viewport | Behavior |
|----------|----------|
| ≤ 768px | Hide hero polaroid; orbit stage uses 44px side navs; intro copy full width |
| ≤ 600px | Tighter orbit track (~280px); smaller phone cards |

### Grids

| Component | ≤ 900px | ≤ 768px | ≤ 600px | ≤ 380px |
|-----------|---------|---------|---------|---------|
| Services / work / blog | straighten notes | 1-col work/blog | tighter section padding | smaller titles |
| Clients | 3-col | — | 2-col | smaller logos |
| Scrapbook tilts | services/about notes flat | work cards flat + full width | tag tilts off | — |

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
| 375px | Yes (Aug 2026) | Drawer buttons; contact uses scroll-padding (no section min-height) |
| 390px | Yes (Aug 2026) | About collage `relative` (not sticky); work cards full-width; no `href="#"` jump |
| 430px | Yes (Aug 2026) | Theme/work filter hover gated to fine pointers; touch targets ≥44px |

### Per feature

- [x] Hamburger: open, backdrop close, Escape, navigate to section closes menu
- [x] Open-menu header stays cream with dark controls over dark hero
- [x] Drawer nav links are full-width buttons; scroll lands with offset
- [x] No horizontal overflow (marquee excluded)
- [x] Work / blog card links ≥44px tall
- [x] Work filter + theme chips don’t stick in “hover” styles on touch
- [x] Reduced motion: marquee static; drawer transition off

### Regression on desktop

- [x] Nav links visible without hamburger above 768px
- [x] About polaroid stack sticky only from 901px up
- [x] Video orbit carousel on all breakpoints

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
