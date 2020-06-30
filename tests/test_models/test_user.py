#!/usr/bin/python3
""" Unittest for User class module """
import models
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """ Testing class """

    def test_isinstance(self):
        """ Test instance of User class """
        new_instance = User()
        self.assertIsInstance(new_instance, User)
