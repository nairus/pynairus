# coding: utf-8

"""Module file helper."""

from pathlib import Path


def get_file_path(filepath):
    """Return the path of the config file if exists.

    :param filepath: The path of the file.

    :type filepath: str

    :return: Path

    :raises: FileNotFoundError if filepath does not exist
    """
    real_filepath = Path(filepath)
    if not real_filepath.exists():
        raise FileNotFoundError(f"{filepath} does not exist")

    return real_filepath
