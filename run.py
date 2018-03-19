#!/usr/bin/env python
# coding: utf-8

"""
Generate ramdoms numbers for mathematical operations

Show the help:
    $ python run.py -h

"""

from pynairus.errors import app_error as err
import pynairus.strategies.operator_strategy as ns_os
from pynairus.actions.list_operators_action import ListOperatorsAction
from pynairus.actions.version_action import VersionAction

if __name__ == "__main__":
    import argparse
    PARSER = argparse.ArgumentParser()

    # Défines the positionals arguments
    PARSER.add_argument("start", type=int,
                        help="Start of the random range")
    PARSER.add_argument("end", type=int,
                        help="End of the random range")
    PARSER.add_argument("limit", type=int,
                        help="Limit of operations to generate")

    # Defines the optionnal arguments
    PARSER.add_argument("-o", "--operator", type=str,
                        help="Add an operator (default: tuple('+', '-'))")
    PARSER.add_argument("-t", "--timer", action="store_true",
                        help="Add a timer")
    PARSER.add_argument("-l", "--list_operator", action=ListOperatorsAction,
                        help="Display the list of operators and exit")
    PARSER.add_argument("-c", "--config", type=str,
                        help="Specify a config name")
    PARSER.add_argument("-V", "--version", action=VersionAction,
                        help="Display the current version and exit")

    ARGS = PARSER.parse_args()

    # we show the operators list
    try:
        # otherwise we launch the application
        from pynairus.pymath import pymath
        pymath(start=ARGS.start, end=ARGS.end, limit=ARGS.limit,
               operator=ARGS.operator, timer=ARGS.timer, config=ARGS.config)
    except err.BadArgmentsError as exc:
        print("An error occured, please see the log!")
        ns_os.display_operators_list()
