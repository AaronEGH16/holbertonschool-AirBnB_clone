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
        self.assertNotEqual(obj1.id, obj2.id)
        self.assertNotEqual(obj1.created_at, obj2.created_at)
        self.assertNotEqual(obj1.to_dict, obj2.to_dict)

    def test_update_time(self):
        obj1 = BaseModel()
        obj1.save()
        self.assertNotEqual(obj1.updated_at, obj1.created_at)

    def test_type_returned(self):
        obj1 = BaseModel()
        self.assertEqual(str, type(obj1.__str__()))
        self.assertEqual(dict, type(obj1.to_dict()))
