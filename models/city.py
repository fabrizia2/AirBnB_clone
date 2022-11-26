#!/usr/bin/python3
"""
City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    public attributes of the class
    """
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        if len(kwargs) == 0:
            self.state_id = ""
            self.name = ""

    def __str__(self):
        super().__str__()
        return f"{[type(self).__name__]} ({self.id}) {self.__dict__}"


    def save(self):
        super().save()

    def to_dict(self):
        city_dict = super().to_dict()
        city_dict["__class__"] = type(self).__name__
        city_dict["state_id"] = self.state_id
        city_dict["name"] = self.name
        return city_dict
