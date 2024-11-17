#!/usr/bin/python
from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    Amenity class inherits from BaseModel.
    Public class attributes:
    - name: string, default is an empty string.
    """
    name = ""