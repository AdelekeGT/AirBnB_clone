#!/usr/bin/python3
"""Module contains the Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class inherits from BaseModel

    Public Class Attributes:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Instance initialization method

        Args:
            args (tuple): tuple of attributes
            kwargs (dict): idctionary of attributes
        """
        super().__init__(*args, **kwargs)

        # Review.place_id = Place.id
        # Review.user_id = User.id
