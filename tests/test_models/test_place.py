#!/usr/bin/env python3
"""
Unittest for models.place
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for Place class."""

    def setUp(self):
        """Set up a Place instance for tests."""
        self.obj = Place()

    def test_docstrings(self):
        self.assertIsNotNone(Place.__doc__)
        self.assertIsNotNone(Place.__init__.__doc__)

    def test_attributes(self):
        """Place should have default attributes defined."""
        defaults = {
            'city_id': '', 'user_id': '', 'name': '', 'description': '',
            'number_rooms': 0, 'number_bathrooms': 0,
            'max_guest': 0, 'price_by_night': 0,
            'latitude': 0.0, 'longitude': 0.0,
            'amenity_ids': []
        }
        for attr, value in defaults.items():
            self.assertTrue(hasattr(self.obj, attr))
            self.assertEqual(getattr(self.obj, attr), value)

    def test_inheritance(self):
        from models.base_model import BaseModel
        self.assertIsInstance(self.obj, BaseModel)


if __name__ == '__main__':
    unittest.main()
