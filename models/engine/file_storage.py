import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """Handles the serialization and deserialization of objects"""
    
    __objects = {}

    def all(self):
        """Returns the dictionary of all stored objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the storage"""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            FileStorage.__objects[key] = obj

    def save(self):
        """Saves all objects to a JSON file"""
        with open('file.json', 'w') as f:
            # Using indent=4 for better readability
            json.dump({key: obj.to_dict() for key, obj in FileStorage.__objects.items()}, f, indent=4)

    def reload(self):
        """Reloads all objects from a JSON file"""
        try:
            with open('file.json', 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name = value.get("__class__")
                    if class_name == "BaseModel":
                        FileStorage.__objects[key] = BaseModel(**value)
                    elif class_name == "User":
                        FileStorage.__objects[key] = User(**value)
                    elif class_name == "State":
                        FileStorage.__objects[key] = State(**value)
                    elif class_name == "City":
                        FileStorage.__objects[key] = City(**value)
                    elif class_name == "Amenity":
                        FileStorage.__objects[key] = Amenity(**value)
                    elif class_name == "Place":
                        FileStorage.__objects[key] = Place(**value)
                    elif class_name == "Review":
                        FileStorage.__objects[key] = Review(**value)
        except FileNotFoundError:
            print("File not found. No data loaded.")  # Optional: Notify when the file isn't found
        except json.JSONDecodeError:
            print("Error decoding JSON data.")  # Handle JSON decoding errors, such as a corrupted file
        except Exception as e:
            print(f"Unexpected error occurred during reload: {e}")