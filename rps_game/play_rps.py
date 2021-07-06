import random
from rps_game.player import Player
from rps_game.game import Game
from rps_game.round import Round
from rps_game.helper.tables import show_pretty_scoreboard


class PlayGame:
    def __init__(self, player_1, player_2, game_type, rounds=1):
        """
        :param player_1: instance of Player class
        :param player_2: instance of Player class
        :param game_type: integer (either 1 or 2)
        :param rounds: integer (between 1 and 10, default is 1)
        """
        game = Game(player_1, player_2, rounds)
        round_number = 0
        for current_round in range(rounds):
            round_number += 1
            print(f"Round {round_number}/{rounds}")
            if game_type == 1:  # that's "human vs cpu"
                Round.show_options()  # options are Rock, Paper or Scissors
                player_1_choice = PlayGame.human_choice()
            elif game_type == 2:  # that's cpu vs cpu
                player_1_choice = PlayGame.virtual_choice()  # random choices are generated
            else:
                raise ValueError("game type can be either 1 or 2")
            player_2_choice = PlayGame.virtual_choice()
            current_round = Round(player_1_choice, player_2_choice)
            PlayGame.show_round_choices(current_round)  # displays the choices made by the challengers
            current_round.winner = game.play_round(player_1_choice, player_2_choice)  # might also be None
            PlayGame.show_round_winner(current_round)
            game.save_round(current_round)  # round instance saved inside Game instance variable
            print()
            if round_number != rounds:
                # checking if there is an early winner before reaching the last round
                if not PlayGame.can_still_win(game):
                    input("there is already a winner! Press ENTER to see")
                    break
                # if there is no early winnerl the next round is launched
                input("Press Enter for next round\n")
            elif round_number == rounds:  # last round completed
                input("Press Enter to show final scores\n")
        show_pretty_scoreboard(game)
        winner = game.declare_winner()  # might also be None in case of a draw
        print()
        # the final message changes depending on the game type
        PlayGame.final_message(game, winner)  # if winner is None, a "draw" message is shown
        print()
        print("Do you want to play again? (Y/N)")
        play_again = input("Enter: ")
        print()
        if play_again.strip() in ["Y", "y", "Yes", "yes"]:
            new_game_rounds = PlayGame.choose_max_rounds()  # asking how many rounds to play in the new game
            print()
            # re-launching a new game with same players
            PlayGame(player_1, player_2, game_type, new_game_rounds)
        else:
            print("See you soon!")

    @staticmethod
    def can_still_win(game):
        """
        :param game: Game class instance
        :return: boolean
        """
        if not isinstance(game, Game):
            raise TypeError("a Game object should be passed")
        tot_rounds = game.amt_rounds
        played_rounds = len(game.played_rounds)
        scoreboard = game.scoreboard
        lowest_points = scoreboard[min(scoreboard, key=scoreboard.get)]
        highest_points = scoreboard[max(scoreboard, key=scoreboard.get)]
        remaining_rounds = tot_rounds - played_rounds
        # the following checks if at least one of the two players can still win/draw based on remaining rounds
        if (lowest_points + remaining_rounds) >= highest_points:
            return True
        else:
            return False

    @staticmethod
    def play_human_vs_cpu():
        human_name = input("choose a nickname: ")
        while True:
            if human_name:
                try:
                    human_player = Player(human_name)
                    break
                except ValueError:
                    human_name = input("Not valid. Nickname should be between 3 and 15 characters"
                                       " with at least one letter"
                                       "\nchoose a valid nickname: ")
            else:
                human_name = input("name cannot be empty.\nchoose a valid nickname: ")

        virtual_player = Player()
        return human_player, virtual_player

    @staticmethod
    def play_cpu_vs_cpu():
        cpu_1 = Player()
        cpu_2 = Player()
        return cpu_1, cpu_2

    @staticmethod
    def human_choice():
        choice_code = input("choose a number: ")
        retry_message = "Not valid.\nPlease enter a number between 1 and 3: "
        while True:
            try:
                choice_code = int(choice_code)
                if choice_code in Round.choices:  # choice code must be either 1 (Rock), 2 (Paper) or 3 (Scissors)
                    return choice_code
                else:
                    choice_code = input(retry_message)
            except:
                choice_code = input(retry_message)

    @staticmethod
    def virtual_choice():
        random_choice = random.randrange(1, 4)  # a random code between 1 and 3
        return random_choice

    @staticmethod
    def choose_game_type():
        for game_type in Game.types:  # game type can be either 1 (human vs cpu) or 2 (cpu vs cpu)
            print(f"{game_type} - {Game.types[game_type]}")
        game_code = input("choose a number: ")
        while True:
            try:
                game_code = int(game_code)
                if game_code in [1, 2]:
                    return game_code
                else:
                    game_code = input("Not valid.\nPlease enter 1 or 2: ")
            except ValueError:
                game_code = input("Not valid.\nPlease enter 1 or 2: ")

    @staticmethod
    def choose_max_rounds():
        max_rounds = input("How many rounds (max 10)? ")
        while True:
            try:
                max_rounds = int(max_rounds)
                if 1 <= max_rounds <= 10:
                    return max_rounds
                else:
                    max_rounds = input("Not valid.\nPlease enter a number between 1 and 10: ")
            except ValueError:
                max_rounds = input("Not valid.\nPlease enter a number between 1 and 10: ")

    @staticmethod
    def show_round_choices(round):
        """
        :param round: a Round class instance
        """
        print(f"{Round.choices[round.player_1_choice]} VS {Round.choices[round.player_2_choice]}")

    @staticmethod
    def show_round_winner(round):
        """
        :param round: a Round class instance
        """
        if round.winner:
            print(f"winner of the round: {round.winner.name}")
        else:
            print("Draw")

    @staticmethod
    def final_message(game, winner):
        """
        :param game: a Game class instance
        :param winner: either a Player class instance or None
        :return:
        """
        if not isinstance(game, Game):
            raise TypeError("a Game object must be passed as first argument")

        if winner:
            if not isinstance(winner, Player):
                raise TypeError("a Player object must be passed as second argument")
            if game.player_1.player_type == "virtual" and game.player_1.player_type == "virtual":
                print(f"{winner.name}, you WON !")
            elif winner.player_type == 'human':
                print(f"{winner.name}, you WON !")
            else:
                print(f"you LOST against {winner.name}")
        else:  # case of winner argument being None
            print("It's a draw !")


if __name__ == '__main__':
    pass