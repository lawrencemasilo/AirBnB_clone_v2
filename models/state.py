#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if DBStorage:
        cities = relationship('City', cascade='all, delete', backref='state')

    if FileStorage:
        @property
        def cities(self):
            return [
                    city for city in models.storage.all('City').values()
                    if city.state_id == self.id
                    ]
