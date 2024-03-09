#!/usr/bin/python3
"""Module contains test for user.py"""

from models.base_model import BaseModel
from models.user import User
from models import storage
import unittest


class TestUser(unittest.TestCase):
    """Class inherits from unittest.TestCase"""

    @classmethod
    def setUpClass(cls):
        """Perform setup actions before any test cases in the class"""
        storage.reload()

    def setUp(self):
        """PErform setup actions before each test case"""
        self.all_objs = storage.all()

    def tearDown(self):
        """Perform teardown actions after each test case
        Reset the JSON file or perform any cleanup
        Ensures that instances creaed during tests do not get stored
        """
        storage.reload()

    def test_initialization(self):
        """Tests initialization of instance from User class"""

        user_obj = User()
        user_obj.first_name = "Raphase"
        user_obj.last_name = "Pharel"
        user_obj.email = "citadel@gmail.com"
        user_obj.password = "indaboski"

        self.assertIsInstance(user_obj, BaseModel)
        self.assertIsNotNone(user_obj.id)
        self.assertIsNotNone(user_obj.created_at)
        self.assertIsNotNone(user_obj.updated_at)

        user_key = f"{user_obj.__class__.__name__}.{user_obj.id}"

        self.assertIn(user_key, self.all_objs)  # New object not stored yet

        user_obj.save()

        self.assertIn(user_key, self.all_objs)   # New object is now stored

        user_obj2 = User()
        user_obj2.first_name = "Indaboski"
        user_obj2.last_name = "Bahose"
        user_obj2.email = "ribadu@mail.com"
        user_obj2.password = "sepree"
        user_key2 = f"{user_obj2.__class__.__name__}.{user_obj2.id}"
        user_obj2.save()

        self.assertIsInstance(user_obj2, BaseModel)
        self.assertIsInstance(user_obj2, User)
        self.assertIsNotNone(user_obj2.id)
        self.assertIsNotNone(user_obj2.created_at)
        self.assertIsNotNone(user_obj2.updated_at)

        self.assertIn(user_key2, self.all_objs)


if __name__ == "__main__":
    unittest.main()
