#!/usr/bin/python
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_instance_creation(self):
        """Test the creation of a BaseModel instance."""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        self.assertIsInstance(my_model, BaseModel)
        self.assertEqual(my_model.name, "My First Model")
        self.assertEqual(my_model.my_number, 89)

    def test_to_dict(self):
        """Test conversion of a BaseModel instance to a dictionary."""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertIn('id', my_model_dict)
        self.assertEqual(my_model_dict['name'], "My First Model")
        self.assertEqual(my_model_dict['my_number'], 89)

    def test_from_dict(self):
        """Test creation of BaseModel from a dictionary."""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_dict = my_model.to_dict()
        my_new_model = BaseModel(**my_model_dict)
        self.assertIsInstance(my_new_model, BaseModel)
        self.assertEqual(my_new_model.name, my_model.name)
        self.assertEqual(my_new_model.my_number, my_model.my_number)
        self.assertEqual(my_model.id, my_new_model.id)

if __name__ == '__main__':
    unittest.main()