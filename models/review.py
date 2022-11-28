#!/usr/bin/python3
"""
review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    public class attributes
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

    def __str__(self):
        super().__str__()
        return f"[Review] ({self.id}) {self.__dict__}"

    def save(self):
        super().save()

    def to_dict(self):
        review_dict = super().to_dict()
        review_dict["__class__"] = type(self).__name__
        review_dict["place_id"] = type(self).place_id
        review_dict["user_id"] = type(self).user_id
        review_dict["text"] = type(self).text
        return review_dict
