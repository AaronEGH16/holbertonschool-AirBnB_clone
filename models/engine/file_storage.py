#!/usr/bin/python3
"""recreate a BaseModel from another one by
using a dictionary representation
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage():
    """serializes instances to a JSON file
    and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}
    objclass = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity,
                "City": City, "Place": Place, "Review": Review, "State": State}

    def all(self):
        """Returns the __objects dictionary."""
        return self.__objects

    def new(self, obj):
        """Adds an object to __objects with the key <class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to a JSON file at __file_path."""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file at __file_path to __objects
        (only if the JSON file (__file_path) exists; otherwise,
        do nothing. If the file doesn't exist,
        no exception should be raised)."""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                for key, val in data.items():
                    obj = self.objclass[val["__class__"]](**val)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
