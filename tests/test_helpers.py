# coding: utf-8

"""Test module for helpers module."""

import unittest
from pynairus.helpers.file_helper import get_file_path, Path
from pynairus.helpers.string_helper import get_bool_from_str, STR_BOOL_VALS
from pynairus.config import CONFIG_FOLDER


class FileHelperTest(unittest.TestCase):
    """Unit test class for file helper module."""

    def test_get_file_path(self):
        """Test the the [get_file_path] function."""
        with self.assertRaises(FileNotFoundError,
                               msg="1. The function must raise an error"):
            get_file_path("not_exists_file")

        config_file = get_file_path(
            "pynairus/config/app_config.yml.dist")
        self.assertIsInstance(config_file, Path,
                              msg="2. the object must be an instance of Path")

        with self.assertRaises(FileNotFoundError,
                               msg="3. The function must raise an error"):
            get_file_path(["bad_type_file"])

        filepath = Path(CONFIG_FOLDER, "app_config.yml.dist")
        config_file = get_file_path(filepath)
        self.assertIsInstance(config_file, Path,
                              msg="4. the object must be an instance of Path")


class StringHelperTest(unittest.TestCase):
    """Unit test class for string helper module."""

    def test_str_bool_vals_dict(self):
        """Test the dict of str_bool vals allowed."""
        self.assertEqual(10, len(STR_BOOL_VALS),
                         msg="1. the dict musts contain 10 items")

    def test_get_bool_from_str(self):
        """Test the [get_bool_from_str] function."""
        # True allowed values
        self.assertTrue(get_bool_from_str("1"),
                        msg="1. the val [1] must be true")
        self.assertTrue(get_bool_from_str("True"),
                        msg="2. the val [True] must be true")
        self.assertTrue(get_bool_from_str("T"),
                        msg="3. the val [T] must be true")
        self.assertTrue(get_bool_from_str("yes"),
                        msg="4. the val [yes] must be true")
        self.assertTrue(get_bool_from_str("y"),
                        msg="5. the val [y] must be true")

        # False allowed values
        self.assertFalse(get_bool_from_str("0"),
                         msg="6. the [0] val must be false")
        self.assertFalse(get_bool_from_str("false"),
                         msg="7. the [false] val must be false")
        self.assertFalse(get_bool_from_str("f"),
                         msg="8. the [f] val must be false")
        self.assertFalse(get_bool_from_str("no"),
                         msg="9. the [no] val must be false")
        self.assertFalse(get_bool_from_str("n"),
                         msg="10. the [n] val must be false")

        # not allowed values
        with self.assertRaisesRegex(KeyError, "not_allowed"):
            get_bool_from_str("not_allowed")
