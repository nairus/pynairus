# coding: utf-8

"""pymath module"""

import timeit
from .config import app_context as ns_ac
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


def pymath(**kwargs):
    """
    Launch application with random operations.
        keys required:
            - start: start range (int).
            - end:   end range (int).
            - limit: max operations to generate (int).

        keys optionals:
            - operator:  operator (str).
            - timer:     activate the timer (bool).
            - config:    the name the config file (str).
    """
    # init the context
    app_context = ns_ac.init_app_context(**kwargs)
    logger = app_context.app_config.logger

    # init vars
    start = app_context.start
    end = app_context.end
    limit = app_context.limit
    timer = app_context.options.get("timer")
    operator = app_context.options.get("operator")

    # we clear the awnsers dict
    ANSWERS.clear()

    if timer is True:
        # Initialisation of the total time for the answers.
        total_time = 0
        logger.info(f"timer is activated at {total_time}s.")

    # by default we build a tuple of addition and substraction operations
    if operator is None:
        operators = (ns_os.ADD_OPERATOR_KEY, ns_os.SUB_OPERATOR_KEY)
    else:
        operators = (operator, operator)

    numbers_operations = []
    try:
        numbers_operations = [generate_random(
            start, end, operators[x % 2]) for x in range(limit)]

        logger.debug(f"numbers_operations generated: {numbers_operations}")
    except BadArgmentsError as identifier:
        logger.error("An error occured during operation generation",
                     identifier)

    score = 0
    for numbers in numbers_operations:
        # we generate the key for the answer
        answer_key = (numbers.first, numbers.second, numbers.operator)

        # loop until we found an good anwser not already given
        while is_already_answered(answer_key):
            logger.debug(f"key {answer_key} already exists.")
            # generate another operation
            numbers = generate_random(start, end, numbers.operator)
            # we create another answer key
            answer_key = (numbers.first, numbers.second, numbers.operator)

        print(f"{numbers}")
        result = numbers.get_good_result()

        if timer is True:
            start_time = timeit.default_timer()

        try:
            response = int(input())
        except ValueError as identifier:
            # log a warning to not stop the application.
            logger.warning(f"Input error: {identifier}")
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

        print(f"Ton score est de {score} / {limit}")

    logger.info(f"final score: {score}/{limit}")
    if timer is True:
        logger.info(f"total time: {total_time:04.2f}")
        print(f"Temps de réponse total : {total_time:04.2f}")
