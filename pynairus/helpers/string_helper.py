# coding: utf-8


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
