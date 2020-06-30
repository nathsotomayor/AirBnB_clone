#!/usr/bin/python3
""" Unittest for Review class module """
import models
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """ Testing class """

    def test_isinstance(self):
        """ Test instance of User class """
        new_instance = Review()
        self.assertIsInstance(new_instance, Review)
