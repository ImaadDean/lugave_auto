from fastapi import APIRouter
from models.user import User
from config.database import user_collection
from schema.user_schema import user_serializer, users_serializer
from bson import ObjectId

router = APIRouter()

@router.get("/")
async def get_users():
    users = users_serializer(user_collection.find())
    return users

@router.post("/")
async def create_user(user: User):
    user_id = user_collection.insert_one(user.dict()).inserted_id
    return {"id": str(user_id)}

@router.put("/{id}")
async def update_user(id: str, user: User):
    user_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": user.dict()})
    return {"message": "User updated successfully"}

@router.delete("/{id}")
async def delete_user(id: str):
    user_collection.find_one_and_delete({"_id": ObjectId(id)})
    return {"message": "User deleted successfully"}
