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
                names = re.findall('^[a-z]+|[A-Z][^A-Z]*', arg)
                if len(names) > 1:
                    lower_names = []
                    for name in names:
                        lower_names.append(name.lower())
                    class_name = "_".join(lower_names)
                else:
                    class_name = arg.lower()
                mod_name = "models." + class_name
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
                if len(args) >= 2:
                    key = f"{args[0]}.{args[1]}"
                    if key in obj_dict.keys():
                        obj = obj_dict[key]
                        print(obj)
                    else:
                        print(f"** no instance found **")
                elif len(args) == 1:
                    print(f"** instance id missing **")
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
                if len(args) >= 2:
                    key = f"{args[0]}.{args[1]}"
                    if key in obj_dict.keys():
                        del obj_dict[key]
                        storage.modify_objects(obj_dict)
                    else:
                        print(f"** no instance found **")
                elif len(args) == 1:
                    print(f"** instance id missing **")
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
        ls = []
        if arg:
            if arg in type(self).__class_list:
                for key, val in obj_dict.items():
                    if type(val).__name__ == arg:
                        ls.append(str(val))
            else:
                print(f"** class doesn't exist **")
        else:
            for key, val in obj_dict.items():
                ls.append(str(val))
        if ls:
            print(ls)

    def do_update(self, arg):
        """
        Update command  in instance based on class name and id
        by adding or updating attribute
        """

        all_dicts = storage.all()
        if arg:
            args = arg.split(" ")
            if len(args) >= 2:
                key = f"{args[0]}.{args[1]}"
            else:
                key = ""
            if len(args) == 1 and args == "":
                print(f"** class name missing **")
            elif args[0] not in type(self).__class_list:
                print(f"** class doesn't exist **")
            elif len(args) == 1 and args[0] in type(self).__class_list:
                print(f"** instance id missing **")
            elif len(args) >= 2 and key not in all_dicts.keys():
                print(f"** no instance found **")
            elif len(args) == 2 and key in all_dicts.keys():
                print(f"** attribute name missing **")
            elif len(args) == 3 and key in all_dicts.keys():
                print(f"** value missing **")
            else:
                if args[3].startswith('"'):
                    args[3] = args[3].lstrip('"')
                    args[3] = args[3].rstrip('"')
                    value = args[3]
                else:
                    try:
                        value = int(args[3])
                    except ValueError:
                        try:
                            value = float(args[3])
                        except ValueError:
                            value = str(args[3])
                obj = all_dicts[key]
                setattr(obj, args[2], value)
                all_dicts[key] = obj
                storage.modify_objects(all_dicts)
        else:
            print(f"** class name missing **")

    def default(self, line):
        """Called on an input line when the command prefix is not recognized.
           In that case we execute the line as Python code.
        """

        commands = ["all()", "count()", "show(id)", "destroy(id)",
                    "update(id, name, value)", "update(id, dict)"]
        obj_dict = storage.all()
        try:
            args = line.split(".")
            if args[0] in type(self).__class_list:
                if args[1] in commands and args[1] == "all()":
                    type(self).all_helper(obj_dict, args)
                elif args[1] in commands and args[1] == "count()":
                    ls = []
                    for key, val in obj_dict.items():
                        if type(val).__name__ == args[0]:
                            ls.append(val)
                elif args[1].startswith("show"):
                    class_id = args[1].split('"')[1]
                    full_key = f"{args[0]}" + " " + class_id
                    self.do_show(full_key)
                elif args[1].startswith("destroy"):
                    class_id = args[1].split('"')[1]
                    full_key = f"{args[0]}" + " " + class_id
                    self.do_destroy(full_key)
                elif args[1].startswith("update"):
                    identifiers = args[1].split('"')
                    class_id = identifiers[1]
                    dict_or_no = identifiers[2]
                    if dict_or_no == ",":
                        self.update_helper(args, identifiers)
                    else:
                        identifiers = args[1].split(" ")
                        self.update_helper_d(args, class_id, identifiers)
        except Exception as e:
            print(e.__class__, ":", e)

    @staticmethod
    def all_helper(obj_dict, args):
        """
        Helper function for <class_name>.all() default function
        """

        ls = []
        for key, val in obj_dict.items():
            if type(val).__name__ == args[0]:
                ls.append(val)
                print("[", end="")
                for i in range(len(ls)):
                    print(ls[i], end="")
                    if i < len(ls) - 1:
                        print(",", end="")
                print("]")

    def update_helper(self, args, identifiers):
        """
        Update helper without dictionary
        """

        class_id = identifiers[1]
        name = identifiers[3]
        value = identifiers[5]
        print(f"{class_id} {name} {value}")
        key = f"{args[0]}" + " " + class_id
        full_arg = key + " " + name + " " + value
        print(full_arg)
        self.do_update(full_arg)

    def update_helper_d(self, args, class_id, identifiers):
        """
        helper function to help update dictionary
        """

        names = []
        for i in range(1, len(identifiers)):
            if identifiers[i].startswith("{"):
                if identifiers[i].endswith(":"):
                    name = identifiers[i].lstrip("{")
                    name = name.rstrip(":")
                    names.append(name)
            elif identifiers[i].endswith("})"):
                names.append(identifiers[i].rstrip("})"))
            elif identifiers[i].endswith(":"):
                names.append(identifiers[i].rstrip(":"))
            else:
                names.append(identifiers[i])
        key = f"{args[0]}" + " " + class_id
        for i in range(0, len(names), 2):
            full_arg = key + " " + names[i] + " " + names[i+1]
            self.do_update(full_arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
