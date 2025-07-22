import pytesseract
from pdf2image import convert_from_bytes
from PIL import Image
import io

# ✅ Set tesseract path explicitly
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image: Image.Image) -> str:
    return pytesseract.image_to_string(image)

def extract_text_from_pdf(file_bytes: bytes) -> str:
    images = convert_from_bytes(file_bytes)
    text = ""
    for img in images:
        text += extract_text_from_image(img)
    return text