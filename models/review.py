#!/usr/bin/python
from models.base_model import BaseModel

class Review(BaseModel):
    """
    Review class inherits from BaseModel.
    Public class attributes:
    - place_id: string, references Place.id, default is an empty string.
    - user_id: string, references User.id, default is an empty string.
    - text: string, default is an empty string.
    """
    place_id = ""
    user_id = ""
    text = ""