#!/usr/bin/python3
"""
Test for the user class
"""
import unittest
from models.base_model import BaseModel
from models.review import Review
import datetime


class TestReview(unittest.TestCase):
    """
    testing the class review
    """
    def test_instance(self):
        """
        Test object is instance
        """

        my_review = Review()
        self.assertIsInstance(my_review, BaseModel)

    def test_is_str(self):
        """
        test if the class attributes are strings
        """

        my_review1 = Review()
        self.assertIs(type(my_review1.place_id), str)
        self.assertIs(type(my_review1.user_id), str)
        self.assertIs(type(my_review1.text), str)

    def test_id_unique(self):
        """
        Test id attribute is unique
        """

        obj1 = Review()
        obj2 = Review()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_id_string(self):
        """
        Test id attribute is string
        """

        obj3 = Review()
        self.assertIs(type(obj3.id), str)

    def test_instance(self):
        """
        Test object is instance
        """

        obj4 = Review()
        self.assertIsInstance(obj4, BaseModel)

    def test_created_at(self):
        """
        Test created_at attribute is a datetime instance
        """

        obj5 = Review()
        self.assertIs(type(obj5.created_at), datetime.datetime)

    def test_updated_at(self):
        """
        Test updated_at attribute is a datetime instance
        """

        obj6 = Review()
        self.assertIs(type(obj6.updated_at), datetime.datetime)

    def test_str_rep(self):
        """
        Test str is printed as specified
        """

        obj7 = Review()
        strv = str(obj7)
        strv1 = f"[Review] ({obj7.id}) {obj7.__dict__}"
        self.assertEqual(strv, strv1)

    def test_save_method(self):
        """
        Test save method updates the updated attribute
        """

        obj8 = Review()
        old_updated = obj8.updated_at
        obj8.save()
        new_updated = obj8.updated_at
        self.assertNotEqual(old_updated, new_updated)

    def test_to_dict_method_return(self):
        """
        Test to_dict method that it returns an appropriate dict
        """

        obj9 = Review()
        dic = obj9.to_dict()
        self.assertIs(type(dic), dict)

    def test_to_dict_method_keys(self):
        """
        Test dict keys are present
        """

        obj10 = Review()
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

        obj11 = Review()
        obj11.name = "my_first_clone"
        obj11.my_number = 99
        dict_rep = obj11.to_dict()
        obj11_copy = Review(**dict_rep)
        str1 = str(obj11)
        str2 = str(obj11_copy)
        self.assertEqual(str1, str2)


if __name__ == '__main__':
    unittest.main()
