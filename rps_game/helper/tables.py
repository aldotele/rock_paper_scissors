def display_game_name():
    message = "WELCOME to Rock Paper Scissors Game"
    hor_stick = "-" * len(message)
    print(hor_stick)
    print(message)
    print(hor_stick)


def show_challengers(player_1, player_2):
    hor_stick_len = len(player_1.name) + len(player_2.name) + 8
    hor_stick = "-" * hor_stick_len
    print(hor_stick)
    print(f"| {player_1.name} VS {player_2.name} |")
    print(hor_stick)


def show_pretty_scoreboard(game):
    hor_stick = "-" * 27
    first_column = "Player"
    second_column = "Score"
    print(hor_stick)
    print('|  {:<15}{:^7} |'.format(first_column, second_column))
    print(hor_stick)
    print('|  {:<15}{:^7} |'.format(game.player_1.name, game.scoreboard[game.player_1.name]))
    print('|  {:<15}{:^7} |'.format(game.player_2.name, game.scoreboard[game.player_2.name]))
    print(hor_stick)

