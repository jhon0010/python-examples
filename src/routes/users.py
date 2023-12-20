"""
This is the users router, which will be used to handle all requests to the /users endpoint.
"""
from fastapi import APIRouter
from src.schemas.user import userEntity, usersEntity
from src.config.mongodb import conn
from src.models.user import User
from passlib.hash import sha256_crypt


# This is the router we will use in our app as a module
users = APIRouter()

@users.get("/")
def find_all_users():
    return usersEntity(conn.local.users.find())

@users.get("/{id}")
def find_user_by_id(id: int):
    return {"Hello": id}

@users.post("/")
def create_user(user: User):
    user_to_save = dict(user)
    #del user_to_save["id"] # Remove id from the user object not needed to save in the database
    user_to_save["password"] = sha256_crypt.encrypt(user_to_save["password"]) # encrypt password
    id = conn.local.users.insert_one(user_to_save).inserted_id
    created_user = conn.local.users.find_one({"_id": id})
    return userEntity(created_user)

@users.put("/{id}")
def update_user(id: str):
    return {"Hello": id}

@users.delete("/{id}")
def delete_user(id: str):
    return {"Hello": id}