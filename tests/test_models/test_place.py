#!/usr/bin/python3
""" Unittest for Place class module """
import models
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """ Testing class """

    def test_isinstance(self):
        """ Test instance of User class """
        new_instance = Place()
        self.assertIsInstance(new_instance, Place)
