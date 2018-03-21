# coding: utf-8

"""Test module for AppConfig class."""

import unittest
import logging
from pathlib import Path
import pynairus.config.app_config as py_ac
from pynairus.errors.app_error import BadArgmentsError

LOG_FILE_PATH = Path("pynairus/logs/pymath.default.log")
TEST_DEBUG = "Test DEBUG"
TEST_INFO = "Test INFO"
TEST_WARN = "Test WARN"
TEST_ERROR = "Test ERROR"
TEST_CRITICAL = "Test CRITICAL"
TEST_LOG = "Test LOG"


class AppConfigTest(unittest.TestCase):
    """Unit test class for AppConfig."""
    # Instance of AppConfig.
    app_config = None

    @classmethod
    def setUpClass(cls):
        if LOG_FILE_PATH.is_file():
            LOG_FILE_PATH.unlink()

    def tearDown(self):
        if self.app_config is not None:
            self.app_config.logger.close()
            self.app_config = None

        if LOG_FILE_PATH.is_file():
            LOG_FILE_PATH.unlink()

    def test_contructor(self):
        """Test the constructor of AppConfig class."""
        with self.assertRaises(
                BadArgmentsError,
                msg="1. The class must raise an [BadArgmentsError] exception"):
            py_ac.AppConfig(None)

        app_config = py_ac.AppConfig(logging.getLogger())
        self.assertFalse(app_config.log_enabled,
                         msg="2. The property [log_enabled] must be set")

        self.assertIsNotNone(app_config.logger,
                             msg="3. The [logger] property must be set")

        self.assertFalse(app_config.clear_onstart,
                         msg="4. The [clear_onstart] property must be set")

        with self.assertRaisesRegex(
            TypeError,
            r"\[bool\] type expected: \[<class 'str'>\] given"
        ):
            py_ac.AppConfig(logging.getLogger(), log_enabled="false")

        with self.assertRaisesRegex(
            TypeError,
            r"\[bool\] type expected: \[<class 'str'>\] given"
        ):
            py_ac.AppConfig(logging.getLogger(), clear_onstart="false")

    def test_logger_setter(self):
        with self.assertRaises(BadArgmentsError):
            app_config = py_ac.AppConfig(logging.getLogger())
            app_config.logger = None

    def test_log_enabled_setter(self):
        with self.assertRaisesRegex(
            TypeError,
            r"\[bool\] type expected: \[<class 'int'>\] given"
        ):
            app_config = py_ac.AppConfig(logging.getLogger())
            app_config.log_enabled = 1

    def test_parse_yml(self):
        """Test of the [parse_yml] function."""
        self.app_config = py_ac.parse_yml()

        self.assertIsInstance(
            self.app_config, py_ac.AppConfig,
            msg="1. The methode must return an instance of [AppConfig]")

        self.assertFalse(self.app_config.log_enabled,
                         msg="2. The logs must be disabled")

        self.assertTrue(LOG_FILE_PATH.exists(),
                        msg="3. The log file musts exist")

        self.assertTrue(self.app_config.clear_onstart,
                        msg="4. The log file musts be cleared on start")

        with self.assertRaisesRegex(
            KeyError,
            r"\[log\] section is missing",
            msg="5. The function must raise a [KeyError]"
        ):
            test_filepath = "tests/config/app_config.yml.bad.dist"
            py_ac.parse_yml(filepath=test_filepath)

    def test_parse_ini(self):
        """Test of the [parse_ini] function."""
        self.app_config = py_ac.parse_ini()

        self.assertIsInstance(
            self.app_config, py_ac.AppConfig,
            msg="1. The methode must return an instance of [AppConfig]")

        self.assertFalse(self.app_config.log_enabled,
                         msg="2. The logs must be disabled")

        self.assertTrue(LOG_FILE_PATH.exists(),
                        msg="3. The log file musts exist")

        self.assertTrue(self.app_config.clear_onstart,
                        msg="4. The log file musts be cleared on start")

        with self.assertRaisesRegex(
            KeyError,
            r"\[log\] section is missing",
            msg="5. The function must raise a [KeyError]"
        ):
            test_filepath = "tests/config/app_config.ini.dist"
            py_ac.parse_ini(filename=test_filepath)

    def test_parse_json(self):
        """Test of the [parse_json] function."""
        self.app_config = py_ac.parse_json()

        self.assertIsInstance(
            self.app_config, py_ac.AppConfig,
            msg="1. The methode must return an instance of [AppConfig]")

        self.assertFalse(self.app_config.log_enabled,
                         msg="2. The logs must be disabled")

        self.assertTrue(LOG_FILE_PATH.exists(),
                        msg="3. The log file musts exist")

        self.assertTrue(self.app_config.clear_onstart,
                        msg="4. The log file musts be cleared on start")

        with self.assertRaisesRegex(
            KeyError,
            r"\[log\] section is missing",
            msg="5. The function must raise a [KeyError]"
        ):
            test_filepath = "tests/config/app_config.json.dist"
            py_ac.parse_json(filename=test_filepath)

    def test_parse_xml(self):
        """Test of the [parse_xml] function."""
        self.app_config = py_ac.parse_xml()

        self.assertIsInstance(
            self.app_config, py_ac.AppConfig,
            msg="1. The methode must return an instance of [AppConfig]")

        self.assertFalse(self.app_config.log_enabled,
                         msg="2. The logs must be disabled")

        self.assertTrue(LOG_FILE_PATH.exists(),
                        msg="3. The log file musts exist")

        self.assertTrue(self.app_config.clear_onstart,
                        msg="4. The log file musts be cleared on start")

        with self.assertRaisesRegex(
            KeyError,
            r"\[log\] section is missing",
            msg="5. The function must raise a [KeyError]"
        ):
            test_filepath = "tests/config/app_config.xml.dist"
            py_ac.parse_xml(filename=test_filepath)

    def test_logger_wrapper_disabled(self):
        """Test the wrapper of the logger with log disabled."""

        app_config = py_ac.parse_yml()
        logger = app_config.logger
        logger.debug(TEST_DEBUG)
        logger.info(TEST_INFO)
        logger.warning(TEST_WARN)
        logger.error(TEST_ERROR)
        logger.critical(TEST_CRITICAL)
        logger.log(logging.FATAL, TEST_LOG)

        # free the resource for the other tests
        logger.close()

        with open(LOG_FILE_PATH) as test_log_file:
            log_content = test_log_file.read()
            self.assertNotIn(TEST_DEBUG, log_content,
                             msg="1. The debug message must not be written")

            self.assertNotIn(TEST_CRITICAL, log_content,
                             msg="2. The critical message must not be written")

            self.assertNotIn(TEST_ERROR, log_content,
                             msg="3. The error message must not be written")

            self.assertNotIn(TEST_INFO, log_content,
                             msg="4. The info message must not be written")

            self.assertNotIn(TEST_LOG, log_content,
                             msg="5. The log message must not be written")

            self.assertNotIn(TEST_WARN, log_content,
                             msg="6. The warn message must not be written")

    def test_logger_wrapper_enabled(self):
        """Test the log enabled."""
        # test
        app_config = py_ac.parse_yml("tests/config/app_config.yml.good.dist")
        logger = app_config.logger
        logger.debug(TEST_DEBUG)
        logger.info(TEST_INFO)
        logger.warning(TEST_WARN)
        logger.log(logging.FATAL, TEST_LOG)

        # free the resource for the other tests
        logger.close()

        with open(LOG_FILE_PATH) as test_log_file:
            log_content = test_log_file.read()
            self.assertIn(TEST_DEBUG, log_content,
                          msg="1. The message must be written")

            self.assertIn(TEST_LOG, log_content,
                          msg="2. The log message must be written")

            self.assertIn(TEST_WARN, log_content,
                          msg="3. The warn message must be written")

            self.assertIn(TEST_INFO, log_content,
                          msg="4. The info message must be written")

    def test_error_log(self):
        """Test error log with exception raised."""
        with self.assertRaises(BadArgmentsError,
                               msg="1. The function must raise a \
                               [BadArgmentsError]"):
            app_config = py_ac.parse_yml(
                "tests/config/app_config.yml.good.dist")
            logger = app_config.logger
            logger.error(TEST_ERROR, BadArgmentsError("Args Error"))

        # free the resource for the other tests
        logger.close()

        with open(LOG_FILE_PATH) as test_log_file:
            log_content = test_log_file.read()
            self.assertIn(TEST_ERROR, log_content,
                          msg="2. The error message must be written")

    def test_critical_log(self):
        """Test critical log with exception raises."""
        with self.assertRaises(BadArgmentsError,
                               msg="1. The function must raise a \
                               [BadArgmentsError]"):
            app_config = py_ac.parse_yml(
                "tests/config/app_config.yml.good.dist")
            logger = app_config.logger
            logger.critical(TEST_CRITICAL, BadArgmentsError("Args Error"))

        # free the resource for the other tests
        logger.close()

        with open(LOG_FILE_PATH) as test_log_file:
            log_content = test_log_file.read()
            self.assertIn(TEST_CRITICAL, log_content,
                          msg="2 The critical message must be written")

    def test_clear_log(self):
        """Test clear log file content."""
        # test
        app_config = py_ac.parse_yml("tests/config/app_config.yml.good.dist")
        logger = app_config.logger
        logger.debug(TEST_DEBUG)
        logger.info(TEST_INFO)

        # free the resource for the other tests
        logger.close()

        # verify we write into the log file
        with open(LOG_FILE_PATH) as test_log_file:
            log_content = test_log_file.read()
            self.assertIn(TEST_DEBUG, log_content,
                          msg="1. The message must be written")

            self.assertIn(TEST_INFO, log_content,
                          msg="2. The info message must be written")

        # clear the log file
        logger.clear()

        with open(LOG_FILE_PATH) as test_log_file:
            log_content = test_log_file.read()
            self.assertIs('', log_content,
                          msg="3. The log content must an empty string")
