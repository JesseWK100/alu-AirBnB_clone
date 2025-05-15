#!/usr/bin/env python3
"""
Unittest for models.user
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for User class."""

    def setUp(self):
        """Set up a User instance for tests."""
        self.obj = User()

    def test_docstrings(self):
        """All modules, classes, and functions have docstrings."""
        self.assertIsNotNone(User.__doc__)
        self.assertIsNotNone(User.__init__.__doc__)

    def test_attributes(self):
        """User should have email, password, first_name, and last_name default to empty strings."""
        attrs = ['email', 'password', 'first_name', 'last_name']
        for attr in attrs:
            self.assertTrue(hasattr(self.obj, attr))
            self.assertEqual(getattr(self.obj, attr), '')

    def test_inheritance(self):
        """User should inherit from BaseModel."""
        from models.base_model import BaseModel

        self.assertIsInstance(self.obj, BaseModel)


if __name__ == '__main__':
    unittest.main()
