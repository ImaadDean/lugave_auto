from fastapi import APIRouter
from models.expense import Expense
from config.database import expense_collection
from schema.expense_schema import expense_serializer, expenses_serializer
from bson import ObjectId

router = APIRouter()

@router.get("/")
async def get_expenses():
    expenses = expenses_serializer(expense_collection.find())
    return expenses

@router.post("/")
async def create_expense(expense: Expense):
    expense_id = expense_collection.insert_one(expense.dict()).inserted_id
    return {"id": str(expense_id)}

@router.put("/{id}")
async def update_expense(id: str, expense: Expense):
    expense_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": expense.dict()})
    return {"message": "Expense updated successfully"}

@router.delete("/{id}")
async def delete_expense(id: str):
    expense_collection.find_one_and_delete({"_id": ObjectId(id)})
    return {"message": "Expense deleted successfully"}
