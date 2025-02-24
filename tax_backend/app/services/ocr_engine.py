import pytesseract
from PIL import Image
from config import OCR_ENGINE_PATH

pytesseract.pytesseract.tesseract_cmd = OCR_ENGINE_PATH

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text
