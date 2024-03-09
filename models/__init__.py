#!/usr/bin/python3
"""Module imports file_storage.py"""

from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
