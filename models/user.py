#!/usr/bin/python3
from models.base_model import BaseModel

class User(BaseModel):
    """User class that inherits from BaseModel"""
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def show(self, user_id):
        """Displays a user by ID"""
        key = f"User.{user_id}"
        user = storage.all().get(key)  # Get user by key
        if user:
            print(user)
        else:
            print(f"** no user found with id {user_id} **")