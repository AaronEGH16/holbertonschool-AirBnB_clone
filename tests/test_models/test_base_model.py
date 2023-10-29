#!/usr/bin/python3
"""
this module contains all test of base_model
"""
import unittest
from unittest.mock import patch
from models.engine.file_storage import FileStorage
import uuid
from datetime import datetime
from models.base_model import BaseModel


class Tests_BaseModel(unittest.TestCase):
    """
    tests of BaseModel class:
        - test unique objects
        - test update time
        - test str representation
        - test type returned
        - test initialize BaseModel from kwargs
        - test save storage
    """
    def test_unique_objects(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.to_dict(), obj2.to_dict())

    def test_update_time(self):
        obj1 = BaseModel()
        origin = obj1.to_dict()
        obj1.save()
        new = obj1.to_dict()
        self.assertNotEqual(origin["updated_at"], new["updated_at"])

    def test_str_repr(self):
        obj1 = BaseModel()
        str_obj1 = f"[{type(obj1).__name__}] ({obj1.id}) {obj1.__dict__}"
        self.assertEqual(str(obj1), str_obj1)

    def test_type_returned(self):
        obj1 = BaseModel()
        self.assertEqual(str, type(obj1.__str__()))
        self.assertEqual(dict, type(obj1.to_dict()))

    def test_base_from_kwargs(self):
        obj1 = BaseModel(id=1, created_at="2003-03-18T16:30:01.100000",
                         updated_at="2003-03-18T16:30:01.100000")
        answer = {
            "__class__": type(obj1).__name__,
            "id": 1,
            "created_at": "2003-03-18T16:30:01.100000",
            "updated_at": "2003-03-18T16:30:01.100000"
        }
        self.assertEqual(obj1.to_dict(), answer)

    def test_save_storage(self):
        obj = BaseModel()
        with unittest.mock.patch.object(FileStorage, 'save') as mock_save:
            obj.save()
            mock_save.assert_called_once()
