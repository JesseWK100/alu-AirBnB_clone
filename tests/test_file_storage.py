#!/usr/bin/env python3
"""
Unittest for models.engine.file_storage
"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage engine."""

    def setUp(self):
        """Prepare storage and temp file path."""
        self.storage = FileStorage()
        # ensure no side-effects
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_docstrings(self):
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_all_and_new(self):
        """Test that new object is added to storage."""
        bm = BaseModel()
        key = f"BaseModel.{bm.id}"
        self.storage.new(bm)
        self.assertIn(key, self.storage.all())
        self.assertIs(self.storage.all()[key], bm)

    def test_save_and_reload(self):
        """Test save writes to file and reload restores objects."""
        bm = BaseModel()
        key = f"BaseModel.{bm.id}"
        self.storage.new(bm)
        self.storage.save()
        # clear in-memory and reload
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        self.assertIn(key, self.storage.all())
        obj2 = self.storage.all()[key]
        self.assertEqual(obj2.id, bm.id)
        self.assertEqual(type(obj2), BaseModel)


if __name__ == '__main__':
    unittest.main()
