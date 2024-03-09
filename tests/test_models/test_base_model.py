#!/usr/bin/python3
"""Module contains unittest for 'base_model.py' module"""

from models.base_model import BaseModel
import unittest
from datetime import datetime
from models import storage


class TestBaseModel(unittest.TestCase):
    """Class for unit tests"""

    def setUp(self):
        """Perform setup actions before each test case"""
        storage.reload()

    def tearDown(self):
        """Perform cleanup actions after each test case"""
        storage.reload()

    def test_initialization(self):
        """Test for the creation of instance attributes"""
        base_instance = BaseModel()
        self.assertIsInstance(base_instance, BaseModel)
        self.assertIsNotNone(base_instance.id)
        self.assertIsInstance(base_instance.id, str)
        self.assertIsNotNone(base_instance.created_at)
        self.assertIsInstance(base_instance.created_at, datetime)
        self.assertIsNotNone(base_instance.updated_at)
        self.assertIsInstance(base_instance.updated_at, datetime)

    def test_create_instance_from_dict(self):
        """Create a dict from instance, and then create a new instance
        from information in that dictionary."""
        base_instance = BaseModel()
        base_instance.number = 89
        base_instance.name = "Abidushaker"
        instance_dict = base_instance.to_dict()

        new_model = BaseModel(**instance_dict)
        self.assertEqual(new_model.name, "Abidushaker")
        self.assertEqual(new_model.number, 89)
        self.assertIsInstance(new_model.id, str)
        self.assertIsInstance(new_model.created_at, datetime)
        self.assertIsInstance(new_model.updated_at, datetime)

    def test_save(self):
        """Tests for the save method"""
        obj_instance = BaseModel()
        time_update = obj_instance.updated_at
        obj_instance.save()
        self.assertNotEqual(time_update, obj_instance.updated_at)

    def test_to_dict(self):
        """Tests the 'to_dict' method"""
        obj_instance = BaseModel()
        obj_dict = obj_instance.to_dict()
        self.assertIsNotNone(obj_dict)
        self.assertIsInstance(obj_dict, dict)
        self.assertIn("__class__", obj_dict)
        self.assertIn("created_at", obj_dict)
        self.assertIn("updated_at", obj_dict)


if __name__ == "__main__":
    unittest.main()
