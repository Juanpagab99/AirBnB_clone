#!/usr/bin/python3
"""This file contains the
console.py with cmd"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import shlex
from models.user import User
from models import state
from models import city
from models import amenity
from models import review
from models import place
classes = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review
}


class HBNBCommand(cmd.Cmd):
    """HBNB command interpreter"""
    prompt = "(hbnb) "

    def do_EOF(self, args):
        """Clean method to logs out
        the terminal"""
        return True

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """"Emptyline"""
        pass

    def do_create(self, args):
        """Creates a new instance"""
        if args:
            if args in classes:
                class_to_ins = classes.get(args)
                new_instance = class_to_ins()
                new_instance.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, args):
        """Prints the string
        representation"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        else:
            if len(args) > 1:
                key = "{}.{}".format(args[0], args[1])
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")

    def do_destroy(self, args):
        """Deletes an instance"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        else:
            if len(args) > 1:
                key = "{}.{}".format(args[0], args[1])
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                    return
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")

    def do_all(self, args):
        """Prints all the
        string representations of
        all instance"""
        args = args.split()
        list1 = []
        dict1 = storage.all()
        if len(args) < 1:
            for value in dict1.keys():
                obj = dict1[value]
                list1.append("{}".format(obj))
            print(list1)
        else:
            if args[0] in classes:
                for id_o in dict1.keys():
                    if args[0] in id_o:
                        obj = dict1[id_o]
                        list1.append("{}".format(obj))
                print(list1)
            else:
                print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an intance
        based on the class name
        and id"""
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj = storage.find_object(args[1])
        if obj:
            if len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                setattr(obj, args[2], args[3])
                storage.save()
        else:
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
