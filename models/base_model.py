#!/usr/bin/python3
"""
Defines the BaseModel class, which serves as the base for all models.
"""

import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """
    Base class for all models in the AirBnB clone project.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel instance.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.utcnow()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.utcnow()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            storage.new(self)

    def save(self):
        """
        Update the updated_at attribute and save the instance to storage.
        """
        self.updated_at = datetime.utcnow()
        storage.save()

    def to_dict(self):
        """
        Return a dictionary representation of the instance.
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary

    def __str__(self):
        """
        Return the string representation of the instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"