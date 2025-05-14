#!/usr/bin/python3
"""
Command interpreter for AirBnB clone.
Handles basic commands to manipulate objects.
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for the AirBnB clone project.
    """

    prompt = "(hbnb) "

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        # Add other models here
    }

    def do_quit(self, arg):
        """Quit the command interpreter."""
        return True

    def do_EOF(self, arg):
        """Exit the command interpreter."""
        print()
        return True

    def emptyline(self):
        """Override to do nothing on empty input."""
        pass

    def do_create(self, arg):
        """
        Create a new instance of a given class.
        Usage: create <ClassName>
        """
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return

        new_instance = self.classes[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Show an instance of a given class and id.
        Usage: show <ClassName> <id>
        """
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        instance = storage.all().get(key)
        if not instance:
            print("** no instance found **")
            return

        print(instance)

    # Additional commands like destroy, all, update can go here

if __name__ == '__main__':
    HBNBCommand().cmdloop()
