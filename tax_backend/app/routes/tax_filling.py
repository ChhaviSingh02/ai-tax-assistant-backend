from fastapi import APIRouter
from database import tax_data_collection
from models.tax_data import TaxData

router = APIRouter()

@router.post("/submit-tax")
def submit_tax_data(data: TaxData):
    tax_data_collection.insert_one(data.dict())
    return {"message": "Tax data submitted successfully!"}
