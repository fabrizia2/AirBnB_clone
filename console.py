#!/usr/bin/python3
"""The console that contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """
        exits the program
        """
        return True

    def do_EOF(self, arg):
        """
        exits the program
       """
        print("")
        return True

    def emptyline(self):
        """
        overrides the ENTER and empty line
       """
        pass

    def do_create(self, arg):
        if arg == "BaseModel":
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
