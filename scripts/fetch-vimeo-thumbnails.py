#!/usr/bin/env python3
"""Download high-resolution Vimeo thumbnails for all portfolio videos."""

import json
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "images" / "videos"

# vimeo_id -> filename slug (without extension)
VIDEOS = {
    "1169808818": "anejo-ugc",
    "1169808849": "just-bought-it-hair",
    "1169808854": "garba-ahmedabad",
    "1199274119": "greek-town-grill",
    "1199274113": "sambal",
    "1199274104": "bom-dia",
    "1199274106": "freddo-crepes",
    "1199274095": "menali",
    "1199274112": "carpe-diem-men",
    "1199274108": "skincare-beauty",
    "1199274094": "home-gifts",
    "1199274090": "garden-neighbours",
    "1199274116": "all-access-fitness",
    "1199274107": "soma-bone-broth",
    "1199274115": "westwood-wago",
    "1199274096": "sunny-greektown",
    "1199274100": "danforth-stroll",
    "1199274086": "greektown-reel-1",
    "1199274087": "greektown-reel-2",
    "1199274088": "greektown-reel-3",
    "1199274085": "greektown-reel-4",
}

THUMB_SIZE = "_960x540"  # sharp enough for cards; run optimize-images.py after fetch


def best_thumbnail_url(vimeo_id: str) -> str:
    url = f"https://vimeo.com/api/oembed.json?url=https://vimeo.com/{vimeo_id}"
    with urllib.request.urlopen(url, timeout=30) as resp:
        data = json.load(resp)
    thumb = data["thumbnail_url"]
    return re.sub(r"-d_\d+x\d+", f"-d{THUMB_SIZE}", thumb)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for vimeo_id, slug in VIDEOS.items():
        thumb_url = best_thumbnail_url(vimeo_id)
        dest = OUT / f"{slug}.jpg"
        urllib.request.urlretrieve(thumb_url, dest)
        kb = dest.stat().st_size // 1024
        print(f"OK {slug}.jpg ({kb} KB)")


if __name__ == "__main__":
    main()
