#!/usr/bin/python3
""" Unittest for Review class module """
import os
import models
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """ Testing class """

    def test_isinstance(self):
        """ Test instance of Review class """
        new_instance = Review()
        self.assertIsInstance(new_instance, Review)

    def test_docstring(self):
        """ Test docstring in module, class and function """
        self.assertTrue(len(Review.__doc__) > 0)
        for funct in dir(Review):
            self.assertTrue(len(funct.__doc__) > 0)

    def test_permissions(self):
        """ Test for validate the permissions """
        read = os.access('models/review.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/review.py', os.W_OK)
        self.assertTrue(write)
        exe = os.access('models/review.py', os.X_OK)
        self.assertTrue(exe)
