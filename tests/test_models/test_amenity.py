#!/usr/bin/python3
"""
Test for the user class
"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestUser(unittest.TestCase):
    """
    testing the class user
    """
    def test_instance(self):
        """
        Test object is instance
        """

        my_amenity = Amenity()
        self.assertIsInstance(my_amenity, BaseModel)

    def test_is_str(self):
        """
        test if the class attributes are strings
        """

        my_amenity1 = Amenity()
        self.assertIs(type(my_amenity1.name), str)


if __name__ == '__main__':
    unittest.main()
