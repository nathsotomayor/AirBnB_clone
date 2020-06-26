#!/usr/bin/python3
""" Create BaseModel class """

from uuid import uuid4
from datetime import datetime


class BaseModel():
    """ Defines all common attributes/methods for other classes """

    def __init__(self):
        """ Define constructor """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """String representation"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates instance 'update_at' with the current time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary with all keys/values of __dict__"""
        cp_dict = self.__dict__.copy()
        cp_dict["__class__"] = self.__class__.__name__
        cp_dict["created_at"] = self.created_at.isoformat()
        cp_dict["updated_at"] = self.updated_at.isoformat()
        return cp_dict
