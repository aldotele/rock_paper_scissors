from rps_game.helper.funny_names import FunnyNameGenerator
import re


class Player:
    def __init__(self, name=""):
        if name:  # if a name is given, it is a human player
            if Player.is_name_valid(name):
                self.player_type = "human"
                self.name = name
            else:
                raise ValueError("Player name must have at least three characters with one letter")
        else:  # a random name is generated
            self.player_type = "virtual"
            self.name = FunnyNameGenerator.compose_name()

    @staticmethod
    def is_name_valid(name):
        if len(name) >= 3:
            out = re.search("[a-zA-Z]", name)  # making sure the name has at least one letter
            if out:
                return True
            else:
                return False
        else:
            return False



