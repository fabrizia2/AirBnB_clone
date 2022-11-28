#!/usr/bin/python3
"""
amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    public attributes
    """

    name = ""
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

    def __str__(self):
        super().__str__()
        return f"[Amenity] ({self.id}) {self.__dict__}"

    def save(self):
        super().save()

    def to_dict(self):
        amenity_dict = super().to_dict()
        amenity_dict["__class__"] = type(self).__name__
        amenity_dict["name"] = type(self).name
