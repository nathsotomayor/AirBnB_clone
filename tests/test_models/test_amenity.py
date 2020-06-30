#!/usr/bin/python3
""" Unittest for Amenity class module """
import models
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ Testing class """

    def test_isinstance(self):
        """ Test instance of Amenity class """
        new_instance = Amenity()
        self.assertIsInstance(new_instance, Amenity)

    def test_docstring(self):
        """ Test docstring in module, class and function """
        self.assertTrue(len(amenity.__doc__) > 0)
        self.assertTrue(len(Amenity.__doc__) > 0)
        for funct in dir(Amenity):
            self.assertTrue(len(funct.__doc__) > 0)
