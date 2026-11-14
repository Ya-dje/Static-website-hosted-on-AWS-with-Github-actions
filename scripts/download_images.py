"""
==============================================
  OLIVE'S SPACE — Image Downloader
  Run this script once to download all images.

  Requirements: Python 3.7+  (no extra installs needed)

  Usage:
      python download_images.py

  All images will be saved into an "images/" folder
  in the same directory as this script.
==============================================
"""

import urllib.request
import os
import sys

IMAGES = [
    # ── Carousel (home hero) ──────────────────────────────────────────
    ("images/carousel-1.jpg",     "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1400&q=80&fit=crop"),
    ("images/carousel-2.jpg",     "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=1400&q=80&fit=crop"),
    ("images/carousel-3.jpg",     "https://images.unsplash.com/photo-1469334031218-e382a71b716b?w=1400&q=80&fit=crop"),
    ("images/carousel-4.jpg",     "https://images.unsplash.com/photo-1483985988355-763728e1935b?w=1400&q=80&fit=crop"),

    # ── Category grid (home) ─────────────────────────────────────────
    ("images/cat-dresses.jpg",    "https://images.unsplash.com/photo-1551232864-3f0890e580d9?w=800&q=80&fit=crop"),
    ("images/cat-outerwear.jpg",  "https://images.unsplash.com/photo-1594938298603-c8148c4b4057?w=600&q=80&fit=crop"),
    ("images/cat-accessories.jpg","https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=600&q=80&fit=crop"),

    # ── Products ─────────────────────────────────────────────────────
    ("images/product-trench.jpg", "https://images.unsplash.com/photo-1591369822096-ffd140ec948f?w=600&q=80&fit=crop"),
    ("images/product-dress.jpg",  "https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=600&q=80&fit=crop"),
    ("images/product-blazer.jpg", "https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=600&q=80&fit=crop"),
    ("images/product-pumps.jpg",  "https://images.unsplash.com/photo-1543163521-1bf539c55dd2?w=600&q=80&fit=crop"),
    ("images/product-tote.jpg",   "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=600&q=80&fit=crop"),
    ("images/product-scarf.jpg",  "https://images.unsplash.com/photo-1601924994987-69e26d50dc26?w=600&q=80&fit=crop"),
    ("images/product-mules.jpg",  "https://images.unsplash.com/photo-1603487742131-4160ec999306?w=600&q=80&fit=crop"),
    ("images/product-gloves.jpg", "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=600&q=80&fit=crop"),
    ("images/product-hat.jpg",    "https://images.unsplash.com/photo-1529958030586-3aae4ca485ff?w=600&q=80&fit=crop"),

    # ── Home banner CTA ──────────────────────────────────────────────
    ("images/banner-cta.jpg",     "https://images.unsplash.com/photo-1445205170230-053b83016050?w=1400&q=80&fit=crop"),

    # ── Testimonial avatars ──────────────────────────────────────────
    ("images/avatar-amara.jpg",   "https://images.unsplash.com/photo-1531746020798-e6953c6e8e04?w=80&q=80&fit=crop&crop=face"),
    ("images/avatar-sophie.jpg",  "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=80&q=80&fit=crop&crop=face"),
    ("images/avatar-nadia.jpg",   "https://images.unsplash.com/photo-1580489944761-15a19d654956?w=80&q=80&fit=crop&crop=face"),
    ("images/avatar-chioma.jpg",  "https://images.unsplash.com/photo-1567532939604-b6b5b0db2604?w=80&q=80&fit=crop&crop=face"),
    ("images/avatar-leila.jpg",   "https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91?w=80&q=80&fit=crop&crop=face"),
    ("images/avatar-isabelle.jpg","https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=80&q=80&fit=crop&crop=face"),

    # ── Instagram strip ──────────────────────────────────────────────
    ("images/insta-1.jpg",        "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=300&q=80&fit=crop"),
    ("images/insta-2.jpg",        "https://images.unsplash.com/photo-1509631179647-0177331693ae?w=300&q=80&fit=crop"),
    ("images/insta-3.jpg",        "https://images.unsplash.com/photo-1496747611176-843222e1e57c?w=300&q=80&fit=crop"),
    ("images/insta-4.jpg",        "https://images.unsplash.com/photo-1485968579580-b6d095142e6e?w=300&q=80&fit=crop"),
    ("images/insta-5.jpg",        "https://images.unsplash.com/photo-1520367445093-50dc08a59d9d?w=300&q=80&fit=crop"),

    # ── Products page hero ───────────────────────────────────────────
    ("images/page-hero-products.jpg","https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=1400&q=80&fit=crop"),

    # ── About page ───────────────────────────────────────────────────
    ("images/about-hero.jpg",     "https://images.unsplash.com/photo-1556905055-8f358a7a47b2?w=900&q=80&fit=crop"),
    ("images/about-story.jpg",    "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=700&q=80&fit=crop"),
    ("images/about-numbers-bg.jpg","https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=1400&q=80&fit=crop"),

    # ── Team ─────────────────────────────────────────────────────────
    ("images/team-olive.jpg",     "https://images.unsplash.com/photo-1531746020798-e6953c6e8e04?w=400&q=80&fit=crop&crop=face"),
    ("images/team-diane.jpg",     "https://images.unsplash.com/photo-1580489944761-15a19d654956?w=400&q=80&fit=crop&crop=face"),
    ("images/team-marie.jpg",     "https://images.unsplash.com/photo-1567532939604-b6b5b0db2604?w=400&q=80&fit=crop&crop=face"),
]

def download_all():
    os.makedirs("images", exist_ok=True)
    total = len(IMAGES)
    success = 0
    failed = []

    print(f"\n{'='*52}")
    print(f"  OLIVE'S SPACE — Downloading {total} images")
    print(f"{'='*52}\n")

    headers = {"User-Agent": "Mozilla/5.0"}

    for i, (path, url) in enumerate(IMAGES, 1):
        filename = os.path.basename(path)
        bar = f"[{i:02d}/{total}]"
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=20) as resp:
                data = resp.read()
            with open(path, "wb") as f:
                f.write(data)
            kb = len(data) // 1024
            print(f"  {bar} ✓  {filename:<35} {kb} KB")
            success += 1
        except Exception as e:
            print(f"  {bar} ✗  {filename:<35} FAILED — {e}")
            failed.append(filename)

    print(f"\n{'='*52}")
    print(f"  Done! {success}/{total} images downloaded.")
    if failed:
        print(f"  Failed ({len(failed)}): {', '.join(failed)}")
    print(f"{'='*52}\n")
    print("  Next step: open index.html in your browser — everything")
    print("  will work offline using the local images/ folder.\n")

if __name__ == "__main__":
    download_all()
