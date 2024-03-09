#!/usr/bin/python3
"""Module contains the Amenity class"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class inherits from BaseModel

    Public Class Attributes:
        name (str) - empty string
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Instance initialization method

        Args:
            args (tuple): tuple of attributes
            kwargs (dict): idctionary of attributes
        """
        super().__init__(*args, **kwargs)
