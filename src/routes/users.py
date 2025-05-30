"""
This is the users router, which will be used to handle all requests to the /users endpoint.
"""
from bson import ObjectId
from fastapi import APIRouter, Response
from src.schemas.user import userEntity, usersEntity
from src.config.mongodb import conn
from src.models.user import User
from passlib.hash import sha256_crypt

users = APIRouter()

@users.get("/", response_model=list[User], tags=["users"])
def find_all_users():
    return usersEntity(conn.local.users.find())


@users.get("/{name}", response_model=User, tags=["users"])
def find_user_by_name(name: str):
    user = conn.local.users.find_one({"name": name})
    return userEntity(user)


@users.post("/", response_model=User, tags=["users"])
def create_user(user: User):
    user_to_save = dict(user)
    user_to_save["password"] = sha256_crypt.encrypt(user_to_save["password"])
    id: ObjectId = conn.local.users.insert_one(user_to_save).inserted_id
    created_user = conn.local.users.find_one({"_id": id})
    return userEntity(created_user)


@users.put("/{name}", response_model=User, tags=["users"])
def update_user(name: str, user: User):
    user_to_update = dict(user)
    user_to_update["password"] = sha256_crypt.encrypt(user_to_update["password"])
    conn.local.users.find_one_and_update({"name": name}, {"$set": user_to_update})
    updated_user = conn.local.users.find_one({"name": name})
    return userEntity(updated_user)


@users.delete("/{name}", status_code=204, response_model=None, tags=["users"])
def delete_user(name: str):
    conn.local.users.find_one_and_delete({"name": name})
    return Response(status_code=204)
