#!/usr/bin/python3
"""
class User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    public attributes
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
