#!/usr/bin/env python3

from models.base_model import BaseModel

class Amenity(BaseModel):
    """Class representing an amenity."""

    def __init__(self, *args, **kwargs):
        """Initialize a new Amenity."""
        super().__init__(*args, **kwargs)
        self.name = kwargs.get("name", "")
