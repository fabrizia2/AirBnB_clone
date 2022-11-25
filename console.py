#!/usr/bin/python3
"""The script that contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    A class that defines the commmand interpreter
    forming basis of AirBnb console
    """

    prompt = '(hbnb) '
    __file_path = 'file.json'
    __class_list = ["BaseModel"]

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
            if arg in type(self).class_list:
                new_instance = BaseModel()
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
        print(len(args))
        print(args)
        if len(args) >= 4:
            if arg[0] in type(self).__class_list:
                key = f"{args[0]}.{args[1]}"
                if key in all_dicts.keys():
                    obj_dict = all_dicts[key]
                    obj_dict[args[2]] = args[3]
                    storage.modify_objects(all_dicts)
                else:
                    print(f"** no instance found **")
            else:
                print(f"** class doesn't exist **")
        elif len(args) == 3:
            if arg[0] not in type(self).__class_list:
                print(f"** class doesn't exist **")
            else:
                print(f"** value missing **")
        elif len(args) == 2:
            if arg[0] not in type(self).__class_list:
                print(f"** class doesn't exist **")
            else:
                key = f"{args[0]}.{args[1]}"
                if key in all_dicts.keys():
                    print(f"** attribute name missing **")
                else:
                    print(f"** no instance found **")
        elif len(args) == 1 and args[0] != "":
            if arg[0] not in type(self).__class_list:
                print(f"** class doesn't exist **")
            else:
                print(f"** instance id missing **")
        else:
            print(f"** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
