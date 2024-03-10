#!/usr/bin/python3
"""
Console module for HBNB project
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for the command interpreter
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        return True

    def emptyline(self):
        """
        Do nothing on empty input line
        """
        pass

    def help_quit(self):
        """
        Help message for quit command
        """
        print("Quit command to exit the program")

    def help_EOF(self):
        """
        Help message for EOF command
        """
        print("EOF command to exit the program")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

