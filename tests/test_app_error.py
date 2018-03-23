# coding: utf-8

"""Unit tests module for errors.app_error module."""

import unittest

from pynairus.errors import app_error as py_ae


class AppErrorTest(unittest.TestCase):
    """Unit tests for all errors."""

    def test_bad_argments_error(self):
        """Test the inheritance of BadArgmentsError class."""
        self.assertIsInstance(py_ae.BadArgmentsError(), Exception)

    def test_validate_error(self):
        """Test the inheritance of ValidateError class."""
        self.assertIsInstance(py_ae.ValidateError(), Exception)

    def test_compute_error(self):
        """Test the inheritance of ComputeError class."""
        self.assertIsInstance(py_ae.ComputeError(), Exception)

    def test_strategy_error(self):
        """Test the inheritance of StrategyError class."""
        self.assertIsInstance(py_ae.StrategyError(), Exception)
