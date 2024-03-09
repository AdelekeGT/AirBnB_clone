#!/usr/bin/python3
"""This module contains class FileStorage for
storing object instances of BaseModel"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os

_cls = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class FileStorage:
    """Serializes instances to a JSON file and
    deserializes JSON file to instances

    Attributes:
        file_path (str): path to the JSON file
        objects (dict):
            Key: <Classname>.<id>
            Value: Instance of ClassName
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Add an instance of BaseModel to __objects
        with key <obj classname>.id

        Args:
            obj (instance): object to be stored
        """
        if obj is not None:
            store_key = f"{obj.__class__.__name__}.{obj.id}"
            FileStorage.__objects[store_key] = obj

    def save(self):
        """Serializes __objects to the JSON file in __file_path"""
        all_objects = {}

        for obj in FileStorage.__objects:
            all_objects[obj] = FileStorage.__objects[obj].to_dict()

        with open(FileStorage.__file_path, 'w') as json_file:
            json.dump(all_objects, json_file)

    def reload(self):
        """Deserializes JSON file to __objects only if
        the JSON file in __file_path exists"""
        if not os.path.exists(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, 'r') as json_file:
            all_obj = json.load(json_file)

        for key, obj in all_obj.items():
            cls_name = obj["__class__"]
            cls = _cls.get(cls_name)
            if cls:
                FileStorage.__objects[key] = cls(**obj)
