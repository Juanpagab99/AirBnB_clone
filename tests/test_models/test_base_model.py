#!/usr/bin/python3
"""This file contains
test of base_model"""
import unittest
import pep8
import os
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test for the BaseModel class"""
    def test_basemodel_pep8(self):
        """Verify pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        resultado = pep8style.check_files(["./models/base_model.py"])
        self.assertEqual(resultado.total_errors, 0)
