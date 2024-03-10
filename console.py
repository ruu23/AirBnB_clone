#!/usr/bin/python3
"""
Console module for HBNB project
"""

import cmd
from models.base_model import BaseModel
from models import storage

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
        Do nothing on an empty input line
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

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
        Usage: create <class_name>
        """
        if not arg:
            print("** class name missing **")
        elif arg not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id.
        Usage: show <class_name> <id>
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        Usage: destroy <class_name> <id>
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name.
        Usage: all <class_name> or all
        """
        if arg and arg not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif arg and arg not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
        else:
            instances = [str(value) for key, value in storage.all().items()]
            print(instances)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute.
        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                obj = storage.all()[key]
                setattr(obj, args[2], args[3].strip('"'))
                obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

