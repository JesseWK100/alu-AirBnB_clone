#!/usr/bin/env python3

"""
Entry point of the command interpreter for the HBNB project.
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

# Dictionary of allowed classes
classes = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review
}

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for HBNB project.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF signal."""
        print("")
        return True

    def emptyline(self):
        """Do nothing on an empty line input."""
        pass

    def do_create(self, arg):
        """
        Create a new instance of a class, saves it, and prints its id.
        Usage: create <class_name>
        """
        if not arg:
            print("** class name missing **")
            return
        if arg not in classes:
            print("** class doesn't exist **")
            return

        obj = classes[arg]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """
        Show the string representation of an instance.
        Usage: show <class_name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Destroy an instance based on its class name and id.
        Usage: destroy <class_name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """
        Show all instances, or all instances of a specific class.
        Usage: all [<class_name>]
        """
        if arg and arg not in classes:
            print("** class doesn't exist **")
            return

        objects = [
            str(obj) for key, obj in storage.all().items()
            if not arg or key.startswith(arg)
        ]
        print(objects)

    def do_update(self, arg):
        """
        Update an instance by adding or updating an attribute.
        Usage: update <class_name> <id> <attribute_name> <attribute_value>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        obj = storage.all()[key]
        attr_name = args[2]
        attr_value = args[3]

        try:
            attr_value = eval(attr_value)  # Convert to proper type if possible
        except (SyntaxError, NameError):
            pass  # Keep as string if evaluation fails

        setattr(obj, attr_name, attr_value)
        obj.save()

    def do_count(self, arg):
        """
        Count the number of instances of a specific class.
        Usage: count <class_name>
        """
        if not arg:
            print("** class name missing **")
            return
        if arg not in classes:
            print("** class doesn't exist **")
            return

        count = sum(1 for key in storage.all() if key.startswith(f"{arg}."))
        print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
