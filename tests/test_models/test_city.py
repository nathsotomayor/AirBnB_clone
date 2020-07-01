#!/usr/bin/python3
""" Unittest for City class module """
import os
import pep8
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """ Testing class """
    def test_pep8(self):
        """ pep8 unittest
        """
        style = pep8.StyleGuide(quiet=True)
        file1_path = 'models/city.py'
        file2_path = 'tests/test_models/test_city.py'
        checking = style.check_files((file1_path, file2_path))
        mess = "Found code style errors (and warning)."
        self.assertEqual(checking.total_errors, 0, mess)

    def test_isinstance(self):
        """ Test instance of City class """
        new_instance = City()
        self.assertIsInstance(new_instance, City)

    def test_docstring(self):
        """ Test docstring in module, class and function """
        self.assertTrue(len(City.__doc__) > 0)
        for funct in dir(City):
            self.assertTrue(len(funct.__doc__) > 0)

    def test_permissions(self):
        """ Test for validate the permissions """
        read = os.access('models/city.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/city.py', os.W_OK)
        self.assertTrue(write)
        exe = os.access('models/city.py', os.X_OK)
        self.assertTrue(exe)
