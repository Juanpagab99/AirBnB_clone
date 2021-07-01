#!/usr/bin/python3
"""This file contains
test of city"""
import unittest
import pep8
import os
from datetime import datetime


class TestCity(unittest.TestCase):
    """Test for the City class"""
    def test_city_pep8(self):
        """Verify pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        resultado = pep8style.check_files(["./models/city.py"])
        self.assertEqual(resultado.total_errors, 0)
