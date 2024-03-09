#!/usr/bin/python3
"""This module contains test for file_storage.py"""

from models.base_model import BaseModel
from models.user import User
from models import storage
import unittest
# import json


class TestFileStorage(unittest.TestCase):
    """Class inherits from unittest.TestCase"""

    def setUp(self):
        """Perform setup actions before each test case
        Reload the storage to ensure clean state before each test
        """
        storage.reload()

    def tearDown(self):
        """Perform teardown actions after each test case
        Reload the storage to ensure clean state after each test
        """
        storage.reload()

    def test_new(self):
        """Test the new method to add an instance to storage.__objects"""
        base_inst = BaseModel()
        base_inst.name = "Model_akoko"
        base_inst.my_number = 89

        store_key = f"{base_inst.__class__.__name__}.{base_inst.id}"

        all_inst = storage.all()
        self.assertIn(store_key, all_inst)
        self.assertEqual(all_inst[store_key], base_inst)
        self.assertIsNotNone(all_inst[store_key].name)
        self.assertIsNotNone(all_inst[store_key].my_number)

        user_inst = User()
        user_inst.email = "reina@gmail.com"
        user_inst.password = "password"
        user_inst.first_name = "Reina"
        user_inst.last_name = "Oyewole"

        user_key = f"{user_inst.__class__.__name__}.{user_inst.id}"

        all_inst = storage.all()
        self.assertIn(user_key, all_inst)
        self.assertEqual(all_inst[user_key], user_inst)
        self.assertIsNotNone(all_inst[user_key].email)
        self.assertIsNotNone(all_inst[user_key].password)
        self.assertIsNotNone(all_inst[user_key].first_name)
        self.assertIsNotNone(all_inst[user_key].last_name)
        self.assertIsNotNone(all_inst[user_key].id)
        self.assertIsNotNone(all_inst[user_key].created_at)
        self.assertIsNotNone(all_inst[user_key].updated_at)

    def test_save(self):
        """Test the save method to serialize __objects to JSON file"""
        base_inst = BaseModel()
        base_inst.name = "Model_akoko"
        base_inst.my_number = 89
        base_inst.save()

        # file_name = storage.__file_path
        # self.assertTrue(os.path.exists(file_name))

        # with open(storage.__file_path, 'r') as json_file:
        #     data = json.load(json_file)
        #     self.assertIsNotNone(data)

    def test_reload(self):
        """Test the reload method to deserialize JSON file to __objects"""
        base_inst = BaseModel()
        base_inst.name = "Model_akoko"
        base_inst.my_number = 89
        base_inst.save()

        store_key = f"{base_inst.__class__.__name__}.{base_inst.id}"
        all_objs = storage.all()

        self.assertIn(store_key, all_objs)
        self.assertEqual(all_objs[store_key].__class__.__name__, "BaseModel")
        self.assertNotEqual(all_objs[store_key].__class__.__name__, "User")

        my_user = User()
        my_user.first_name = "Betty"
        my_user.last_name = "Bar"
        my_user.email = "airbnb@mail.com"
        my_user.password = "root"
        my_user.save()

        my_user2 = User()
        my_user2.first_name = "John"
        my_user2.email = "airbnb2@mail.com"
        my_user2.password = "root"
        my_user2.save()

        user_key1 = f"{my_user.__class__.__name__}.{my_user.id}"
        user_key2 = f"{my_user2.__class__.__name__}.{my_user2.id}"
        all_objs = storage.all()

        present_keys = [store_key, user_key1, user_key2]
        all_keys = [keys for keys in all_objs.keys()]

        for key in present_keys:
            self.assertIn(key, all_keys)

        self.assertEqual(all_objs[store_key].__class__.__name__, "BaseModel")
        self.assertEqual(all_objs[user_key1].__class__.__name__, "User")
        self.assertEqual(all_objs[user_key2].__class__.__name__, "User")


if __name__ == "__main__":
    unittest.main()
