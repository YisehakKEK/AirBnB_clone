import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w') as f:
            dict_objs = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
            json.dump(dict_objs, f)

    def reload(self):
        """Deserializes the JSON file to __objects (if file exists)"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                dict_objs = json.load(f)
                for key, value in dict_objs.items():
                    cls_name = value['__class__']
                    del value['__class__']
                    self.new(eval(cls_name)(**value))
        except FileNotFoundError:
            pass
