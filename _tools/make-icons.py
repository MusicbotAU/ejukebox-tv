"""Render the eJukebox TV mark (assets/favicon.svg) to raster icons.

Same geometry as the inline SVG in _layouts/default.html, drawn directly so no
SVG rasteriser is needed. Supersampled 8x then downsampled for clean edges.
"""
from PIL import Image, ImageDraw

INK   = (8, 12, 18, 255)      # #080c12  the site's ground
AMBER = (255, 179, 71, 255)   # #ffb347
STEEL = (142, 160, 181, 255)  # #8ea0b5

SS = 8  # supersample factor


def draw(size, rounded, pad):
    """size px output. rounded: corner radius in 32-unit space, 0 for square.
    pad: inset of the glyph in 32-unit space (0 = full bleed)."""
    S = size * SS
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)

    def u(v, span=32.0, off=0.0):
        # map a 32-unit coordinate into the padded glyph box
        inner = 32.0 - 2 * pad
        return (pad + v * inner / 32.0) * S / 32.0

    # ground
    if rounded:
        d.rounded_rectangle([0, 0, S - 1, S - 1], radius=rounded * S / 32.0, fill=INK)
    else:
        d.rectangle([0, 0, S - 1, S - 1], fill=INK)

    # the amber panel
    d.rounded_rectangle([u(4.5), u(7), u(27.5), u(21.5)],
                        radius=2.5 * (32 - 2 * pad) / 32.0 * S / 32.0, fill=AMBER)
    # the dark glass
    d.rounded_rectangle([u(7), u(9.5), u(25), u(19)],
                        radius=1.5 * (32 - 2 * pad) / 32.0 * S / 32.0, fill=INK)
    # the lens
    r = 2.6 * (32 - 2 * pad) / 32.0 * S / 32.0
    cx, cy = u(16), u(14.2)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=AMBER)
    # the stand
    d.rounded_rectangle([u(12.5), u(23.5), u(19.5), u(25.5)],
                        radius=1 * (32 - 2 * pad) / 32.0 * S / 32.0, fill=STEEL)

    return im.resize((size, size), Image.LANCZOS)


# favicon.ico - multi-size, rounded like the inline SVG, at the repo root so the
# browser default path resolves without any markup.
ico = [draw(s, rounded=7, pad=0) for s in (16, 32, 48)]
ico[1].save("favicon.ico", format="ICO",
            sizes=[(16, 16), (32, 32), (48, 48)])

# favicon-32.png - the crawlable PNG Google Search will actually fetch.
draw(32, rounded=7, pad=0).convert("RGB").save("assets/favicon-32.png")

# apple-touch-icon - iOS does not honour transparency and applies its own
# corner mask, so this is a full square on the site's own dark ground.
draw(180, rounded=0, pad=3).convert("RGB").save("assets/apple-touch-icon.png")

# PWA / Android manifest icons.
draw(192, rounded=0, pad=3).convert("RGB").save("assets/icon-192.png")
draw(512, rounded=0, pad=3).convert("RGB").save("assets/icon-512.png")

print("done")
