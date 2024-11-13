import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
        """Test cases for the BaseModel class"""

            def test_instantiation(self):
                        """Test if the BaseModel instance is created correctly"""
                                model = BaseModel()
                                        self.assertIsInstance(model, BaseModel)
                                                self.assertTrue(hasattr(model, 'id'))
                                                        self.assertTrue(hasattr(model, 'created_at'))
                                                                self.assertTrue(hasattr(model, 'updated_at'))

                                                                    def test_save(self):
                                                                                """Test if the save method updates updated_at"""
                                                                                        model = BaseModel()
                                                                                                old_updated_at = model.updated_at
                                                                                                        model.save()
                                                                                                                self.assertNotEqual(model.updated_at, old_updated_at)

                                                                                                                    def test_to_dict(self):
                                                                                                                                """Test if the to_dict method works as expected"""
                                                                                                                                        model = BaseModel()
                                                                                                                                                model_dict = model.to_dict()
                                                                                                                                                        self.assertEqual(model_dict["__class__"], "BaseModel")
                                                                                                                                                                self.assertEqual(type(model_dict["created_at"]), str)
                                                                                                                                                                        self.assertEqual(type(model_dict["updated_at"]), str)

                                                                                                                                                                            def test_str(self):
                                                                                                                                                                                        """Test the __str__ method"""
                                                                                                                                                                                                model = BaseModel()
                                                                                                                                                                                                        string_representation = model.__str__()
                                                                                                                                                                                                                self.assertTrue(isinstance(string_representation, str))
                                                                                                                                                                                                                        self.assertIn(model.id, string_representation)
                                                                                                                                                                                                                                self.assertIn("BaseModel", string_representation)

                                                                                                                                                                                                                                if __name__ == "__main__":
                                                                                                                                                                                                                                        unittest.main()

