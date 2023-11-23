#!/usr/bin/python3
"""Import modules for unittests."""
import unittest
import console
import pep8
import inspect
HBNBCommand = console.HBNBCommand


class TestConsoleDocs(unittest.TestCase):
    """Tests for the console."""
    def test_pep8_compliance(self):
        """Tests whether the console complies with pep8 guides"""
        style = pep8.StyleGuide(quiet=True)
        outcome = style.check_files(['console.py'])
        self.assertEqual(
                outcome.total_errors,
                0,
                "Found code style errors (and warnings)."
                )

    def test_pep8_test_compliance(self):
        """Tests whether tests/test_console.py complies with pep8"""
        style = pep8.StyleGuide(quiet=True)
        outcome = style.check_files(['tests/test_console.py'])
        self.assertEqual(
                outcome.total_errors,
                0,
                "Found code style errors (and warnings)."
                )

    def test_console_docstring(self):
        """Tests docstring."""
        self.assertIsNot(console.__doc__, None, "Docstring needed")
        self.assertTrue(len(console.__doc__) >= 1, "Docstring needed")

    def test_HBNBCommand_docstring(self):
        """Tests docstring for HBNBCommand class."""
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand needs docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand needs docstring")
