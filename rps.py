from rps_game.play_rps import PlayGame
from rps_game.helper.tables import display_game_name, show_challengers


def start_game():
    game_type = PlayGame.choose_game_type()  # 1 is human vs cpu, 2 is cpu vs cpu
    max_rounds = PlayGame.choose_max_rounds()  # the number of rounds per game
    if game_type == 1:
        player_1, player_2 = PlayGame.play_human_vs_cpu()
        print(f"your opponent: {player_2.name}")
        print()
    else:
        player_1, player_2 = PlayGame.play_cpu_vs_cpu()
    show_challengers(player_1, player_2)
    input("press ENTER to launch the game")
    print()
    PlayGame(player_1, player_2, game_type, max_rounds)  # game launched


if __name__ == '__main__':
    display_game_name()
    print('\n***** GAME SETTINGS *****')
    start_game()
