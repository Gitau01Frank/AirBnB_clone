#!/usr/bin/python3
"""Defines the BaseModel class."""
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """Defines the BaseModel class"""
    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel
        Args:
            *args(any): Unused
            **kwargs(dict): Key/value pairs of attributes
        """
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.utcnow()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

    def save(self):
        """updates updated_at with the current datetime"""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """Returns a dictionary representation of the BaseModel instance
        Includes the key/value pair __class__ that represents
        the class name of the object.
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict.pop("_sa_instance_state", None)
        return my_dict

    def __str__(self):
        """Returns the print/str representation of the BaseModel instance"""
        dict = self.__dict__.copy()
        dict.pop("_sa_instance_state", None)
        return "[{}] ({}) {}".format(type(self).__name__, self.id, dict)
