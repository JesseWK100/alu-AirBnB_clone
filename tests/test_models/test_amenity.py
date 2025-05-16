#!/usr/bin/env python3

import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Tests for the Amenity class."""

    def test_instance(self):
        """Test if object is an instance of Amenity."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

if __name__ == "__main__":
    unittest.main()
