import easyocr

# Initialize EasyOCR reader (supports multiple languages)
reader = easyocr.Reader(['en'])  # Add other languages if needed

# Run OCR on the image
image_path = "test3.png"
text = reader.readtext(image_path, detail=0)  # detail=0 returns plain text

# Print extracted text
print("Extracted Text:\n", "\n".join(text))
