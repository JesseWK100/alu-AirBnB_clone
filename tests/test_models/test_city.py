#!/usr/bin/env python3
"""
Unittest for models.city.py
"""
import unittest
import models.city


class Test City(unittest.TestCase):
    """Test cases for City."""

    def setUp(self):
        """Create a new instance for each test."""
        self.obj = models.city.City()

    def test_docstrings(self):
        """All modules, classes, and functions have docstrings."""
        # Module docstring
        self.assertIsNotNone(models.city.__doc__)
        # Class docstring
        self.assertIsNotNone(models.city.City.__doc__)
        # (Optional) Function docstrings

    def test_instance_attributes(self):
        """Test that the object has expected default attributes."""
        self.assertTrue(hasattr(self.obj, 'id'))
        self.assertTrue(hasattr(self.obj, 'created_at'))
        self.assertTrue(hasattr(self.obj, 'updated_at'))

    # Add more tests for methods, serialization, updates, etc.


if __name__ == '__main__':
    unittest.main()
