#!/usr/bin/env python3
"""
Unittest for models.amenity
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class."""

    def setUp(self):
        """Set up an Amenity instance for tests."""
        self.obj = Amenity()

    def test_docstrings(self):
        """All modules, classes, and functions have docstrings."""
        self.assertIsNotNone(Amenity.__doc__)
        self.assertIsNotNone(Amenity.__init__.__doc__)

    def test_attributes(self):
        """Amenity should have name attribute as empty string by default."""
        self.assertTrue(hasattr(self.obj, 'name'))
        self.assertEqual(self.obj.name, '')

    def test_inheritance(self):
        """Amenity should inherit from BaseModel."""
        from models.base_model import BaseModel

        self.assertIsInstance(self.obj, BaseModel)


if __name__ == '__main__':
    unittest.main()
