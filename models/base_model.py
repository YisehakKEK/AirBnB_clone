#!/usr/bin/python
import uuid
from datetime import datetime

class BaseModel:
    """
    Defines all common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the BaseModel instance from dictionary or by creating a new one.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            # Import storage here to avoid circular import
            from models import storage
            storage.new(self)

    def __str__(self):
        """
        String representation of the BaseModel class.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at attribute with the current datetime and saves to file.
        """
        self.updated_at = datetime.now()
        # Import storage here to avoid circular import
        from models import storage
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of the instance.
        """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary