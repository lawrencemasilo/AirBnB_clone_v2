#!/usr/bin/python3
"""this module defines a class to manage db storage for hbnb clone"""
from sqlalchemy import create_engine
import os
from sqlalchemy.orm import sessionmaker, scoped_session
from models import base_model


class DBStorage:
    """This class manages storage of hbnb models in using SQL"""

    __engine = None
    __session = None

    def __init__(self):
        """handles initialization"""
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', default='localhost')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
                f'mysql+mysqldb://{user}:{password}@{host}/{db}',
                pool_pre_ping=True
                )

        if os.getenv('HBNB_ENV') == 'test':
            models.Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        session = self.__session()
        if cls:
            objects = session.query(cls).all()
        else:
            classes = [
                    base_model.User, base_model.State, base_model.City,
                    base_model.Amenity, base_model.Place, base_model.Review
            ]
            objects = []
            for clas in classes:
                objects.extend(session.query(clas).all())

        session.close()
        obj_dict = {f"{type(obj).__name__}.{obj.id}": obj for obj in objects}
        return obj_dict

    def new(self, obj):
        """Adds new object to storage"""
        if obj:
            session = self.__session()
            session.add(obj)
            session.commit()
            session.close()

    def save(self):
        """Saves storage to Database"""
        session = self.__session()
        session.commit()
        session.close()

    def delete(self, obj=None):
        """Deletes object from Database"""
        if obj:
            session = self.__session()
            session.delete(obj)
            session.commit()
            session.close()

    def reload(self):
        """Loads storage dictionary from Database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine,
                expire_on_commit=False
                )
        self.__session = scoped_session(session_factory)
