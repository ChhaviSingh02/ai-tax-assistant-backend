import os
from dotenv import load_dotenv # type: ignore

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OCR_ENGINE_PATH = os.getenv("OCR_ENGINE_PATH")  # Path to Tesseract OCR
