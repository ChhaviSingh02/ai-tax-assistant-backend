from fastapi import APIRouter, UploadFile, File
from services.ocr_engine import extract_text_from_image

router = APIRouter()

@router.post("/extract-text")
async def ocr_extract(file: UploadFile = File(...)):
    file_path = f"temp/{file.filename}"
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    extracted_text = extract_text_from_image(file_path)
    return {"extracted_text": extracted_text}
