#!/usr/bin/env python
# coding: utf-8

"""Unit tests for operator validator."""

import unittest
import pynairus.validators.operator_validator as ov
from pynairus.errors.app_error import ValidateError


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

    def test_substraction_validate(self):
        """Test the SubstractionValidator.validate method."""
        validator = ov.SubstractionValidator()
        self.assertIsInstance(validator, ov.BaseValidator)
        self.assertTrue(validator.validate(2, 3, 1))
        self.assertFalse(validator.validate(2, 2, 1))

    def test_multiplication_validate(self):
        """Test the MultiplicationValidator.validate method."""
        validator = ov.MultiplicationValidator()
        self.assertIsInstance(validator, ov.BaseValidator)
        self.assertTrue(validator.validate(9, 3, 3))
        self.assertFalse(validator.validate(8, 3, 3))
