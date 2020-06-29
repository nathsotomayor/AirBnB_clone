#!/usr/bin/python3
""" FileStorage class module """
import json
from os import path
from models.city import City
from models.user import User
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel


class FileStorage:
    """ FileStorage class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary
            __objects
        """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key
            <obj class name>.id
        """
        if obj:
            k = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[k] = obj

    def save(self):
        """ serializes __objects to the
            JSON file (path: __file_path)
        """
        new_dict = {}
        for k, v in self.__objects.items():
            new_dict[k] = v.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(new_dict, file)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file
            (__file_path) exists; otherwise, do nothing. If the file doesn’t
            exist no exception should be raised)
        """
        if not path.exists(self.__file_path):
            pass
        else:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
            for k, v in data.items():
                self.__objects[k] = eval(v["__class__"])(**v)
