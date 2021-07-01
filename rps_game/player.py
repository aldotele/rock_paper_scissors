import random
from rps_game.helper.funny_names import FunnyNameGenerator


class Player:
    def __init__(self, name=""):
        if name:  # if a name is given, it is a human player
            self.player_type = "human"
            self.name = name
        else:  # a random choice code is generated
            self.player_type = "virtual"
            self.name = FunnyNameGenerator.compose_name()


if __name__ == '__main__':
    pass








