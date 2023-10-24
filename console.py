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
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit: Command to close the console"""
        return True

    def do_EOF(self, args):
        """EOF: Close console when user calls EOF (End Of File)"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
