#!/usr/bin/python3
""" State Module for HBNB project """
import models
import sqlalchemy
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.engine.db_storage import DBStorage


class State(BaseModel, Base):
    """ State class """
    if models.storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete" backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initialises state class."""
        super().__init__(*args, **kwargs)

    if models.storage_t != "db":
        @property
        def cities(self):
            """gets list of city instances related to state instance"""
            city_ls = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_ls.append(city)
            return city_ls
