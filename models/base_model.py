#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import models
import uuid
import sqlalchemy
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from os import getenv
import os

storage_t = os.getenv('HBNB_TYPE_STORAGE')
if storage_t == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""
    if storage_t == "db":
        id = Column(String(60), unique=True, primary_key=True, nullable=False)
        created_at = Column(
                DateTime,
                nullable=False,
                default=datetime.utcnow()
                )
        updated_at = Column(
                DateTime,
                nullable=False,
                default=datetime.utcnow()
                )

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"],
                                                    '%Y-%m-%dT%H:%M:%S.%f')
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                    '%Y-%m-%dT%H:%M:%S.%f')
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())

            """kwargs.pop('__class__', None)
            for key, value in kwargs.items():
                if not hasattr(self, key):
                    setattr(self, key, value)"""
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()

        if "created_at" in dictionary:
            dictionary["created_at"] = dictionary["created_at"].strftime(
                    '%Y-%m-%dT%H:%M:%S.%f')
        if "updated_at" in dictionary:
            dictionary["updated_at"] = dictionary["updated_at"].strftime(
                    '%Y-%m-%dT%H:%M:%S.%f')
        dictionary["__class__"] = self.__class__.__name__

        if '_sa_instance_state' in dictionary:
            dictionary.pop('_sa_instance_state', None)

        return (dictionary)

    def delete(self):
        """Deletes the current instance from the storage"""
        models.storage.delete(self)
