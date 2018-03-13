# coding: utf-8

"""Module for application errors."""


class ConfigError(Exception):
    """Raised in case of bad config parsing."""
    pass


class BadArgmentsError(Exception):
    """Raised in case of bad arguments passed."""
    pass


class ValidateError(Exception):
    """Raised if the validate method is not implemented."""
    pass


class ComputeError(Exception):
    """Raised if compute methode is not implemented."""
    pass


class StrategyError(Exception):
    """Raises when generate_random is not implemented."""
    pass
