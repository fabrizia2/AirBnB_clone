#!/usr/bin/python3
"""
Test for the user class
"""
import unittest
from models.base_model import BaseModel
from models.user import User
from models import user


class TestUser(unittest.TestCase):
    """
    testing the class user
    """
    def test_instance(self):
        """
        Test object is instance
        """

        my_user = User()
        self.assertIsInstance(my_user, BaseModel)

    def test_is_str(self):
        """
        test if the class attributes are strings
        """

        my_user1 = User()
        self.assertTrue(type(my_user1.email) == str)
        self.assertIs(type(my_user1.password), str)
        self.assertIs(type(my_user1.first_name), str)
        self.assertIs(type(my_user1.last_name), str)


if __name__ == '__main__':
    unittest.main()
