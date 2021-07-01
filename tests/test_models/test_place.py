#!/usr/bin/python3
"""This file contains
test of place"""
import unittest
import pep8
import os
from datetime import datetime


class TestPlace(unittest.TestCase):
    """Test for the Place class"""
    def test_place_pep8(self):
        """Verify pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        resultado = pep8style.check_files(["./models/place.py"])
        self.assertEqual(resultado.total_errors, 0)
