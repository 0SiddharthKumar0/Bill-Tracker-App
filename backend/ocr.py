from PIL import Image
import pytesseract
from pdf2image import convert_from_path

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def extract_text_from_pdf(pdf_path):
    pages = convert_from_path(pdf_path)
    texts = [pytesseract.image_to_string(page) for page in pages]
    return "\n".join(texts)