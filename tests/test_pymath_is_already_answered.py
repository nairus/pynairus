# coding: utf-8

"""Unit tests module for is_already_answered function."""

import unittest
from pynairus.pymath import is_already_answered
from pynairus.pymath import ANSWERS

GOOD_ANSWER = (1, 5, "*")
BAD_ANSWER = (1, 3, "-")


class TestPymathIsAlreadyAnswered(unittest.TestCase):
    """Unit test for is_already_answered function."""

    def setUp(self):
        """Invoked before every tests."""
        ANSWERS[GOOD_ANSWER] = True
        ANSWERS[BAD_ANSWER] = False

    def tearDown(self):
        """Invoked after every tests."""
        # On vide le dictionnaire après chaque test.
        ANSWERS.clear()

    def test_not_exists(self):
        """Not exist test."""
        self.assertFalse(is_already_answered((1, 2, '+')),
                         msg="the tuple (1, 2, '+') musts not exist.")

    def test_exists_and_true(self):
        """Testing if the right anwser exists."""
        self.assertTrue(is_already_answered(GOOD_ANSWER),
                        f"the tuple {GOOD_ANSWER} musts exist and be True.")

    def test_exists_and_false(self):
        """Testing if the wrong answer exists."""
        self.assertFalse(is_already_answered(BAD_ANSWER),
                         f"the tuple {BAD_ANSWER} musts exist and be False.")
