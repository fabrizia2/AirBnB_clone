#!/usr/bin/python3
"""
place class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    class public attributes
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

    def __init__(self, *args, **kwargs):
        """
        Initializing functions inheriting from BaseModel
        """
        super().__init__(self, *args, **kwargs)

    def __str__(self):
        return f"[Place] ({self.id}) {self.__dict__}"

    def save(self):
        super().save()

    def to_dict(self):
        place_dict = super().to_dict()
        place_dict["__class__"] = type(self).__name__
        place_dict["city_id"] = type(self).city_id
        place_dict["user_id"] = type(self).user_id
        place_dict["name"] = type(self).name
        place_dict["description"] = type(self).description
        place_dict["number_rooms"] = type(self).number_rooms
        place_dict["number_bathrooms"] = type(self).number_bathrooms
        place_dict["max_guest"] = type(self).max_guest
        place_dict["price_by_night"] = type(self).price_by_night
        place_dict["latitude"] = type(self).latitude
        place_dict["longitude"] = type(self).longitude
        place_dict["amenity_ids"] = type(self).amenity_ids
        return place_dict
