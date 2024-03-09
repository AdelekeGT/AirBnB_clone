#!/usr/bin/python3
"""Module contains test for amenity.py"""

from models.base_model import BaseModel
from models.city import City
from models import storage
import unittest


class TestAmenity(unittest.TestCase):
    """Test for City Class"""

    @classmethod
    def setUpClass(cls):
        """Perform setup actions before any test cases in the class"""
        storage.reload()

    def setUp(self):
        """PErform setup actions before each test case"""
        storage.reload()
        self.all_objs = storage.all()

    def tearDown(self):
        """Perform teardown actions after each test case
        Reset the JSON file or perform any cleanup
        Ensures that instances created during tests do not get stored
        """
        storage.reload()
        self.all_objs = storage.all()

    def test_city_inheritance(self):
        """Tests if Amenity class inherits from BaseModel"""

        city_obj = City()
        self.assertIsInstance(city_obj, BaseModel)

    def test_amenity_attr(self):
        """Tests for name attribute in City instance"""

        city_obj = City()
        city_obj.name = "Electricity"
        city_obj.state_id = "id_state_wa"
        self.assertIn("name", vars(city_obj))
        self.assertIn("name", city_obj.__dict__)
        self.assertIn("name", city_obj.__dir__())
        self.assertIn("state_id", vars(city_obj))
        self.assertIn("state_id", city_obj.__dict__)
        self.assertIn("state_id", city_obj.__dir__())
        self.assertIsNotNone(city_obj.name)

    def test_inherited_attr(self):
        """Tests for presence of other attributes inherited from BaseModel"""

        city_obj = City()
        self.assertTrue("id" in vars(city_obj))
        self.assertTrue("created_at" in vars(city_obj))
        self.assertTrue("updated_at" in vars(city_obj))

    def test_attribute_type(self):
        """Test that type of d name attribute of City instance is string"""

        city_obj = City()
        _name = getattr(city_obj, "name")
        _state_id = getattr(city_obj, "state_id")
        self.assertIsInstance(_name, str)
        self.assertIsInstance(_state_id, str)


if __name__ == "__main__":
    unittest.main()
