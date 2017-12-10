#!/usr/bin/env python
# coding: utf-8
"""
Module qui génére des calculs aléatoire

Aide:
    $ python run.py -h

"""

import random
import timeit

# Stocke les réponses justes
ANSWERS = {}


def is_already_answered(numbers):
    """
    Vérifie si la réponse juste a déjà été donnée au tuple (left,right,operator)
        :param numbers: Le tuple de calcul à tester.
        :type numbers: tuple
        :return bool
    """
    if ANSWERS.get(numbers) is None:
        return False

    return ANSWERS.get(numbers)


def generate_random(start, end, operator):
    """"
    Génère un nombre aléatoire.
        :param start:    Borne de début.
        :param end:      Borne de fin.
        :param operator: Opérateur.
        :type start:     int
        :type end:       int
        :type operator:  str
        :return tuple Retourne un tuple de (first_number, second_number, operator)
    """
    if operator == '-':
        """cas des soustractions:
        - la première opérande doit être supérieure ou égale à la seconde
        afin d'éviter un résultat négatif"""
        second_number = random.randrange(start, int(end / 2))
        first_number = random.randrange(second_number, end)
    elif operator == "*" and (1 <= start <= 10) and (1 <= end <= 10):
        """cas des tables de multiplication simple :
        - les bornes doivent être comprises entre 1 et 10)
        - la première opérande doit être compris dans la borne
        - la seconde opérande doit être un nombre entre 1 et 10"""
        first_number = random.randrange(start, end)
        second_number = random.randrange(1, 10)
    elif operator == "+":
        first_number = random.randrange(start, end)
        second_number = random.randrange(start, end)
    else:
        # Dans les autres les arguments ne sont pas reconnus.
        from errors.bad_arguments_error import BadArgmentsError
        raise BadArgmentsError(
            f"Erreur d'opération pour le tuple : ({start}, {end}, {operator})")

    return (first_number, second_number, operator)


def pymath(start, end, max_range, operator, timer):
    """
    Fonction principale.
        :param start:     Borne de début.
        :param end:       Borne de fin.
        :param max_range: Plage maximum de calculs à générer.
        :param operator:  Opérateur.
        :type start:      int
        :type end:        int
        :type max_range:  int
        :type operator:   str
    """
    if timer is True:
        # Initialisation du temps total de réponse.
        total_time = 0

    if operator is None:
        operators = ("+", "-")
    else:
        operators = (operator, operator)

    numbers_operations = [generate_random(
        start, end, operators[x % 2]) for x in range(0, max_range)]

    score = 0

    for numbers in numbers_operations:
        while is_already_answered(numbers):
            numbers = generate_random(*numbers)

        left, right, operator = numbers

        print(f"{left} {operator} {right} = ?")
        if operator == "+":
            result = left + right
        elif operator == "*":
            result = left * right
        else:
            result = left - right

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

            if response == result:
                print(f"Bonne réponse!")
                score += 1
                ANSWERS[(left, right, operator)] = True
            else:
                ANSWERS[(left, right, operator)] = False
                print(f"Mauvaise réponse, le résulat attendue est: {result}")

        print(f"Ton score est de {score} / {max_range}")
        print(f"Temps de réponse total : {total_time:04.2f}")


if __name__ == "__main__":
    import argparse
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument("start", type=int,
                        help="Nombre de début de l'intervale")
    PARSER.add_argument("end", type=int,
                        help="Nombre de fin de l'intervale")
    PARSER.add_argument("range", type=int,
                        help="Nombre de début de calculs")
    PARSER.add_argument("-o", "--operator", type=str,
                        help="Force l'opérateur")
    PARSER.add_argument("-t", "--timer", action="store_true",
                        help="Ajoute un timer")
    ARGS = PARSER.parse_args()

    pymath(ARGS.start, ARGS.end, ARGS.range, ARGS.operator, ARGS.timer)