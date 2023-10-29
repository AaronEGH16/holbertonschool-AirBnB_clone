#!/usr/bin/python3
"""
this module contains all test of file_storage
"""
import unittest
from unittest.mock import patch
import os
from models import storage
from models.base_model import BaseModel
from datetime import datetime


class Tests_FileStorage(unittest.TestCase):
    """
    tests of FileStorage class:
        - test 'all'
        - test 'new'
        - test 'save'
        - test 'reload'
    """

    def setUp(self):
        self.base_model = BaseModel()
        self.file_path = storage._FileStorage__file_path

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        self.assertIsInstance(storage.all(), dict)

    def test_new(self):
        storage.new(self.base_model)
        obj_key = f"{self.base_model.__class__.__name__}.{self.base_model.id}"
        self.assertIsNotNone((storage.all())[obj_key])

    def test_save_storage(self):
        obj = BaseModel()
        with unittest.mock.patch.object(storage, 'save') as mock_save:
            storage.save(obj)
            mock_save.assert_called_once()
        obj_key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIsNotNone((storage.all())[obj_key])

    def test_reload(self):
        objects = storage._FileStorage__objects
        if os.path.isfile(self.file_path):
            os.remove(self.file_path)
        storage.reload()
        obj1 = BaseModel()
        obj2 = BaseModel()
        obj3 = BaseModel()

        obj_key1 = f"{obj1.__class__.__name__}.{obj1.id}"
        obj_key2 = f"{obj2.__class__.__name__}.{obj2.id}"
        obj_key3 = f"{obj3.__class__.__name__}.{obj3.id}"
        all_obj = storage.all()
        obj1.save()
        obj2.save()
        obj3.save()
        self.assertIsNotNone((storage.all())[obj_key1])
        self.assertEqual(obj1.to_dict(), (all_obj[obj_key1]).to_dict())
        self.assertIsNotNone((storage.all())[obj_key2])
        self.assertEqual(obj2.to_dict(), (all_obj[obj_key2]).to_dict())
        self.assertIsNotNone((storage.all())[obj_key3])
        self.assertEqual(obj3.to_dict(), (all_obj[obj_key3]).to_dict())
        if objects != {}:
            objects.clear()
        storage.reload()
        self.assertNotEqual(objects, {})
