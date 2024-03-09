#!/usr/bin/python3
"""Module contains the State class"""

from models.base_model import BaseModel


class State(BaseModel):
    """Class inherits from BaseModel

    Public Class Attributes:
        name (str) - empty string
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Instance initialization method

        Args:
            args (tuple): tuple of attributes
            kwargs (dict): dictionary of attributes
        """
        super().__init__(*args, **kwargs)
