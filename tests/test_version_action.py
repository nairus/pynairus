# coding: utf-8

"""Unit tests module for actions.version module."""

import unittest
import argparse
from pynairus.actions.version_action import VersionAction


class VersionActionTest(unittest.TestCase):
    """Unit test class for VersionAction."""

    def test_inheritance(self):
        """Test the inheritance of the class."""
        self.assertIn(argparse.Action, VersionAction.__bases__)
