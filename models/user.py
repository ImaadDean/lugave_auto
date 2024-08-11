from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class User(BaseModel):
    username: str
    password: str  # This will be stored as a hashed password.
    email: EmailStr  # EmailStr validates that the input is a valid email.
    telephone: Optional[int] = None
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

    class Config:
        schema_extra = {
            "example": {
                "username": "johndoe",
                "password": "strongpassword123",
                "email": "johndoe@example.com",
                "telephone": 1234567890,
            }
        }