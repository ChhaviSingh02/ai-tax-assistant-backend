from pydantic import BaseModel
from typing import Optional

class TaxData(BaseModel):
    user_id: str
    income: float
    deductions: Optional[float] = 0.0
    tax_paid: Optional[float] = 0.0
