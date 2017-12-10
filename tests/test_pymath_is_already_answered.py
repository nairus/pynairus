"""Test de la fonction is_already_answered du module pymath."""

import unittest
from pymath import is_already_answered
from pymath import ANSWERS

GOOD_ANSWER = (1, 5, "*")
BAD_ANSWER = (1, 3, "-")


class TestPymathIsAlreadyAnswered(unittest.TestCase):
    """Classe de test de la fonction is_already_answered du module pymath."""

    def setUp(self):
        """Méthode invoquée avant chaque test."""
        ANSWERS[GOOD_ANSWER] = True
        ANSWERS[BAD_ANSWER] = False

    def tearDown(self):
        """Méthode invoquée après chaque test."""
        # On vide le dictionnaire après chaque test.
        ANSWERS.clear()

    def test_not_exists(self):
        """Test de non existance."""
        self.assertFalse(is_already_answered((1, 2, '+')),
                         msg=f"Le tuple (1, 2, '+') ne doit pas exister dans les réponses.")

    def test_exists_and_true(self):
        """Test d'existance avec une réponse juste."""
        self.assertTrue(is_already_answered(GOOD_ANSWER),
                        msg=f"Le tuple {GOOD_ANSWER} doit exister et True.")

    def test_exists_and_false(self):
        """Test d'existance avec une réponse fausse."""
        self.assertFalse(is_already_answered(BAD_ANSWER),
                         msg=f"Le tuple {BAD_ANSWER} doit exister et False.")
