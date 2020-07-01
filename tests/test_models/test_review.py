#!/usr/bin/python3
""" Unittest for Review class module """
import os
import pep8
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """ Testing class """
    def test_pep8(self):
        """ pep8 unittest
        """
        style = pep8.StyleGuide(quiet=True)
        file1_path = 'models/review.py'
        file2_path = 'tests/test_models/test_review.py'
        checking = style.check_files((file1_path, file2_path))
        mess = "Found code style errors (and warning)."
        self.assertEqual(checking.total_errors, 0, mess)

    def test_isinstance(self):
        """ Test instance of Review class """
        new_instance = Review()
        self.assertIsInstance(new_instance, Review)

    def test_docstring(self):
        """ Test docstring in module, class and function """
        self.assertTrue(len(Review.__doc__) > 0)
        for funct in dir(Review):
            self.assertTrue(len(funct.__doc__) > 0)

    def test_permissions(self):
        """ Test for validate the permissions """
        read = os.access('models/review.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/review.py', os.W_OK)
        self.assertTrue(write)
        exe = os.access('models/review.py', os.X_OK)
        self.assertTrue(exe)
