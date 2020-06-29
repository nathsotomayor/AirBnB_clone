#!/usr/bin/python3
""" Create User class inherits from BaseModel class """

from models.base_model import BaseModel


class User(BaseModel):
    """ Defines all common attributes/methods for other classes """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
