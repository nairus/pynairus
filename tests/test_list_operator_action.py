# coding: utf-8

"""Unit tests module for actions.list_operator module."""

import unittest
import argparse
from pynairus.actions.list_operators_action import ListOperatorsAction


class ListOperatorsActionTest(unittest.TestCase):
    """Unit test for ListOperatorsAction class."""

    def test_inheritance(self):
        """Test the inheritance of the class."""
        self.assertIn(argparse.Action, ListOperatorsAction.__bases__)
