from models.user import User

def user_serializer(user) -> dict:
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "password": user["password"],
        "email": user["email"],
        "telephone": user.get("telephone")
    }

def users_serializer(users) -> list:
    return [user_serializer(user) for user in users]