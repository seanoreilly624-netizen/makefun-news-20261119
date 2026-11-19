#!/usr/bin/env python3
"""Draw entry.png: the world news of Thursday 19 November 2026.

One 1024x1024 PNG, drawn entirely with Pillow primitives and DejaVu Sans.
No AI generation, no photos, no borrowed artwork: every glyph is a shape
or a line of text rendered by this script.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (13, 26, 46)          # deep navy
CARD = (23, 38, 63)        # lighter navy card
CARD_LINE = (48, 68, 99)   # card border
WHITE = (244, 246, 250)
MUTED = (199, 210, 224)
GOLD = (242, 193, 78)
INK = (13, 26, 46)         # dark ink for glyphs on coloured discs

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
TITLE = ImageFont.truetype(FONT_DIR + "DejaVuSans-Bold.ttf", 68)
SUB = ImageFont.truetype(FONT_DIR + "DejaVuSans.ttf", 27)
TAG = ImageFont.truetype(FONT_DIR + "DejaVuSans-Bold.ttf", 17)
HEAD = ImageFont.truetype(FONT_DIR + "DejaVuSans-Bold.ttf", 30)
BODY = ImageFont.truetype(FONT_DIR + "DejaVuSans.ttf", 21)  # 21, not 22:
# the corrected Anthropic line is 864px at 22pt but the card only fits
# 844px; 21pt brings it to ~825px so it stays inside the card.
FOOT = ImageFont.truetype(FONT_DIR + "DejaVuSans.ttf", 18)

# (tag, colour, headline, one-line summary)
STORIES = [
    ("DIPLOMACY", (242, 193, 78),
     "FIRST-EVER TRUMP\u2013XI\u2013PUTIN SUMMIT",
     "The US, Chinese and Russian leaders meet in Shenzhen at APEC."),
    ("MIDDLE EAST", (232, 106, 51),
     "ISRAEL LAUNCHES GAZA GROUND PUSH",
     "Troops advance in central Gaza as the truce body faults both sides."),
    ("ENERGY", (43, 179, 163),
     "TANKERS HIT MINES NEAR HORMUZ",
     "Three oil tankers catch fire east of the strait; oil holds near $92."),
    ("JUSTICE", (155, 126, 222),
     "WORLD COURT RULES ON ROHINGYA",
     "The ICJ delivers its landmark judgment on Myanmar's alleged genocide."),
    ("CULTURE", (229, 72, 77),
     "GTA VI LAUNCHES AFTER 13 YEARS",
     "Rockstar's blockbuster arrives; an estimated 17m copies sold day one."),
    ("MARKETS", (76, 175, 125),
     "ANTHROPIC DEBUTS ON NASDAQ",
     "The AI firm lists as ANT after pricing at $83 a share in a record $81bn offering."),
]


def rounded(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill,
                           outline=outline, width=width)


def icon_summit(draw, cx, cy, r, colour):
    # Three overlapping discs: three leaders at one table.
    draw.ellipse([cx - r, cy - r * 0.55, cx - r * 0.15, cy + r * 0.55],
                 fill=(242, 193, 78))
    draw.ellipse([cx - r * 0.42, cy - r, cx + r * 0.42, cy + r * 0.1],
                 fill=(229, 72, 77))
    draw.ellipse([cx + r * 0.15, cy - r * 0.55, cx + r, cy + r * 0.55],
                 fill=(76, 175, 125))
    draw.ellipse([cx - r * 0.55, cy + r * 0.3, cx + r * 0.55, cy + r],
                 fill=colour)


def icon_burst(draw, cx, cy, r, colour):
    # Starburst: a sudden ground advance.
    import math
    pts = []
    for i in range(16):
        ang = math.pi * i / 8
        rad = r if i % 2 == 0 else r * 0.45
        pts.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
    draw.polygon(pts, fill=colour)
    draw.ellipse([cx - r * 0.28, cy - r * 0.28, cx + r * 0.28, cy + r * 0.28],
                 fill=INK)


def icon_drop(draw, cx, cy, r, colour):
    # Oil drop with a small flame.
    draw.polygon([(cx, cy - r), (cx + r * 0.62, cy + r * 0.1),
                  (cx - r * 0.62, cy + r * 0.1)], fill=colour)
    draw.ellipse([cx - r * 0.62, cy - r * 0.1, cx + r * 0.62, cy + r * 0.85],
                 fill=colour)
    draw.ellipse([cx - r * 0.22, cy - r * 0.45, cx + r * 0.22, cy + r * 0.05],
                 fill=(255, 214, 90))


def icon_scales(draw, cx, cy, r, colour):
    # Scales of justice.
    draw.line([cx, cy - r * 0.9, cx, cy + r * 0.85], fill=colour, width=5)
    draw.line([cx - r * 0.8, cy - r * 0.55, cx + r * 0.8, cy - r * 0.55],
              fill=colour, width=5)
    for sx in (-1, 1):
        x = cx + sx * r * 0.8
        draw.line([x, cy - r * 0.55, x - r * 0.3, cy + r * 0.1],
                  fill=colour, width=3)
        draw.line([x, cy - r * 0.55, x + r * 0.3, cy + r * 0.1],
                  fill=colour, width=3)
        draw.arc([x - r * 0.3, cy - r * 0.15, x + r * 0.3, cy + r * 0.45],
                 0, 180, fill=colour, width=4)
    draw.line([cx - r * 0.45, cy + r * 0.85, cx + r * 0.45, cy + r * 0.85],
              fill=colour, width=5)


def icon_pad(draw, cx, cy, r, colour):
    # Game controller.
    draw.rounded_rectangle([cx - r * 0.85, cy - r * 0.5, cx + r * 0.85,
                            cy + r * 0.55], radius=18, fill=colour)
    draw.line([cx - r * 0.55, cy - r * 0.05, cx - r * 0.25, cy - r * 0.05],
              fill=INK, width=7)
    draw.line([cx - r * 0.4, cy - r * 0.2, cx - r * 0.4, cy + r * 0.1],
              fill=INK, width=7)
    draw.ellipse([cx + r * 0.18, cy - r * 0.28, cx + r * 0.42, cy - r * 0.04],
                 fill=INK)
    draw.ellipse([cx + r * 0.48, cy - r * 0.05, cx + r * 0.72, cy + r * 0.19],
                 fill=INK)


def icon_chart(draw, cx, cy, r, colour):
    # Rising market arrow.
    pts = [(cx - r * 0.8, cy + r * 0.55), (cx - r * 0.35, cy + r * 0.05),
           (cx, cy + r * 0.3), (cx + r * 0.45, cy - r * 0.45)]
    draw.line(pts, fill=colour, width=7, joint="curve")
    draw.polygon([(cx + r * 0.45, cy - r * 0.45), (cx + r * 0.85, cy - r * 0.45),
                  (cx + r * 0.45, cy - r * 0.05)], fill=colour)


ICONS = [icon_summit, icon_burst, icon_drop, icon_scales, icon_pad, icon_chart]


def draw_globe(draw, cx, cy, r):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=GOLD, width=3)
    draw.ellipse([cx - r * 0.45, cy - r, cx + r * 0.45, cy + r],
                 outline=GOLD, width=2)
    draw.line([cx - r, cy, cx + r, cy], fill=GOLD, width=2)
    draw.arc([cx - r, cy - r * 0.45, cx + r, cy + r * 0.45], 0, 360,
             fill=GOLD, width=2)


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # --- header -------------------------------------------------------
    d.text((48, 26), "THURSDAY  \u00b7  THE WORLD IN ONE DAY", font=SUB,
           fill=GOLD)
    d.text((48, 58), "19 NOVEMBER 2026", font=TITLE, fill=WHITE)
    draw_globe(d, 950, 84, 36)
    d.line([48, 156, W - 48, 156], fill=GOLD, width=3)

    # --- story rows ---------------------------------------------------
    top, row_h, gap = 172, 128, 8
    for i, (tag, colour, headline, summary) in enumerate(STORIES):
        y0 = top + i * (row_h + gap)
        y1 = y0 + row_h
        rounded(d, [24, y0, W - 24, y1], 14, CARD, CARD_LINE, 2)
        cx, cy = 88, (y0 + y1) // 2
        d.ellipse([cx - 42, cy - 42, cx + 42, cy + 42], fill=WHITE)
        ICONS[i](d, cx, cy, 30, colour)
        tx = 156
        d.text((tx, y0 + 14), tag, font=TAG, fill=colour)
        d.text((tx, y0 + 40), headline, font=HEAD, fill=WHITE)
        d.text((tx, y0 + 82), summary, font=BODY, fill=MUTED)

    # --- footer -------------------------------------------------------
    foot = "Six stories that defined the day."
    fw = d.textlength(foot, font=FOOT)
    d.text(((W - fw) / 2, 990), foot, font=FOOT, fill=MUTED)

    img.save("entry.png", optimize=True)
    print("wrote entry.png")


if __name__ == "__main__":
    main()
