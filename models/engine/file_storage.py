#!/usr/bin/python3
"""
Filestorage module
"""
import os
import json
import importlib
import re


class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON file to instances
    """

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
        type(self).__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        """

        obj_dict = self.all()
        serializer_dict = {}
        for key in obj_dict.keys():
            serializer_dict[key] = obj_dict[key].to_dict()
        with open(type(self).__file_path, 'w') as write_file:
            json.dump(serializer_dict, write_file)

    def reload(self):
        """
        deserializes the JSON file to  dict then to __objects dictionary
        containing objects
        """

        try:
            with open(self.__file_path, "r") as read_file:
                obj_dicts = json.load(read_file)
            for key in obj_dicts.keys():
                try:
                    class_str = obj_dicts[key]["__class__"]
                    names = re.findall('^[a-z]+|[A-Z][^A-Z]*', class_str)
                    if len(names) > 1:
                        lower_names = []
                        for name in names:
                            lower_names.append(name.lower())
                            str_join = "_".join(lower_names)
                    else:
                        names[0] = names[0].lower()
                        str_join = names[0]
                    module_name = "models." + str_join
                    class_mod = importlib.import_module(module_name)
                    class_ = getattr(class_mod, class_str)
                    type(self).__objects[key] = class_(**obj_dicts[key])
                except Exception as E:
                    pass
        except FileNotFoundError:
            pass

    def modify_objects(self, new_dict):
        """
        Modify the __objects dictionary and save changes
        to json file
        """
        self.__objects = new_dict
        self.save()
