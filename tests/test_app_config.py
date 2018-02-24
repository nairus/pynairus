# coding: utf-8

"""Test module for AppConfig class."""

import unittest
import logging
from pathlib import Path
import pynairus.config.app_config as py_ac
from pynairus.errors.app_error import BadArgmentsError

TEST_LOG_FILE_PATH = Path("pynairus/logs/pymath.default.log")


class AppConfigTest(unittest.TestCase):
    """Unit test class for AppConfig."""

    @classmethod
    def setUpClass(cls):
        if TEST_LOG_FILE_PATH.exists():
            TEST_LOG_FILE_PATH.unlink()

    def tearDown(self):
        if TEST_LOG_FILE_PATH.exists():
            TEST_LOG_FILE_PATH.unlink()

    def test_contructor(self):
        """Test the constructor of AppConfig class."""
        with self.assertRaises(
                BadArgmentsError,
                msg="1. The class must raise an [BadArgmentsError] exception"):
            py_ac.AppConfig(None, True)

        app_config = py_ac.AppConfig(logging.getLogger())
        self.assertFalse(app_config.log_enabled,
                         msg="2. The property [log_enabled] must be set")

        self.assertIs(app_config.logger, logging.getLogger(),
                      msg="3. The [logger] property must be set")

    def test_parse_yml(self):
        """Test of the [parse_yml] function."""
        app_config = py_ac.parse_yml(filename="app_config.yml.dist")

        self.assertIsInstance(
            app_config, py_ac.AppConfig,
            msg="1. The methode must return an instance of [AppConfig]")

        self.assertFalse(app_config.log_enabled,
                         msg="2. The logs must be disabled")

        self.assertTrue(TEST_LOG_FILE_PATH.exists(),
                        msg="3. The log file musts exist")

        # free the resource for the other tests
        app_config.logger.handlers[1].close()

    def test_parse_ini(self):
        """Test of the [parse_ini] function."""
        app_config = py_ac.parse_ini(filename="app_config.ini.dist")

        self.assertIsInstance(
            app_config, py_ac.AppConfig,
            msg="1. The methode must return an instance of [AppConfig]")

        self.assertFalse(app_config.log_enabled,
                         msg="2. The logs must be disabled")

        self.assertTrue(TEST_LOG_FILE_PATH.exists(),
                        msg="3. The log file musts exist")

        # free the resource for the other tests
        app_config.logger.handlers[0].close()

    @unittest.skip("To implement")
    def test_parse_json(self):
        """Test of the [parse_json] function."""

    @unittest.skip("To implement")
    def test_parse_xml(self):
        """Test of the [parse_xml] function."""
