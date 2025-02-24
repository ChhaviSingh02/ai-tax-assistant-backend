def calculate_tax(income, deductions=0):
    taxable_income = income - deductions
    if taxable_income <= 50000:
        return taxable_income * 0.05
    elif taxable_income <= 100000:
        return taxable_income * 0.10
    else:
        return taxable_income * 0.20  # 20% for higher slabs
