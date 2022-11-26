#!/usr/bin/python3
"""
Test for the state class
"""
import unittest
from models.base_model import BaseModel
from models.state import State
from models import state


class TestUser(unittest.TestCase):
    """
    testing the class user
    """
    def test_instance(self):
        """
        Test object is instance
        """

        my_state = State()
        self.assertIsInstance(my_state, BaseModel)

    def test_is_str(self):
        """
        test if the class attributes are strings
        """

        my_state1 = State()
        self.assertTrue(type(my_state1.name) == str)


if __name__ == '__main__':
    unittest.main()
