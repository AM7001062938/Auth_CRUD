from app.auth import get_password_hash
from app.database import users_collection

def create_user(user):
    hashed_password = get_password_hash(user.password)
    user_data = {
        "email": user.email,
        "password": hashed_password,
        "is_verified": False
    }
    users_collection.insert_one(user_data)
    return user_data

def get_user_by_email(email: str):
    return users_collection.find_one({"email": email})

def get_all_users():
    return list(users_collection.find())

def verify_user(email: str):
    user = get_user_by_email(email)
    if user:
        users_collection.update_one({"email": email}, {"$set": {"is_verified": True}})
        return True
    return False
