#!/usr/bin/env python3

import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """Tests for the City class."""

    def test_instance(self):
        """Test if object is an instance of City."""
        city = City()
        self.assertIsInstance(city, City)

if __name__ == "__main__":
    unittest.main()
