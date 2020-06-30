#!/usr/bin/python3
""" Unittest for User class module """
import models
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ Testing class """

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
