#!/usr/bin/python3
"""Test amenity"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class Test_Amenity(unittest.TestCase):
    """Test:
            name its created
            Amenity inherit BaseModel
    """
    def test_amenity_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_amenity_inheritance(self):
        amenity = Amenity()
        self.assertTrue(isinstance(amenity, BaseModel))
