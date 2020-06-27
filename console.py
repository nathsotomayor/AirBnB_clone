#!/usr/bin/python3
""" Create console 0.0.1 """

import cmd


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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
