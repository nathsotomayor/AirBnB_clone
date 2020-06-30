#!/usr/bin/python3
""" Unittest for City class module """
import models
import unittest
from models.city import City 


class TestCity(unittest.TestCase):
    """ Testing class """

    def test_isinstance(self):
        """ Test instance of User class """
        new_instance = City()
        self.assertIsInstance(new_instance, City)
