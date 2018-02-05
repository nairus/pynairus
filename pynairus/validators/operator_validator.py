# coding: utf-8

"""Module for operation validation."""

from ..errors.app_error import ValidateError


class BaseValidator():
    """Abstract class for validators."""

    def validate(self, answer, first, second):
        """Validate the answer.

            :param answer: the answer to validate
            :param first:  the first number of the operation
            :param second: the second number of the operation

            :type answer: int
            :type first:  int
            :type second: int

            :return: bool
        """
        return answer == self.get_result(first, second)

    def get_result(self, first, second):
        """Return the good result for the operation."""
        message = f"method not implemented for class {self.__class__.__name__}"
        raise ValidateError(message)


class AdditionValidator(BaseValidator):
    """Validator for addition."""

    def get_result(self, first, second):
        """Return the result of the addition.

            :param first:  first number
            :param second: second number

            :type first:  int
            :type second: int

            :return: int
        """
        return first + second


class SubstractionValidator(BaseValidator):
    """Validator for substraction."""

    def get_result(self, first, second):
        """Return the result of the substraction.

            :param first:  first number
            :param second: second number

            :type first:  int
            :type second: int

            :return: int
        """
        return first - second


class MultiplicationValidator(BaseValidator):
    """Validator for multiplication."""

    def get_result(self, first, second):
        """Return the result for the multiplication.

            :param first:  first number
            :param second: second number

            :type first:  int
            :type second: int

            :return: int
        """
        return first * second
