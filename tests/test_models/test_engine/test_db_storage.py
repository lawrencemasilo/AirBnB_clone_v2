#!/usr/bin/python3
"""Import modules for unittests."""
import models
import unittest
import inspect
import os
import pep8
import json
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

DBStorage = db_storage.DBStorage
classes = {
        'Amenity': Amenity ,
        'City': City ,
        'Place': Place ,
        'Review': Review ,
        'State': State ,
        'User': User
        }


class TestDBStorageDocs(unittest.TestCase):
    """Test checks doc-style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Sets up class"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_compliance(self):
        """Tests whether db_storage complies with pep8"""
        style = pep8.StyleGuide(quiet=True)
        outcome = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(outcome.total_errors, 0,
                "Found code style errors (and warnings).")

    def test_pep8_compliance_test(self):
        """Tests whether db_storage test file complies with pep8"""
        style = pep8.StyleGuide(quiet=True)
        outcome = style.check_files(['tests/test_models/test_engine/test_db_storage.py'])
        self.assertEqual(outcome.total_errors, 18,
                "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for module docstrings."""
        self.assertIsNot(db_storage.__doc__, None,
                "Module needs docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1, "Module needs docstring")

    def test_db_storage_class_docstring(self):
        """Test for class docstrings."""
        self.assertIsNot(DBStorage.__doc__, None,
                "Module needs docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1, "Module needs docstring")

    def test_docstrings(self):
        """Test if there are docstings in DBStorage method"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                    "{:s} method needs docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                    "{:s} method needs docstring".format(func[0]))

class TestFileStorage(unittest.TestCase):
    """Tests for filestorage class."""
    @unittest.skipIf(models.base_model.storage_t != "db",
            "Not testing db storage")
    def test_all_returns_dict(self):
        """tests all."""
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(models.base_model.storage_t != "db",
            "Not testing db storage")
    def test_all_no_class(self):
        """Tests all when no class is passed."""

    @unittest.skipIf(models.base_model.storage_t != "db",
            "Not testing db storage")
    def test_new(self):
        """Tests whether new objects are added to db."""

    @unittest.skipIf(models.base_model.storage_t != "db",
            "Not testing db storage")
    def test_save(self):
        """Tests whether objects saved to file.json."""

