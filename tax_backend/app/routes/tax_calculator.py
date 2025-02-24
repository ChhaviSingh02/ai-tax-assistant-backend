from fastapi import APIRouter, HTTPException
from services.tax_logic import calculate_tax
from models.tax_data import TaxData

router = APIRouter()

@router.post("/calculate-tax")
def compute_tax(data: TaxData):
    tax_amount = calculate_tax(data.income, data.deductions)
    return {"tax_payable": tax_amount}
