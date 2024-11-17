#!/usr/bin/python
from models.base_model import BaseModel

class State(BaseModel):
    """
    State class inherits from BaseModel.
    Public class attributes:
    - name: string, default is an empty string.
    """
    name = ""