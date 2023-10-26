#!/usr/bin/python3
"""
this module contains all test of file_storage
"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class Tests_FileStorage(unittest.TestCase):
    """
    tests of FileStorage class:
        - test 'all'
        - test 'new'
        - test 'save'
        - test 'reload'
    """

    def setUp(self):
        self.storage = FileStorage()
        self.base_model = BaseModel()
        self.file_path = "file.json"

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        self.storage.new(self.base_model)
        obj_key = f"{self.base_model.__class__.__name__}.{self.base_model.id}"
        self.assertTrue(obj_key in self.storage.all())

    def test_save(self):
        self.storage.new(self.base_model)
        self.storage.save()
        obj_key = f"{self.base_model.__class__.__name__}.{self.base_model.id}"
        self.assertTrue(obj_key in self.storage.all())

    def test_reload(self):
        obj1 = BaseModel()
        self.storage.new(obj1)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        obj_key = f"{obj1.__class__.__name__}.{obj1.id}"
        all_obj = new_storage.all()
        self.assertTrue(obj_key in new_storage.all())
        self.assertEqual(obj1.to_dict(), (all_obj[obj_key]).to_dict())
