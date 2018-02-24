# coding: utf-8

"""Test module for file helper."""

import unittest
from pynairus.helpers.file_helper import get_file_path, BadArgmentsError, Path


class FileHelperTest(unittest.TestCase):
    """Unit test class for file helper module."""

    def test_get_file_path(self):
        """Test the the [get_file_path] function."""
        with self.assertRaises(BadArgmentsError,
                               msg="1. The function must raise an error"):
            get_file_path("not_exists_file")

        config_file = get_file_path(
            "pynairus/config/app_config.yml.dist")
        self.assertIsInstance(config_file, Path,
                              msg="2. the object must be an instance of Path")
