import unittest
from rps_game.round import Round
from rps_game.player import Player


class TestRound(unittest.TestCase):
    def setUp(self):
        self.round_1 = Round(1, 3)
        self.round_2 = Round("2", "1")

    def test_round(self):
        self.assertRaises(ValueError, Round, 0, 1)
        self.assertRaises(ValueError, Round, 4, 3)
        self.assertEqual(self.round_2.player_1_choice, 2)
        self.assertEqual(self.round_2.player_2_choice, 1)
