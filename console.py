#!/usr/bin/python3
""" Create console 0.0.1 """

import cmd
import shlex
from models import storage
from models.city import City
from models.user import User
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """ Define methods to the console """
    prompt = "(hbnb) "
    __class_name = (
        "BaseModel",
        "Amenity",
        "Review",
        "State",
        "Place",
        "User",
        "City",
    )

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """Ctrl-D to exit the program"""
        return True

    def emptyline(self):
        """This instruction shouldn't execute anything"""
        pass

    def do_create(self, args):
        """ Creates a new instance of BaseModel,
            saves it and print the id.
        """
        args = shlex.split(args)
        if args[0] in self.__class_name:
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)
        elif not args:
            print("** class name missing **")
        elif not args[0] in self.__class_name:
            print("** class doesn't exist **")

    def do_show(self, args):
        """ Prints the string representation of
            an instance based an the class name.
        """
        args = shlex.split(args)
        dic = storage.all()
        if not args:
            print("** class name missing **")
        elif not args[0] in self.__class_name:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) in dic:
            print(dic["{}.{}".format(args[0], args[1])])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """ Deletes an instance based an the class name. """
        args = shlex.split(args)
        dic = storage.all()
        if not args:
            print("** class name missing **")
        elif not args[0] in self.__class_name:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) in dic:
            dic.pop("{}.{}".format(args[0], args[1]))
            storage.save()
            storage.reload()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """ Prints all string representation of all
            instances based or not on the class name
        """
        args = shlex.split(args)
        dic = storage.all()
        print_all = []
        if args == []:
            print_all = [str(value) for value in dic.values()]
            print(print_all)
        elif args[0] in self.__class_name:
            for k, v in dic.items():
                if v.__class__.__name__ == args[0]:
                    print_all.append(v.__str__())
            print(print_all)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """ Updates an instance based on the class name
            and id by adding or updating attribute and save it
        """
        args = args.split(" ")
        dic = storage.all()
        if not args:
            print("** class name missing **")
        elif not args[0] in self.__class_name:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif not "{}.{}".format(args[0], args[1]) in dic:
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        elif "{}.{}".format(args[0], args[1]) in dic:
            key = dic["{}.{}".format(args[0], args[1])]
            setattr(key, args[2], args[3].strip("\""))
            key.save()
            storage.reload()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
