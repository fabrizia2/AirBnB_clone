#!/usr/bin/python3
"""
Test for the user class
"""
import unittest
from models.base_model import BaseModel
from models.city import City
import datetime


class TestCity(unittest.TestCase):
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

    def test_id_unique(self):
        """
        Test id attribute is unique
        """

        obj1 = City()
        obj2 = City()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_id_string(self):
        """
        Test id attribute is string
        """

        obj3 = City()
        self.assertIs(type(obj3.id), str)

    def test_instance(self):
        """
        Test object is instance
        """

        obj4 = City()
        self.assertIsInstance(obj4, BaseModel)

    def test_created_at(self):
        """
        Test created_at attribute is a datetime instance
        """

        obj5 = City()
        self.assertIs(type(obj5.created_at), datetime.datetime)

    def test_updated_at(self):
        """
        Test updated_at attribute is a datetime instance
        """

        obj6 = City()
        self.assertIs(type(obj6.updated_at), datetime.datetime)

    def test_str_rep(self):
        """
        Test str is printed as specified
        """

        obj7 = City()
        strv = str(obj7)
        strv1 = f"{[type(obj7).__name__]} ({obj7.id}) {obj7.__dict__}"
        self.assertEqual(strv, strv1)

    def test_save_method(self):
        """
        Test save method updates the updated attribute
        """

        obj8 = City()
        old_updated = obj8.updated_at
        obj8.save()
        new_updated = obj8.updated_at
        self.assertNotEqual(old_updated, new_updated)

    def test_to_dict_method_return(self):
        """
        Test to_dict method that it returns an appropriate dict
        """

        obj9 = City()
        dic = obj9.to_dict()
        self.assertIs(type(dic), dict)

    def test_to_dict_method_keys(self):
        """
        Test dict keys are present
        """

        obj10 = City()
        dic = obj10.__dict__.copy()
        dic["__class__"] = type(obj10).__name__
        dic["created_at"] = obj10.created_at.isoformat()
        dic["updated_at"] = obj10.updated_at.isoformat()
        dic1 = obj10.to_dict()
        self.assertDictEqual(dic, dic1)

    def test_recreate_instance_from_dict(self):
        """
        Test instance recreation from dict
        """

        obj11 = City()
        obj11.name = "my_first_clone"
        obj11.my_number = 99
        dict_rep = obj11.to_dict()
        obj11_copy = City(**dict_rep)
        str1 = str(obj11)
        str2 = str(obj11_copy)
        self.assertEqual(str1, str2)


if __name__ == '__main__':
    unittest.main()
