from pydantic import BaseModel
from typing import Optional

class PaymentSchedule(BaseModel):
    sale_id: str
    total_amount: Optional[int] = None
    amount_paid: Optional[int] = None
    remaining_balance: Optional[int] = None
    next_due_date: Optional[str] = None
    installment_amount: Optional[int] = None