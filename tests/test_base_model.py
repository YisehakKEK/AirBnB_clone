#!/usr/bin/python

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_base_model_instance(self):
        """Test instantiation of BaseModel class."""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIn('id', my_model.__dict__)

    def test_base_model_save(self):
        """Test save method of BaseModel."""
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)

    def test_base_model_to_dict(self):
        """Test to_dict method of BaseModel."""
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')


if __name__ == '__main__':
    unittest.main()
