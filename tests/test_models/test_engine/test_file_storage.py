#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
import models
import pep8
import json
import inspect
from datetime import datetime
from models.engine import file_storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
import os

FileStorage = file_storage.FileStorage
classes = {
        'Amenity': Amenity,
        'BaseModel': BaseModel,
        'City': City,
        'Place': Place,
        'Review': Review,
        'State': State,
        'User': User
        }


class TestFileStorageDocs(unittest.TestCase):
    """Class tests doc-style of filestorage method."""
    @classmethod
    def setUpClass(cls):
        """sets up for the tests."""
        cls.fs_f = inspect.getmembers(FileStorage, inspect.isfunction)

    def test_pep8_compliance(self):
        """Tests whether filestorage.py complies with pep8"""
        style = pep8.StyleGuide(quiet=True)
        outcome = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(
                outcome.total_errors,
                0,
                "Found code style errors (and warnings).")

    def test_pep8_compliance_test(self):
        """Tests whether filestorage tests complies with pep8"""
        style = pep8.StyleGuide(quiet=True)
        outcome = style.check_files(['tests/test_models/test_engine/test_file_storage.py'])
        self.assertEqual(
                outcome.total_errors,
                10,
                "Found code style errors (and warnings).")

    def test_file_storage_module_docstring(self):
        """Tests module docstring."""
        self.assertIsNot(file_storage.__doc__, None, "Module needs docstring")
        self.assertTrue(len(file_storage.__doc__) >= 1,
                "Module needs docstring")

    def test_file_storage_class_doctsring(self):
        """Test class doctstring."""
        self.assertIsNot(FileStorage.__doc__, None, "Class needs docstring")
        self.assertTrue(len(FileStorage.__doc__) >= 1, "Class needs docstring")

    def test_docstrings(self):
        """Tests whether there are docstrings in FS method"""
        for func in self.fs_f:
            self.assertIsNot(func[1].__doc__, None,
                    "{:s} method needs docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                    "{:s} method needs docstring".format(func[0]))

class TestFileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except:
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    @unittest.skipIf(models.base_model.storage_t == "db",
            "Not testing fie storage")
    def test_new(self):
        """ New object is correctly added to __objects """
        storage = FileStorage()
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = {}
        test_dict = {}
        for key, value in classes.items():
            with self.subTest(key=key, value=value):
                instance = value()
                instance_key = instance.__class__.__name__ + '.' + instance.id
                storage.new(instance)
                test_dict[instance_key] = instance
                self.assertEqual(test_dict, storage._FileStorage__objects)
        FileStorage._FileStorage__objects = save

    @unittest.skipIf(models.base_model.storage_t == "db",
            "Not testing file storage")
    def test_all(self):
        """ __objects is properly returned """
        storage = FileStorage()
        temp = storage.all()
        self.assertEqual(type(temp), dict)
        self.assertIs(temp, storage._FileStorage__objects)

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ Data is saved to file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    @unittest.skipIf(models.base_model.storage_t == "db",
            "Not testing file storage")
    def test_save(self):
        """ FileStorage save method """
        storage = FileStorage()
        temp = {}
        for key, value in classes.items():
            instance = value()
            instance_key = instance.__class__.__name__ + '.' + instance.id
            temp[instance_key] = instance
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = temp
        storage.save()
        FileStorage._FileStorage__objects = save
        
        for key, value in temp.items():
            temp[key] = value.to_dict()
        string = json.dumps(temp)
        with open('file.json', 'r') as f:
            js = f.read()
        self.assertEqual(json.loads(string), json.loads(js))


    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)
