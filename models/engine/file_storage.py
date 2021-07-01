#!/usr/bin/python3
"""This file contains the Filestorage class"""
from models.user import User
from models.base_model import BaseModel
import json
from models.user import User
from models import state
from models import city
from models import amenity
from models import review
from models import place
classes = {
    "User": User,
    "Place": Place,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review
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

    def find_object(cls, id):
        """Returns obj id"""
        objs = cls.__objects
        for obj in objs.values():
            if obj.id == id:
                return obj
