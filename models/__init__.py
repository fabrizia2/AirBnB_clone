#!/usr/bin/python3
"""
 serializes instances to a JSON file and deserializes JSON file to instances
 """

"""importing file_storage"""
from models.engine.file_storage import FileStorage
"""creating the variable storage, an instance of FileStorage"""
storage = FileStorage()
"""calls reload() method on this variable"""
storage.reload()
