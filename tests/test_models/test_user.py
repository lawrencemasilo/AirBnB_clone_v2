#!/usr/bin/python3
"""Import modules for unittests."""
import models
import unittest
import inspect
import pep8
from models.base_model import BaseModel
from models.user import User

User = models.user.User


class TestUserDocs(unittest.TestCase):
    """
    Tests to check the documentation and style of User class
    """
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.user_f = inspect.getmembers(User, inspect.isfunction)

    def test_pep8_compliance_amenity(self):
        """Test that models/user.py complies with PEP8."""
        style = pep8.StyleGuide(quiet=True)
        outcome = style.check_files(['models/user.py'])
        self.assertEqual(outcome.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_compliance_test_user(self):
        """
        Test that tests/test_models/test_user.py complies with PEP8.
        """
        style = pep8.StyleGuide(quiet=True)
        outcome = style.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(outcome.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_user_module_docstring(self):
        """
        Test for the user.py module docstring
        """
        user = models.user.__doc__
        self.assertIsNot(user, None,
                         "user.py needs a docstring")
        self.assertTrue(len(user) >= 1,
                        "user.py needs a docstring")

    def test_user_class_docstring(self):
        """
        Test for the User class docstring
        """
        self.assertIsNot(User.__doc__, None,
                         "User class needs a docstring")
        self.assertTrue(len(User.__doc__) >= 1,
                        "User class needs a docstring")

    def test_user_func_docstrings(self):
        """
        Test for the presence of docstrings in User methods
        """
        for func in self.user_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestUser(unittest.TestCase):
    """Tests for user class."""
    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_is_subclass(self):
        """Test that User is a subclass of BaseModel"""
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_first_name(self):
        """Firstname test """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """Last name test """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """test for email """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """test for password """
        new = self.value()
        self.assertEqual(type(new.password), str)

    def test_str(self):
        """test str method."""
        user = User()
        string = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(string, str(user))
