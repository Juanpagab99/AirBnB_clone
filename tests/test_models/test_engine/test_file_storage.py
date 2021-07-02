#!/usr/bin/python3
"""This file contains
test of user"""
import unittest
import pep8
import os
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    """Test for the FileStorage class"""
    def test_file_storage_pep8(self):
        """Verify pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        resultado = pep8style.check_files(["./models/engine/file_storage.py"])
        self.assertEqual(resultado.total_errors, 0)
