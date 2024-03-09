#!/usr/bin/python3
"""Module contains emtry point of the command interpreter"""

import cmd
import models
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


_cls = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class HBNBCommand(cmd.Cmd):
    """Inherits from Cmd class

    Attributes:
        prompt (str): custom prompt display
    """
    prompt = "(hbnb) "

    def emptyline(self) -> bool:
        """By default, when an empty line is entered,
        last command is repeated.
        This method overrides the default behaviour
        by doing nothing"""
        pass

    def do_create(self, cls_name):
        """Creates a new instance of BaseModel

        Args:
            cls_name (str): Name of class of which instance shoudl be created

        Usage:
            (hbnb) create <class_name>

        Example:
            (hbnb) create BaseModel
        """
        if not cls_name:
            print("** class name missing **")
        if cls_name not in _cls:
            print("** class doesn't exist **")
        else:
            cls = _cls.get(cls_name)
            an_instance = cls()
            an_instance.save()
            print(an_instance.id)

    def do_show(self, instance):
        """PRints the string representation of an instance
        based on the classname

        Args:
            instance (str): Classname and id

        Usage:
            (hbnb) show <class_name> <instance_id>

        Example:
            (hbnb) show BaseModel 1234-1234-1234
        """
        if not instance:
            print("** class name missing **")
        else:
            inst_info = instance.split()
            if len(inst_info) == 1 and inst_info[0] not in _cls.keys():
                print("** class doesn't exist **")
            elif len(inst_info) < 2 and inst_info[0] in _cls.keys():
                print("** instance id missing **")
            else:
                if len(inst_info) == (
                     2) and inst_info[0] in _cls.keys() and inst_info[1]:
                    new_key = f"{inst_info[0]}.{inst_info[1]}"

                    # models.storage.reload()
                    all_obj = models.storage.all()

                    if new_key not in all_obj:
                        print("** no instance found **")
                    else:
                        print(all_obj[new_key])

    def do_destroy(self, instance):
        """Deletes an instance based on the class name and id

        Args:
            instance (str): classname and id

        Usage:
            (hbnb) show <class_name> <instance_id>

        Example:
            (hbnb) destroy BaseModel 1234-1234-1234
        """
        if not instance:
            print("** class name missing **")
        else:
            inst_info = instance.split()
            if len(inst_info) == 1 and inst_info[0] not in _cls.keys():
                print("** class doesn't exist **")
            elif len(inst_info) < 2 and inst_info[0] in _cls.keys():
                print("** instance id missing **")
            else:
                if len(inst_info) == (
                     2) and inst_info[0] in _cls.keys() and inst_info[1]:
                    new_key = f"{inst_info[0]}.{inst_info[1]}"

                    # models.storage.reload()
                    all_obj = models.storage.all()

                    if new_key not in all_obj:
                        print("** no instance found **")
                    else:
                        del models.storage.all()[new_key]
                        models.storage.save()

    def do_all(self, classname):
        """Prints all string representation of all instances
        based or not on the class name

        Usage:
            (hbnb) all <class_name> or all

        Example:
            (hbnb) all BaseModel or all
        """
        all_objs = models.storage.all()
        list_of_str = []

        if not classname:
            for obj in all_objs.values():
                list_of_str.append(str(obj))
        else:
            if classname not in _cls.keys():
                print("** class doesn't exist **")
                return
            else:
                for obj in all_objs.values():
                    if isinstance(obj, _cls[classname]
                                  ) and obj.__class__ is _cls[classname]:
                        list_of_str.append(str(obj))

        print(list_of_str)

    def do_update(self, line):
        """Updates an instance based on the class name and id by
        adding or updating attribute
        Changes will be saved to the JSON file

        Args:
            line (str): containing classname, id, attribute, value

        Usage:
            update <class name> <id> <attribute name> "<attribute value>"

        Example:
            update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """

        if not line:
            print("** class name missing **")
        else:
            line_info = line.split()
            if len(line_info) == 1 and line_info[0] not in _cls.keys():
                print("** class doesn't exist **")
            elif len(line_info) < 2 and line_info[0] in _cls.keys():
                print("** instance id missing **")
            else:
                if len(line_info) >= (
                     2) and line_info[0] in _cls.keys() and line_info[1]:
                    new_key = f"{line_info[0]}.{line_info[1]}"

                    # models.storage.reload()
                    all_obj = models.storage.all()

                    if new_key not in all_obj:
                        print("** no instance found **")
                    else:
                        if not line_info[2]:
                            print("** attribute name missing **")
                        elif line_info[2] and not line_info[3]:
                            print("** value missing **")
                        else:
                            _attr = line_info[2]
                            _val = line_info[3].replace('"', '')

                            setattr(models.storage.all()[new_key], _attr, _val)

                            models.storage.save()

    def default(self, line):
        """To configure command line to take in User.all()
        and print out all User objects

        Args:
            line (str): user input at command line

        Usage:
            (hbnb) <class name>.all()

        Example:
            (hbnb) User.all()
        """
        token = line.split(".")

        if len(token) > 1 and token[0] in _cls:
            list_of_str = []
            all_objs = models.storage.all()
            cls = _cls[token[0]]
            count = 0

            for obj in all_objs.values():
                if isinstance(obj, cls) and obj.__class__ is cls:
                    list_of_str.append(obj.__str__())
                    count += 1

            if token[1] == "all()":
                print(list_of_str)

            elif token[1] == "count()":
                print(count)
                # print(len(models.storage.all()))

            else:

                if "show(" in token[1]:
                    obj_id = token[1][5:-1].replace('"', '')
                    full_id = f"{cls.__name__}.{obj_id}"

                    if full_id in all_objs:
                        print(all_objs[full_id])
                    else:
                        print("** no instance found **")

                elif "destroy(" in token[1]:
                    obj_id = token[1][8:-1].replace('"', '')

                    full_id = f"{cls.__name__} {obj_id}"
                    self.do_destroy(full_id)
                    # if full_id in all_objs:
                    #     print("can find it but cannot destroy")
                    #     del models.storage.__objects[full_id]
                    #     models.storage.save()
                    # else:
                    #     print("** no instance found **")
                elif "update(" in token[1]:
                    obj_token = token[1][7:-1].replace('"', '')
                    obj_token = obj_token.replace(',', '')

                    if all(c in obj_token for c in ("{", ":")):
                        toks = obj_token.replace("{", "").replace(
                            "}", "").replace(":", "").replace("'", "")

                        t_toks = toks.split()

                        full_id = f"{cls.__name__} {t_toks[0]}"

                        update_a = f"{full_id} {t_toks[1]} {t_toks[2]}"
                        update_b = f"{full_id} {t_toks[3]} {t_toks[4]}"

                        self.do_update(update_a)
                        self.do_update(update_b)

                    else:

                        full_id = f"{cls.__name__} {obj_token}"
                        self.do_update(full_id)

    def do_quit(self, line):
        """Implements the quit command to exit program"""
        return True

    def do_EOF(self, line):
        """EOF to exit program using Cntrl+D"""
        return True


if __name__ == "__main__":
    if len(sys.argv) > 1:
        HBNBCommand().onecmd(' '.join(sys.argv[1:]))
        # onecmd takes a string as input, so arguments need
        # to be joined together into one string
    else:
        HBNBCommand().cmdloop()
