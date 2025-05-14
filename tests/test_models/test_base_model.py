#!/usr/bin/python3
"""
Unittest for BaseModel class.
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """
    Tests for the BaseModel class.
    """

    def test_instance_creation(self):
        """Test instance creation and attributes."""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
