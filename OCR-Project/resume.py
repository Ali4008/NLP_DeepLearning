import fitz  # PyMuPDF
import easyocr

# Path to your PDF file
pdf_path = "MuhammadAliMahmood.pdf"

# Initialize EasyOCR
reader = easyocr.Reader(['en'])

# Open PDF and extract text
with fitz.open(pdf_path) as doc:
    full_text = []
    for page_num in range(len(doc)):
        text = doc[page_num].get_text("text")  # Extract text directly
        full_text.append(text)

# Print extracted text
print("\nExtracted Text:\n", "\n".join(full_text))
