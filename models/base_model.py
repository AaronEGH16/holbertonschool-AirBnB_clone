#!/usr/bin/python3
from queue import Empty
from datetime import datetime
import uuid
from models.__init__ import storage
"""class BaseModel that defines all common attributes/methods for other classes
"""


class BaseModel:
    """
    BaseModel:

    methods:
        - __init__(self, *args, **kwargs)
        - __str__(self)
        - save(self)
        - to_dict(self)
    """
    def __init__(self, *args, **kwargs):
        """initialize a new object of BaseModel
        """
        if kwargs and kwargs is not Empty:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "created_at" in kwargs:
                self.created_at = datetime.strptime(
                    kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            if "updated_at" in kwargs:
                self.updated_at = datetime.strptime(
                    kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """should print [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()
        storage.save(self)

    def to_dict(self):
        """ returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        result = self.__dict__.copy()
        result["__class__"] = type(self).__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()

        return result
