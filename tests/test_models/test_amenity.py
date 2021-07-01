#!/usr/bin/python3
"""This file contains
test of amenity"""
import unittest
import pep8
import os
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """Test for the Amenity class"""
    def test_amenity_pep8(self):
        """Verify pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        resultado = pep8style.check_files(["./models/amenity.py"])
        self.assertEqual(resultado.total_errors, 0)
