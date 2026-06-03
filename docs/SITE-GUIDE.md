# Site guide

How the Krishna Thakkar portfolio is built and how to update it without breaking behavior.

## Architecture

```
index.html
├── <style>           All CSS (tokens, layout, responsive)
├── <nav>             Logo + hamburger + #nav-menu
├── <sections>        Hero, about, services, work, videos, social, collateral, blog, contact
├── #lightbox         Image lightbox + Vimeo iframe
└── <script>          Scroll, filters, modals, mobile nav
```

No bundler or framework. Deploy as static files.

## Key JavaScript behaviors

| Function / listener | Purpose |
|---------------------|---------|
| `scrollToSection(id)` | Smooth scroll with nav height offset |
| `setNavOpen(open)` | Mobile drawer + body scroll lock |
| `openLightbox(src, caption)` | Full-size collateral image |
| `openVideoModal(id, title)` | Vimeo iframe in lightbox |
| `closeLightbox()` | Clears image and iframe `src` |
| `filterWork(type, btn)` | Work grid filter |

`data-target` on nav links and hero CTA triggers scroll. Video grid uses `data-vimeo-id` and `data-title` on `.video-item` buttons.

## Add a video to the grid

1. Upload the video to Vimeo; note the numeric ID from the URL.
2. Add a poster image to `assets/images/videos/your-slug.jpg` (see [ASSETS.md](ASSETS.md)).
3. In `index.html`, duplicate a `.video-item` block inside `#videoGrid`:

```html
<button type="button" class="video-item" data-vimeo-id="YOUR_ID" data-title="Your Title">
  <div class="video-wrap">
    <img src="assets/images/videos/your-slug.jpg" alt="Your Title" loading="lazy" ... />
    ...
  </div>
  <div class="video-label">Your Title</div>
</button>
```

4. Optionally add a work card with `.watch-video-btn` and the same `data-vimeo-id`.
5. Enable Vimeo **embed** for your production domain.

## Swap an image

Replace the file under `assets/images/` keeping the same filename, or update every `src` and `openLightbox('...')` path that references it.

## Edit collateral

Each `.collateral-card` has:

- `onclick="openLightbox('assets/images/collateral/slug.jpg', 'Title')"`
- Thumbnail `<img src="assets/images/collateral/slug.jpg" ...>`

Keep both paths in sync.

## Colors and fonts

CSS variables in `:root` at the top of `index.html`. Fonts load from Google Fonts in `<head>`.

## Scripts

| Script | When to use |
|--------|-------------|
| `scripts/extract-images.mjs` | Only if you re-embed base64 in HTML and need to extract files again |

## Local preview

```bash
python3 -m http.server 8080
```

## When you change X, also update Y

| Change | Update |
|--------|--------|
| New section | Nav links (desktop + mobile), `CHANGELOG.md`, consider MOBILE-STANDARDS grid rules |
| New Vimeo ID | Video grid + any work card button |
| JS behavior | This guide if workflow changes |

## Related docs

- [ASSETS.md](ASSETS.md)
- [MOBILE-STANDARDS.md](MOBILE-STANDARDS.md)
- [PORTFOLIO-BEST-PRACTICES.md](PORTFOLIO-BEST-PRACTICES.md)
