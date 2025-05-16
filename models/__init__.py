#!/usr/bin/env python3

from models.engine.file_storage import FileStorage

# Create a single instance of FileStorage
storage = FileStorage()

# Reload objects from file
storage.reload()
