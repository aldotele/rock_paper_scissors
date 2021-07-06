import unittest
from rps_game.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.human_player = Player("John")
        self.virtual_player = Player()

    def test_player(self):
        self.assertEqual(self.human_player.player_type, 'human')
        self.assertEqual(self.human_player.name, 'John')
        self.assertIs(type(self.human_player.player_type), str)
        self.assertIs(type(self.human_player.name), str)
        self.assertRaises(ValueError, Player, "J.")  # name too short
        self.assertRaises(ValueError, Player, "007")  # name needs at least one letter

    def test_is_name_valid(self):
        self.assertTrue(Player.is_name_valid("John"))
        self.assertTrue(Player.is_name_valid("Constantine Jr."))  # exactly 15 characters
        self.assertFalse(Player.is_name_valid("Constantine Junior"))  # exactly 15 characters
        self.assertFalse(Player.is_name_valid(""))
        self.assertFalse(Player.is_name_valid("J."))
        self.assertFalse(Player.is_name_valid("007"))


