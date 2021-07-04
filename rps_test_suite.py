import unittest
from tests.test_player import TestPlayer
from tests.test_round import TestRound


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestPlayer('test_player'))
    suite.addTest(TestRound('test_round'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())