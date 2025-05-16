#!/usr/bin/env python3

import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    """Tests for the Place class."""

    def test_instance(self):
        """Test if object is an instance of Place."""
        place = Place()
        self.assertIsInstance(place, Place)

if __name__ == "__main__":
    unittest.main()
