#!/usr/bin/env python
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel}

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it, and prints the id"""
        if not args:
            print("** class name missing **")
            return
        if args not in self.classes:
            print("** class doesn't exist **")
            return
        obj = self.classes[args]()
        obj.save()
        print(obj.id)

    def do_show(self, args):
        """Prints the string representation of an instance based on class name and id"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        obj = storage.all().get(key)
        if obj is None:
            print("** no instance found **")
        else:
            print(obj)

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
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

    def do_all(self, args):
        """Prints all instances, optionally filtered by class name"""
        if args and args not in self.classes:
            print("** class doesn't exist **")
            return
        objects = [
            str(obj) for key, obj in storage.all().items() if not args or key.startswith(args + ".")
        ]
        print(objects)

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding/updating attribute"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        obj = storage.all().get(key)
        if obj is None:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3].strip('"')
        if hasattr(obj, attr_name):
            attr_type = type(getattr(obj, attr_name))
            try:
                attr_value = attr_type(attr_value)
            except ValueError:
                print(f"** value for {attr_name} is not of type {attr_type.__name__} **")
                return
        setattr(obj, attr_name, attr_value)
        obj.save()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit on EOF (Ctrl+D)"""
        return True

    def emptyline(self):
        """Overrides the emptyline behavior to do nothing"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()

