#!/usr/bin/python3
"""Import modules for unittests."""
import models
import unittest
import pep8
import inspect
from models.base_model import BaseModel
from models import city

City = city.City


class TestCityDocs(unittest.TestCase):
    """
    Tests to check the documentation and style of City class
    """
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.city_f = inspect.getmembers(City, inspect.isfunction)

    def test_pep8_compliance_city(self):
        """Test that models/city.py complies with PEP8."""
        style = pep8.StyleGuide(quiet=True)
        outcome = style.check_files(['models/city.py'])
        self.assertEqual(outcome.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_compliance_test_city(self):
        """
        Test that tests/test_models/test_city.py complies with PEP8.
        """
        style = pep8.StyleGuide(quiet=True)
        outcome = style.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(outcome.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_city_module_docstring(self):
        """
        Test for the city.py module docstring
        """
        city = models.city.__doc__
        self.assertIsNot(city, None,
                         "city.py needs a docstring")
        self.assertTrue(len(city) >= 1,
                        "city.py needs a docstring")

    def test_city_class_docstring(self):
        """
        Test for the City class docstring
        """
        self.assertIsNot(City.__doc__, None,
                         "City class needs a docstring")
        self.assertTrue(len(City.__doc__) >= 1,
                        "City class needs a docstring")

    def test_city_func_docstrings(self):
        """
        Test for the presence of docstrings in City methods
        """
        for func in self.city_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestCity(unittest.TestCase):
    """Tests for city class"""
    def __init__(self, *args, **kwargs):
        """Initialises tests """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """State id test """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """tests name """
        new = self.value()
        self.assertEqual(type(new.name), str)
