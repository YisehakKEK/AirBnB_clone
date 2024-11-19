#!/usr/bin/python

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of all objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the storage dictionary.
        Args:
            obj: The object to add.
        """
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes the storage dictionary to a JSON file.
        """
        with open(FileStorage.__file_path, 'w') as f:
            json_dict = {
                k: v.to_dict() for k, v in FileStorage.__objects.items()
            }
            json.dump(json_dict, f)

    def reload(self):
        """
        Deserializes the JSON file back to objects in the storage dictionary.
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    cls_name = value['__class__']
                    # Dynamically load the class and initialize the object
                    if cls_name in FileStorage.classes():
                        cls = FileStorage.classes()[cls_name]
                        FileStorage.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass

    @staticmethod
    def classes():
        """
        Returns a dictionary of all valid classes for deserialization.
        """
        return {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
        }
