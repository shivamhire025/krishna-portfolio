# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added

- Mobile breakpoint CSS tokens (`--bp-xs` through `--bp-xl`) — see [docs/MOBILE-STANDARDS.md](docs/MOBILE-STANDARDS.md)
- Hamburger navigation with drawer panel, backdrop, and keyboard support
- Documentation set under `docs/` and root `README.md`
- `theme-color` meta and `prefers-reduced-motion` support for marquee

### Changed

- Consolidated responsive rules into one documented block in `index.html`
- Phone layout: full-width work/blog cards, flatter scrapbook notes, tighter gutters
- Lightbox / orbit-focus / footer respect safe-area insets
- Drawer nav uses full-width `<button>` links and instant scroll after close

### Fixed

- Navigation was hidden on phones with no alternative; hamburger menu restores access to all sections
- Mobile drawer menu links were nearly invisible after scroll (light pink text on cream); scroll styling now uses `nav-scrolled` class and drawer-specific colors
- About collage stayed `position: sticky` on phones (later scrapbook CSS overrode the mobile rule)
- Open hamburger over the dark hero left logo/toggle burgundy-on-burgundy; open state now forces a cream bar
- Contact nav uses `scroll-padding-top` (viewport min-height on contact was removed — it left a large empty band above the footer)
- “Available for freelance” used `href="#"` and jumped to the top of the page
- Work/blog text links were ~20px tall; now meet 44px touch minimum
- Theme/work filter `:hover` styles no longer stick after tap on touch devices

---

## [0.2.0] - 2025-06-02

### Added

- `assets/images/` folder structure for hero, video posters, and collateral
- In-page Vimeo playback via modal (no new tab)
- `scripts/extract-images.mjs` for migrating embedded base64 images

### Changed

- Replaced 34 inline base64 images with file paths (~570 KB → ~59 KB HTML)
- Work section links open video modal instead of external Vimeo tabs

### Removed

- Custom pink cursor (system default cursor restored)

---

## [0.1.0] - Initial

- Single-file portfolio with embedded assets and external Vimeo links
