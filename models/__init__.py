#!/usr/bin/python3
"""
 serializes instances to a JSON file and deserializes JSON file to instances
 """

"""importing file_storage"""
import models.engine.file_storage as f
"""creating the variable storage, an instance of FileStorage"""
storage = f.FileStorage()
"""calls reload() method on this variable"""
storage.reload()
