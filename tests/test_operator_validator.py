# coding: utf-8

"""Unit tests for operator validator."""

import unittest
import pynairus.validators.operator_validator as ov
from pynairus.errors.app_error import ValidateError
from pynairus.errors.app_error import BadArgumentError


class ValidatorsTest(unittest.TestCase):
    """Unit tests for all Validator classes."""

    def test_base_validator(self):
        """Test the base validator."""

        with self.assertRaisesRegex(ValidateError, "ValidatorTest"):
            class ValidatorTest(ov.BaseValidator):
                """Testing class for BaseValidator."""
                pass

            validator_test = ValidatorTest()
            validator_test.validate(1, 2, 2)

    def test_addition_validate(self):
        """Test the AdditionValidator.validate method."""
        validator = ov.AdditionValidator()
        self.assertIsInstance(validator, ov.BaseValidator)
        self.assertTrue(validator.validate(2, 1, 1))
        self.assertFalse(validator.validate(2, 2, 1))

        with self.assertRaises(ValueError):
            validator.validate("a", 1, 1)

    def test_substraction_validate(self):
        """Test the SubstractionValidator.validate method."""
        validator = ov.SubstractionValidator()
        self.assertIsInstance(validator, ov.BaseValidator)
        self.assertTrue(validator.validate(2, 3, 1))
        self.assertFalse(validator.validate(2, 2, 1))

        with self.assertRaises(ValueError):
            validator.validate("a", 1, 1)

    def test_multiplication_validate(self):
        """Test the MultiplicationValidator.validate method."""
        validator = ov.MultiplicationValidator()
        self.assertIsInstance(validator, ov.BaseValidator)
        self.assertTrue(validator.validate(9, 3, 3))
        self.assertFalse(validator.validate(8, 3, 3))

        with self.assertRaises(ValueError):
            validator.validate("a", 2, 2)

    def test_division_validate(self):
        """Test the DivisionValidator.validate method."""
        validator = ov.DivisionValidator()
        self.assertIsInstance(validator, ov.BaseValidator)
        self.assertTrue(validator.validate("8r1", 65, 8))
        self.assertTrue(validator.validate("8", 64, 8))
        with self.assertRaisesRegex(
            ValidateError,
            r"The first number \(8\) isn't greater than 9"
        ):
            validator.validate(None, 8, 9)

    def test_time_addition_validate(self):
        """Test the TimeAdditionValidator.validate method."""
        validator = ov.TimeAdditionValidator()
        self.assertIsInstance(validator, ov.BaseValidator)
        self.assertTrue(validator.validate("1h31m10s", "50m56s", "40m14s"))
        self.assertTrue(validator.validate("51m10s", "30m56s", "20m14s"))
        self.assertFalse(validator.validate("50m10s", "30m56s", "20m14s"))
        with self.assertRaisesRegex(
            ValidateError,
            r"An error occured while validating: 50m \+ 40m14s"
        ) as ctx:
            validator.validate(None, "50m", "40m14s")

        self.assertEqual(2, len(ctx.exception.args))
        self.assertIsInstance(ctx.exception.args[1], BadArgumentError)

    def test_time_substraction_validate(self):
        """Test the TimeSubstractionValidator.validate method."""
        validator = ov.TimeSubstractionValidator()
        self.assertIsInstance(validator, ov.BaseValidator)
        self.assertTrue(validator.validate("1h30m10s", "2h10m20s", "40m10s"))
        self.assertTrue(validator.validate("30m10s", "1h10m20s", "40m10s"))

        # test parsing time try/except parsing exception
        with self.assertRaisesRegex(
            ValidateError,
            r"An error occured while validating: 50m \- 40m14s"
        ) as ctx:
            validator.validate(None, "50m", "40m14s")

        self.assertEqual(2, len(ctx.exception.args))
        self.assertIsInstance(ctx.exception.args[1], BadArgumentError)

        # test raise exception in case of bad numbers
        with self.assertRaisesRegex(
            ValidateError,
            r"The first time \(50m10s\) isn't greater than 1h10m14s"
        ) as ctx2:
            validator.validate(None, "50m10s", "1h10m14s")

        self.assertEqual(1, len(ctx2.exception.args))
