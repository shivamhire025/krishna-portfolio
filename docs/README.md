# Documentation index

Self-learning guides for the Krishna Thakkar portfolio. Read these before making structural changes.

## Start here

| If you want to… | Read |
|-----------------|------|
| Change layout on phone or tablet | [MOBILE-STANDARDS.md](MOBILE-STANDARDS.md) |
| Add a video or swap a poster | [SITE-GUIDE.md](SITE-GUIDE.md) + [ASSETS.md](ASSETS.md) |
| Improve imagery or brand consistency | [PORTFOLIO-BEST-PRACTICES.md](PORTFOLIO-BEST-PRACTICES.md) |
| See what shipped when | [../CHANGELOG.md](../CHANGELOG.md) |

## Files in this folder

- **MOBILE-STANDARDS.md** — Breakpoint tokens, component behavior, testing checklist
- **SITE-GUIDE.md** — Architecture of `index.html`, JS behaviors, content updates
- **ASSETS.md** — Image paths, naming, and quality targets
- **PORTFOLIO-BEST-PRACTICES.md** — Portfolio design and content best practices

## When you change X, also update Y

| You change | Also update |
|------------|-------------|
| Breakpoint values in `:root` | `docs/MOBILE-STANDARDS.md` |
| New video in the grid | `index.html`, poster in `assets/images/videos/`, `docs/ASSETS.md` slug list |
| New collateral piece | `index.html`, `assets/images/collateral/`, lightbox `onclick` |
| User-facing behavior | `CHANGELOG.md` under `[Unreleased]` |

## Related

- [../README.md](../README.md) — project overview and quick start
