

class Round:
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

    def __init__(self, player_1_choice, player_2_choice):
        if Round.is_choice_valid(player_1_choice) and Round.is_choice_valid(player_2_choice):
            self.player_1_choice = int(player_1_choice)
            self.player_2_choice = int(player_2_choice)
            self.winner = ""
        else:
            raise ValueError("choice must be an integer between 1 and 3")

    @staticmethod
    def is_choice_valid(choice_code):
        try:
            choice_code = int(choice_code)
            if choice_code in Round.choices:
                return True
            else:
                return False
        except ValueError:
            return False

    @staticmethod
    def show_options():
        for code in Round.choices:
            print(f"{code} - {Round.choices[code]}")


if __name__ == '__main__':
    pass
