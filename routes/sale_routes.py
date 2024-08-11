from fastapi import APIRouter
from models.sale import Sale
from config.database import sale_collection
from schema.sale_schema import sale_serializer, sales_serializer
from bson import ObjectId

router = APIRouter()

@router.get("/")
async def get_sales():
    sales = sales_serializer(sale_collection.find())
    return sales

@router.post("/")
async def create_sale(sale: Sale):
    sale_id = sale_collection.insert_one(sale.dict()).inserted_id
    return {"id": str(sale_id)}

@router.put("/{id}")
async def update_sale(id: str, sale: Sale):
    sale_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": sale.dict()})
    return {"message": "Sale updated successfully"}

@router.delete("/{id}")
async def delete_sale(id: str):
    sale_collection.find_one_and_delete({"_id": ObjectId(id)})
    return {"message": "Sale deleted successfully"}
