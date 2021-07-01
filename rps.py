from rps_game.play_rps import PlayGame
from rps_game.player import Player


def start_game():
    game_type = PlayGame.choose_game_type()
    max_rounds = PlayGame.choose_max_rounds()
    if game_type == 1:
        play_human_vs_cpu(game_type, max_rounds)
    else:
        play_cpu_vs_cpu(game_type, max_rounds)


def play_human_vs_cpu(game_type, max_rounds):
    human_name = input("choose a name: ")
    human_player = Player(human_name)
    virtual_player = Player()
    print(f"your opponent: {virtual_player.name}")
    print()
    PlayGame(human_player, virtual_player, game_type, max_rounds)


def play_cpu_vs_cpu(game_type, max_rounds):
    cpu_1 = Player()
    cpu_2 = Player()
    print()
    print(f"{cpu_1.name} against {cpu_2.name}")
    print()
    PlayGame(cpu_1, cpu_2, game_type, max_rounds)


if __name__ == '__main__':
    print("***** Welcome to Rock Paper Scissors Game *****")
    print('\n*** GAME TYPE ***')
    start_game()