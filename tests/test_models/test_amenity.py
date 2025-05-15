#!/usr/bin/env python3
"""
Unittest for <models.amenity>.py
"""
import unittest
import <models.amenity>


class Test<Amenity>(unittest.TestCase):
    """Test cases for Amenity."""

    def setUp(self):
        self.obj = <models.amenity>.<Amenity>()

    def test_docstrings(self):
        # Module docstring
        self.assertIsNotNone(<models.amenity>.__doc__)
        # Class docstring
        self.assertIsNotNone(<models.amenity>.<Amenity>.__doc__)
        # (Optional) Function docstrings

    def test_instance_attributes(self):
        self.assertTrue(hasattr(self.obj, 'id'))
        self.assertTrue(hasattr(self.obj, 'created_at'))
        self.assertTrue(hasattr(self.obj, 'updated_at'))

    # Add more tests for methods, serialization, updates, etc.


if __name__ == '__main__':
    unittest.main()
