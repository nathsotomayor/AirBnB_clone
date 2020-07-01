#!/usr/bin/python3
""" Unittest for Place class module """
import os
import pep8
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """ Testing class """
    def test_pep8(self):
        """ pep8 unittest
        """
        style = pep8.StyleGuide(quiet=True)
        file1_path = 'models/place.py'
        file2_path = 'tests/test_models/test_place.py'
        checking = style.check_files((file1_path, file2_path))
        mess = "Found code style errors (and warning)."
        self.assertEqual(checking.total_errors, 0, mess)

    def test_isinstance(self):
        """ Test instance of Place class """
        new_instance = Place()
        self.assertIsInstance(new_instance, Place)

    def test_docstring(self):
        """ Test docstring in module, class and function """
        self.assertTrue(len(Place.__doc__) > 0)
        for funct in dir(Place):
            self.assertTrue(len(funct.__doc__) > 0)

    def test_permissions(self):
        """ Test for validate the permissions """
        read = os.access('models/place.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/place.py', os.W_OK)
        self.assertTrue(write)
        exe = os.access('models/place.py', os.X_OK)
        self.assertTrue(exe)
