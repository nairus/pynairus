# coding: utf-8

"""Application config module"""

from pathlib import Path
import logging
import logging.config
from ..helpers.file_helper import get_file_path
from ..errors.app_error import BadArgmentsError


class AppLogger():
    """Descriptor for the app logger."""

    def __get__(self, inst, insttype):
        """"Getter for the _logger property."""
        return inst._logger

    def __set__(self, inst, logger):
        """Setter for the _logger property."""
        if logger is None:
            raise BadArgmentsError(
                f"logger arg must be an instance of Logger class: None given")

        inst._logger = logger


class AppConfig():
    """Application config class."""

    def __init__(self, logger, log_enabled=False):
        """Constructor.

        :param log_enabled: Activate the logging and raising exception
        :param logger: The app logger instance

        :type log_enabled: bool
        :type logger: logging.Logger
        """
        self._log_enabled = log_enabled
        self.logger = logger

        logging.raiseExceptions = log_enabled

    @property
    def log_enabled(self):
        """Getter of the property "log_enabled"."""
        return self._log_enabled

    @log_enabled.setter
    def set_log_enabled(self, log_enabled):
        """Setter of the property "log_enabled"."""
        self._log_enabled = bool(log_enabled)

    logger = AppLogger()


def parse_yml(filename=None):
    """Parse the yml config file.

    :return: AppConfig
    """
    import yaml

    if filename is None:
        # set the default config file
        filename = "pynairus/config/app_config.yml.dist"

    app_config_path = get_file_path(filename)
    with open(app_config_path, "r") as ymlfile:
        yml_app_config_file = yaml.load(ymlfile)

        if "log" not in yml_app_config_file:
            raise KeyError("[log] section is missing")

    log_config = yml_app_config_file.get("log")
    log_enabled = log_config.get("enabled")
    logger_name = log_config.get("logger_name")
    log_config_name = log_config.get("config_name")
    log_config_path = get_file_path(f"pynairus/config/{log_config_name}")

    with open(log_config_path, "r") as log_config_file:
        yml_log_config = yaml.load(log_config_file)

        logging.config.dictConfig(yml_log_config)
        logger = logging.getLogger(logger_name)
        return AppConfig(logger, log_enabled=log_enabled)


def parse_ini(filename=None):
    """Parse the ini config file.

    :return: AppConfig
    """
    if filename is None:
        # set the default config file
        # to use another config file,
        # copy it without the `dist` extension,
        # ignore it in you git repos
        # and all this function with your config filepath.
        filename = "pynairus/config/app_config.ini.dist"

    app_config_path = get_file_path(filename)

    with open(app_config_path.absolute()) as f:
        import configparser
        config_parser = configparser.ConfigParser()
        config_parser.read_file(f)
        if not config_parser.has_section("log"):
            raise KeyError("[log] section is missing")

        log_enabled = config_parser.getboolean("log", "enabled")
        config_name = config_parser.get("log", "config_name")
        logger_name = config_parser.get("log", "logger_name")

        return AppConfig(__init_logger(config_name, logger_name),
                         log_enabled)


def parse_json(filename=None):
    """Parse the json file.

    :return: AppConfig
    """
    if filename is None:
        # set default config file
        filename = "pynairus/config/app_config.json.dist"

    app_config_path = get_file_path(filename)

    with open(app_config_path) as json_config_file:
        import json
        config_datas = json.load(json_config_file)

        if "log" not in config_datas:
            raise KeyError("[log] section is missing")

        log_enabled, config_name, logger_name = config_datas.get(
            "log").values()

        return AppConfig(__init_logger(config_name, logger_name),
                         log_enabled)


def parse_xml(filename="app_config.xml"):
    """Parse the xml file.

    :return: AppConfig
    """
    pass


def __init_logger(config_name, logger_name):
    """Init the app logger with ini config.
    Internal function, doo not call !

    :param config_name: the name of the config file
    :param logger_name: the name of the app logger

    :type config_name: str
    :type logger_name: str

    :return: logging.Logger
    """
    logging.config.fileConfig(Path(f"pynairus/config/{config_name}"))
    return logging.getLogger(logger_name)
