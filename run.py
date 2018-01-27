#!/usr/bin/env python
# coding: utf-8

"""
Generate ramdoms numbers for mathematical operations

Show the help:
    $ python run.py -h

"""

from pprint import pprint
from pynairus.errors import app_error as err
import pynairus.strategies.operator_strategy as ns_os

if __name__ == "__main__":
    import argparse
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument("start", type=int,
                        help="Start of the random range")
    PARSER.add_argument("end", type=int,
                        help="End of the random range")
    PARSER.add_argument("range", type=int,
                        help="Number of operations to generate")
    PARSER.add_argument("-o", "--operator", type=str,
                        help="Add an operator (default: tuple('+', '-'))")
    PARSER.add_argument("-t", "--timer", action="store_true",
                        help="Add a timer")
    PARSER.add_argument("-l", "--list_operator", action="store_true",
                        help="Display the list of operators")

    ARGS = PARSER.parse_args()

    # we show the operators list
    if ARGS.list_operator:
        print("Operators list:")
        pprint(ns_os.get_list_operator_key())
    else:
        try:
            # otherwise we launch the application
            from pynairus.pymath import pymath
            pymath(ARGS.start, ARGS.end, ARGS.range, ARGS.operator, ARGS.timer)
        except err.BadArgmentsError as exc:
            print(f"An error occured: {exc}")
            print("There is the available operators:")
            pprint(ns_os.get_list_operator_key())
