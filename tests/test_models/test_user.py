#!/usr/bin/python3
"""This file contains
test of user"""
import unittest
import pep8
import os
from datetime import datetime


class TestUser(unittest.TestCase):
    """Test for the User class"""
    def test_user_pep8(self):
        """Verify pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        resultado = pep8style.check_files(["./models/user.py"])
        self.assertEqual(resultado.total_errors, 5)
