#!/usr/bin/python3
"""Import modules for unittests."""
import models
import unittest
import pep8
import inspect
from models.base_model import BaseModel
from models import place

Place = place.Place


class TestPlaceDocs(unittest.TestCase):
    """
    Tests to check the documentation and style of Place class
    """
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.place_f = inspect.getmembers(Place, inspect.isfunction)

    def test_pep8_compliance_place(self):
        """Test that models/place.py complies with PEP8."""
        style = pep8.StyleGuide(quiet=True)
        outcome = style.check_files(['models/place.py'])
        self.assertEqual(outcome.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_compliance_test_place(self):
        """
        Test that tests/test_models/test_place.py complies with PEP8.
        """
        style = pep8.StyleGuide(quiet=True)
        outcome = style.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(outcome.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_place_module_docstring(self):
        """
        Test for the place.py module docstring
        """
        place = models.place.__doc__
        self.assertIsNot(place, None,
                         "place.py needs a docstring")
        self.assertTrue(len(place) >= 1,
                        "place.py needs a docstring")

    def test_place_class_docstring(self):
        """
        Test for the Place class docstring
        """
        self.assertIsNot(Place.__doc__, None,
                         "Place class needs a docstring")
        self.assertTrue(len(Place.__doc__) >= 1,
                        "Place class needs a docstring")

    def test_place_func_docstrings(self):
        """
        Test for the presence of docstrings in Place methods
        """
        for func in self.place_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestPlace(unittest.TestCase):
    """Tests for place class"""
    def __init__(self, *args, **kwargs):
        """initialises tests"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """test for city ids"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """test for user id"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """test for name"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """description test"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """test no. of rooms"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """no. of bathrooms """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ test max guest capacity"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """price attr test """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ lat attr test"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ long attr test"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ test amenity ids"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
