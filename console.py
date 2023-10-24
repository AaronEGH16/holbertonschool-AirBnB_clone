#!/usr/bin/python3
"""this module contains user console of AirBnB proyect
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand (console comands):
        - help (default)
        - quit (EXIT)
        - EOF (EXIT)
    """
    prompt = "(hbnb)"

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Exit the program when user calls EOF"""
        print()
        return True

    def emptyline(self):
        """This method ensures that the last cmd
        is not repeated when a line is left blank."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
