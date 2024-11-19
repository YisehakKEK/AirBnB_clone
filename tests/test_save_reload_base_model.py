#!/usr/bin/python

import unittest
from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage integration with BaseModel."""

    def test_reload_objects(self):
        """Test reloading objects from file storage."""
        all_objs = storage.all()
        print("-- Reloaded objects --")
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            print(obj)

    def test_create_new_object(self):
        """Test creating and saving a new BaseModel object."""
        print("-- Create a new object --")
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model.save()
        print(my_model)


if __name__ == '__main__':
    unittest.main()
