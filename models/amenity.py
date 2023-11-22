#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship
import models

"""if models.base_model.storage_t == 'db':
    place_amenity = Table(
            'place_amenity',
            Base.metadata,
            Column(
                'amenity_id',
                String(60),
                ForeignKey('amenities.id'),
                primary_key=True
                ),
            Column(
                'place_id',
                String(60),
                ForeignKey('places.id'),
                primary_key=True
                ),
            extend_existing=True
            )"""


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)
    place_amenities = relationship(
            "Place",
            secondary=models.place.place_amenity,
            backref="amenities"
            )
