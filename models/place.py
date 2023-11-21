#!/usr/bin/python3
""" Place Module for HBNB project """
import models
import sqlalchemy
from models.base_model import BaseModel, Base
from models.review import Review
from os import getenv
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    if models.base_model.storage_t == "db":
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place")

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initialises place class."""
        super().__init__(*args, **kwargs)

    if models.base_model.storage_t != "db":
        @property
        def review(self):
            """gets lists of review instances relating to place instance"""
            review_ls = []
            all_reviews = models.storage.all(Review)
            for review in all_reviews.value():
                if review.place_id == self.id:
                    review_ls.append(review)
            return (review_ls)
