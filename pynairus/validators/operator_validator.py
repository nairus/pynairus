# coding: utf-8

"""Module for operation validation."""

from ..errors.app_error import BadArgumentError
from ..errors.app_error import ValidateError
from ..helpers.string_helper import parse_time_string, convert_seconds_to_time


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


class TimeAdditionValidator(BaseValidator):
    """Validator for time addition."""

    def get_result(self, first, second):
        """Return the result for the time addition.

            :param first:  first time
            :param second: second ttime

            :type first:  str
            :type second: str

            :return: str

            :raise ValidateError: if an error occured while parsing the args
        """

        try:
            # parse the firt time string
            first_tuple = parse_time_string(first)
            # parse the second time string
            second_tuple = parse_time_string(second)
            # add the hours, minutes and seconds
            hours = first_tuple[0] + second_tuple[0]
            mins = first_tuple[1] + second_tuple[1]
            secs = first_tuple[2] + second_tuple[2]
            # convert in seconds
            timestamp = (hours * 60 * 60) + (mins * 60) + secs
            # return the result
            return convert_seconds_to_time(timestamp)
        except BadArgumentError as error:
            raise ValidateError(
                f"An error occured while validating: {first} + {second}",
                error)


class TimeSubstractionValidator(BaseValidator):
    """Validator for substraction."""

    def get_result(self, first, second):
        """Return the result of the substraction.

            :param first:  first number
            :param second: second number

            :type first:  int
            :type second: int

            :return: int

            :raise ValidateError: if an error occured
        """
        try:
            # parse the firt time string and convert in second
            first_tuple = parse_time_string(first)
            first_seconds = (first_tuple[0] * 60 * 60) + \
                (first_tuple[1] * 60) + first_tuple[2]

            # parse the second time string and convert in second
            second_tuple = parse_time_string(second)
            second_seconds = (second_tuple[0] * 60 * 60) + \
                (second_tuple[1] * 60) + second_tuple[2]

            # verify the numbers:
            # second number must not be greater than the first one
            if second_seconds > first_seconds:
                raise ValidateError(
                    f"The first time ({first}) isn't greater than {second}")

            # return the final result
            return convert_seconds_to_time(first_seconds - second_seconds)
        except BadArgumentError as error:
            raise ValidateError(
                f"An error occured while validating: {first} - {second}",
                error)


class DivisionValidator(BaseValidator):
    """Validator for multiplication."""

    def get_result(self, first, second):
        """Return the result for the division.

            :param first:  first number
            :param second: second number

            :type first:  int
            :type second: int

            :return: str

            :raise ValidateError: if first arg isn't greater than second args
        """
        if second > first:
            message = f"The first number ({first}) isn't greater than {second}"
            raise ValidateError(message)

        quotient = first // second
        tmp_rest = first % second
        rest = f"r{tmp_rest}" if tmp_rest > 0 else ""

        return f"{quotient}{rest}"
