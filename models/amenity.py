#!/usr/bin/python3
"""
amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    public attributes
    """
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        if len(kwargs) == 0:
            self.name = ""

    def __str__(self):
        super().__str__()
        return f"{[type(self).__name__]} ({self.id}) {self.__dict__}"

    def save(self):
        super().save()

    def to_dict(self):
        amenity_dict = super().to_dict()
        amenity_dict["__class__"] = type(self).__name__
        amenity_dict["name"] = self.name
