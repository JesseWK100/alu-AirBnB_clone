#!/usr/bin/python3
"""
Unittest for Amenity class.
"""

import unittest
from models.amenity import Amenity
from datetime import datetime

class TestAmenity(unittest.TestCase):
    """
    Tests for the Amenity class.
    """

    def test_instance_creation(self):
        """Test instance creation and attributes."""
        model = Amenity()
        self.assertIsInstance(model, Amenity)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
