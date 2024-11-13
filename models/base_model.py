import uuid
from datetime import datetime
from models import storage

class BaseModel:
        def __init__(self, *args, **kwargs):
                    if kwargs:
                                    for key, value in kwargs.items():
                                                        if key != '__class__':
                                                                                setattr(self, key, value)
                                                                                            # Convert date strings back to datetime objects
                                                                                                        self.created_at = datetime.strptime(self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
                                                                                                                    self.updated_at = datetime.strptime(self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")
                                                                                                                            else:
                                                                                                                                            self.id = str(uuid.uuid4())
                                                                                                                                                        self.created_at = datetime.now()
                                                                                                                                                                    self.updated_at = self.created_at
                                                                                                                                                                                storage.new(self)

                                                                                                                                                                                    def to_dict(self):
                                                                                                                                                                                                """Returns a dictionary representation of the instance"""
                                                                                                                                                                                                        dict_rep = self.__dict__.copy()
                                                                                                                                                                                                                dict_rep['created_at'] = self.created_at.isoformat()
                                                                                                                                                                                                                        dict_rep['updated_at'] = self.updated_at.isoformat()
                                                                                                                                                                                                                                dict_rep['__class__'] = self.__class__.__name__
                                                                                                                                                                                                                                        return dict_rep

                                                                                                                                                                                                                                        def save(self):
                                                                                                                                                                                                                                                    """Updates updated_at attribute and saves the object to storage"""
                                                                                                                                                                                                                                                            self.updated_at = datetime.now()
                                                                                                                                                                                                                                                                    storage.save()

                                                                                                                                                                                                                                                                        def __str__(self):
                                                                                                                                                                                                                                                                                    """Returns a string representation of the object"""
                                                                                                                                                                                                                                                                                            return f"[{self.__class__.__name__}] ({self.id}) {self.to_dict()}"

