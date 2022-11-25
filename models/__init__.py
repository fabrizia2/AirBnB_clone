#!/usr/bin/python3
"""
 serializes instances to a JSON file and deserializes JSON file to instances
 """

from models.engine import file_storage
storage = file_storage.FileStorage()
storage.reload()
