from pydantic import BaseModel
from typing import Optional

class Customer(BaseModel):
    first_name: str
    last_name: str
    telephone: Optional[int] = None
    address: Optional[str] = None