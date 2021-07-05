import unittest
from rps_game.round import Round


class TestRound(unittest.TestCase):
    def setUp(self):
        self.round_1 = Round(1, 3)
        self.round_2 = Round("2", "1")  # strings will be converted into integers

    def test_round(self):
        self.assertEqual(self.round_1.player_1_choice, 1)
        self.assertEqual(self.round_1.player_2_choice, 3)
        self.assertIsInstance(self.round_1.player_1_choice, int)
        self.assertIsInstance(self.round_1.player_2_choice, int)
        self.assertEqual(self.round_2.player_1_choice, 2)
        self.assertEqual(self.round_2.player_2_choice, 1)
        self.assertIsInstance(self.round_2.player_1_choice, int)  # converted into integer
        self.assertIsInstance(self.round_2.player_2_choice, int)  # converted into integer
        self.assertEqual(Round.choices[self.round_1.player_1_choice], "Rock")
        self.assertEqual(Round.choices[self.round_1.player_2_choice], "Scissors")
        self.assertRaises(ValueError, Round, 0, 1)  # choices must be between 1 and 3

    def test_is_choice_valid(self):
        self.assertTrue(Round.is_choice_valid(1))
        self.assertTrue(Round.is_choice_valid("1"))
        self.assertFalse(Round.is_choice_valid(4))
        self.assertFalse(Round.is_choice_valid("one"))





