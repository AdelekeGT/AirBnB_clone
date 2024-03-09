#!/usr/bin/python3
"""Module contains the User class"""

from models.base_model import BaseModel


class User(BaseModel):
    """Class inherits from BaseModel

    Public Class Attributes:
        email (str) - empty string
        password (str) - empty string
        first_name (str) - empty string
        last_name (str) - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Instance initialization method

        Args:
            args (tuple): tuple of attributes
            kwargs (dict): idctionary of attributes
        """
        super().__init__(*args, **kwargs)
