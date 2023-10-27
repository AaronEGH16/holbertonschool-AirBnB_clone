#!/usr/bin/python3
"""this module contains user console of AirBnB proyect
"""
from ctypes import cast
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
        - update (updates a class attribute value)
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
            class_dict = models.FileStorage.objclass
            if args[0] in class_dict:
                new_obj = class_dict[args[0]]()
                new_obj.save()
                print(new_obj.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, *args):
        """Prints the string representation of an instance
        based on the class name and id
        """
        args = args[0].split()
        try:
            obj_cls = args[0]
            class_dict = models.FileStorage.objclass
            if obj_cls in class_dict:
                try:
                    obj_id = args[1]
                    obj = (models.FileStorage()).all()
                    try:
                        print(obj[f"{obj_cls}.{obj_id}"])
                    except:
                        print("** no instance found **")
                except:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        except:
            print("** class name missing **")

    def do_destroy(self, *args):
        """Deletes an instance based on the class name and id
        """
        args = args[0].split()
        try:
            obj_cls = args[0]
            class_dict = models.FileStorage.objclass
            if obj_cls in class_dict:
                try:
                    obj_id = args[1]
                    obj = (models.FileStorage()).all()
                    try:
                        del obj[f"{obj_cls}.{obj_id}"]
                        models.storage.save()
                    except:
                        print("** no instance found **")
                except:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        except:
            print("** class name missing **")

    def do_all(self, *args):
        """Prints all string representation of all
        instances based or not on the class name
        """
        all_obj = (models.FileStorage()).all()
        if args[0]:
            args = args[0].split()
            obj_cls = args[0]
            class_dict = models.FileStorage.objclass
            if obj_cls in class_dict:
                for key, object in all_obj.items():
                    if object.__class__.__name__ == obj_cls:
                        print(all_obj[key])
            else:
                print("** class doesn't exist **")
        else:
            for key in all_obj.keys():
                print(all_obj[key])

    def do_update(self, *args):
        """Updates an instance based on the class
        name and id by adding or updating attribute
        ej: update <class name> <id> <attribute name> "<attribute value>"
        """
        if args[0]:
            args = args[0].split()
            obj_cls = args[0]
            class_dict = models.FileStorage.objclass
            if obj_cls in class_dict:
                try:
                    id = args[1]
                    all_obj = (models.FileStorage()).all()
                    try:
                        obj = all_obj[f"{args[0]}.{id}"]
                        try:
                            att = args[2]
                            try:
                                val = args[3].strip("'")
                                val = val.strip('"')
                                setattr(obj, att, val)
                                obj.save()
                            except:
                                print("** value missing **")
                        except:
                            print("** attribute name missing **")
                    except:
                        print("** no instance found **")
                except:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
