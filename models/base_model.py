#!/usr/bin/python3
"""
BaseModel module.
Defines the BaseModel class that will serve as the foundation for other models.
"""

from datetime import datetime
import uuid

class BaseModel:
    """
    Defines common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
