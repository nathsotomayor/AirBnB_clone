#!/usr/bin/python3
""" Create console 0.0.1 """

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User 
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
        print()
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
            print("** class name missing")
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
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) in dic:
            print(dic["{}.{}".format(arg[0], arg[1])])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """ Deletes an instance based an the class name. """
        args = shlex.split(args)
        dic = storage.all()
        if not args:
            print("** class name missing **")
        elif not arg[0] in self.__class_name:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) in dic:
            dic.pop("{}.{}".format(arg[0], arg[1]))
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """ Prints all string representation of all
            instances based or not on the class name
        """
        dic = storage.all().values()
        print_all = []
        if not arg or arg in self.__class_name:
            print_all = [str(value) for value in dic]
            print(print_all)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """ Updates an instance based on the class name
            and id by adding or updating attribute and save it
        """
        args = shlex.split(args)
        dic = storage.all()
        if not args:
            print("** class name missing **")
        elif not arg[0] in self.__class_name:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif not "{}.{}".format(arg[0], arg[1]) in dic:
            print("** no instance found **")
        elif len(arg) == 2:
            print("** attribute name missing **")
        elif len(arg) == 3:
            print("** value missing **")
        elif "{}.{}".format(arg[0], arg[1]) in dic:
            key = dic["{}.{}".format(arg[0], arg[1])]
            if arg[3].isdigit():
                arg3_int = int(arg[3])
                setattr(key, arg[2], arg3_int)
            elif ".com" in arg[3]:
                arg3_str = str(arg[3])
                setattr(key, arg[2], arg3_str.strip("\""))
            elif arg[3].isnumeric and "." in arg[3]:
                arg3_float = float(arg[3])
                setattr(key, arg[2], arg3_float)
            key.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
