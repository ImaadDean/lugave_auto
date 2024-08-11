from fastapi import APIRouter
from models.customer import Customer
from config.database import customer_collection
from schema.customer_schema import customer_serializer, customers_serializer
from bson import ObjectId

router = APIRouter()

@router.get("/")
async def get_customers():
    customers = customers_serializer(customer_collection.find())
    return customers

@router.post("/")
async def create_customer(customer: Customer):
    customer_id = customer_collection.insert_one(customer.dict()).inserted_id
    return {"id": str(customer_id)}

@router.put("/{id}")
async def update_customer(id: str, customer: Customer):
    customer_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": customer.dict()})
    return {"message": "Customer updated successfully"}

@router.delete("/{id}")
async def delete_customer(id: str):
    customer_collection.find_one_and_delete({"_id": ObjectId(id)})
    return {"message": "Customer deleted successfully"}
