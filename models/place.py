#!/usr/bin/python3
"""
place class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    class public attributes
    """
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        if len(kwargs) == 0:
            self.city_id = ""
            self.user_id = ""
            self.name = ""
            self.description = ""
            self.number_rooms = 0
            self.number_bathrooms = 0
            self.max_guests = 0
            self.price_by_night = 0
            self.latitude = 0.0
            self.longitude = 0.0
            self.amenity_ids = []

    def __str__(self):
        super().__str__()
        return f"{[type(self).__name__]} ({self.id}) {self.__dict__}"

    def save(self):
        super().save()

    def to_dict(self):
        place_dict = super().to_dict()
        place_dict["__class__"] = type(self).__name__
        place_dict["city_id"] = self.city_id
        place_dict["user_id"] = self.user_id
        place_dict["name"] = self.name
        place_dict["description"] = self.description
        place_dict["number_rooms"] = self.number_rooms
        place_dict["number_bathrooms"] = self.number_bathrooms
        place_dict["max_guests"] = self.max_guests
        place_dict["price_by_night"] = self.price_by_night
        place_dict["latitude"] = self.latitude
        place_dict["longitude"] = self.longitude
        place_dict["amenity_ids"] = self.amenity_ids
        return place_dict
