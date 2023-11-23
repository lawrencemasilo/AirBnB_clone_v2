#!/usr/bin/python3
"""Import modules for unittests"""
import models
import unittest
import pep8
import inspect
from models.base_model import BaseModel
from models import review

Review = review.Review


class TestReviewDocs(unittest.TestCase):
    """
    Tests to check the documentation and style of Review class
    """
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.review_f = inspect.getmembers(Review, inspect.isfunction)

    def test_pep8_compliance_review(self):
        """Test that models/review.py complies with PEP8."""
        style = pep8.StyleGuide(quiet=True)
        outcome = style.check_files(['models/review.py'])
        self.assertEqual(outcome.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_compliance_test_review(self):
        """
        Test that tests/test_models/test_review.py complies with PEP8.
        """
        style = pep8.StyleGuide(quiet=True)
        outcome = style.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(outcome.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_review_module_docstring(self):
        """
        Test for the review.py module docstring
        """
        review = models.review.__doc__
        self.assertIsNot(review, None,
                         "review.py needs a docstring")
        self.assertTrue(len(review) >= 1,
                        "review.py needs a docstring")

    def test_review_class_docstring(self):
        """
        Test for the Review class docstring
        """
        self.assertIsNot(Review.__doc__, None,
                         "Review class needs a docstring")
        self.assertTrue(len(Review.__doc__) >= 1,
                        "Review class needs a docstring")

    def test_review_func_docstrings(self):
        """
        Test for the presence of docstrings in Review methods
        """
        for func in self.review_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestReview(unittest.TestCase):
    """Tests for review class"""

    def __init__(self, *args, **kwargs):
        """init tests """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """palce id """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """user id """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """text """
        new = self.value()
        self.assertEqual(type(new.text), str)
