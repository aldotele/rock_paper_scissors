"""
•	Posso giocare Umano vs Computer?
•	Posso giocare Computer vs Computer?
•	Posso giocare una nuova partita conclusa quella precedente?

•	Non è necessaria una GUI appariscente (può essere semplice)
•	Non dovrebbero essere necessarie librerie o moduli esterni se non per i test
•	Usa le pratiche riconosciute nell’industry dello sviluppo software
•	Considera di scrivere codice estendibile. Se lo farai dovrebbe essere relativamente semplice estendere il gioco alla variante Rock, paper, scissors, lizard and Spock
•	Questo è un Minimum Viable Product: eleganza e semplicità battono una ricca lista di feature
"""

import random

# rock beats scissors, paper beats rock, scissors beats paper

choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
print("1 - Rock\n2 - Paper\n3 - Scissors")
print()
choice = int(input("choose: "))
virtual = random.randrange(1, 4)
print()
print(f"You chose {choices[choice]}")
print(f"CPU chose {choices[virtual]}")


def round(human):
    if choice == virtual:
        return print('it is a draw')
    elif choice == 1 and virtual == 2:
        return print('you lost')
    elif choice == 1 and virtual == 3:
        return print('you won')
    elif choice == 2 and virtual == 1:
        return print('you won')
    elif choice == 2 and virtual == 3:
        return print('you lost')
    elif choice == 3 and virtual == 1:
        return print('you lost')
    elif choice == 3 and virtual == 2:
        return print('you won')

round(choice)