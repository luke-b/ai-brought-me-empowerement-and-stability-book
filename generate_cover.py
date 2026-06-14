import logging

from PIL import Image, ImageDraw, ImageFont


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

CANVAS_WIDTH = 1800
CANVAS_HEIGHT = 2700
MARGIN = 140

GRADIENT_TOP_RGB = (10, 18, 34)
GRADIENT_BOTTOM_RGB = (36, 42, 58)

TITLE_BLOCK_TOP = 300
IMPRINT_LINE_Y = 2125
AUTHOR_LINE_Y = 2268


def _load_font(preferred, size):
    for font_name in preferred:
        try:
            return ImageFont.truetype(font_name, size)
        except IOError:
            continue
    LOGGER.warning("Falling back to PIL default font for size %s.", size)
    return ImageFont.load_default()


def _draw_centered(draw, text, font, y, fill, width):
    left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
    text_width = right - left
    draw.text(((width - text_width) / 2, y), text, font=font, fill=fill)
    return bottom - top


def _create_vertical_gradient(width, height, top_rgb, bottom_rgb):
    mask = Image.linear_gradient("L").resize((width, height))
    top_layer = Image.new("RGB", (width, height), top_rgb)
    bottom_layer = Image.new("RGB", (width, height), bottom_rgb)
    return Image.composite(bottom_layer, top_layer, mask)


def create_cover():
    width, height = CANVAS_WIDTH, CANVAS_HEIGHT
    margin = MARGIN

    img = _create_vertical_gradient(
        width,
        height,
        GRADIENT_TOP_RGB,
        GRADIENT_BOTTOM_RGB,
    )

    draw = ImageDraw.Draw(img, "RGBA")

    for y in range(0, height, 60):
        alpha = 38 if (y // 60) % 3 == 0 else 22
        draw.line([(0, y), (width, y)], fill=(138, 155, 183, alpha), width=1)
    for x in range(0, width, 80):
        alpha = 30 if (x // 80) % 4 == 0 else 16
        draw.line([(x, 0), (x, height)], fill=(111, 130, 161, alpha), width=1)

    ring_center_x = width // 2
    ring_center_y = int(height * 0.56)
    ring_sizes = [1300, 1000, 720, 420]
    ring_colors = [
        (183, 198, 224, 56),
        (167, 186, 219, 82),
        (191, 213, 240, 120),
        (223, 232, 245, 170),
    ]
    ring_widths = [8, 7, 6, 5]

    for size, color, line_width in zip(ring_sizes, ring_colors, ring_widths):
        half = size // 2
        draw.ellipse(
            [
                ring_center_x - half,
                ring_center_y - half,
                ring_center_x + half,
                ring_center_y + half,
            ],
            outline=color,
            width=line_width,
        )

    panel_top = 170
    panel_bottom = height - 170
    draw.rectangle(
        [(margin, panel_top), (width - margin, panel_bottom)],
        outline=(217, 196, 143, 190),
        width=5,
    )
    draw.rectangle(
        [(margin + 22, panel_top + 22), (width - margin - 22, panel_bottom - 22)],
        outline=(217, 196, 143, 110),
        width=2,
    )

    title_font = _load_font(["DejaVuSerif-Bold.ttf", "DejaVuSans-Bold.ttf"], 194)
    subtitle_font = _load_font(["DejaVuSerif.ttf", "DejaVuSans.ttf"], 64)
    author_font = _load_font(["DejaVuSans-Bold.ttf", "DejaVuSerif-Bold.ttf"], 78)
    imprint_font = _load_font(["DejaVuSans.ttf", "DejaVuSerif.ttf"], 36)

    y = TITLE_BLOCK_TOP
    y += _draw_centered(
        draw,
        "AGENTIC",
        title_font,
        y,
        fill=(240, 238, 230, 255),
        width=width,
    ) + 6
    y += _draw_centered(
        draw,
        "ABUNDANCE",
        title_font,
        y,
        fill=(240, 238, 230, 255),
        width=width,
    ) + 110

    _draw_centered(
        draw,
        "THE SOVEREIGN EXPERT",
        subtitle_font,
        y,
        fill=(191, 206, 230, 255),
        width=width,
    )
    y += 90
    _draw_centered(
        draw,
        "AND THE END OF FRICTION",
        subtitle_font,
        y,
        fill=(191, 206, 230, 255),
        width=width,
    )

    _draw_centered(
        draw,
        "A NOVELLA OF HUMAN-AI SYMBIOSIS",
        imprint_font,
        IMPRINT_LINE_Y,
        fill=(215, 198, 158, 255),
        width=width,
    )
    _draw_centered(
        draw,
        "DR. SILAS VANE",
        author_font,
        AUTHOR_LINE_Y,
        fill=(239, 236, 226, 255),
        width=width,
    )

    img.save("cover.jpg", quality=95, optimize=True)


if __name__ == "__main__":
    create_cover()
