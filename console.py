#!/usr/bin/python3
"""this module contains user console of AirBnB proyect
"""
from queue import Empty
import models
import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand (console comands):
        - help (default)
        - quit (EXIT)
        - EOF (EXIT)
        - create (new class object)
        - show (show a class object)
        - destroy (del a class object)
        - all (print all instances of class)
    """
    prompt = "(hbnb)"

    def do_quit(self, *args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, *args):
        """Exit the program when user calls EOF"""
        print()
        return True

    def emptyline(self):
        """This method ensures that the last cmd
        is not repeated when a line is left blank."""
        pass

    def do_create(self, *args):
        """Creates a new instance of 'CLASS' passed by arguments"""
        args = args[0].split()
        if not args or args is Empty:
            print("** class name missing **")
        else:
            obj_class = models.FileStorage.objclass
            if args[0] in obj_class:
                new_obj = obj_class[args[0]]()
                new_obj.save()
                print(new_obj.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, *args):
        """Prints the string representation of an instance
        based on the class name and id
        """
        args = args[0].split()
        obj_cls = args[0]
        obj_id = args[1]
        if obj_cls:
            obj_class = models.FileStorage.objclass
            if obj_cls in obj_class:
                if obj_id:
                    obj = (models.FileStorage()).all()
                    try:
                        print(obj[f"{obj_cls}.{obj_id}"])
                    except:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, *args):
        """Deletes an instance based on the class name and id
        """
        args = args[0].split()
        obj_cls = args[0]
        obj_id = args[1]
        if obj_cls:
            obj_class = models.FileStorage.objclass
            if obj_cls in obj_class:
                if obj_id:
                    obj = (models.FileStorage()).all()
                    try:
                        del obj[f"{obj_cls}.{obj_id}"]
                        models.storage.save()
                    except:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, *args):
        """Prints all string representation of all
        instances based or not on the class name
        """
        all_obj = (models.FileStorage()).all()
        if args[0]:
            args = args[0].split()
            obj_cls = args[0]
            if obj_cls:
                obj_class = models.FileStorage.objclass
                if obj_cls in obj_class:
                    for key, object in all_obj.items():
                        if object.__class__.__name__ == obj_cls:
                            print(all_obj[key])
                else:
                    print("** class doesn't exist **")
            else:
                print("** class name missing **")
        else:
            for key in all_obj.keys():
                print(all_obj[key])

if __name__ == '__main__':
    HBNBCommand().cmdloop()
