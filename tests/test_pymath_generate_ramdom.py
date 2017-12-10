"""Test de la fonction generate_random du module pymath."""

from pymath import generate_random
from errors.bad_arguments_error import BadArgmentsError
import pytest


class TestPymathGenerateRandom(object):
    """ Classe de test du module pymath.generate_random."""

    def test_substraction_generation(self):
        """Test de la génération de soustraction aléatoire."""

        # On fait le test sur 50 générations
        for i in range(50):
            left, right, _ = generate_random(10, 50, '-')

            # L'opérande de gauche doit être comprise entre l'opérande de droite et la borne max.
            assert right <= left <= 50

    def test_addition_generation(self):
        """Test de la génération de l'addition."""
        min_num = 10
        max_num = 20

        # On fait le test sur 50 générations
        for i in range(50):
            left, right, _ = generate_random(min_num, max_num, '+')

            assert min_num <= left <= max_num
            assert min_num <= right <= max_num

    def test_multiplication_generation(self):
        """Test de la génération de multiplication."""

        # On fait le test sur 50 générations
        for i in range(50):
            min_num = 1
            max_num = 3
            left, right, _ = generate_random(min_num, max_num, '*')

            # Le facteur de gauche doit être compris entre le min et le max.
            assert min_num <= left <= max_num

            # Le facteur de droite doit être compris entre 1 et 10.
            assert 1 <= right <= 10

    def test_bad_parameters(self):
        """Test de levée d'exception en cas de mauvais paramètres."""
        with pytest.raises(BadArgmentsError, message="BadArgmentsError attendue"):
            generate_random(0, 0, "*")
