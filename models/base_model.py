#!/usr/bin/python3
import uuid
import datetime
"""class BaseModel that defines all common attributes/methods for other classes
"""


class BaseModel:
    """
    BaseModel:

    methods:
        - __init__(self)
        - __str__(self)
        - save(self)
        - to_dict(self)
    """
    def __init__(self):
        """initialize a new object of BaseModel
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """should print [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        result = self.__dict__
        result["__class__"] = type(self).__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()

        return result
