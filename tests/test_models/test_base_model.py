    import unittest
    from models.base_model import BaseModel
    class TestBaseModel(unittest.TestCase):
    def test_create_instance(self):
        obj = BaseModel()
                            self.assertIsInstance(obj, BaseModel)

                                def test_to_dict(self):
                                    obj = BaseModel()
                                                    obj_dict = obj.to_dict()
                                                            self.assertIsInstance(obj_dict, dict)
                                                                    self.assertIn("id", obj_dict)
                                                                            self.assertIn("created_at", obj_dict)

                                                                                def test_save(self):
                                                                                    obj = BaseModel()
                                                                                                    old_updated_at = obj.updated_at
                                                                                                            obj.save()
                                                                                                                    self.assertNotEqual(obj.updated_at, old_updated_at)

