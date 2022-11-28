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
        """
        Initialisation function from BaseModel
        """

        super().__init__(self, *args, **kwargs)

    def __str__(self):
        """
        User frriendly string representation of Ameninty
        object
        """

        return f"[Amenity] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Save method for Amenity objects
        """
        super().save()

    def to_dict(self):
        """
        returns a dictionary representaion of the object
        """
        amenity_dict = super().to_dict()
        amenity_dict["__class__"] = type(self).__name__
        amenity_dict["name"] = type(self).name
        return amenity_dict
