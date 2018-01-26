"""Test de la fonction generate_random du module pymath."""

import unittest
from pynairus.pymath import generate_random
from pynairus.errors.app_error import BadArgmentsError


class TestPymathGenerateRandom(unittest.TestCase):
    """ Classe de test du module pymath.generate_random."""

    def test_substraction_generation(self):
        """Test de la génération de soustraction aléatoire."""

        min_num = 10
        max_num = 50

        # On fait le test sur 50 générations
        for i in range(50):
            left, right, _ = generate_random(min_num, max_num, '-')

            # L'opérande de gauche doit être comprise entre l'opérande de droite et la borne max.
            self.assertTrue(
                right <= left <= max_num,
                msg=f"{i + 1}. L'opérande de gauche({left}) doit être comprise entre l'opérande de droite({right}) et la borne max({max_num}).")

    def test_addition_generation(self):
        """Test de la génération de l'addition."""
        min_num = 10
        max_num = 20

        # On fait le test sur 50 générations
        for i in range(50):
            left, right, _ = generate_random(min_num, max_num, '+')

            self.assertTrue(min_num <= left <= max_num,
                            msg=f"1.{i+1}. L'opérande de gauche ({left}) doit être comprise entre {min_num} et {max_num}).")

            self.assertTrue(min_num <= right <= max_num,
                            msg=f"2.{i+1}. L'opérande de droite ({right}) doit être comprise entre {min_num} et {max_num}).")

    def test_multiplication_generation(self):
        """Test de la génération de multiplication."""

        # On fait le test sur 50 générations
        for i in range(50):
            min_num = 1
            max_num = 3
            left, right, _ = generate_random(min_num, max_num, '*')

            # Le facteur de gauche doit être compris entre le min et le max.
            self.assertTrue(min_num <= left <= max_num,
                            msg=f"1.{i+1}. Le facteur de gauche ({left}) doit être compris entre {min_num} et {max_num}.")

            # Le facteur de droite doit être compris entre 1 et 10.
            self.assertTrue(1 <= right <= 10,
                            msg=f"1.{i+1}. Le facteur de droite ({right}) doit être compris entre 1 et 10.")

    def test_bad_parameters(self):
        """Test de levée d'exception en cas de mauvais paramètres."""
        with self.assertRaises(BadArgmentsError,
                               message="BadArgmentsError attendue"):
            generate_random(0, 0, "*")
