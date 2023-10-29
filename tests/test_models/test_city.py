#!/usr/bin/python3
"""Test city"""
import unittest
from models.city import City
from models.base_model import BaseModel


class Test_city(unittest.TestCase):
    """Tests:
            state_id and name its created
            City inherit BaseModel
    """
    def test_city_attributes(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_inheritance(self):
        city = City()
        self.assertTrue(isinstance(city, BaseModel))
