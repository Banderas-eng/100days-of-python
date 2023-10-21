from getpass import getpass as input

print("""E P I C  🥌  📄  ✂  B A T T L E""")
print()

exit = "no"
R = "ROCK 🥌"
P = "PAPER 📄"
S = "SCISSORS ✂"

while exit == "no":
    player1 = input("Player 1: Select your move (R, P OR S): ")
    print()
    player2 = input("Player 2: Select your move (R, P OR S): ")


    if player1 == "R":
        if player2 == "S":
            print(player1, R, " WINS! 💃")
        elif player2 == "P":
            print(player2, P, " WINS! 💃")
        elif player2 == "R":
            print("DRAW! 😮")
        else:
            print(player2, "Try Again")                
    elif player1 == "P":
        if player2 == "S":
            print(player2, S, " WINS! 💃")
        elif player2 == "R":
            print(player1, P, " WINS! 💃")
        elif player2 == "P":
            print("DRAW! 😮")
        else:
            print(player2, "Try Again")
    elif player1 == "S":
        if player2 == "R":
            print(player2, R, " WINS! 💃")
        elif player2 == "P":
            print(player1, S, " WINS! 💃")
        elif player2 == "S":
            print("DRAW! 😮")
        else:
            print(player2, "Try Again")             
    else:
        print(player1, "Try Again")

    exit = input("Do you want to quite game?: ")            