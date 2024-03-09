#!/usr/bin/python3
"""This module contains the base class"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """Base class from which other classes will inherit"""
    def __init__(self, *args, **kwargs):
        """Instance initialization function for every object

        Attributes:
            id (int): unique ID
            created_at (str): time created
            updated_at (str): time updated

        Args:
            args: not to be used
            kwargs:
                id (str): uuid from dictionary
                created_at (datetime): creation date and time
                updated_at (datetime): updated date and time
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = str(value)
                elif key == 'created_at':
                    self.created_at = datetime.fromisoformat(value)
                elif key == 'updated_at':
                    self.updated_at = datetime.fromisoformat(value)
                else:
                    if key != '__class__':
                        setattr(self, key, value)

        else:
            # If no arguments are passed we create the attributes
            # all attributes set to default values
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """Updates the public instance attribute "updated_at"
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of instance

        Returns:
            dictionary
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()

        return obj_dict

    def __str__(self):
        """Returns a string representation of the instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
