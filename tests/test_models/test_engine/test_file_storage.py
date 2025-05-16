#!/usr/bin/evn python3

import unittest
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """Tests for the FileStorage class."""

    def test_instance(self):
        """Test if object is an instance of FileStorage."""
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)

if __name__ == "__main__":
    unittest.main()
