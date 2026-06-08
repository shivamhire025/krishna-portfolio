#!/usr/bin/env python3
"""Generate WebP versions of portfolio images (requires Pillow)."""

import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Install Pillow: pip3 install Pillow", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[1]
IMAGES = ROOT / "assets" / "images"
WEBP_QUALITY = 82

TARGETS = [
    IMAGES / "videos",
    IMAGES / "blog",
    IMAGES / "hero.png",
]


def to_webp(src: Path) -> None:
    dest = src.with_suffix(".webp")
    with Image.open(src) as img:
        if img.mode not in ("RGB", "RGBA"):
            img = img.convert("RGB")
        elif img.mode == "RGBA":
            img = img.convert("RGB")
        img.save(dest, "WEBP", quality=WEBP_QUALITY, method=6)
    before = src.stat().st_size
    after = dest.stat().st_size
    pct = max(0, 100 - (after * 100 // max(before, 1)))
    print(f"  {dest.name}: {before // 1024}KB → {after // 1024}KB ({pct}% smaller)")


def main() -> None:
    for target in TARGETS:
        if target.is_file():
            print(target.name)
            to_webp(target)
            continue
        if not target.is_dir():
            continue
        print(f"\n{target.name}/")
        for path in sorted(target.iterdir()):
            if path.suffix.lower() in {".jpg", ".jpeg", ".png"}:
                to_webp(path)


if __name__ == "__main__":
    main()
