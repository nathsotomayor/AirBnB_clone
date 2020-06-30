#!/usr/bin/python3
""" Unittest for State  class module """
import os
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

    def test_permissions(self):
        """ Test for validate the permissions """
        read = os.access('models/state.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/state.py', os.W_OK)
        self.assertTrue(write)
        exe = os.access('models/state.py', os.X_OK)
        self.assertTrue(exe)
