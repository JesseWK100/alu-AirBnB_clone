#!/usr/bin/env python3

import unittest
from models.state import State

class TestState(unittest.TestCase):
    """Tests for the State class."""

    def test_instance(self):
        """Test if object is an instance of State."""
        state = State()
        self.assertIsInstance(state, State)

if __name__ == "__main__":
    unittest.main()
