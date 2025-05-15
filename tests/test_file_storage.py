#!/usr/bin/env python3
"""
Unittest for models.engine.file_storage
"""
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage engine."""

    def setUp(self):
        """Prepare storage and backup existing file path."""
        self.storage = FileStorage()
        self.file_path = FileStorage._FileStorage__file_path
        # Backup any existing storage file to avoid side effects
        if os.path.exists(self.file_path):
            os.rename(self.file_path, self.file_path + '.bak')

    def tearDown(self):
        """Clean up storage file and restore backup."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        if os.path.exists(self.file_path + '.bak'):
            os.rename(self.file_path + '.bak', self.file_path)

    def test_docstrings(self):
        """Test presence of docstrings in FileStorage and its methods."""
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_all_initially_empty(self):
        """all() should return an empty dict initially."""
        result = self.storage.all()
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 0)

    def test_new_and_all(self):
        """Test that new() registers object in storage."""
        bm = BaseModel()
        key = f"BaseModel.{bm.id}"
        self.storage.new(bm)
        objs = self.storage.all()
        self.assertIn(key, objs)
        self.assertIs(objs[key], bm)

    def test_save_writes_file(self):
        """Test save() writes a JSON file with correct content."""
        bm = BaseModel()
        key = f"BaseModel.{bm.id}"
        self.storage.new(bm)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))
        with open(self.file_path, 'r') as f:
            data = json.load(f)
        self.assertIn(key, data)
        self.assertIsInstance(data[key], dict)

    def test_reload_restores_objects(self):
        """Test reload() loads objects back into storage."""
        bm = BaseModel()
        key = f"BaseModel.{bm.id}"
        self.storage.new(bm)
        self.storage.save()
        # Clear current objects and reload from file
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        objs = self.storage.all()
        self.assertIn(key, objs)
        obj2 = objs[key]
        self.assertEqual(obj2.id, bm.id)
        self.assertIsInstance(obj2, BaseModel)


if __name__ == '__main__':
    unittest.main()
```python
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
