from fastapi import FastAPI
from src.routes import users
from docs import tags_metadata

app = FastAPI(
    title="Example of FastAPI with MongoDB",
    description="This is a simple example of a FastAPI application using MongoDB",
    version="0.0.1",
    tags_metadata=tags_metadata
)


app.include_router(users.users, prefix="/users", tags=["users"])
