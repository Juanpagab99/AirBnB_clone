#!/usr/bin/python3
"""This file contains the
console.py with cmd"""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNB command interpreter"""
    prompt = "(hbnb) "

    def do_EOF(self, args):
        """Clean method to logs out
        the terminal"""
        return True

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """"Emptyline"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
