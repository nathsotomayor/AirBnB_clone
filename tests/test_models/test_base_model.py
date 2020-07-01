#!/usr/bin/python3
""" Unittest for BaseModel class module """
import os
import pep8
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Testing class"""
    def test_pep8(self):
        """ pep8 unittest
        """
        style = pep8.StyleGuide(quiet=True)
        file1_path = 'models/base_model.py'
        file2_path = 'tests/test_models/test_base_model.py'
        checking = style.check_files((file1_path, file2_path))
        mess = "Found code style errors (and warning)."
        self.assertEqual(checking.total_errors, 0, mess)

    def test_docstring(self):
        """ Test docstring in module, class and function """
        self.assertTrue(len(BaseModel.__doc__) > 0)
        for funct in dir(BaseModel):
            self.assertTrue(len(funct.__doc__) > 0)

    def test_to_dict(self):
        """ Checking if to_dict method is
            returning a dictionary with all
            keys/values of __dict__
        """
        new_ins = BaseModel()
        dic = new_ins.to_dict()
        self.assertIsInstance(dic, dict)
        self.assertTrue(dic["__class__"] == "BaseModel")
        for k, v in dic.items():
            if k == "created_at" and k == "updated_at":
                self.assertIsInstance(v, str)

    def test_isinstance(self):
        """ Test if a object is an instances
            of BaseModel class.
        """
        new_instance = BaseModel()
        self.assertIsInstance(new_instance, BaseModel)

    def test_save(self):
        """ Checking if updated_at is updated with
            the current datetime.
        """
        new_instance1 = BaseModel()
        update = new_instance1.updated_at
        new_instance1.save()
        self.assertNotEqual(update, new_instance1.updated_at)

    def test_ids(self):
        """ Cheking if two new instances have
            differents ids
        """
        new_instance2 = BaseModel()
        new_instance3 = BaseModel()
        id2 = new_instance2.id
        id3 = new_instance3.id
        self.assertNotEqual(id2, id3)

    def test_str_repr(self):
        """ Validating string representation
            format output.
        """
        formt = "[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__)
        self.assertTrue(formt)

    def test_permissions(self):
        """ Test for validate the permissions """
        read = os.access('models/base_model.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/base_model.py', os.W_OK)
        self.assertTrue(write)
        exe = os.access('models/base_model.py', os.X_OK)
        self.assertTrue(exe)
