#!/usr/bin/python3
""" Unittest for Place class module """
import models
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """ Testing class """

    def test_isinstance(self):
        """ Test instance of Place class """
        new_instance = Place()
        self.assertIsInstance(new_instance, Place)

    def test_docstring(self):
        """ Test docstring in module, class and function """
        self.assertTrue(len(Place.__doc__) > 0)
        for funct in dir(Place):
            self.assertTrue(len(funct.__doc__) > 0)
