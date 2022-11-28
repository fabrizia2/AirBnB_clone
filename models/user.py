#!/usr/bin/python3
"""
class User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    public attributes
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

    def __str__(self):
        return f"[User] ({self.id}) {self.__dict__}"

    def save(self):
        super().save()

    def to_dict(self):
        user_dict = super().to_dict()
        user_dict["__class__"] = type(self).__name__
        user_dict["email"] = type(self).email
        user_dict["password"] = type(self).password
        user_dict["first_name"] = type(self).first_name
        user_dict["last_name"] = type(self).last_name
        return user_dict
