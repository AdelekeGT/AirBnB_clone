#!/usr/bin/python3
"""Module contains test for amenity.py"""

from models.base_model import BaseModel
from models.amenity import Amenity
from models import storage
import unittest


class TestAmenity(unittest.TestCase):
    """Test for Amenity Class"""

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
        self.all_objs = storage.all()

    def test_amenity_inheritance(self):
        """Tests if Amenity class inherits from BaseModel"""

        amenity_obj = Amenity()
        self.assertIsInstance(amenity_obj, BaseModel)

    def test_amenity_attr(self):
        """Tests for name attribute in Amenity instance"""

        amenity_obj = Amenity()
        amenity_obj.name = "Electricity"
        self.assertIn("name", vars(amenity_obj))
        self.assertIn("name", amenity_obj.__dict__)
        self.assertIn("name", amenity_obj.__dir__())
        self.assertIsNotNone(amenity_obj.name)

    def test_inherited_attr(self):
        """Tests for presence of other attributes inherited from BaseModel"""

        amenity_obj = Amenity()
        self.assertTrue("id" in vars(amenity_obj))
        self.assertTrue("created_at" in vars(amenity_obj))
        self.assertTrue("updated_at" in vars(amenity_obj))

    def test_attribute_type(self):
        """Test that type of d name attribute of Amenity instance is string"""

        amenity_obj = Amenity()
        _name = getattr(amenity_obj, "name")
        self.assertIsInstance(_name, str)


if __name__ == "__main__":
    unittest.main()
