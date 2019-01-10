# coding: utf-8
import re
from ..errors.app_error import BadArgumentError

"""Strings helper module."""

# allowed string values for boolean conversion.
STR_BOOL_VALS = {
    "1": True,
    "true": True,
    "t": True,
    "yes": True,
    "y": True,
    "0": False,
    "false": False,
    "f": False,
    "no": False,
    "n": False
}

# regex for parsing time string.
TIME_PARSING_REGEX = re.compile(
    r"((?P<hour>[\d]+)h)?((?P<minute>[\d]+)m)?(?P<second>[\d]+)s")


def get_bool_from_str(val):
    """Return the bool values for a string.
    The string is case insensitive.

    :param val: the string value

    :type val: str

    :return: bool

    :raises KeyError: if the string value is not allowed
    """
    cleaned_val = val.lower()
    if cleaned_val not in STR_BOOL_VALS:
        raise KeyError(f"key [{val}] not exists")

    return STR_BOOL_VALS[cleaned_val]


def parse_time_string(time):
    """Parse the time string and return a tuple with 3 values.

    Example: parse_time_string("1h52m34s") will output (1, 52, 34).

    :param time: the string to parse

    :type time: str

    :return: tuple

    :raises BadArgumentError: if the string cannot be parsed
    """

    result = TIME_PARSING_REGEX.fullmatch(time)

    if result is None:
        raise BadArgumentError(f"The time [{time}] can't be parsed")

    hour = int(result.group("hour")) if result.group("hour") is not None else 0
    minute = int(result.group("minute")) if result.group(
        "minute") is not None else 0
    second = int(result.group("second"))

    return (hour, minute, second)


def convert_seconds_to_time(timestamp):
    """Convert seconds to time string.
        Example: 1501 => 25m01s
    """
    # raise an error if the number is greater than a day
    if timestamp > (24 * 60 * 60):
        raise BadArgumentError(f"The timestamp is greater than a day")

    # raise an error if the number is lower than one second
    if timestamp < 1:
        raise BadArgumentError(f"The timestamp is lower than one second")

    # caculate the seconds
    secs = timestamp % 60
    # caculate the minutes
    tmp_mins = timestamp // 60 % 60
    mins = f"{tmp_mins:02d}m" if tmp_mins > 0 else ""
    # calculate the hours
    tmp_hours = timestamp // 60 // 60
    hours = f"{tmp_hours}h" if tmp_hours > 0 else ""

    return f"{hours}{mins}{secs:02d}s"
