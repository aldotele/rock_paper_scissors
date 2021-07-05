from rps_game.player import Player
from rps_game.round import Round


class Game:
    types = {1: "human versus CPU", 2: "CPU vs CPU"}

    def __init__(self, player_1, player_2, amt_rounds=1):
        """
        :param player_1: a Player class instance
        :param player_2: a Player class instance
        :param amt_rounds: an integer between 1 and 10
        """
        if not isinstance(player_1, Player) or not isinstance(player_2, Player):
            raise TypeError("first two arguments must be Player objects")
        if amt_rounds not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            raise ValueError("the number of rounds must an integer between 1 and 10")
        self.player_1 = player_1
        self.player_2 = player_2
        self.amt_rounds = amt_rounds
        self.played_rounds = []
        self.scoreboard = {player_1.name: 0, player_2.name: 0}  # where to store the points earned at each round
        self.winner = ""

    def play_round(self, first_player_choice, second_player_choice):
        """
        :param first_player_choice: integer between 1 and 3
        :param second_player_choice: integer between 1 and 3
        :return: Player class instance (the winner of the round)
        the method also updates the game scoreboard
        """
        if first_player_choice not in Round.choices or second_player_choice not in Round.choices:
            raise ValueError("each player choice must be a number between 1 and 3")
        if first_player_choice == second_player_choice:
            pass
        elif first_player_choice == 1 and second_player_choice == 2:
            self.scoreboard[self.player_2.name] += 1
            return self.player_2
        elif first_player_choice == 1 and second_player_choice == 3:
            self.scoreboard[self.player_1.name] += 1
            return self.player_1
        elif first_player_choice == 2 and second_player_choice == 1:
            self.scoreboard[self.player_1.name] += 1
            return self.player_1
        elif first_player_choice == 2 and second_player_choice == 3:
            self.scoreboard[self.player_2.name] += 1
            return self.player_2
        elif first_player_choice == 3 and second_player_choice == 1:
            self.scoreboard[self.player_2.name] += 1
            return self.player_2
        elif first_player_choice == 3 and second_player_choice == 2:
            self.scoreboard[self.player_1.name] += 1
            return self.player_1

    def save_round(self, current_round):
        """
        :param current_round: a Round class instance
        """
        if not isinstance(current_round, Round):
            raise TypeError("argument must be a Round object")
        self.played_rounds.append(current_round)

    def declare_winner(self):
        if self.scoreboard[self.player_1.name] > self.scoreboard[self.player_2.name]:
            self.winner = self.player_1
            return self.winner
        elif self.scoreboard[self.player_2.name] > self.scoreboard[self.player_1.name]:
            self.winner = self.player_2
            return self.winner
        else:
            return None
