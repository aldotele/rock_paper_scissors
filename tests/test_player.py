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


