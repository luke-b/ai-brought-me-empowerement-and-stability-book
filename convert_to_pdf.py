import markdown
from weasyprint import HTML, CSS

def convert():
    with open("manuscript.md", "r") as f:
        md_text = f.read()

    html_content = markdown.markdown(md_text)

    # We wrap the content in basic HTML, including the cover image at the beginning
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Agentic Abundance</title>
        <style>
            @page {{
                size: 6in 9in;
                margin: 0.75in;
            }}
            @page :first {{
                margin: 0;
            }}
            body {{
                font-family: 'Times New Roman', serif;
                font-size: 11pt;
                line-height: 1.4;
                color: #000;
            }}
            h1, h2, h3 {{
                font-family: 'Arial', sans-serif;
                page-break-after: avoid;
            }}
            p {{
                text-align: justify;
                margin-bottom: 1em;
            }}
            .cover {{
                width: 100%;
                height: 100%;
                object-fit: cover;
                page-break-after: always;
            }}
            /* Additional CSS to make sure page breaks work correctly */
            div[style*="page-break-after: always;"] {{
                page-break-after: always;
            }}
        </style>
    </head>
    <body>
        <img src="cover.jpg" class="cover" alt="Cover">
        {html_content}
    </body>
    </html>
    """

    with open("temp.html", "w") as f:
        f.write(html_template)

    HTML('temp.html').write_pdf('Agentic_Abundance.pdf')

if __name__ == "__main__":
    convert()
