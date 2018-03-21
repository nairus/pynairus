# coding: utf-8

"""Test of the app_context module."""


import unittest
import logging
from pynairus import config
from pynairus.config import app_context as ac, app_config as ag
from pynairus.errors.app_error import ConfigError
from .config import TEST_CONFIG_FOLDER_PATH


class AppContextTest(unittest.TestCase):
    """Class of unit test for app_context module."""

    def setUp(self):
        """Init env for testing this module."""
        self.CONFIG_FOLDER_PATH = config.CONFIG_FOLDER
        config.CONFIG_FOLDER = TEST_CONFIG_FOLDER_PATH

    def tearDown(self):
        """Clean the tests."""
        ac.AppContext.clearContext()
        config.CONFIG_FOLDER = self.CONFIG_FOLDER_PATH

    def test_app_context_singleton(self):
        """Test the singleton creation of AppContext class."""

        app_config = ag.AppConfig(logging.getLogger(), False)
        test_args = {
            "start": 1,
            "end": 2,
            "limit": 2,
            "timer": True,
            "operator": "+"
        }

        app_context = ac.AppContext(app_config, **test_args)
        self.assertIs(app_config, app_context.app_config,
                      msg="1. app_config property musts be ok")

        self.assertIs(1, app_context.start,
                      msg="2. start property musts be ok")

        self.assertIs(2, app_context.end,
                      msg="3. end property musts be ok")

        self.assertIs(2, app_context.limit,
                      msg="4. limit property musts be ok")

        self.assertIn("timer", app_context.options,
                      msg="5.1 options property musts contain timer key.")
        self.assertTrue(app_context.options.get("timer"),
                        msg="5.2 The timer option musts be set to [True]")

        self.assertIn("operator", app_context.options,
                      msg="6.1 options property musts contain operator key.")
        self.assertIs("+", app_context.options.get("operator"),
                      msg="6.2 The operator musts be set to [+] string")

        self.assertEqual(2, len(app_context.options),
                         msg="7. 2 items musts remain in [options] property.")

        self.assertIs(app_context, ac.AppContext(),
                      msg="8. The instance musts be a singleton")

    def test_app_context_bad_config(self):
        """Test with bad [app_config] property."""
        with self.assertRaisesRegex(
                TypeError,
                r"is not an instance of \[AppConfig\]"):
            test_args = {
                "start": 1,
                "end": 2,
                "limit": 2,
                "timer": True,
                "operator": "+"
            }

            ac.AppContext(None, **test_args)

    def test_app_context_bad_start(self):
        """Test with bad [start] property."""
        with self.assertRaisesRegex(
                TypeError,
                r"is not an \[int\]"):
            app_config = ag.AppConfig(logging.getLogger(), False)
            test_args = {
                "end": 2,
                "limit": 2,
                "timer": True,
                "operator": "+"
            }

            ac.AppContext(app_config, **test_args)

    def test_app_context_bad_end(self):
        """Test with bad [end] property."""
        with self.assertRaisesRegex(
                TypeError,
                r"is not an \[int\]"):
            app_config = ag.AppConfig(logging.getLogger(), False)
            test_args = {
                "start": 2,
                "limit": 2,
                "timer": True,
                "operator": "+"
            }

            ac.AppContext(app_config, **test_args)

    def test_app_context_bad_limit(self):
        """Test with bad [limit] property."""
        with self.assertRaisesRegex(
                TypeError,
                r"is not an \[int\]"):
            app_config = ag.AppConfig(logging.getLogger(), False)
            test_args = {
                "start": 2,
                "end": 2,
                "timer": True,
                "operator": "+"
            }

            ac.AppContext(app_config, **test_args)

    def test_app_context_bad_options(self):
        """Test with bad [options] property."""
        with self.assertRaisesRegex(
                TypeError,
                r"is not an instance of \[dict\]"):
            app_config = ag.AppConfig(logging.getLogger(), False)
            test_args = {
                "start": 1,
                "end": 2,
                "limit": 2,
                "timer": True,
                "operator": "+"
            }

            app_context = ac.AppContext(app_config, **test_args)
            app_context.options = False

    def test_file_extension_detection(self):
        """Test the regex for config file detection."""

        result1 = ac.ALLOWED_FILE_EXTENSION.fullmatch("app_config.ini")
        self.assertIsNotNone(result1, msg="1.1 the pattern musts match")
        self.assertEqual("ini", result1.group("extension"),
                         msg="1.2 the file extension musts be captured.")

        result2 = ac.ALLOWED_FILE_EXTENSION.fullmatch("app-config.json")
        self.assertIsNotNone(result2, msg="2.1 the pattern musts match")
        self.assertEqual("json", result2.group("extension"),
                         msg="2.2 the file extension musts be captured.")

        result3 = ac.ALLOWED_FILE_EXTENSION.fullmatch("AppConfig.xml")
        self.assertIsNotNone(result3, msg="3.1 the pattern musts match")
        self.assertEqual("xml", result3.group("extension"),
                         msg="3.2 the file extension musts be captured.")

        result4 = ac.ALLOWED_FILE_EXTENSION.fullmatch("app_config.yml")
        self.assertIsNotNone(result4, msg="4.1 the pattern musts match")
        self.assertEqual("yml", result4.group("extension"),
                         msg="4.2 the file extension musts be captured.")

        self.assertIsNone(
            ac.ALLOWED_FILE_EXTENSION.fullmatch("app_config.ini.dist"),
            msg="5. the pattern musts not match")

        self.assertIsNone(
            ac.ALLOWED_FILE_EXTENSION.fullmatch("test1.ini"),
            msg="6. the pattern musts not match")

    def test_get_config_parser(self):
        """Test the get_config_parser function."""
        self.assertEqual(4, len(ac.CONFIG_PARSER_DICT),
                         msg="1. The dict musts contain 4 items.")

        self.assertIs(ag.parse_yml, ac.get_config_parser(),
                      msg="2. The yml parser musts be returned by default.")

        self.assertIs(ag.parse_ini, ac.get_config_parser("config.ini"),
                      msg="3. The ini parser musts be returned")

        self.assertIs(ag.parse_json, ac.get_config_parser("config.json"),
                      msg="4. The json parser musts be returned by default.")

        self.assertIs(ag.parse_xml, ac.get_config_parser("config.xml"),
                      msg="5. The xml parser musts be returned")

        self.assertIs(ag.parse_yml, ac.get_config_parser("config.yml"),
                      msg="6. The yml parser musts be returned")

        with self.assertRaisesRegex(ConfigError,
                                    r"config \[config.py\] not allowed!"):
            ac.get_config_parser("config.py")

    def test_init_default_app_context(self):
        """Test the init_app_context function."""
        app_context = ac.init_app_context(
            start=2, end=4, limit=2)

        self.assertIsInstance(app_context, ac.AppContext,
                              msg="It musts be an instance of [AppContext]")

    def test_init_app_context(self):
        """Test the initialization of app_context."""
        app_context = ac.init_app_context(
            start=2, end=4, limit=2, config="config.yml")

        self.assertIsInstance(app_context, ac.AppContext,
                              msg="It musts be an instance of [AppContext]")
