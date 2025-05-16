#!/usr/bin/env python3

import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """Tests for the User class."""

    def test_instance(self):
        """Test if object is an instance of User."""
        user = User()
        self.assertIsInstance(user, User)

if __name__ == "__main__":
    unittest.main()
