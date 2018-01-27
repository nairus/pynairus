#!/usr/bin/env python
# coding: utf-8

"""pymath module"""

import timeit
from .errors.app_error import BadArgmentsError
from .strategies import operator_strategy as ns_os

# Store good anwsers
ANSWERS = {}


def is_already_answered(numbers):
    """
    Check if a good anwser has been stored in the "ANSWERS" tuple.

        :param numbers: The operations tuple to test.

        :type numbers: tuple

        :return: bool
    """
    if ANSWERS.get(numbers) is None:
        return False

    return ANSWERS.get(numbers)


def generate_random(start, end, operator):
    """"
    Generate ramdom number.
        :param start:    Start range.
        :param end:      End range.
        :param operator: Operator.

        :type start:     int
        :type end:       int
        :type operator:  str

        :return ComputeNumbers
    """
    if operator not in ns_os.STRATEGIES:
        raise BadArgmentsError(f"the operator {operator} not exists")

    strategy = ns_os.STRATEGIES[operator]
    return strategy.generate_random(start, end)


def pymath(start, end, max_range, operator, timer):
    """
    Main function.
        :param start:     start range.
        :param end:       end range.
        :param max_range: max operations to generate.
        :param operator:  operator.
        :param timer:     activate the timer.

        :type start:      int
        :type end:        int
        :type max_range:  int
        :type operator:   str
        :type timer:      bool
    """
    # we clear the awnsers dict
    ANSWERS.clear()

    if timer is True:
        # Initialisation of the total time for the answers.
        total_time = 0

    if operator is None:
        operators = ("+", "-")
    else:
        operators = (operator, operator)

    numbers_operations = [generate_random(
        start, end, operators[x % 2]) for x in range(max_range)]

    score = 0

    for numbers in numbers_operations:
        # loop until we found an good anwser not already given
        while is_already_answered(numbers):
            # generate another operation
            numbers = generate_random(start, end, numbers.operator)

        print(f"{numbers}")
        result = numbers.get_good_result()
        answer_key = (numbers.left, numbers.right, numbers.operator)

        if timer is True:
            start_time = timeit.default_timer()

        try:
            response = int(input())
        except ValueError as identifier:
            print(f"Erreur de saisie: {identifier}")
        else:
            if timer is True:
                response_time = timeit.default_timer() - start_time
                print(f"Temps de réponse : {response_time:04.2f} secondes")
                total_time += response_time

            if numbers.validate(response):
                print(f"Bonne réponse!")
                score += 1
                ANSWERS[answer_key] = True
            else:
                ANSWERS[answer_key] = False
                print(f"Mauvaise réponse, le résulat attendue est: {result}")

        print(f"Ton score est de {score} / {max_range}")

        if timer is True:
            print(f"Temps de réponse total : {total_time:04.2f}")
