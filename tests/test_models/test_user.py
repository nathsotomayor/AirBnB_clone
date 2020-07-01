#!/usr/bin/python3
""" Unittest for User class module """
import os
import pep8
import models
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ Testing class """
    def test_pep8(self):
        """ pep8 unittest
        """
        style = pep8.StyleGuide(quiet=True)
        file1_path = 'models/user.py'
        file2_path = 'tests/test_models/test_user.py'
        checking = style.check_files((file1_path, file2_path))
        mess = "Found code style errors (and warning)."
        self.assertEqual(checking.total_errors, 0, mess)

    def test_isinstance(self):
        """ Test instance of User class """
        new_instance = User()
        self.assertIsInstance(new_instance, User)

    def test_id(self):
        """ Check if user has id attribute
            inherite from BaseModel
        """
        user = User()
        self.assertTrue(hasattr(user, 'id'))

    def test_id_str(self):
        """ Check if id is string
        """
        user = User()
        self.assertIsInstance(user.id, str)

    def test_unique_id(self):
        """ Checking if user has a unique ID
        """
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_attr_set(self):
        """ Cheking if user class has
            attributes inizialice
        """
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")
        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")

    def test_permissions(self):
        """ Test for validate the permissions """
        read = os.access('models/user.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/user.py', os.W_OK)
        self.assertTrue(write)
        exe = os.access('models/user.py', os.X_OK)
        self.assertTrue(exe)
