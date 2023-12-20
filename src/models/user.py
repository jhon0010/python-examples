"""
Pydantic is a data validation and settings management library for Python. It is primarily used for parsing and validating data, 
particularly for settings/configuration files, JSON objects, and data models in Python applications. Pydantic leverages Python 
type annotations to enforce type checking and data validation at runtime, providing a simple, concise, and powerful way to define 
data schemas and perform validation.
"""
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    #id: Optional[str]
    name: str
    email: str
    password: str