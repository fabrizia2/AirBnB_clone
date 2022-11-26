#!/usr/bin/python3
"""
class User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    public attributes
    """
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        if len(kwargs) == 0:
            self.email = ""
            self.password = ""
            self.first_name = ""
            self.last_name = ""

    def __str__(self):
        super().__str__()
        return f"{[type(self).__name__]} ({self.id}) {self.__dict__}"

    def save(self):
        super().save()

    def to_dict(self):
        user_dict = super().to_dict()
        user_dict["__class__"] = type(self).__name__
        user_dict["email"] = self.email
        user_dict["password"] = self.password
        user_dict["fisrt_nme"] = self.first_name
        user_dict["last_name"]= self.last_name
        return user_dict
