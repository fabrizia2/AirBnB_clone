#!/usr/bin/python3
"""
Module that defines all common attributes/methods for all other
classes to inherit from
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    Class that contains the common attributes/methods that all other
    classes inherit from
    """

    def __init__(self, *args, **kwargs):
        """
        Initialises BaseModel class with default arguments
        """

        if len(kwargs) != 0:
            for k in kwargs:
                if k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.fromisoformat(kwargs[k]))
                elif k != "__class__":
                    setattr(self, k, kwargs[k])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Prints a friendly representation of BaseModel's instances
        """

        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates public instance attribute 'updated_at'
        """

        self.updated_at = datetime.now()
        """calling the save(self) method of storage"""
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        returns a dictionary with all key/values of the instance's __dict__
        """

        dic = self.__dict__.copy()
        dic["__class__"] = type(self).__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
