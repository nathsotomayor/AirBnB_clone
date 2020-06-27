#!/usr/bin/python3
""" Create console 0.0.1 """

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Define methods to the console """
    prompt = "(hbnb) "

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
        new_instance = BaseModel()
        if args == type(new_instance).__name__:
            new_instance.save()
            print(new_instance.id)
        elif not args:
            print("** class name missing")
        elif args != type(new_instance).__name__:
            print("** class doesn't exist **")

    def do_show(self, args):
        """ Prints the string representation of
            an instance based an the class name.
        """
        arg = args.split(" ")
        dic = storage.all()
        if not args:
            print("** class name missing **")
        elif arg[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) in dic:
            print(dic["{}.{}".format(arg[0], arg[1])])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """ Deletes an instance based an the class name. """
        arg = args.split(" ")
        dic = storage.all()
        if not args:
            print("** class name missing **")
        elif arg[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) in dic:
            dic.pop("{}.{}".format(arg[0], arg[1]))
            storage.save()
        else:
            print("** no instance found **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
