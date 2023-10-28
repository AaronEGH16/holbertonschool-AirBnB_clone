#!/usr/bin/python3
import unittest
from models.user import User
from models.base_model import BaseModel


class Test_User(unittest.TestCase):
    """test:
            test its created all atribute class
            User inherit BaseModel
    """
    def test_user_attributes(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_inheritance(self):
        user = User()
        self.assertTrue(isinstance(user, BaseModel))
