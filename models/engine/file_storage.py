#!/usr/bin/python3
"""
Filestorage module
"""
import json


class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON file to instances
    """

    def __init__(self):
        """Initialises Private attributes"""

        type(self).__file_path = 'file.json'
        type(self).__objects = {}

    """Public instances"""
    def all(self):
        """returns the dictionary __objects"""

        return type(self).__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """

        key = f"{type(obj).__name__}.{obj.id}"
        my_obj = obj
        type(self).__objects[key] = my_obj

    def save(self):
        """
        serializes __objects to the JSON file
        """

        obj_dict = self.all()
        serializer_dict = {}
        for key in obj_dict.keys():
            print(obj_dict[key])
            serializer_dict[key] = obj_dict[key].to_dict()
        with open(type(self).__file_path, 'w') as write_file:
            json.dump(serializer_dict, write_file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """

        from models.base_model import BaseModel
        try:
            with open(self.__file_path, "r") as read_file:
                obj_dicts = json.load(read_file)
            for key in obj_dicts.keys():
                type(self).__objects[key] = BaseModel(**obj_dicts[key])
        except FileNotFoundError:
            pass
