from fastapi import APIRouter
from models.payment_schedule import PaymentSchedule
from config.database import payment_schedule_collection
from schema.payment_schedule_schema import payment_schedule_serializer, payment_schedules_serializer
from bson import ObjectId

router = APIRouter()

@router.get("/")
async def get_payment_schedules():
    payment_schedules = payment_schedules_serializer(payment_schedule_collection.find())
    return payment_schedules

@router.post("/")
async def create_payment_schedule(payment_schedule: PaymentSchedule):
    payment_schedule_id = payment_schedule_collection.insert_one(payment_schedule.dict()).inserted_id
    return {"id": str(payment_schedule_id)}

@router.put("/{id}")
async def update_payment_schedule(id: str, payment_schedule: PaymentSchedule):
    payment_schedule_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": payment_schedule.dict()})
    return {"message": "Payment schedule updated successfully"}

@router.delete("/{id}")
async def delete_payment_schedule(id: str):
    payment_schedule_collection.find_one_and_delete({"_id": ObjectId(id)})
    return {"message": "Payment schedule deleted successfully"}
