#!/usr/bin/python3
"""This file contains
test of review"""
import unittest
import pep8
import os
from datetime import datetime


class TestReview(unittest.TestCase):
    """Test for the Review class"""
    def test_review_pep8(self):
        """Verify pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        resultado = pep8style.check_files(["./models/review.py"])
        self.assertEqual(resultado.total_errors, 0)
