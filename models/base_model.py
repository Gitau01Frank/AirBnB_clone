#!/usr/bin/python3
"""Defines the BaseModel class."""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """Defines the BaseModel class"""
    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel
        Args:
            *args(any): Unused
            **kwargs(dict): Key/value pairs of attributes
        """
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.utcnow()
            storage.new(self)

    def save(self):
        """updates updated_at with the current datetime"""
        self.updated_at = datetime.utcnow()
        storage.save()

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
