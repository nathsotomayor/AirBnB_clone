#!/usr/bin/python3
""" Unittest for State  class module """
import models
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """ Testing class """

    def test_isinstance(self):
        """ Test instance of State class """
        new_instance = State()
        self.assertIsInstance(new_instance, State)


    def test_docstring(self):
        """ Test docstring in module, class and function """
        self.assertTrue(len(State.__doc__) > 0)
        for funct in dir(State):
            self.assertTrue(len(funct.__doc__) > 0)
