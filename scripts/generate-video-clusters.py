#!/usr/bin/env python3
"""Generate clustered video section HTML for index.html."""
play_svg = '<svg width="18" height="18" viewBox="0 0 24 24" fill="white"><polygon points="5,3 19,12 5,21"/></svg>'


def item(vid, title, slug):
    t = title.replace('"', "&quot;")
    return f"""    <button type="button" class="video-item" data-vimeo-id="{vid}" data-title="{t}">
      <div class="video-wrap">
        <picture>
          <source srcset="assets/images/videos/{slug}.webp" type="image/webp">
          <img src="assets/images/videos/{slug}.jpg" alt="{t}" loading="lazy" decoding="async" onerror="this.style.display='none';this.closest('.video-wrap')?.querySelector('.video-fallback').style.display='flex';" />
        </picture>
        <div class="video-fallback" style="display:none;position:absolute;inset:0;align-items:center;justify-content:center;flex-direction:column;gap:0.5rem;">
          <div style="font-size:2.5rem;">🎬</div>
          <div style="font-size:0.75rem;color:var(--fig);letter-spacing:0.1em;text-transform:uppercase;">{t}</div>
        </div>
        <div class="video-play-btn">{play_svg}</div>
        <div class="video-overlay"></div>
      </div>
      <div class="video-label">{t}</div>
    </button>"""


scroll_edge_left = '<div class="video-scroll-edge video-scroll-edge--left" aria-hidden="true"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M15 6l-6 6 6 6"/></svg></div>'
scroll_edge_right = '<div class="video-scroll-edge video-scroll-edge--right" aria-hidden="true"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M9 6l6 6-6 6"/></svg></div>'


def cluster(title, desc, items):
    body = "\n".join(items)
    return f"""  <div class="video-cluster">
    <div class="video-cluster-header">
      <h3 class="video-cluster-title">{title}</h3>
      <p class="video-cluster-desc">{desc}</p>
    </div>
    <div class="video-scroll-wrap">
      {scroll_edge_left}
      <div class="video-grid">
{body}
    </div>
      {scroll_edge_right}
    </div>
  </div>"""


clusters = [
    (
        "Restaurants & Dining",
        "Short-form edits for restaurants, cafés, and food brands.",
        [
            item("1169804875", "Distillery District", "distillery-district"),
            item("1169808802", "Distillery District #2", "distillery-district-2"),
            item("1169808809", "Tamasha", "tamasha"),
            item("1169808824", "Oro", "oro"),
            item("1169808834", "Oro #2", "oro-2"),
            item("1169808844", "Oro #3", "oro-3"),
            item("1199274119", "GreekTown Grill", "greek-town-grill"),
            item("1199274113", "Sambal", "sambal"),
            item("1199274104", "Bom Dia", "bom-dia"),
            item("1199274106", "Freddo & Crepes", "freddo-crepes"),
            item("1199274095", "Menali", "menali"),
        ],
    ),
    (
        "UGC & Social Reels",
        "Authentic, scroll-stopping content for Instagram and TikTok.",
        [
            item("1169808818", "Anejo — UGC Story Edit", "anejo-ugc"),
            item("1169808849", "Just Bought It Hair", "just-bought-it-hair"),
            item("1199274086", "GreekTown Reel 1", "greektown-reel-1"),
            item("1199274087", "GreekTown Reel 2", "greektown-reel-2"),
            item("1199274088", "GreekTown Reel 3", "greektown-reel-3"),
            item("1199274085", "GreekTown Reel 4", "greektown-reel-4"),
        ],
    ),
    (
        "Retail & Lifestyle",
        "Brand stories for local shops, services, and everyday lifestyle.",
        [
            item("1199274112", "Carpe Diem Men", "carpe-diem-men"),
            item("1199274108", "Skincare & Beauty", "skincare-beauty"),
            item("1199274094", "Home & Gifts", "home-gifts"),
            item("1199274090", "Garden Neighbours", "garden-neighbours"),
        ],
    ),
    (
        "Health & Wellness",
        "Fitness studios, nutrition, and wellbeing-focused content.",
        [
            item("1199274116", "All Access Fitness", "all-access-fitness"),
            item("1199274107", "Soma Bone Broth", "soma-bone-broth"),
        ],
    ),
    (
        "Community & Culture",
        "Events, neighbourhoods, and cultural moments brought to life.",
        [
            item("1169808854", "Garba Ahmedabad", "garba-ahmedabad"),
            item("1199274115", "Westwood WAGO", "westwood-wago"),
            item("1199274096", "Sunny Greektown", "sunny-greektown"),
            item("1199274100", "Danforth Stroll", "danforth-stroll"),
        ],
    ),
]

if __name__ == "__main__":
    print("\n".join(cluster(t, d, items) for t, d, items in clusters))
