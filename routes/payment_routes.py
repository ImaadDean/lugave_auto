from fastapi import APIRouter
from models.payment import Payment
from config.database import payment_collection
from schema.payment_schema import payment_serializer, payments_serializer
from bson import ObjectId

router = APIRouter()

@router.get("/")
async def get_payments():
    payments = payments_serializer(payment_collection.find())
    return payments

@router.post("/")
async def create_payment(payment: Payment):
    payment_id = payment_collection.insert_one(payment.dict()).inserted_id
    return {"id": str(payment_id)}

@router.put("/{id}")
async def update_payment(id: str, payment: Payment):
    payment_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": payment.dict()})
    return {"message": "Payment updated successfully"}

@router.delete("/{id}")
async def delete_payment(id: str):
    payment_collection.find_one_and_delete({"_id": ObjectId(id)})
    return {"message": "Payment deleted successfully"}
