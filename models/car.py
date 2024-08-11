from pydantic import BaseModel
from typing import Optional

class Car(BaseModel):
    maker: str
    model: str
    No_Plate: str
    price: int
    date: Optional[str] = None
    Added_by: Optional[str] = None
    status: Optional[str] = None
    year: Optional[int] = None