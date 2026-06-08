#!/usr/bin/env python3
"""Compress portfolio images for web (uses macOS sips). Skips upscaling small files."""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMAGES = ROOT / "assets" / "images"

MAX_EDGE = {
    "videos": 720,
    "blog": 800,
    "hero.jpg": 1200,
}


def get_max_dimension(path: Path) -> int:
    result = subprocess.run(
        ["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(path)],
        capture_output=True,
        text=True,
        check=True,
    )
    dims = [int(line.split()[-1]) for line in result.stdout.splitlines() if "pixel" in line]
    return max(dims) if dims else 0


def optimize_file(path: Path, max_edge: int, force_jpg: bool = False) -> None:
    before = path.stat().st_size
    current_max = get_max_dimension(path)

    args = ["sips", "-s", "format", "jpeg", "-s", "formatOptions", "82"]
    if current_max > max_edge:
        args.extend(["-Z", str(max_edge)])
    args.extend([str(path), "--out", str(path.with_suffix(".opt.jpg"))])

    subprocess.run(args, check=True, capture_output=True)
    tmp = path.with_suffix(".opt.jpg")

    if force_jpg or path.parent.name == "videos":
        dest = path.with_suffix(".jpg")
        if dest != path and path.exists():
            path.unlink()
    else:
        dest = path

    tmp.replace(dest)
    after = dest.stat().st_size
    if after >= before and current_max <= max_edge:
        print(f"  {dest.name}: kept ({after // 1024}KB, already small)")
        return
    pct = max(0, 100 - (after * 100 // max(before, 1)))
    print(f"  {dest.name}: {before // 1024}KB → {after // 1024}KB ({pct}% smaller)")


def main() -> None:
    if sys.platform != "darwin":
        print("This script requires macOS sips.", file=sys.stderr)
        sys.exit(1)

    hero = IMAGES / "hero.jpg"
    if hero.exists():
        print("hero.jpg")
        optimize_file(hero, MAX_EDGE["hero.jpg"])

    for folder, max_edge in (("videos", MAX_EDGE["videos"]), ("blog", MAX_EDGE["blog"])):
        dir_path = IMAGES / folder
        if not dir_path.is_dir():
            continue
        print(f"\n{folder}/")
        for path in sorted(dir_path.iterdir()):
            if path.suffix.lower() in {".jpg", ".jpeg", ".png"}:
                optimize_file(path, max_edge, force_jpg=(folder == "blog"))


if __name__ == "__main__":
    main()
