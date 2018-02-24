# coding: utf-8

"""Module list operators action."""

import argparse
import pynairus.strategies.operator_strategy as ns_os


class ListOperatorsAction(argparse.Action):
    """Class for listing operators."""

    def __init__(self, option_strings, dest, **kwargs):
        """Constructor."""
        kwargs["nargs"] = 0

        super().__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_strings=None):
        """Call action"""
        ns_os.display_operators_list()
        parser.exit()
