# coding: utf-8

"""Module version action."""

import argparse
import pprint
from .. import __version__ as v, __author__ as a, __year__ as y


class VersionAction(argparse.Action):
    """Class for version action"""

    def __init__(self, *args, **kwargs):
        """Constructor."""
        kwargs["nargs"] = 0

        super().__init__(*args, **kwargs)

    def __call__(self, parser, namespace, values, option_strings=None):
        """Call action"""
        pprint.pprint(f"current version: {v} / author : {a} ({y})")
        parser.exit()
