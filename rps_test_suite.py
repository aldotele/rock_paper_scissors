import unittest
from tests.test_player import TestPlayer
from tests.test_round import TestRound
from tests.test_game import TestGame


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestPlayer('test_player'))
    suite.addTest(TestPlayer('test_is_name_valid'))
    suite.addTest(TestRound('test_round'))
    suite.addTest(TestRound('test_is_choice_valid'))
    suite.addTest(TestGame('test_game'))
    suite.addTest(TestGame('test_play_round'))
    suite.addTest(TestGame('test_save_round'))
    suite.addTest(TestGame('test_declare_winner'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
