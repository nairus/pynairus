#!/usr/bin/env python
# coding: utf-8
"""
Module qui génére des calculs aléatoire

Aide:
    $ python run.py -h

"""

import random
import timeit


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
        - la première opérande doit être supérieur ou égale à la seconde
        afin d'éviter un résultat négatif"""
        second_number = random.randrange(start, int(end / 2))
        first_number = random.randrange(second_number, end)
    elif operator == "*" and start <= 10 and end <= 10:
        """cas des tables de multiplication simple :
        - les bornes doivent être comprises entre 0 et 10)
        - la première opérande doit être compris dans la borne
        - la seconde opérande doit être un nombre entre 0 et 10"""
        first_number = random.randrange(start, end)
        second_number = random.randrange(0, 10)
    else:
        first_number = random.randrange(start, end)
        second_number = random.randrange(start, end)

    return (first_number, second_number, operator)


def main(start, end, max_range, operator):
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
    if operator is None:
        operators = ("+", "-")
    else:
        operators = (operator, operator)

    numbers_operations = [generate_random(
        start, end, operators[x % 2]) for x in range(0, max_range)]

    score = 0

    for numbers in numbers_operations:
        print(f"{numbers[0]} {numbers[2]} {numbers[1]} = ?")
        if numbers[2] == "+":
            result = numbers[0] + numbers[1]
        elif numbers[2] == "*":
            result = numbers[0] * numbers[1]
        else:
            result = numbers[0] - numbers[1]

        response = int(input())

        if response == result:
            print(f"Bonne réponse!")
            score += 1
        else:
            print(f"Mauvaise réponse, le résulat attendue est: {result}")

    print(f"Ton score est de {score} / {max_range}")


if __name__ == "__main__":
    import argparse
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument("start", type=int,
                        help="Nombre de début de l'intervale")
    PARSER.add_argument("end", type=int, help="Nombre de fin de l'intervale")
    PARSER.add_argument("range", type=int, help="Nombre de début de calculs")
    PARSER.add_argument("-o", "--operator", type=str, help="Force l'opérateur")
    ARGS = PARSER.parse_args()

    main(ARGS.start, ARGS.end, ARGS.range, ARGS.operator)