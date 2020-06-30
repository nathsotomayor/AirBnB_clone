#!/usr/bin/python3
""" Unittest for Review class module """
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
        self.assertTrue(len(review.__doc__) > 0)
        self.assertTrue(len(Review.__doc__) > 0)
        for funct in dir(Review):
            self.assertTrue(len(funct.__doc__) > 0)
