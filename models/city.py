#!/usr/bin/python3
"""Module contains the City class"""

# from models.base_model import BaseModel
from models.base_model import BaseModel


class City(BaseModel):
    """Class inherits from State

    Public Class Attributes:
        state_id (str) - empty string : it will be the State.id
        name (str) - empty string
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Instance initialization method

        Args:
            kwargs (dict): idctionary of attributes
        """
        super().__init__(*args, **kwargs)

        # City.state_id = State.id
