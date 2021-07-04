"""
in case of final draw, it is "fight to the bitter end"
"""
import random
from rps_game.player import Player
from rps_game.game import Game
from rps_game.round import Round
from rps_game.helper.tables import show_pretty_scoreboard


class PlayGame:
    def __init__(self, player_1, player_2, game_type, rounds=1):
        game = Game(player_1, player_2, rounds)
        round_number = 0
        for current_round in range(rounds):
            round_number += 1
            print(f"Round {round_number}/{rounds}")
            if game_type == 1:  # game type 1 is "human vs cpu"
                Round.show_options()
                player_1_choice = PlayGame.human_choice()
            elif game_type == 2:  # game type 2 is "cpu vs cpu"
                player_1_choice = PlayGame.virtual_choice()
            else:
                raise ValueError("game type can be either 1 or 2")
            player_2_choice = PlayGame.virtual_choice()
            current_round = Round(player_1_choice, player_2_choice)
            PlayGame.show_round_choices(current_round)
            current_round.winner = game.play_round(player_1_choice, player_2_choice)
            PlayGame.show_round_winner(current_round)
            game.save_round(current_round)
            print()
            if round_number != rounds:
                # check here if both can still win or draw
                if not PlayGame.can_still_win(game):
                    input("there is already a winner! Press ENTER to see")
                    break
                # check finish
                input("Press Enter for next round\n")
            elif round_number == rounds:
                input("Press Enter to show final scores\n")
        #game.show_scoreboard()
        show_pretty_scoreboard(game)
        winner = game.declare_winner()
        print()
        if winner:
            # customized message: it changes depending of type of game
            PlayGame.final_message(game, winner)
        else:
            print("It's a draw !")
            print()
        print()
        print("Do you want to play again? (Y/N)")
        play_again = input("Enter: ")
        print()
        if play_again in ["Y", "y", "Yes", "yes"]:
            new_game_rounds = PlayGame.choose_max_rounds()
            PlayGame(player_1, player_2, game_type, new_game_rounds)
        else:
            print("See you soon!")

    @staticmethod
    def can_still_win(game):
        tot_rounds = game.amt_rounds
        played_rounds = len(game.played_rounds)
        scoreboard = game.scoreboard
        lowest_points = scoreboard[min(scoreboard, key=scoreboard.get)]
        highest_points = scoreboard[max(scoreboard, key=scoreboard.get)]
        remaining_rounds = tot_rounds - played_rounds
        if (lowest_points + remaining_rounds) >= highest_points:
            return True
        else:
            return False

    @staticmethod
    def play_human_vs_cpu():
        human_name = input("choose a name: ")
        human_player = Player(human_name)
        virtual_player = Player()
        return human_player, virtual_player

    @staticmethod
    def play_cpu_vs_cpu():
        cpu_1 = Player()
        cpu_2 = Player()
        return cpu_1, cpu_2

    @staticmethod
    def human_choice():
        choice_code = input("choose one: ")
        retry_message = "Not valid. Please enter a number between 1 and 3: "
        while True:
            try:
                choice_code = int(choice_code)
                if choice_code in Round.choices:
                    return choice_code
                else:
                    choice_code = input(retry_message)
            except:
                choice_code = input(retry_message)

    @staticmethod
    def virtual_choice():
        random_choice = random.randrange(1, 4)
        return random_choice

    @staticmethod
    def choose_game_type():
        for game_type in Game.types:
            print(f"{game_type} - {Game.types[game_type]}")
        game_code = input("choose one: ")
        while True:
            try:
                game_code = int(game_code)
                if game_code in [1, 2]:
                    return game_code
                else:
                    game_code = input("not valid. Please enter 1 or 2: ")
            except ValueError:
                game_code = input("not valid. Please enter 1 or 2: ")

    @staticmethod
    def choose_max_rounds():
        max_rounds = input("How many rounds? ")
        while True:
            try:
                max_rounds = int(max_rounds)
                if 1 <= max_rounds <= 10:
                    return max_rounds
                else:
                    max_rounds = input("not valid. Please enter a number between 1 and 10: ")
            except ValueError:
                max_rounds = input("not valid. Please enter a number between 1 and 10: ")

    @staticmethod
    def show_round_choices(round):
        print(f"{Round.choices[round.player_1_choice]} VS {Round.choices[round.player_2_choice]}")

    @staticmethod
    def show_round_winner(round):
        if round.winner:
            print(f"winner of the round: {round.winner.name}")
        else:
            print("Draw")

    @staticmethod
    def final_message(game, winner):
        if game.player_1.player_type == "virtual" and game.player_1.player_type == "virtual":
            print(f"{winner.name}, you WON !")
        elif winner.player_type == 'human':
            print(f"{winner.name}, you WON !")
        else:
            print(f"you LOST against {winner.name}")


if __name__ == '__main__':
    player_1 = Player("Human")
    player_2 = Player()
    PlayGame(player_1, player_2, 2)