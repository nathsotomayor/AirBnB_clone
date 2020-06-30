#!/usr/bin/python3
""" Unittest for State  class module """
import models
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """ Testing class """

    def test_isinstance(self):
        """ Test instance of User class """
        new_instance = State()
        self.assertIsInstance(new_instance, State)
