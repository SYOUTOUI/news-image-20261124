"""Render asset/entry.png for the make.fun news-image-20261124 entry.

Newspaper-style infographic summarising Tuesday 24 November 2026.
Run locally with Pillow (render-time only); the submitted main.py is
standard-library only and just copies the bundled PNG.

Facts (public news coverage of 24 Nov 2026):
- Nvidia reinstated Jensen Huang as CEO; shares rose 31% in a day.
- Ukraine said it sank the Russian corvette Merkury off Benghazi, Libya,
  with naval drones (Zelenskyy confirmed).
- Iran said three tankers were hit by mines in the Strait of Hormuz.
- Russian aircraft flew into South Korea's air defence identification
  zone; a Russian drone briefly entered Polish airspace.
- Factory fire in Banten, Indonesia: 26 killed, dozens missing.
- S&P 500 +4.7%, Nikkei 225 +3.9%.
"""

import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
OUT = HERE / "asset" / "entry.png"

W, H = 1024, 1024
PAPER = (247, 242, 232)
INK = (26, 26, 26)
RED = (209, 52, 44)
GREY = (60, 60, 60)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def icon_chip(d, x, y, s=64):
    d.rectangle([x + 14, y + 14, x + s - 14, y + s - 14], outline=INK, width=4)
    d.rectangle([x + 24, y + 24, x + s - 24, y + s - 24], outline=INK, width=3)
    for i in range(3):
        px = x + 22 + i * 10
        d.line([px, y + 4, px, y + 14], fill=INK, width=3)
        d.line([px, y + s - 14, px, y + s - 4], fill=INK, width=3)
        d.line([x + 4, y + 22 + i * 10, x + 14, y + 22 + i * 10], fill=INK, width=3)
        d.line([x + s - 14, y + 22 + i * 10, x + s - 4, y + 22 + i * 10], fill=INK, width=3)


def icon_ship(d, x, y, s=64):
    d.polygon([(x + 6, y + 40), (x + s - 6, y + 40), (x + s - 14, y + 54), (x + 14, y + 54)], outline=INK, width=4)
    d.rectangle([x + 22, y + 22, x + 42, y + 40], outline=INK, width=3)
    d.line([x + 32, y + 10, x + 32, y + 22], fill=INK, width=3)
    d.line([x + 32, y + 10, x + 44, y + 16], fill=INK, width=3)
    for wx in (8, 26, 44):
        d.arc([x + wx, y + 56, x + wx + 12, y + 62], 0, 180, fill=INK, width=3)


def icon_tanker(d, x, y, s=64):
    d.polygon([(x + 4, y + 38), (x + s - 4, y + 38), (x + s - 12, y + 54), (x + 12, y + 54)], outline=INK, width=4)
    for i, cx in enumerate((14, 26, 38)):
        d.rectangle([x + cx, y + 24, x + cx + 9, y + 38], outline=INK, width=3)
    for ang in range(0, 360, 45):
        import math
        r1, r2 = 4, 11
        x1 = x + 52 + r1 * math.cos(math.radians(ang))
        y1 = y + 14 + r1 * math.sin(math.radians(ang))
        x2 = x + 52 + r2 * math.cos(math.radians(ang))
        y2 = y + 14 + r2 * math.sin(math.radians(ang))
        d.line([x1, y1, x2, y2], fill=INK, width=3)


def icon_plane(d, x, y, s=64):
    d.polygon([(x + 8, y + 34), (x + 30, y + 30), (x + 56, y + 14), (x + 52, y + 26),
               (x + 34, y + 40), (x + 44, y + 52), (x + 34, y + 50), (x + 22, y + 42),
               (x + 12, y + 46), (x + 10, y + 40)], outline=INK, width=3)
    d.arc([x + 44, y + 4, x + 60, y + 20], 200, 340, fill=INK, width=3)
    d.arc([x + 50, y + 10, x + 62, y + 22], 200, 340, fill=INK, width=3)


def icon_factory(d, x, y, s=64):
    d.rectangle([x + 8, y + 30, x + 44, y + 56], outline=INK, width=4)
    d.polygon([(x + 8, y + 30), (x + 17, y + 20), (x + 26, y + 30), (x + 35, y + 20), (x + 44, y + 30)],
              outline=INK, width=3)
    d.rectangle([x + 46, y + 12, x + 54, y + 56], outline=INK, width=3)
    d.polygon([(x + 50, y + 4), (x + 56, y + 12), (x + 52, y + 12), (x + 58, y + 20),
               (x + 46, y + 20), (x + 50, y + 12), (x + 46, y + 12)], fill=INK)
    d.rectangle([x + 14, y + 40, x + 20, y + 48], outline=INK, width=2)
    d.rectangle([x + 26, y + 40, x + 32, y + 48], outline=INK, width=2)


def icon_chart(d, x, y, s=64):
    d.line([x + 8, y + 56, x + 56, y + 56], fill=INK, width=3)
    for i, h in enumerate((14, 24, 34)):
        bx = x + 14 + i * 13
        d.rectangle([bx, y + 52 - h, bx + 8, y + 52], fill=INK)
    d.line([x + 10, y + 34, x + 26, y + 24, x + 38, y + 28, x + 56, y + 8], fill=INK, width=4)
    d.polygon([(x + 56, y + 8), (x + 46, y + 10), (x + 54, y + 18)], fill=INK)


def draw_globe(d, cx, cy, r=26):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=INK, width=3)
    d.ellipse([cx - 10, cy - r, cx + 10, cy + r], outline=INK, width=2)
    d.line([cx - r, cy, cx + r, cy], fill=INK, width=2)
    d.arc([cx - r, cy - 12, cx + r, cy + 12], 0, 360, fill=INK, width=2)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    rng = random.Random(20261124)
    for _ in range(6000):
        x, y = rng.randrange(W), rng.randrange(H)
        shade = rng.choice([(238, 233, 221), (252, 248, 240)])
        d.point((x, y), fill=shade)

    d.rectangle([0, 0, W, 62], fill=RED)
    d.rectangle([0, H - 62, W, H], fill=RED)

    f_head = font(SERIF_B, 78)
    d.text((W // 2, 92), "24 NOVEMBER 2026", font=f_head, fill=INK, anchor="ma")

    f_sub = font(SANS, 30)
    sub = "THE WORLD IN ONE DAY"
    spaced = " ".join(list(sub.replace(" ", "  ")))
    d.text((W // 2, 196), spaced, font=f_sub, fill=INK, anchor="ma")
    d.line([80, 252, W - 80, 252], fill=INK, width=2)

    stories = [
        (icon_chip, "NVIDIA BRINGS BACK HUANG",
         "Shares jump 31% as Jensen Huang returns as CEO."),
        (icon_ship, "UKRAINE SINKS RUSSIAN WARSHIP",
         "Naval drones sink the corvette Merkury off Libya."),
        (icon_tanker, "TANKERS HIT IN HORMUZ",
         "Three tankers struck by mines in the Strait of Hormuz."),
        (icon_plane, "AIRSPACE BREACHES",
         "Russian aircraft enter South Korea's air defence zone; Russian drone over Poland."),
        (icon_factory, "INDONESIA FACTORY FIRE",
         "26 killed, dozens missing in Banten."),
        (icon_chart, "MARKETS RALLY",
         "S&P 500 up 4.7%, Nikkei up 3.9%."),
    ]
    f_title = font(SANS_B, 32)
    f_body = font(SANS, 21)
    xs = [72, 524]
    ys = [286, 488, 690]
    for i, (icon, title, body) in enumerate(stories):
        x0, y0 = xs[i % 2], ys[i // 2]
        icon(d, x0, y0 + 6)
        tx = x0 + 78
        tw = 360
        lines = wrap(d, title, f_title, tw)
        ly = y0
        for ln in lines[:2]:
            d.text((tx, ly), ln, font=f_title, fill=INK)
            ly += 38
        for ln in wrap(d, body, f_body, tw)[:3]:
            d.text((tx, ly + 4), ln, font=f_body, fill=GREY)
            ly += 27

    draw_globe(d, W // 2, 918, 24)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT, format="PNG", optimize=True)
    print(f"wrote {OUT} {img.size} {OUT.stat().st_size} bytes")


if __name__ == "__main__":
    main()
