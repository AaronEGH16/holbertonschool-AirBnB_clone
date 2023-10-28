#!/usr/bin/python3
"""classs Review that define the review attributes
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Define the class Review"""
    place_id = ""
    user_id = ""
    text = ""