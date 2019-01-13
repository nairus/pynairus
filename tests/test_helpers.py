# coding: utf-8

"""Test module for helpers module."""

import unittest
from pynairus.helpers.file_helper import get_file_path, Path
from pynairus.helpers import string_helper as sh
from pynairus.config import CONFIG_FOLDER
from pynairus.errors.app_error import BadArgumentError


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
        self.assertEqual(10, len(sh.STR_BOOL_VALS),
                         msg="1. the dict musts contain 10 items")

    def test_get_bool_from_str(self):
        """Test the [get_bool_from_str] function."""
        # True allowed values
        self.assertTrue(sh.get_bool_from_str("1"),
                        msg="1. the val [1] must be true")
        self.assertTrue(sh.get_bool_from_str("True"),
                        msg="2. the val [True] must be true")
        self.assertTrue(sh.get_bool_from_str("T"),
                        msg="3. the val [T] must be true")
        self.assertTrue(sh.get_bool_from_str("yes"),
                        msg="4. the val [yes] must be true")
        self.assertTrue(sh.get_bool_from_str("y"),
                        msg="5. the val [y] must be true")

        # False allowed values
        self.assertFalse(sh.get_bool_from_str("0"),
                         msg="6. the [0] val must be false")
        self.assertFalse(sh.get_bool_from_str("false"),
                         msg="7. the [false] val must be false")
        self.assertFalse(sh.get_bool_from_str("f"),
                         msg="8. the [f] val must be false")
        self.assertFalse(sh.get_bool_from_str("no"),
                         msg="9. the [no] val must be false")
        self.assertFalse(sh.get_bool_from_str("n"),
                         msg="10. the [n] val must be false")

        # not allowed values
        with self.assertRaisesRegex(KeyError, "not_allowed"):
            sh.get_bool_from_str("not_allowed")

    def test_parse_time_string(self):
        """Test the [parse_time_string] function."""
        self.assertTupleEqual((1, 24, 3), sh.parse_time_string("1h24m03s"))
        self.assertTupleEqual((0, 54, 25), sh.parse_time_string("54m25s"))
        self.assertTupleEqual((0, 0, 45), sh.parse_time_string("45s"))

        with self.assertRaisesRegex(BadArgumentError, "23m"):
            sh.parse_time_string("23m")

    def test_convert_seconds_to_time(self):
        """Test the [convert_seconds_to_time] function."""
        self.assertEqual("4h06m24s", sh.convert_seconds_to_time(14784))
        self.assertEqual("10m06s", sh.convert_seconds_to_time(606))

        # case timestamp > a day
        with self.assertRaises(BadArgumentError):
            sh.convert_seconds_to_time(25 * 60 * 60)

        # case timestamp < 1 second
        with self.assertRaises(BadArgumentError):
            sh.convert_seconds_to_time(0)
