#!/usr/bin/env python3
"""
Unittest for models.state
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for State class."""

    def setUp(self):
        self.obj = State()

    def test_docstrings(self):
        self.assertIsNotNone(State.__doc__)
        self.assertIsNotNone(State.__init__.__doc__)

    def test_attributes(self):
        self.assertTrue(hasattr(self.obj, 'name'))
        self.assertEqual(self.obj.name, '')

    def test_inheritance(self):
        from models.base_model import BaseModel
        self.assertIsInstance(self.obj, BaseModel)


if __name__ == '__main__':
    unittest.main()
