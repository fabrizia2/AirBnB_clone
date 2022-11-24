#!/usr/bin/python3
"""The console that contains the entry point of the command interpreter"""
import cmd


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

    def emptyLine(self):
        """
        overrides the ENTER and empty line
       """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
