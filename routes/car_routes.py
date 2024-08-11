from fastapi import APIRouter
from models.car import Car
from config.database import car_collection
from schema.car_schema import car_serializer, cars_serializer
from bson import ObjectId

router = APIRouter()

@router.get("/")
async def get_cars():
    cars = cars_serializer(car_collection.find())
    return cars

@router.post("/")
async def create_car(car: Car):
    car_id = car_collection.insert_one(car.dict()).inserted_id
    return {"id": str(car_id)}

@router.put("/{id}")
async def update_car(id: str, car: Car):
    car_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": car.dict()})
    return {"message": "Car updated successfully"}

@router.delete("/{id}")
async def delete_car(id: str):
    car_collection.find_one_and_delete({"_id": ObjectId(id)})
    return {"message": "Car deleted successfully"}
