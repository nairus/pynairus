# coding: utf-8

"""Module file helper."""

from pathlib import Path


def get_file_path(filepath):
    """Return the path of the config file if exists.

    :param filepath: The path of the file.

    :type filepath: str|Path

    :return: Path

    :raises: FileNotFoundError if file path does not exist
    """
    if type(filepath) is str:
        real_filepath = Path(filepath)
    elif isinstance(filepath, Path):
        real_filepath = filepath
    else:
        real_filepath = None

    if real_filepath is None or not real_filepath.exists():
        raise FileNotFoundError(f"{filepath} does not exist")

    return real_filepath
