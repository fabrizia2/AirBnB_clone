#!/usr/bin/python3
"""
Test for the user class
"""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestUser(unittest.TestCase):
    """
    testing the class user
    """
    def test_instance(self):
        """
        Test object is instance
        """

        my_city = City()
        self.assertIsInstance(my_city, BaseModel)

    def test_is_str(self):
        """
        test if the class attributes are strings
        """

        my_city1 = City()
        self.assertIs(type(my_city1.state_id), str)
        self.assertIs(type(my_city1.name), str)


if __name__ == '__main__':
    unittest.main()
