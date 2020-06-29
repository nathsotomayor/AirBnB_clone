#!/usr/bin/python3
""" Create console 0.0.1 """

import cmd
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


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

    def do_all(self, arg):
        """ Prints all string representation of all
            instances based or not on the class name
        """
        dic = storage.all().values()
        print_all = []
        if not arg or arg == "BaseModel":
            print_all = [str(value) for value in dic]
            print(print_all)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        # P E N D I N G  complete this method !!!!
        """ Updates an instance based on the class name
            and id by adding or updating attribute and save it
        """
        arg = args.split(" ")
        dic = storage.all()
        if not args:
            print("** class name missing **")
        elif arg[0] != "BaseModel":
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
            elif "." in arg[3] and arg[3].isnumeric:
                arg3_float = float(arg[3])
                setattr(key, arg[2], arg3_float)
            else:
                setattr(key, arg[2], arg[3].strip("\""))
            key.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
