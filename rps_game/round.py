

class Round:
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

    def __init__(self, player_1_choice, player_2_choice):
        self.player_1_choice = player_1_choice
        self.player_2_choice = player_2_choice
        self.winner = ""

    @staticmethod
    def show_options():
        for code in Round.choices:
            print(f"{code} - {Round.choices[code]}")


if __name__ == '__main__':
    pass
