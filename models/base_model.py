from datetime import datetime
import uuid

class BaseModel:
    """A class that defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes a BaseModel instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self) -> str:
        """Returns a string representation of the object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self) -> None:
        """Updates the updated_at attribute and saves the object"""
        self.updated_at = datetime.now()
        # The storage should be defined elsewhere in the project
        # storage.save()  # Uncomment and define storage logic in the project

    def to_dict(self) -> dict:
        """Converts the object to a dictionary format"""
        dict_rep = self.__dict__.copy()
        dict_rep["__class__"] = self.__class__.__name__
        dict_rep["created_at"] = self.created_at.isoformat()
        dict_rep["updated_at"] = self.updated_at.isoformat()
        return dict_rep