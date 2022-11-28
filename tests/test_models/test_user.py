#!/usr/bin/python3
"""
Test for the user class
"""
import unittest
from models.base_model import BaseModel
from models.user import User
from models import user
import datetime


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

    def test_id_unique(self):
        """
        Test id attribute is unique
        """

        my_user2 = User()
        my_user3 = User()
        self.assertNotEqual(my_user2.id, my_user3.id)

    def test_id_string(self):
        """
        Test id attribute is string
        """

        my_user4 = User()
        self.assertIs(type(my_user4.id), str)

    def test_instance(self):
        """
        Test object is instance
        """

        my_user5 = User()
        self.assertIsInstance(my_user5, User)

    def test_created_at(self):
        """
        Test created_at attribute is a datetime instance
        """

        my_user6 = User()
        self.assertIs(type(my_user6.created_at), datetime.datetime)

    def test_updated_at(self):
        """
        Test updated_at attribute is a datetime instance
        """

        my_user7 = User()
        self.assertIs(type(my_user7.updated_at), datetime.datetime)

    def test_str_rep(self):
        """
        Test str is printed as specified
        """

        obj8 = User()
        strv = str(obj8)
        strv1 = f"[User] ({obj8.id}) {obj8.__dict__}"
        self.assertEqual(strv, strv1)

    def test_save_method(self):
        """
        Test save method updates the updated attribute
        """

        my_user9 = User()
        old_updated = my_user9.updated_at
        my_user9.save()
        new_updated = my_user9.updated_at
        self.assertNotEqual(old_updated, new_updated)

    def test_to_dict_method_return(self):
        """
        Test to_dict method that it returns an appropriate dict
        """

        my_user10 = User()
        dic = my_user10.to_dict()
        self.assertIs(type(dic), dict)

    def test_to_dict_method_keys(self):
        """
        Test dict keys are present
        """

        my_user11 = User()
        dic = my_user11.__dict__.copy()
        dic["__class__"] = type(my_user11).__name__
        dic["created_at"] = my_user11.created_at.isoformat()
        dic["updated_at"] = my_user11.updated_at.isoformat()
        dic1 = my_user11.to_dict()
        self.assertDictEqual(dic, dic1)

    def test_recreate_instance_from_dict(self):
        """
        Test instance recreation from dict
        """

        obj11 = User()
        obj11.name = "my_first_clone"
        obj11.my_number = 99
        dict_rep = obj11.to_dict()
        obj11_copy = User(**dict_rep)
        str1 = str(obj11)
        str2 = str(obj11_copy)
        self.assertEqual(str1, str2)


if __name__ == '__main__':
    unittest.main()
