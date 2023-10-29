#!/usr/bin/python3
"""Test state"""
import unittest
from models.state import State
from models.base_model import BaseModel


class Tests_state(unittest.TestCase):
    """test:
            name its created
            Sate inherit BaseModel
    """
    def test_state_attributes(self):
        state = State()
        self.assertEqual(state.name, "")

    def test_state_inheritance(self):
        state = State()
        self.assertTrue(isinstance(state, BaseModel))
