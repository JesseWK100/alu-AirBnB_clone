#!/usr/bin/env python3
"""
Unittest for models.review
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for Review class."""

    def setUp(self):
        self.obj = Review()

    def test_docstrings(self):
        self.assertIsNotNone(Review.__doc__)
        self.assertIsNotNone(Review.__init__.__doc__)

    def test_attributes(self):
        defaults = {'place_id': '', 'user_id': '', 'text': ''}
        for attr, val in defaults.items():
            self.assertTrue(hasattr(self.obj, attr))
            self.assertEqual(getattr(self.obj, attr), val)

    def test_inheritance(self):
        from models.base_model import BaseModel
        self.assertIsInstance(self.obj, BaseModel)


if __name__ == '__main__':
    unittest.main()
