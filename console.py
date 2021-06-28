#!/usr/bin/python3
''' The console '''

import cmd
import models
from models.base_model import BaseModel
from shlex import split


classes = {"BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):
    ''' El console '''

    prompt = '(hbnb) '

    ''' quit xd '''
    
    def do_quit(self, line):
        ''' exit console '''
        return True

    '''  EOF '''

    def do_EOF(self, line):
        ''' exit console '''
        return True

    ''' Create '''

    def do_create(self, line):
        '''  Creates a new instance of BaseModel '''
        s = split(line)
        if len(s) < 1:
            print("** class name missing **")
        elif s[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            insta = BaseModel()
            insta.save()
            print(insta.id)

    ''' Show '''
    def do_show(self, line):
        ''' Prints the string representation of an instance based on the class name and id '''
        s = split(line)
        if len(s) == 0:
            print("** class name missing **")
        elif len(s) == 1:
            if s[0] in classes:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            if s[0] not in classes: 
                print("** class doesn't exist **")
            else:
                aux = s[0] + '.' + s[1]
                if str(aux) in models.storage.all():
                    print(models.storage.all()[aux])
                else:
                    print("** no instance found **")

    ''' destroy '''
    def do_destroy(self, line):
        '''' Deletes an instance based on the class name and id '''
        s = split(line)
        if len(s) == 0:
            print("** class name missing **")
        elif len(s) == 1:
            if s[0] in classes:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            if s[0] not in classes:
                print("** class doesn't exist **")
            else:
                aux = s[0] + '.' + s[1]
                if str(aux) in models.storage.all():
                    models.storage.all().pop(aux)
                else:
                    print("** no instance found **")

    ''' show all objects '''

    def do_all(self, line):
        ''' Prints all string representation of all instances based or not on the class name '''
        s = split(line)
        aux = []
        if len(s) == 0:
            for values in models.storage.all().values():
                aux.append(values.__str__())
        elif len(s) == 1:
            if s[0] not in classes:
                print("** class doesn't exist **")
                return
            for key, values in models.storage.all().items():
                temp = key.split('.')
                if temp[0] == s[0]:
                    aux.append(values.__str__())
        print(aux)

    ''' Update '''
    def do_update(self, line):
        ''' Updates an instance based on the class name and id by adding or updating attribute '''
        s = split(line)
        if len(s) == 0:
            print("** class name missing **")
            return
        elif len(s) == 1:
            if s[0] not in classes:
                print("** class doesn't exist **")
                return
            else:
                print("** instance id missing **")
                return
        bol = False
        for key in models.storage.all():
            temp = key.split('.')
            if temp[1] == s[1]:
                bol = True
                break
        if bol == False:
            print("** no instance found **")
            return
        elif len(s) < 3:
            print("** attribute name missing **")
        elif len(s) < 4:
            print("** value missing **")            
        else:
            if s[0] not in classes:
                print("** class doesn't exist **")
                return
            bul = False
            for key in models.storage.all():
                temp = key.split('.')
                if temp[1] == s[1]:
                    bol = True
                    break
            if bol == False:
                print("** no instance found **")
                return
            else:
                aux = s[0] + "." + s[1]
                setattr(models.storage.all()[aux], s[2], s[3])

        '''
        if len(s) == 0:
            print("** class name missing **")
        elif s[0] not in classes:
            print("** class doesn't exist **")
        elif len(s) == 1:
            print("** instance id missing **")
        elif len(s) == 2 and s[2]:
            for key in models.storage.all():
                temp = key.split(".")
                if temp[1]
        '''

    ''' Empty line '''

    def emptyline(self):
        ''' empty line '''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()