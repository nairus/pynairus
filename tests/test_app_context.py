# coding: utf-8

"""Test of the app_context module."""


import unittest
import logging
from pynairus.config import app_context as ac, app_config as af


class AppContextTest(unittest.TestCase):
    """Class of unit test for app_context module."""

    # test config folder path
    TEST_CONFIG_FOLDER_PATH = "pynairus/test/config/"

    @classmethod
    def setUpClass(cls):
        """Init env for testing this module."""
        cls.CONFIG_FOLDER_PATH = ac.CONFIG_FOLDER_PATH
        ac.CONFIG_FOLDER_PATH = cls.TEST_CONFIG_FOLDER_PATH

    @classmethod
    def tearDownClass(cls):
        """Reset test env."""
        ac.CONFIG_FOLDER_PATH = cls.CONFIG_FOLDER_PATH

    def test_app_context_singleton(self):
        """Test the singleton creation of AppContext class."""

        app_config = af.AppConfig(logging.getLogger(), False)
        test_args = {
            "start": 1,
            "end": 2,
            "limit": 2,
            "timer": True,
            "operator": "+"
        }

        app_context = ac.AppContext(app_config, **test_args)
        self.assertIs(app_config, app_context.app_config,
                      msg="1. the [app_config] property must be ok")

        self.assertIs(1, app_context.start,
                      msg="2. the [start] property must be ok")

        self.assertIs(2, app_context.end,
                      msg="3. the [end] property must be ok")

        self.assertIs(2, app_context.limit,
                      msg="4. the [limit] property must be ok")

        self.assertIn("timer", app_context.options,
                      msg="5.1 the options property must contains timer key.")
        self.assertTrue(app_context.options.get("timer"),
                        msg="5.2 The timer option must be set to [True]")

        self.assertIn("operator", app_context.options,
                      msg="6.1 the options property must contains operator key.")
        self.assertIs("+", app_context.options.get("operator"),
                      msg="6.2 The operator must be set to [+] string")

        self.assertEqual(2, len(app_context.options),
                         msg="7. Only 2 items must remain in the [options] property.")

        self.assertIs(app_context, ac.AppContext(),
                      msg="8. The instance must be a singleton")

    @unittest.skip("todo")
    def test_app_context_bad_config(self):
        """Test with bad [app_config] property."""

    @unittest.skip("todo")
    def test_app_context_bad_start(self):
        """Test with bad [start] property."""

    @unittest.skip("todo")
    def test_app_context_bad_end(self):
        """Test with bad [end] property."""

    @unittest.skip("todo")
    def test_app_context_bad_limit(self):
        """Test with bad [limit] property."""

    @unittest.skip("todo")
    def test_app_context_bad_options(self):
        """Test with bad [options] property."""

    @unittest.skip("todo")
    def test_init_app_context(self):
        """Test the init_app_context function."""
        pass
