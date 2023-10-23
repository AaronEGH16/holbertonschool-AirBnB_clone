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
        - test type returned
    """
    def test_unique_objects(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.to_dict(), obj2.to_dict())

    def test_update_time(self):
        obj1 = BaseModel()
        save_obj1 = obj1.to_dict()
        obj1.save()
        self.assertNotEqual(obj1.to_dict, save_obj1)

    def test_type_returned(self):
        obj1 = BaseModel()
        self.assertEqual(str, type(obj1.__str__()))
        self.assertEqual(dict, type(obj1.to_dict()))
