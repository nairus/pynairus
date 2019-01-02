# coding: utf-8

"""Unit tests for operator strategy module."""

import unittest
from pynairus.strategies import operator_strategy as py_os
from pynairus.validators import operator_validator as py_ov
from pynairus.errors import app_error as py_err


class OperatorStrategyTest(unittest.TestCase):
    """Unit test of the operator strategy module."""

    def test_compute_numbers(self):
        """Test of the ComputeNumbers class."""
        validator = py_ov.AdditionValidator()
        compute_number = py_os.ComputeNumbers(2, 2,
                                              '+', validator)

        self.assertEqual(2, compute_number.first)
        self.assertEqual(2, compute_number.second)
        self.assertEqual('+', compute_number.operator)
        self.assertIs(validator, compute_number.validator)
        self.assertEqual("2 + 2 = ?", compute_number.__repr__())
        self.assertTrue(compute_number.validate(4))
        self.assertFalse(compute_number.validate(3))
        self.assertEqual(4, compute_number.get_good_result())

    def test_get_operators_list(self):
        """Test of the get_operators_list function."""
        operators = py_os.get_operators_list()
        self.assertEqual(9, len(operators))

    def test_base(self):
        """Test of the BaseStrategy."""

        class StrategyTest(py_os.BaseStrategy):
            """Test class for BaseStrategy."""

        with self.assertRaisesRegex(py_err.StrategyError, 'StrategyTest'):
            strategy_test = StrategyTest(py_ov.AdditionValidator())
            strategy_test.generate_random(1, 2)

        strategy_test = StrategyTest(py_ov.AdditionValidator())
        validator = strategy_test.get_validator()
        self.assertIsInstance(validator, py_ov.AdditionValidator)

    def test_addition(self):
        """Test of the AdditionStrategy."""
        strategy = py_os.AdditionStrategy(py_ov.AdditionValidator())

        self.assertIsInstance(strategy, py_os.BaseStrategy,
                              msg="instance of BaseStrategy expected")

        with self.assertRaises(ValueError):
            strategy.generate_random(99, 50)

        # we generate 100 tests
        for i in range(100):
            test_num = i + 1

            numbers = strategy.generate_random(10, 99)

            self.assertIsInstance(numbers, py_os.ComputeNumbers,
                                  msg=f"{test_num}.1 instance of ComputeNumbers expected")

            self.assertTrue(10 <= numbers.first <= 99,
                            msg=f"{test_num}.2 the left number must be between 10 and 99")

            self.assertTrue(10 <= numbers.second <= 99,
                            msg=f"{test_num}.3 the right number must be between 10 and 99")

            result = numbers.first + numbers.second
            self.assertEqual(result, numbers.get_good_result(),
                             msg=f"{test_num}.4 the result must be correct")

    def test_substraction(self):
        """Test of the SubstractionStrategy."""
        strategy = py_os.SubstractionStrategy(py_ov.SubstractionValidator())

        self.assertIsInstance(strategy, py_os.BaseStrategy,
                              msg=f"instance of BaseStrategy expected")

        with self.assertRaises(ValueError):
            strategy.generate_random(99, 50)

        # we generate 100 tests
        for i in range(100):
            test_num = i + 1

            numbers = strategy.generate_random(10, 99)

            self.assertIsInstance(numbers, py_os.ComputeNumbers,
                                  msg=f"{test_num}.1 instance of ComputeNumbers expected")

            self.assertTrue(10 <= numbers.first <= 99,
                            msg=f"{test_num}.2 the left number must be between 10 and 99")

            self.assertTrue(10 <= numbers.second <= 99,
                            msg=f"{test_num}.3 the right number must be between 10 and 99")

            self.assertTrue(numbers.first >= numbers.second,
                            msg=f"{test_num}.4 the left number must be >= than the right number")

            result = numbers.first - numbers.second
            self.assertEqual(result, numbers.get_good_result(),
                             msg=f"{test_num}.5 the result must be correct")

    def test_mutliplication_table(self):
        """Test of MutliplicationTableStrategy."""
        strategy = py_os.MutliplicationTableStrategy(
            py_ov.MultiplicationValidator())

        self.assertIsInstance(strategy, py_os.BaseStrategy,
                              msg="instance of BaseStrategy expected")

        err_msg = "the start param must be between 1 and 10 included: 12 given"
        with self.assertRaisesRegex(py_err.BadArgumentError, err_msg):
            strategy.generate_random(12, 10)

        err_msg = "the end param must be between 1 and 10 included: 11 given"
        with self.assertRaisesRegex(py_err.BadArgumentError, err_msg):
            strategy.generate_random(10, 11)

        # we generate 100 tests
        for i in range(100):
            test_num = i + 1

            numbers = strategy.generate_random(1, 4)
            self.assertTrue(1 <= numbers.first <= 4,
                            msg=f"{test_num}.1 the first number must be between 1 and 4")

            self.assertTrue(1 <= numbers.second <= 10,
                            msg=f"{test_num}.2 the second number must be between 1 and 10")

            result = numbers.first * numbers.second
            self.assertEqual(result, numbers.get_good_result(),
                             msg=f"{test_num}.3 the result must be correct")

    def test_simple_multiplication(self):
        """Test of SimpleMutliplicationStrategy."""
        strategy = py_os.SimpleMutliplicationStrategy(
            py_ov.MultiplicationValidator())

        self.assertIsInstance(strategy, py_os.BaseStrategy,
                              msg="instance of BaseStrategy expected")

        # we generate 100 tests
        for i in range(100):
            test_num = i + 1

            numbers = strategy.generate_random(10, 99)
            self.assertTrue(10 <= numbers.first <= 99,
                            msg=f"{test_num}.1 the first number must be between 10 and 99")

            self.assertTrue(1 <= numbers.second <= 10,
                            msg=f"{test_num}.2 the second number must be between 1 and 10")

            result = numbers.first * numbers.second
            self.assertEqual(result, numbers.get_good_result(),
                             msg=f"{test_num}.3 the result must be correct")

    def test_complex_multiplication(self):
        """Test of ComplexMutliplicationStrategy."""
        strategy = py_os.ComplexMutliplicationStrategy(
            py_ov.MultiplicationValidator())

        self.assertIsInstance(strategy, py_os.BaseStrategy,
                              msg="instance of BaseStrategy expected")

        # we generate 100 tests
        for i in range(100):
            test_num = i + 1

            numbers = strategy.generate_random(10, 99)
            self.assertTrue(10 <= numbers.first <= 99,
                            msg=f"{test_num}.1 the first number must be between 10 and 99")

            self.assertTrue(10 <= numbers.second <= 99,
                            msg=f"{test_num}.2 the second number must be between 10 and 99")

            result = numbers.first * numbers.second
            self.assertEqual(result, numbers.get_good_result(),
                             msg=f"{test_num}.3 the result must be correct")

    def test_app_strategies(self):
        """Functionnal tests for all app strategies."""
        self.assertEqual(9, len(py_os.STRATEGIES),
                         msg="must contains 9 strategies.")

        # testing addition strategy
        self.assertIn(py_os.ADD_OPERATOR_KEY, py_os.STRATEGIES)
        add_strategy = py_os.STRATEGIES[py_os.ADD_OPERATOR_KEY]
        self.assertIsInstance(add_strategy, py_os.AdditionStrategy,
                              msg="instance of AdditionStrategy expected")
        self.assertIsInstance(add_strategy.get_validator(),
                              py_ov.AdditionValidator,
                              msg="instance of AdditionValidator expected")

        # testing substraction strategy
        self.assertIn(py_os.MULT_TABLE_OPERATOR_KEY, py_os.STRATEGIES)
        sub_strategy = py_os.STRATEGIES[py_os.SUB_OPERATOR_KEY]
        self.assertIsInstance(sub_strategy, py_os.SubstractionStrategy,
                              msg="instance of AdditionStrategy expected")
        self.assertIsInstance(sub_strategy.get_validator(),
                              py_ov.SubstractionValidator,
                              msg="instance of AdditionValidator expected")

        # testing table multiplication strategy
        self.assertIn(py_os.MULT_TABLE_OPERATOR_KEY, py_os.STRATEGIES)
        mult_table_strategy = py_os.STRATEGIES[py_os.MULT_TABLE_OPERATOR_KEY]
        self.assertIsInstance(mult_table_strategy,
                              py_os.MutliplicationTableStrategy)
        self.assertIsInstance(mult_table_strategy.get_validator(),
                              py_ov.MultiplicationValidator)

        # testing simple multiplication strategy
        self.assertIn(py_os.SIMPLE_MULT_OPERATOR_KEY, py_os.STRATEGIES)
        simple_mult_strategy = py_os.STRATEGIES[py_os.SIMPLE_MULT_OPERATOR_KEY]
        self.assertIsInstance(simple_mult_strategy,
                              py_os.SimpleMutliplicationStrategy)
        self.assertIsInstance(simple_mult_strategy.get_validator(),
                              py_ov.MultiplicationValidator)

        # testing complex multiplication strategy
        self.assertIn(py_os.COMPLEX_MULT_OPERATOR_KEY, py_os.STRATEGIES)
        complex_mult_strategy = py_os.STRATEGIES[py_os.COMPLEX_MULT_OPERATOR_KEY]
        self.assertIsInstance(complex_mult_strategy,
                              py_os.ComplexMutliplicationStrategy)
        self.assertIsInstance(complex_mult_strategy.get_validator(),
                              py_ov.MultiplicationValidator)
