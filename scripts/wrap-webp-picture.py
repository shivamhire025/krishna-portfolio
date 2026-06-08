#!/usr/bin/env python3
"""Wrap <img> tags with <picture> + WebP source for assets that have .webp siblings."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "index.html"

IMG_RE = re.compile(
    r'<img\s+src="(assets/images/[^"]+)\.(jpg|jpeg|png)"([^>]*?)\s*/?>',
    re.IGNORECASE,
)


def wrap_img(match: re.Match) -> str:
    base, ext, rest = match.groups()
    webp = ROOT / f"{base}.webp"
    if not webp.exists():
        return match.group(0)
    rest = rest.replace(
        "this.parentNode.querySelector('.video-fallback')",
        "this.closest('.video-wrap')?.querySelector('.video-fallback')",
    )
    return (
        f'<picture>\n          <source srcset="{base}.webp" type="image/webp">\n'
        f'          <img src="{base}.{ext.lower()}"{rest} />\n'
        f"        </picture>"
    )


def main() -> None:
    html = HTML.read_text()
    updated, count = IMG_RE.subn(wrap_img, html)
    HTML.write_text(updated)
    print(f"Wrapped {count} images with WebP picture sources")


if __name__ == "__main__":
    main()
