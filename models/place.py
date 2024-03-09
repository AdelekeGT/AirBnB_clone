#!/usr/bin/python3
"""Module contains the Place class"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Class inherits from BaseModel class

    Public Class Attributes:
        city_id: string - empty string: it will be the City.id
        user_id: string - empty string: it will be the User.id
        name: string - empty string
        description: string - empty string
        number_rooms: integer - 0
        number_bathrooms: integer - 0
        max_guest: integer - 0
        price_by_night: integer - 0
        latitude: float - 0.0
        longitude: float - 0.0
        amenity_ids: list of string
            empty list: Will be the list of Amenity.id later
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Instance initialization method

        Args:
            args (tuple): tuple of attributes
            kwargs (dict): dictionary of attributes
        """
        super().__init__(*args, **kwargs)

        # Place.city_id = City.id
        # Place.user_id = User.id
