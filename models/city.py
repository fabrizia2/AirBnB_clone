#!/usr/bin/python3
"""
City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    public attributes of the class
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

    def __str__(self):
        super().__str__()
        return f"[City] ({self.id}) {self.__dict__}"

    def save(self):
        super().save()

    def to_dict(self):
        city_dict = super().to_dict()
        city_dict["__class__"] = type(self).__name__
        city_dict["state_id"] = type(self).state_id
        city_dict["name"] = type(self).name
        return city_dict
