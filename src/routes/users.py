"""
This is the users router, which will be used to handle all requests to the /users endpoint.
"""
from bson import ObjectId
from fastapi import APIRouter, Response
from src.schemas.user import userEntity, usersEntity
from src.config.mongodb import conn
from src.models.user import User
from passlib.hash import sha256_crypt


# This is the router we will use in our app as a module
users = APIRouter()


@users.get("/", response_model=list[User], tags=["users"])
def find_all_users():
    return usersEntity(conn.local.users.find())


@users.get("/{id}", response_model=User, tags=["users"])
def find_user_by_id(id: str):
    user = conn.local.users.find_one({"_id": ObjectId(id)})
    return userEntity(user)


@users.post("/", response_model=User, tags=["users"])
def create_user(user: User):
    user_to_save = dict(user)
    # del user_to_save["id"] # Remove id from the user object not needed to save in the database
    user_to_save["password"] = sha256_crypt.encrypt(
        user_to_save["password"])  # encrypt password
    id: ObjectId = conn.local.users.insert_one(user_to_save).inserted_id
    created_user = conn.local.users.find_one({"_id": id})
    return userEntity(created_user)


@users.put("/{id}", response_model=User, tags=["users"])
def update_user(id: str, user: User):
    user_to_update = dict(user)
    user_to_update["password"] = sha256_crypt.encrypt(
        user_to_update["password"])
    conn.local.users.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": user_to_update})
    updated_user = conn.local.users.find_one({"_id": ObjectId(id)})
    return userEntity(updated_user)


@users.delete("/{id}", status_code=204, response_model=None, tags=["users"])
def delete_user(id: str):
    conn.local.users.find_one_and_delete({"_id": ObjectId(id)})
    return Response(status_code=204)
