# coding: utf-8

"""Application context module."""

from ..config.app_config import AppConfig

# config folder path
CONFIG_FOLDER_PATH = "pynairus/config/"


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

            # store the option args.
            instance.options = kwargs

            # store the singleton in the class property.
            cls.__singleton = instance

        return AppContext.__singleton

    @classmethod
    def init_instance(cls, app_config, **kwargs):
        """Initialisation of the application context instance.

        :param app_config: Application config.
        :param kwargs: Arguments of the application.

        :type app_config: AppConfig
        :type kwargs: dict
        """
        # store application config
        inst = cls.__singleton

    @property
    def app_config(self):
        return self._app_config

    @app_config.setter
    def app_config(self, app_config):
        if not isinstance(app_config, AppConfig):
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


def init_app_context(*args, **kwargs):
    """Init the application context."""
    pass
