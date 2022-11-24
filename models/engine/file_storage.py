#!/usr/bin/python3
"""
Filestorage module
"""
import json
import models.base_model

class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON file to instances
    """
    """Private attributes"""
    __file_path = 'file.json'
    __objects = {}

    """Public instances"""
    def all(self):
        """returns the dictionary __objects"""

        return type(self).__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """

        key = f"{type(obj).__name__}.{obj.id}"
        type(self).__objects[key] = obj.to_dict()

    def save(self):
        """
        serializes __objects to the JSON file
        """

        obj_dict = self.all()
        with open(type(self).__file_path, 'w') as write_file:
            json.dump(obj_dict, write_file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """

        try:
            with open(self.__file_path, "r") as read_file:
                obj_dict = json.load(read_file)
                #need to recreate the instances here
                for key in obj_dict.keys():
                    type(self).__objects[key] = models.base_model.BaseModel(**obj_dict[key])
        except FileNotFoundError:
            pass
