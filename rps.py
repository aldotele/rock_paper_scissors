from rps_game.play_rps import PlayGame
from rps_game.helper.tables import show_challengers


def start_game():
    game_type = PlayGame.choose_game_type()
    max_rounds = PlayGame.choose_max_rounds()
    if game_type == 1:
        player_1, player_2 = PlayGame.play_human_vs_cpu()
        print(f"your opponent: {player_2.name}")
        print()
    else:
        player_1, player_2 = PlayGame.play_cpu_vs_cpu()
    show_challengers(player_1, player_2)
    PlayGame(player_1, player_2, game_type, max_rounds)


if __name__ == '__main__':
    print("***** Welcome to Rock Paper Scissors Game *****")
    print('\n*** GAME TYPE ***')
    start_game()
