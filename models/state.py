#!/usr/bin/env python3

from models.base_model import BaseModel

class State(BaseModel):
    """Class representing a state."""

    def __init__(self, *args, **kwargs):
        """Initialize a new State."""
        super().__init__(*args, **kwargs)
        self.name = kwargs.get("name", "")
