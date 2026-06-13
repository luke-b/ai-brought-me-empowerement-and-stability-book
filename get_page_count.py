from pypdf import PdfReader
reader = PdfReader("Agentic_Abundance.pdf")
print("Page count:", len(reader.pages))
