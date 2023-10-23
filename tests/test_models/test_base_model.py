#!/usr/bin/python3
"""
this module contains all test of base_model
"""
import unittest
import uuid
import datetime
from models.base_model import BaseModel


class Tests_BaseModel(unittest.TestCase):
    """
    tests of BaseModel class:
        - test unique objects
        - test update time
        - test str representation
        - test type returned
    """
    def test_unique_objects(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.to_dict(), obj2.to_dict())

    def test_update_time(self):
        obj1 = BaseModel()
        origin = obj1.to_dict()
        obj1.save()
        self.assertNotEqual(origin, obj1.to_dict)

    def test_str_repr(self):
        obj1 = BaseModel()
        str_obj1 = f"[{type(obj1).__name__}] ({obj1.id}) {obj1.__dict__}"
        self.assertEqual(str(obj1), str_obj1)

    def test_type_returned(self):
        obj1 = BaseModel()
        self.assertEqual(str, type(obj1.__str__()))
        self.assertEqual(dict, type(obj1.to_dict()))
