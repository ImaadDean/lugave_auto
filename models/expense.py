from pydantic import BaseModel
from typing import Optional

class Expense(BaseModel):
    Car_id: str
    amount: int
    date: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None