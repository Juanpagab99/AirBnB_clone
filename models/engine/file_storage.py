#!/usr/bin/python3
"""This file contains the Filestorage class"""
from models.base_model import BaseModel
import json
classes = {
    "BaseModel": BaseModel
}


class FileStorage:
    """Class file storage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        if obj is not None:
            NC = obj.__class__.__name__
            self.__objects["{}.{}".format(NC, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        data = {}
        for key in self.__objects:
            data[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key in data:
                    self.__objects[key] = classes[data[key]
                                                  ["__class__"]](**data[key])
        except:
            return
