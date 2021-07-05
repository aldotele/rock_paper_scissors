import unittest
from rps_game.game import Game
from rps_game.player import Player
from rps_game.round import Round


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game_human_vs_cpu = Game(Player("John"), Player())
        self.game_cpu_vs_cpu = Game(Player(), Player(), 5)
        # customizing the scoreboard of a new game to declare a winner
        self.new_game_human_vs_cpu = Game(Player("Bill"), Player())
        self.new_game_human_vs_cpu.player_2.name = "CrazyLeopard"
        self.new_game_human_vs_cpu.scoreboard = {"Bill": 1, "CrazyLeopard": 0}
        # customizing the scoreboard of another game to declare a draw
        self.another_game_human_vs_cpu = Game(Player("Frida"), Player())
        self.another_game_human_vs_cpu.player_2.name = "BigWhale"
        self.another_game_human_vs_cpu.scoreboard = {"Frida": 0, "BigWhale": 0}

    def test_game(self):
        self.assertIsInstance(self.game_human_vs_cpu.player_1, Player)
        self.assertIsInstance(self.game_human_vs_cpu.player_2, Player)
        self.assertIsInstance(self.game_cpu_vs_cpu.player_2, Player)
        self.assertIsInstance(self.game_cpu_vs_cpu.player_2, Player)
        self.assertEqual(self.game_human_vs_cpu.player_1.name, "John")
        self.assertIsInstance(self.game_human_vs_cpu.player_2.name, str)  # cannot know the random name of the cpu
        self.assertEqual(self.game_human_vs_cpu.amt_rounds, 1)  # 1 is the default because it was not provided
        self.assertEqual(self.game_cpu_vs_cpu.amt_rounds, 5)  # amount of rounds was provided here
        self.assertRaises(TypeError, Game, "John", "Bill")  # both players must be Player instances
        self.assertRaises(ValueError, Game, Player(), Player(), 0)  # not possible to provide 0 as amount of rounds
        self.assertRaises(ValueError, Game, Player(), Player(), 11)  # max amount of rounds is 10
        self.assertIsInstance(self.game_human_vs_cpu.scoreboard, dict)  # the scoreboard is a dictionary
        self.assertIn("John", self.game_human_vs_cpu.scoreboard)

    def test_play_round(self):
        self.assertEqual(self.game_human_vs_cpu.play_round(3, 1), self.game_human_vs_cpu.player_2)  # R beats S
        self.assertEqual(self.game_human_vs_cpu.play_round(3, 2), self.game_human_vs_cpu.player_1)  # S beats P
        self.assertEqual(self.game_cpu_vs_cpu.play_round(1, 2), self.game_cpu_vs_cpu.player_2)  # P beats R
        self.assertEqual(self.game_cpu_vs_cpu.play_round(2, 1), self.game_cpu_vs_cpu.player_1)  # P beats R
        self.assertIsNone(self.game_human_vs_cpu.play_round(1, 1))  # draw means None is returned
        self.assertRaises(ValueError, self.game_human_vs_cpu.play_round, 0, 1)  # each choice must be between 1 and 3

    def test_save_round(self):
        self.assertIsNone(self.game_human_vs_cpu.save_round(Round(1, 2)))  # round is saved but with no return
        self.assertRaises(TypeError, self.game_human_vs_cpu.save_round, "round one")

    def test_declare_winner(self):
        self.assertEqual(self.new_game_human_vs_cpu.declare_winner(), self.new_game_human_vs_cpu.player_1)
        self.assertIsNone(self.another_game_human_vs_cpu.declare_winner())
