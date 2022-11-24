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

    
