#!/usr/bin/python3
"""Test review"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class Test_Review(unittest.TestCase):
    """Tests:
            test its created all atribute class
            test review inherit BaseModel
    """
    def test_review_attributes(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_inheritance(self):
        review = Review()
        self.assertTrue(isinstance(review, BaseModel))
