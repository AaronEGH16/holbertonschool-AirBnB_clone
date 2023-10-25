#!/usr/bin/python3
"""_summary_
"""
import json
from queue import Empty


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the __objects dictionary."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds an object to __objects with the key <class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to a JSON file at __file_path."""
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file at __file_path to __objects
        (only if the JSON file (__file_path) exists; otherwise,
        do nothing. If the file doesn't exist,
        no exception should be raised)."""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                for key, val in data.items():
                    obj = val["__class__"].__dict__.copy()
                    obj.update(**val)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
