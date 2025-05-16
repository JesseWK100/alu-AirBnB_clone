#!/usr/bin/env python3

"""
BaseModel module: defines the BaseModel class for AirBnB clone.
"""
import uuid
from datetime import datetime


class BaseModel:
    """BaseModel defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel instance.
        If kwargs is not empty, deserialize attributes from dict;
        otherwise, generate a new id and timestamps.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return string representation: [<class name>] (<id>) <__dict__>."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """Update `updated_at` with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dict containing all keys/values of the instance __dict__,
        with `created_at` and `updated_at` as ISO format strings, and a '__class__' key.
        """
        output = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                output[key] = value.isoformat()
            else:
                output[key] = value
        output["__class__"] = self.__class__.__name__
        return output
