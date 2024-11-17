#!/usr/bin/python
from models.base_model import BaseModel

class City(BaseModel):
    """
    City class inherits from BaseModel.
    Public class attributes:
    - state_id: string, references State.id, default is an empty string.
    - name: string, default is an empty string.
    """
    state_id = ""
    name = ""
