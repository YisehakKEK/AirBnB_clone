#!/usr/bin/env python
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_create(self, args):
        """Creates a new instance of a class, saves it, and prints the id"""
        if not args:
            print("** class name missing **")
            return
        if args not in self.classes:
            print("** class doesn't exist **")
            return
        obj = self.classes[args]()  # Create an instance of the class
        obj.save()  # Save the instance
        print(obj.id)  # Print the instance's ID

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
            print(obj)  # Print the string representation of the object

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
        del storage.all()[key]  # Delete the instance from storage
        storage.save()  # Save changes to file

    def do_all(self, args):
        """Prints all instances of a class or all instances if no class name is provided"""
        args = args.strip()
        if args:
            if args not in self.classes:
                print("** class doesn't exist **")
                return
            objects = [
                str(obj) for key, obj in storage.all().items() if key.startswith(args + ".")
            ]
        else:
            objects = [str(obj) for key, obj in storage.all().items()]
        print(objects)  # Print all instances

    def do_count(self, args):
        """Prints the number of instances of a class"""
        if not args:
            print("** class name missing **")
            return
        if args not in self.classes:
            print("** class doesn't exist **")
            return
        count = sum(1 for key in storage.all() if key.startswith(args + "."))
        print(count)  # Print the count of instances

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding/updating an attribute"""
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
        obj.save()  # Save changes to instance

    def do_update_from_dict(self, args):
        """Updates an instance based on the class name and id using a dictionary"""
        args = args.split(" ", 2)  # Split into 3 parts: class, dictionary, and id
        if len(args) < 2:
            print("** class name or dictionary missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        try:
            update_dict = eval(args[1])
        except SyntaxError:
            print("** invalid dictionary format **")
            return
        if not isinstance(update_dict, dict):
            print("** dictionary missing **")
            return
        if len(args) < 3:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[2]}"
        obj = storage.all().get(key)
        if obj is None:
            print("** no instance found **")
            return
        for key, value in update_dict.items():
            setattr(obj, key, value)
        obj.save()  # Save updated instance

    def do_quit(self, arg):
        """Quit the command interpreter"""
        print("Exiting... Goodbye!")
        return True

    def do_EOF(self, arg):
        """Exit the command interpreter on EOF (Ctrl+D)"""
        print("Exiting... Goodbye!")
        return True

    def emptyline(self):
        """Overrides the emptyline behavior to do nothing"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()