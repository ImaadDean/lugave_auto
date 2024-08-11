from pydantic import BaseModel
from typing import Optional

class Sale(BaseModel):
    car_id: str
    customer_id: str
    sale_date: Optional[str] = None
    sale_price: Optional[int] = None
    total_price: Optional[int] = None
    sale_status: Optional[str] = None
    payment_type: Optional[str] = None