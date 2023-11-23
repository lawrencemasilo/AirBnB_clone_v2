#!/usr/bin/python3
"""Import modules for unittests."""
import models
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os
import pep8 as pycodestyle
import inspect

BaseModel = models.base_model.BaseModel


class TestBaseModelDocs(unittest.TestCase):
    """Tests doc-style of base model class"""
    @classmethod
    def setUpClass(self):
        """sets up"""
        self.base_f = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_pep8_compliance(self):
        """Tests if base_model.py complies with pep8"""
        for path in ['models/base_model.py',
                     'tests/test_models/test_base_model.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        module_doc = models.base_model.__doc__
        self.assertIsNot(module_doc, None, "Module needs docstring")
        self.assertTrue(len(module_doc) > 1, "Module needs docstring")

    def test_class_docstring(self):
        """Test for the BaseModel class docstring"""
        self.assertIsNot(BaseModel.__doc__, None, "Class needs docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1, "Class needs docstring")

    def test_func_docstrings(self):
        """Test for the presence of docstrings in BaseModel methods"""
        for func in self.base_f:
            with self.subTest(function=func):
                self.assertIsNot(func[1].__doc__, None,
                                 "{:s} method needs docstring".format(func[0]))
                self.assertTrue(len(func[1].__doc__) > 1,
                                "{:s} method needs docstring".format(func[0]))


class TestBaseModel(unittest.TestCase):
    """Tests for base model class"""

    def __init__(self, *args, **kwargs):
        """Initialises tests """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """Sets up """
        pass

    def tearDown(self):
        """Tears down"""
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_default(self):
        """tests default """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """Test for kwargs """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """Test for kwargs ints """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_uuid(self):
        """Tests whether id is a valid uuid"""
        inst1 = BaseModel()
        inst2 = BaseModel()
        for inst in [inst1, inst2]:
            uuid = inst.id
            with self.subTest(uuid=uuid):
                self.assertIs(type(uuid), str)
                self.assertRegex(uuid, '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertNotEqual(inst1.id, inst2.id)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Test for string"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """Tests dict conversion"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """Test for no kwargs """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_id(self):
        """test for ids """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """Created_at test """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """Updated_at test """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertTrue(new.created_at == new.updated_at)
