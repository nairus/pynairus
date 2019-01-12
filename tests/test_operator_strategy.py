# coding: utf-8

"""Unit tests for operator strategy module."""

import unittest
from pynairus.helpers.string_helper import parse_time_string, convert_seconds_to_time
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
                                  f"{test_num}.1 instance of ComputeNumbers expected")

            self.assertTrue(10 <= numbers.first <= 99,
                            f"{test_num}.2 the left number has to be between 10 and 99")

            self.assertTrue(10 <= numbers.second <= 99,
                            f"{test_num}.3 the right number has to be between 10 and 99")

            result = numbers.first + numbers.second
            self.assertEqual(result, numbers.get_good_result(),
                             f"{test_num}.4 the result has to be correct")

    def test_substraction(self):
        """Test of the SubstractionStrategy."""
        strategy = py_os.SubstractionStrategy(py_ov.SubstractionValidator())

        self.assertIsInstance(strategy, py_os.BaseStrategy,
                              f"instance of BaseStrategy expected")

        with self.assertRaises(ValueError):
            strategy.generate_random(99, 50)

        # we generate 100 tests
        for i in range(100):
            test_num = i + 1

            numbers = strategy.generate_random(10, 99)

            self.assertIsInstance(numbers, py_os.ComputeNumbers,
                                  f"{test_num}.1 instance of ComputeNumbers expected")

            self.assertTrue(10 <= numbers.first <= 99,
                            f"{test_num}.2 the left number has to be between 10 and 99")

            self.assertTrue(10 <= numbers.second <= 99,
                            f"{test_num}.3 the right number has to be between 10 and 99")

            self.assertTrue(numbers.first >= numbers.second,
                            f"{test_num}.4 the left number has to be >= than the right number")

            result = numbers.first - numbers.second
            self.assertEqual(result, numbers.get_good_result(),
                             f"{test_num}.5 the result has to be correct")

    def test_mutliplication_table(self):
        """Test of MutliplicationTableStrategy."""
        strategy = py_os.MutliplicationTableStrategy(
            py_ov.MultiplicationValidator())

        self.assertIsInstance(strategy, py_os.BaseStrategy,
                              msg="instance of BaseStrategy expected")

        err_msg = "the start param has to be between 1 and 10 included: 12 given"
        with self.assertRaisesRegex(py_err.BadArgumentError, err_msg):
            strategy.generate_random(12, 10)

        err_msg = "the end param has to be between 1 and 10 included: 11 given"
        with self.assertRaisesRegex(py_err.BadArgumentError, err_msg):
            strategy.generate_random(10, 11)

        # we generate 100 tests
        for i in range(100):
            test_num = i + 1

            numbers = strategy.generate_random(1, 4)
            self.assertTrue(1 <= numbers.first <= 4,
                            f"{test_num}.1 the first number has to be between 1 and 4")

            self.assertTrue(1 <= numbers.second <= 10,
                            f"{test_num}.2 the second number has to be between 1 and 10")

            result = numbers.first * numbers.second
            self.assertEqual(result, numbers.get_good_result(),
                             f"{test_num}.3 the result has to be correct")

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
                            f"{test_num}.1 the first number has to be between 10 and 99")

            self.assertTrue(1 <= numbers.second < 10,
                            f"{test_num}.2 the second number has to be between 1 and 9")

            result = numbers.first * numbers.second
            self.assertEqual(result, numbers.get_good_result(),
                             f"{test_num}.3 the result has to be correct")

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
                            f"{test_num}.1 the first number has to be between 10 and 99")

            self.assertTrue(10 <= numbers.second <= 99,
                            f"{test_num}.2 the second number has to be between 10 and 99")

            result = numbers.first * numbers.second
            self.assertEqual(result, numbers.get_good_result(),
                             f"{test_num}.3 the result has to be correct")

    def test_single_divisor(self):
        """Test of SingleDivisorStrategy."""
        strategy = py_os.SingleDivisorStrategy(
            py_ov.DivisionValidator())

        self.assertIsInstance(strategy, py_os.BaseStrategy,
                              msg="instance of BaseStrategy expected")

        # we generate 1000 tests
        for i in range(1000):
            test_num = i + 1

            numbers = strategy.generate_random(1, 99)

            self.assertIsNotNone(
                numbers, f"{test_num}.1 the numbers has not to be None")

            self.assertTrue(1 <= numbers.first <= 99,
                            f"{test_num}.2 the dividend has to be between 1 and 99")

            self.assertTrue(1 < numbers.second < 10,
                            f"{test_num}.3 the divisor has to be between 2 and 9: {numbers.second} given")

            self.assertTrue(numbers.second <= numbers.first,
                            f"{test_num}.4 the dividend has to be greater than equal the divisor: {numbers} given.")

            # calculate the result expected
            quotient = numbers.first // numbers.second
            tmp_rest = numbers.first % numbers.second
            rest = f"r{tmp_rest}" if tmp_rest > 0 else ""
            result = f"{quotient}{rest}"

            # verify the result calculated by the strategy
            self.assertEqual(result, numbers.get_good_result(),
                             f"{test_num}.5 The result expected is not ok")

    def test_double_divisor(self):
        """Test of DoubleDivisorStrategy."""
        strategy = py_os.DoubleDivisorStrategy(
            py_ov.DivisionValidator())

        self.assertIsInstance(strategy, py_os.BaseStrategy,
                              msg="instance of BaseStrategy expected")

        # we generate 1000 tests
        for i in range(1000):
            test_num = i + 1

            numbers = strategy.generate_random(10, 999)

            self.assertIsNotNone(
                numbers, f"{test_num}.1 the numbers has not to be None")

            self.assertTrue(10 <= numbers.first <= 999,
                            f"{test_num}.2 the dividend has to be between 10 and 999")

            self.assertTrue(10 <= numbers.second <= 99,
                            f"{test_num}.3 the divisor has to be between 10 and 99: {numbers.second} given")

            self.assertTrue(numbers.second <= numbers.first,
                            f"{test_num}.4 the dividend has to be greater than the divisor: {numbers} given.")

            # calculate the result expected
            quotient = numbers.first // numbers.second
            tmp_rest = numbers.first % numbers.second
            rest = f"r{tmp_rest}" if tmp_rest > 0 else ""
            result = f"{quotient}{rest}"

            # verify the result calculated by the strategy
            self.assertEqual(result, numbers.get_good_result(),
                             f"{test_num}.4 The result expected is not ok")

    def test_time_addition_strategy(self):
        """Test of TimeAdditionStrategy."""
        strategy = py_os.TimeAdditionStrategy(py_ov.TimeAdditionValidator())

        self.assertIsInstance(strategy, py_os.BaseStrategy,
                              msg="instance of BaseStrategy expected")

        # we generate 100 tests
        for i in range(100):
            test_num = i + 1

            # generate timestamp between 1 minute and one hour
            numbers = strategy.generate_random(60, 3600)

            self.assertIs(type(numbers.first), str,
                          f"{test_num}.1 The 1st num. has to be a string")
            self.assertIs(type(numbers.second), str,
                          f"{test_num}.2 The 2nd num. has to be a string")

            # calculate the expected result
            first_tuple = parse_time_string(numbers.first)
            second_tuple = parse_time_string(numbers.second)
            hours = first_tuple[0] + second_tuple[0]
            mins = first_tuple[1] + second_tuple[1]
            secs = first_tuple[2] + second_tuple[2]
            timestamp = (hours * 60 * 60) + (mins * 60) + secs
            result_expected = convert_seconds_to_time(timestamp)

            self.assertEqual(result_expected, numbers.get_good_result(),
                             f"{test_num}.3 The result expected is not ok")

    def test_time_substraction_strategy(self):
        """Test of TimeSubstractionStrategy."""
        strategy = py_os.TimeSubstractionStrategy(
            py_ov.TimeSubstractionValidator())

        self.assertIsInstance(strategy, py_os.BaseStrategy,
                              msg="instance of BaseStrategy expected")

        # we generate 100 tests
        for i in range(100):
            test_num = i + 1

            # generate timestamp between 1 minute and one hour
            numbers = strategy.generate_random(60, 3600)

            self.assertIs(type(numbers.first), str,
                          f"{test_num}.1 The 1st num. has to be a string")
            self.assertIs(type(numbers.second), str,
                          f"{test_num}.2 The 2nd num. has to be a string")

            # calculate the expected result
            first_tuple = parse_time_string(numbers.first)
            second_tuple = parse_time_string(numbers.second)
            first_h, first_m, first_s = first_tuple
            second_h, second_m, second_s = second_tuple

            first_t = (first_h * 60 * 60) + (first_m * 60) + first_s
            second_t = (second_h * 60 * 60) + (second_m * 60) + second_s

            self.assertTrue(first_t > second_t,
                            f"{test_num}.3 The first number [{numbers.first}] has to be greater than the second [{numbers.second}].")
            result_expected = convert_seconds_to_time(first_t - second_t)
            self.assertEqual(result_expected, numbers.get_good_result(),
                             f"{test_num}.4 The result expected is not ok")

    def test_app_strategies(self):
        """Functionnal tests for all app strategies."""
        self.assertEqual(9, len(py_os.STRATEGIES),
                         msg="must contains 9 strategies.")

        # testing addition strategy
        self.assertIn(py_os.ADD_OPERATOR_KEY, py_os.STRATEGIES)
        add_strategy = py_os.STRATEGIES[py_os.ADD_OPERATOR_KEY]
        self.assertIsInstance(add_strategy, py_os.AdditionStrategy)
        self.assertIsInstance(add_strategy.get_validator(),
                              py_ov.AdditionValidator)

        # testing substraction strategy
        self.assertIn(py_os.SUB_OPERATOR_KEY, py_os.STRATEGIES)
        sub_strategy = py_os.STRATEGIES[py_os.SUB_OPERATOR_KEY]
        self.assertIsInstance(sub_strategy, py_os.SubstractionStrategy)
        self.assertIsInstance(sub_strategy.get_validator(),
                              py_ov.SubstractionValidator)

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

        # testing simple division strategy
        self.assertIn(py_os.SINGLE_DIV_OPERATOR_KEY, py_os.STRATEGIES)
        simple_div_strategy = py_os.STRATEGIES[py_os.SINGLE_DIV_OPERATOR_KEY]
        self.assertIsInstance(simple_div_strategy,
                              py_os.SingleDivisorStrategy)
        self.assertIsInstance(simple_div_strategy.get_validator(),
                              py_ov.DivisionValidator)

        # testing complex division strategy
        self.assertIn(py_os.DOUBLE_DIV_OPERATOR_KEY, py_os.STRATEGIES)
        complex_div_strategy = py_os.STRATEGIES[py_os.DOUBLE_DIV_OPERATOR_KEY]
        self.assertIsInstance(complex_div_strategy,
                              py_os.DoubleDivisorStrategy)
        self.assertIsInstance(complex_div_strategy.get_validator(),
                              py_ov.DivisionValidator)

        # testing time addition strategy
        self.assertIn(py_os.TIME_ADD_KEY, py_os.STRATEGIES)
        time_add_strategy = py_os.STRATEGIES[py_os.TIME_ADD_KEY]
        self.assertIsInstance(time_add_strategy,
                              py_os.TimeAdditionStrategy)
        self.assertIsInstance(time_add_strategy.get_validator(),
                              py_ov.TimeAdditionValidator)

        # testing time substraction strategy
        self.assertIn(py_os.TIME_SUB_KEY, py_os.STRATEGIES)
        time_sub_strategy = py_os.STRATEGIES[py_os.TIME_SUB_KEY]
        self.assertIsInstance(time_sub_strategy,
                              py_os.TimeSubstractionStrategy)
        self.assertIsInstance(time_sub_strategy.get_validator(),
                              py_ov.TimeSubstractionValidator)
