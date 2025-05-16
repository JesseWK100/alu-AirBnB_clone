#!/usr/bin/env python3

import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """Tests for the Review class."""

    def test_instance(self):
        """Test if object is an instance of Review."""
        review = Review()
        self.assertIsInstance(review, Review)

if __name__ == "__main__":
    unittest.main()
