#!/usr/bin/python3
"""This file contains
test of state"""
import unittest
import pep8
import os
from datetime import datetime


class TestState(unittest.TestCase):
    """Test for the State class"""
    def test_state_pep8(self):
        """Verify pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        resultado = pep8style.check_files(["./models/state.py"])
        self.assertEqual(resultado.total_errors, 0)
