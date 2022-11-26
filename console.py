#!/usr/bin/python3
"""The script that contains the entry point of the command interpreter"""
import cmd
import importlib
import re
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    A class that defines the commmand interpreter
    forming basis of AirBnb console
    """

    prompt = '(hbnb) '
    __file_path = 'file.json'
    __class_list = ["BaseModel", "User", "Place", "State",
                    "City", "Amenity", "Review"]

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """

        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """

        print("")
        return True

    def emptyline(self):
        """
        Overrides the ENTER and empty line to do nothing
        """

        pass

    def do_create(self, arg):
        """
        Create command to instatiate a new object of BaseModel, saves it to
        JSON file and prints the id. Also does error handling when called
        incorrectly
        """

        if arg:
            if arg in type(self).__class_list:
                names = names = re.findall('^[a-z]+|[A-Z][^A-Z]*', arg)
                if len(names) > 1:
                    lower_names = []
                    for name in names:
                        lower_names.append(name.lower())
                    class_name = "_".join(lower_names)
                else:
                    class_name = arg.lower()
                mod_name = "models." + class_name
                print(mod_name)
                class_mod = importlib.import_module(mod_name)
                class_ = getattr(class_mod, arg)
                new_instance = class_()
                new_instance.save()
                print(new_instance.id)
            else:
                print(f"** class doesn't exist **")
        else:
            print(f"** class name missing **")

    def do_show(self, arg):
        """
        Show command that prints string representation of an instance based
        on class name and id and handles errors
        """

        obj_dict = storage.all()
        if arg:
            args = arg.split(" ")
            if args[0] in type(self).__class_list:
                if len(args) == 2:
                    key = f"{args[0]}.{args[1]}"
                    if key in obj_dict.keys():
                        obj = obj_dict[key]
                        print(obj)
                    else:
                        print(f"** no instance found **")
                elif len(args) == 1:
                    print(f"** instance id missig **")
            else:
                print(f"** class doesn't exist **")
        else:
            print(f"** class name missing **")

    def do_destroy(self, arg):
        """
        Destroy command that deletes an instance based
        on class name and id and handles errors
        """

        obj_dict = storage.all()
        if arg:
            args = arg.split(" ")
            if args[0] in type(self).__class_list:
                if len(args) == 2:
                    key = f"{args[0]}.{args[1]}"
                    if key in obj_dict.keys():
                        del obj_dict[key]
                        storage.modify_objects(obj_dict)
                    else:
                        print(f"** no instance found **")
                elif len(args) == 1:
                    print(f"** instance id missig **")
            else:
                print(f"** class doesn't exist **")
        else:
            print(f"** class name missing **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based on class name
        or no class name
        """

        obj_dict = storage.all()
        if arg:
            print(arg)
            if arg in type(self).__class_list:
                for key, val in obj_dict.items():
                    if type(val).__name__ == arg:
                        print(val)
            else:
                print(f"** class doesn't exist **")
        else:
            for key, val in obj_dict.items():
                print(val)

    def do_update(self, arg):
        """
        Update command  in instance based on class name and id
        by adding or updating attribute
        """

        all_dicts = storage.all()
        args = arg.split(" ")
        key = f"{args[0]}.{args[1]}"
        if len(args) == 1 and args == "":
            print(f"** class name missing **")
        elif len(args) == 1 and args not in type(self).__class_list:
            print(f"** class doesn't exist **")
        elif len(args) == 1 and args in type(self).__class_list:
            printf(f"** instance id missing **")
        elif len(args) >= 2 and key not in all_dicts.keys():
            print(f"** no instance found **")
        elif len(args) == 2 and key in all_dicts.keys():
            print(f"** attribute name missing **")
        elif len(args) == 3 and key in all_dicts.keys():
            print(f"** value mising **")
        else:
            print(args)
            if args[3].startswith('"'):
                args[3] = args[3].lstrip('"')
                args[3] = args[3].rstrip('"')
                value = args[3]
            else:
                try:
                    value = int(args[3])
                except ValueError:
                    value = float(args[3])
            obj = all_dicts[key]
            setattr(obj, args[2], value)
            all_dicts[key] = obj
            storage.modify_objects(all_dicts)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
