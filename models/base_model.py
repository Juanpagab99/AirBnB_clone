#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
class BaseModel:
    """Class Basemodel that defines
    all methods for other classes"""

    def __init__(self):
        """Initialization"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


    def __str__(self):
        """print the following format"""
        NC = __class__.__name__
        return "[{}] ({}) {}".format(NC, self.id, self.__dict__)

    def save(self):
        """updates the public instance
        attribute updated_at with
        the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """updates the public instance
        attribute updated_at with the
        current datetime"""
        Dictionary = self.__dict__.copy()
        Dictionary["__class__"] = self.name.__class__
        Dictionary["updated_at"] = self.updated_at.isoformat()
        Dictionary["created_at"] = self.created_at.isoformat()
        return Dictionary
