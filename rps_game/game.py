class Game:
    types = {1: "human versus CPU", 2: "CPU vs CPU"}

    def __init__(self, player_1, player_2, amt_rounds=1):
        # player_1 and player_2 are two instances of Player class
        self.player_1 = player_1
        self.player_2 = player_2
        self.amt_rounds = amt_rounds
        self.played_rounds = []
        self.scoreboard = {player_1.name: 0, player_2.name: 0}
        self.winner = ""

    def play_round(self, first_player_choice, second_player_choice):
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

    def save_round(self, current_round):  # round is an object
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
