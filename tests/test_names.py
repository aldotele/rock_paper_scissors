import unittest
from rps_game.helper.funny_names import FunnyNameGenerator


class TestFunnyNameGenerator(unittest.TestCase):
    def test_compose_name(self):
        self.assertIsInstance(FunnyNameGenerator.compose_name(), str)
        self.assertIsNotNone(FunnyNameGenerator.compose_name())

