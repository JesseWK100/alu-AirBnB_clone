#!/usr/bin/env python3

"""
Initialize storage instance for models package.
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
