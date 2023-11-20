#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
            }

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    """def all(self, cls=None):
        Returns a dictionary of models currently in storage
        if cls:
            objs = {}
            for key, obj in FileStorage.__objects.items():
                if type(obj).__name__ == cls.__name__:
                    objs[key] = obj
            return objs
        else:
            return FileStorage.__objects"""

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return (new_dict)
        return (self.__objects)

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        temp = {}
        for key in self.__objects:
            temp[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        
        try:
            temp = {}
            with open(self.__file_path, 'r') as f:
                temp = json.load(f)
            for key in temp:
                self.__objects[key] = classes[temp[key]['__class__']](**temp[key])
        except FileNotFoundError:
            pass

    """def delete(self, obj=None):
        Deletes object from __objects if it's inside
        if obj:
            obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects.pop(obj_key, None)"""
