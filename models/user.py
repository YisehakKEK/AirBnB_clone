#!/usr/bin/python
from models.base_model import BaseModel

class User(BaseModel):
    """
    User class inherits from BaseModel.
    Public class attributes:
    - email: string, default is an empty string.
    - password: string, default is an empty string.
    - first_name: string, default is an empty string.
    - last_name: string, default is an empty string.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""