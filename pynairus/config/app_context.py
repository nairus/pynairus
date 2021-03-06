# coding: utf-8

"""Application context module."""

import re
from pathlib import Path
from .. import config
from . import app_config as af
from ..errors.app_error import ConfigError


# regex for detecting the type of config to load
ALLOWED_FILE_EXTENSION = re.compile(
    r"[a-zA-Z-_]+\.(?P<extension>ini|json|xml|yml)")

# dictionary for config parse function
CONFIG_PARSER_DICT = {
    "ini": af.parse_ini,
    "json": af.parse_json,
    "yml": af.parse_yml,
    "xml": af.parse_xml
}


class AppContext():
    """Application context holder class."""

    # singleton of the class
    __singleton = None

    def __new__(cls, *args, **kwargs):
        """Return the singleton of application context."""
        # if there is no singleton, we create one.
        if cls.__singleton is None:
            instance = object.__new__(cls)

            # store the positional args.
            instance.app_config, *_ = args
            instance.start = kwargs.get("start")
            instance.end = kwargs.get("end")
            instance.limit = kwargs.get("limit")

            # clean the positional args.
            [kwargs.pop(key) for key in ['start', 'end', 'limit']]

            # store the optionnal args.
            instance.options = kwargs

            # store the singleton in the class property.
            cls.__singleton = instance

        return cls.__singleton

    @classmethod
    def get_instance(cls):
        """
        Return the singleton of AppContext.

        :return AppContext: the singleton of AppContext
        """
        return cls.__singleton

    @classmethod
    def clearContext(cls):
        cls.__singleton = None

    @property
    def app_config(self):
        return self._app_config

    @app_config.setter
    def app_config(self, app_config):
        if not isinstance(app_config, af.AppConfig):
            raise TypeError(f"{app_config} is not an instance of [AppConfig]")

        self._app_config = app_config

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, val):
        if not isinstance(val, int):
            raise TypeError(f"{val} is not an [int]")

        self._start = val

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, val):
        if not isinstance(val, int):
            raise TypeError(f"{val} is not an [int]")

        self._end = val

    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, val):
        if not isinstance(val, int):
            raise TypeError(f"{val} is not an [int]")

        self._limit = val

    @property
    def options(self):
        """Returns the options dict.

        :return: dict
        """
        return self._options

    @options.setter
    def options(self, options):
        """Defines the options dict of the context.

        :param options: the options dict of the context.

        :type options: dict

        :raise TypeError: if the args is not a dict.
        """
        if not isinstance(options, dict):
            raise TypeError(f"{options} is not an instance of [dict]")

        self._options = options


def get_config_parser(config_name=None):
    """Return the parser function for the config chosen.

        :param config_name: the name of the config file.

        :type config_name: str

        :return: function

        :raises ConfigError: In case of config not allowed
    """
    if config_name is None:
        return CONFIG_PARSER_DICT["yml"]

    result = ALLOWED_FILE_EXTENSION.fullmatch(config_name)
    if result is None:
        raise ConfigError(f"config [{config_name}] not allowed!")

    ext_file = result.group("extension")
    return CONFIG_PARSER_DICT[ext_file]


def init_app_context(**kwargs):
    """Init the application context.

    :param kwargs: the application options

    :type kwargs: dict

    :return: AppContext
    """
    # if the context doesn't exist, init the app context
    app_context = AppContext.get_instance()
    if app_context is None:
        # get the config name if specified.
        config_name = kwargs.get("config")

        # get the config_parser function
        config_parser = get_config_parser(config_name=config_name)

        # defines the config path
        config_path = None
        if config_name is not None:
            config_path = Path(config.CONFIG_FOLDER, config_name)

        # parse the config.
        app_config = config_parser(filepath=config_path)

        # clear the log if enabled
        if app_config.clear_onstart:
            app_config.logger.clear()

        # create and return the singleton of AppContext
        return AppContext(app_config, **kwargs)

    # otherwise update the positional args of the context
    app_context.start = kwargs.get("start")
    app_context.end = kwargs.get("end")
    app_context.limit = kwargs.get("limit")

    # clean the positional args.
    [kwargs.pop(key) for key in ['start', 'end', 'limit']]

    # update the optional args.
    app_context.options = kwargs

    # clear the log if enabled
    app_config = app_context.app_config
    if app_config.clear_onstart:
        app_config.logger.clear()

    return app_context
