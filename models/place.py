#!/usr/bin/python3
"""This file contains place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Public class attributes"""
    city_id = ""
    user_id = ""
    name = ""
    description = 0
    numbers_rooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ""
