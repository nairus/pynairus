# coding: utf-8

"""Module file helper."""

from pathlib import Path
from pynairus.errors.app_error import BadArgmentsError


def get_file_path(filepath):
    """Return the path of the config file if exists.

    :param filepath: The path of the file.

    :type filepath: str

    :return: Path
    """
    real_filepath = Path(filepath)
    if not real_filepath.exists():
        raise BadArgmentsError(f"{filepath} does not exit")

    return real_filepath
