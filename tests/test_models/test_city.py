#!/usr/bin/python3
""" Unittest for City class module """
import models
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """ Testing class """

    def test_isinstance(self):
        """ Test instance of City class """
        new_instance = City()
        self.assertIsInstance(new_instance, City)

    def test_docstring(self):
        """ Test docstring in module, class and function """
        self.assertTrue(len(City.__doc__) > 0)
        for funct in dir(City):
            self.assertTrue(len(funct.__doc__) > 0)
