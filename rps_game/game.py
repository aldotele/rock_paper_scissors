from rps_game.player import Player


class Game:
    types = {1: "human versus CPU", 2: "CPU vs CPU"}

    def __init__(self, player_1, player_2, amt_rounds=1):
        # player_1 and player_2 will be two objects
        self.player_1 = player_1
        self.player_2 = player_2
        self.amt_rounds = amt_rounds
        self.rounds = []
        self.scoreboard = {player_1.name: 0, player_2.name: 0}

    def round(self, first_player_choice, second_player_choice):
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

    def save_round(self, round):  # round is an object
        self.rounds.append(round)

    @staticmethod
    def bitter_end(first_player, second_player):
        first_player = 0
        second_player = 0
        while first_player == 0 and second_player == 0:
            pass
        # here the winner will be the first one to beat the opponent
        pass

    def show_scoreboard(self):
        for player in self.scoreboard:
            print(f"{player}: {self.scoreboard[player]} points")

    def declare_winner(self):
        if self.scoreboard[self.player_1.name] > self.scoreboard[self.player_2.name]:
            return self.player_1
        elif self.scoreboard[self.player_2.name] > self.scoreboard[self.player_1.name]:
            return self.player_2
        else:
            return None