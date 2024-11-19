#!/usr/bin/python
import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the HBNB project.
    """
    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print("")  # Print a newline for clean exit
        return True

    def emptyline(self):
        """Do nothing on empty input."""
        pass

    def do_create(self, arg):
        """Creates a new instance of a class with optional attributes."""
        args = arg.split(" ", 1)
        if len(args) == 0 or not args[0]:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        kwargs = {}
        if len(args) > 1:
            try:
                key_value_pairs = args[1].split()
                for pair in key_value_pairs:
                    key, value = pair.split("=")
                    if value.startswith('"') and value.endswith('"'):
                        value = value.strip('"').replace('_', ' ')
                    elif '.' in value:
                        value = float(value)
                    else:
                        value = int(value)
                    kwargs[key] = value
            except ValueError:
                print("** invalid parameter format **")
                return
        obj = self.classes[class_name](**kwargs)
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            obj = storage.all().get(key)
            if obj:
                print(obj)
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of all instances, optionally filtered by class name."""
        if arg and arg not in self.classes:
            print("** class doesn't exist **")
        else:
            objs = storage.all()
            obj_list = [
                str(obj) for key, obj in objs.items() if not arg or key.startswith(arg)
            ]
            print(obj_list)

    def do_update(self, arg):
        """Updates an instance by adding or updating an attribute."""
        args = arg.split(" ", 2)
        if len(args) < 2:
            print("** class name missing **")
            return
        class_name, obj_id = args[:2]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        key = f"{class_name}.{obj_id}"
        obj = storage.all().get(key)
        if not obj:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if args[2].startswith("{") and args[2].endswith("}"):
            try:
                attr_dict = json.loads(args[2])
                for attr_name, attr_value in attr_dict.items():
                    if attr_name not in ["id", "created_at", "updated_at"]:
                        if hasattr(obj, attr_name):
                            attr_type = type(getattr(obj, attr_name))
                            setattr(obj, attr_name, attr_type(attr_value))
                        else:
                            setattr(obj, attr_name, attr_value)
                obj.save()
            except json.JSONDecodeError:
                print("** invalid dictionary format **")
        else:
            parts = args[2].split(" ", 1)
            if len(parts) < 2:
                print("** value missing **")
                return
            attr_name, attr_value = parts
            if attr_name in ["id", "created_at", "updated_at"]:
                print(f"** cannot update {attr_name} **")
            else:
                if hasattr(obj, attr_name):
                    attr_type = type(getattr(obj, attr_name))
                    setattr(obj, attr_name, attr_type(attr_value))
                else:
                    setattr(obj, attr_name, attr_value)
                obj.save()

    def default(self, line):
        """Handle advanced syntax like <class name>.all(), <class name>.count(), and <class name>.update()."""
        if '.' not in line:
            print(f"*** Unknown syntax: {line}")
            return
        parts = line.split('.', 1)
        if len(parts) != 2:
            print(f"*** Unknown syntax: {line}")
            return
        class_name, command = parts
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if command == "all()":
            self.do_all(class_name)
        elif command == "count()":
            count = sum(1 for key in storage.all() if key.startswith(class_name))
            print(count)
        elif command.startswith("show(") and command.endswith(")"):
            obj_id = command[5:-1].strip('"')
            self.do_show(f"{class_name} {obj_id}")
        elif command.startswith("destroy(") and command.endswith(")"):
            obj_id = command[8:-1].strip('"')
            self.do_destroy(f"{class_name} {obj_id}")
        elif command.startswith("update(") and command.endswith(")"):
            params = command[7:-1]
            if "{" in params and "}" in params:
                try:
                    obj_id, attr_dict = params.split(",", 1)
                    self.do_update(f"{class_name} {obj_id.strip()} {attr_dict.strip()}")
                except ValueError:
                    print(f"*** Invalid update syntax: {line}")
            else:
                params = params.split(", ")
                if len(params) == 3:
                    obj_id, attr_name, attr_value = params
                    self.do_update(f"{class_name} {obj_id.strip()} {attr_name.strip()} {attr_value.strip()}")
                else:
                    print(f"*** Invalid update syntax: {line}")
        else:
            print(f"*** Unknown syntax: {line}")


if __name__ == "__main__":
    HBNBCommand().cmdloop()