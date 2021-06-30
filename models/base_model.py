#!/usr/bin/python3
"""This file contains the BaseModel class"""
from uuid import uuid4
from datetime import datetime
import models
time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Base model class"""
    def __init__(self, *args, **kwargs):
        """Initialization"""
        time = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                else:
                    setattr(self, key, value)
            if id in kwargs.keys():
                self.id = kwargs["id"]
            if "created_at" in kwargs.keys():
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            if "updated_at" in kwargs.keys():
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """print the following format"""
        NC = self.__class__.__name__
        return "[{}] ({}) {}".format(NC, self.id,
                                     self.__dict__)

    def save(self):
        """updates the public instance
        attribute updated_at with
        the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """updates the public instance
        attribute updated_at with the
        current datetime"""
        Dictionary = self.__dict__.copy()
        Dictionary["__class__"] = self.__class__.__name__
        Dictionary["updated_at"] = self.updated_at.isoformat()
        Dictionary["created_at"] = self.created_at.isoformat()
        return Dictionary
