#!/usr/bin/python3
""" Unittest for Amenity class module """
import models
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ Testing class """

    def test_isinstance(self):
        """ Test instance of User class """
        new_instance = Amenity()
        self.assertIsInstance(new_instance, Amenity)
