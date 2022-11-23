#!/usr/bin/python3
"""
Filestorage module
"""
import json


class FileStorage():
    """
    serializes instances to a JSON file and deserializes JSON file to instances
    """
    """Private attributes"""
    __file_path = 'file.json'
    __objects = {}

    """Public instances"""
    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = f"{[type(obj).__name__]}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        """
        obj_dict = {}
        with open(FileStorage.__file_path, 'w') as write_file:
            json.dump(obj_dict, write_file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, "r") as read_file:
                dict_obj = json.load(read_file)
        except FileNotFoundError:
            pass
