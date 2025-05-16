#!/usr/bin/env python3

from models.base_model import BaseModel

class Review(BaseModel):
    """Class representing a review."""
    
    def __init__(self, *args, **kwargs):
        """Initialize a new Review."""
        super().__init__(*args, **kwargs)
        self.place_id = kwargs.get("place_id", "")
        self.user_id = kwargs.get("user_id", "")
        self.text = kwargs.get("text", "")
