#!/usr/bin/env python
# coding: utf-8

"""Module for operation validation."""

from pynairus.errors.app_error import ValidateError


class BaseValidator():
    """Abstract class for validators."""

    def validate(self, answer, first, second):
        """Validate method to overwrite."""
        return answer == self.get_result(first, second)

    def get_result(self, first, second):
        """Return the good result for the operation."""
        message = f"method not implemented for class {self.__class__.__name__}"
        raise ValidateError(message)


class AdditionValidator(BaseValidator):
    """Validator for addition."""

    def get_result(self, first, second):
        """Return the result of the addition."""
        return first + second


class SubstractionValidator(BaseValidator):
    """Validator for substraction."""

    def get_result(self, first, second):
        """Return the result of the substraction."""
        return first - second


class MultiplicationValidator(BaseValidator):
    """Validator for multiplication."""

    def get_result(self, first, second):
        """Return the result for the multiplication."""
        return first * second
