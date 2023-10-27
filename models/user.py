#!/usr/bin/python3
"""classs user that define the user attributes
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class for the database."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
