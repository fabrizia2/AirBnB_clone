#!/usr/bin/python3
"""
Module that test the class BaseModel attributes and methods
"""
import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModelClass(unittest.TestCase):
    """
    Class to define methods testing base class
    """

    def test_id_unique(self):
        """
        Test id attribute is unique
        """

        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_id_string(self):
        """
        Test id attribute is string
        """

        obj3 = BaseModel()
        self.assertIs(type(obj3.id), str)

    def test_instance(self):
        """
        Test object is instance
        """

        obj4 = BaseModel()
        self.assertIsInstance(obj4, BaseModel)

    def test_created_at(self):
        """
        Test created_at attribute is a datetime instance
        """

        obj5 = BaseModel()
        self.assertIs(type(obj5.created_at), datetime.datetime)

    def test_updated_at(self):
        """
        Test updated_at attribute is a datetime instance
        """

        obj6 = BaseModel()
        self.assertIs(type(obj6.updated_at), datetime.datetime)

    def test_str_rep(self):
        """
        Test str is printed as specified
        """

        obj7 = BaseModel()
        strv = str(obj7)
        strv1 = f"{[type(obj7).__name__]} ({obj7.id}) {obj7.__dict__}"
        self.assertEqual(strv, strv1)

    def test_save_method(self):
        """
        Test save method updates the updated attribute
        """

        obj8 = BaseModel()
        old_updated = obj8.updated_at
        obj8.save()
        new_updated = obj8.updated_at
        self.assertNotEqual(old_updated, new_updated)

    def test_to_dict_method_return(self):
        """
        Test to_dict method that it returns an appropriate dict
        """

        obj9 = BaseModel()
        dic = obj9.to_dict()
        self.assertIs(type(dic), dict)

    def test_to_dict_method_keys(self):
        """
        Test dict keys are present
        """

        obj10 = BaseModel()
        dic = obj10.__dict__.copy()
        dic["__class__"] = type(obj10).__name__
        dic["created_at"] = obj10.created_at.isoformat()
        dic["updated_at"] = obj10.updated_at.isoformat()
        dic1 = obj10.to_dict()
        self.assertDictEqual(dic, dic1)


if __name__ == "__main__":
    unittest.main()
