from PIL import Image, ImageDraw, ImageFont
import os

def create_cover():
    width = 1500
    height = 2400

    # Create background
    img = Image.new('RGB', (width, height), color='#0D1B2A')
    draw = ImageDraw.Draw(img)

    # Draw some abstract tech/AI elements
    for i in range(0, height, 100):
        draw.line([(0, i), (width, i)], fill='#1B263B', width=2)
    for i in range(0, width, 100):
        draw.line([(i, 0), (i, height)], fill='#1B263B', width=2)

    draw.ellipse([400, 800, 1200, 1600], outline='#415A77', width=10)
    draw.ellipse([500, 900, 1100, 1500], outline='#778DA9', width=8)
    draw.ellipse([600, 1000, 1000, 1400], outline='#E0E1DD', width=5)

    try:
        # Try to use a default sans-serif font, or fallback to default
        title_font = ImageFont.truetype("DejaVuSans-Bold.ttf", 140)
        subtitle_font = ImageFont.truetype("DejaVuSans.ttf", 70)
        author_font = ImageFont.truetype("DejaVuSans-Bold.ttf", 90)
    except IOError:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        author_font = ImageFont.load_default()

    # Title
    title1 = "AGENTIC"
    title2 = "ABUNDANCE"

    bbox1 = draw.textbbox((0, 0), title1, font=title_font)
    text_w1 = bbox1[2] - bbox1[0]
    draw.text(((width - text_w1) / 2, 250), title1, font=title_font, fill='#E0E1DD')

    bbox2 = draw.textbbox((0, 0), title2, font=title_font)
    text_w2 = bbox2[2] - bbox2[0]
    draw.text(((width - text_w2) / 2, 420), title2, font=title_font, fill='#E0E1DD')

    # Subtitle
    subtitle1 = "The Sovereign Expert"
    subtitle2 = "and the End of Friction"

    bbox = draw.textbbox((0, 0), subtitle1, font=subtitle_font)
    text_w = bbox[2] - bbox[0]
    draw.text(((width - text_w) / 2, 650), subtitle1, font=subtitle_font, fill='#778DA9')

    bbox = draw.textbbox((0, 0), subtitle2, font=subtitle_font)
    text_w = bbox[2] - bbox[0]
    draw.text(((width - text_w) / 2, 750), subtitle2, font=subtitle_font, fill='#778DA9')

    # Author
    author = "Dr. Silas Vane"
    bbox = draw.textbbox((0, 0), author, font=author_font)
    text_w = bbox[2] - bbox[0]
    draw.text(((width - text_w) / 2, 2000), author, font=author_font, fill='#E0E1DD')

    img.save("cover.jpg")

if __name__ == "__main__":
    create_cover()
