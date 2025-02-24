from fastapi import FastAPI, File, UploadFile
import shutil
import pytesseract
from PIL import Image
import uvicorn


from routes import tax_calculator, ocr_processor, chatbot, tax_filling

app = FastAPI(title="AI Tax Assistant")

@app.get("/")
def home():
    return {"message": "Welcome to AI Tax Assistant"}


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "AI Tax Assistant Backend is running"}

@app.post("/upload")
async def upload_file(document: UploadFile = File(...)):
    file_path = f"uploads/{document.filename}"
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(document.file, buffer)

    # Process file with OCR
    text = pytesseract.image_to_string(Image.open(file_path))
    
    return {"extracted_text": text}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

app.include_router(tax_calculator.router, prefix="/api")
app.include_router(ocr_processor.router, prefix="/api")
app.include_router(chatbot.router, prefix="/api")
app.include_router(tax_filling.router, prefix="/api")
