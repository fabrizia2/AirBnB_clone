#!/usr/bin/python3
"""
class state
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    public attributes
    """
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        if len(kwargs) == 0:
            self.name = ""

    def __str__(self):
        super().__str__()
        return f"[State] ({self.id}) {self.__dict__}"

    def save(self):
        super().save()

    def to_dict(self):
        state_dict = super().to_dict()
        state_dict["__class__"] = type(self).__name__
        state_dict["name"] = self.name
        return state_dict
