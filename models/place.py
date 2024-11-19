#!/usr/bin/python

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class inherits from BaseModel.
    Public class attributes:
    - city_id: string, references City.id, default is an empty string.
    - user_id: string, references User.id, default is an empty string.
    - name: string, default is an empty string.
    - description: string, default is an empty string.
    - number_rooms: integer, default is 0.
    - number_bathrooms: integer, default is 0.
    - max_guest: integer, default is 0.
    - price_by_night: integer, default is 0.
    - latitude: float, default is 0.0.
    - longitude: float, default is 0.0.
    - amenity_ids: list of strings, default is an empty list.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
