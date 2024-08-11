from pydantic import BaseModel
from typing import Optional

class Payment(BaseModel):
    sale_id: str
    amount_paid: int
    payment_date: Optional[str] = None
    customer_id: str
    car_id: str
    balance_after_payment: Optional[int] = None