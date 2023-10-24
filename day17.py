from getpass import getpass as input

print("""E P I C  🥌  📄  ✂  B A T T L E""")
print()

exit = "no"
R = "ROCK 🥌"
P = "PAPER 📄"
S = "SCISSORS ✂"
player1Score = 0
player2Score = 0

while exit == "no":
    player1 = input("Player 1: Select your move (R, P OR S): ")
    print()
    player2 = input("Player 2: Select your move (R, P OR S): ")


    if player1 == "R":
        if player2 == "S":
            print(player1, R, " WINS! 💃")
          
            player1Score += 1
        elif player2 == "P":
            print(player2, P, " WINS! 💃")
          
            player2Score += 1
        elif player2 == "R":
            print("DRAW! 😮")
        else:
            print(player2, "Try Again")                
    elif player1 == "P":
        if player2 == "S":
            print(player2, S, " WINS! 💃")
            player2Score += 1
        elif player2 == "R":
            print(player1, P, " WINS! 💃")
            player1Score += 1
        elif player2 == "P":
            print("DRAW! 😮")
        else:
            print(player2, "Try Again")
    elif player1 == "S":
        if player2 == "R":
            print(player2, R, " WINS! 💃")
            player2Score += 1
        elif player2 == "P":
            print(player1, S, " WINS! 💃")
            player1Score += 1
        elif player2 == "S":
            print("DRAW! 😮")
        #else:
            #print(player2, "Try Again")
    #else:
        #print(player1, "Try Again")
  
    print()
    print("S C O R E")
    print("Player 1|", player1Score, "-", player2Score, "|Player 2")
    print()
    if player1Score == 3 or player2Score == 3:
      print("GAME OVER")
      print()
      exit = input("Do you want to quite game?: ")
    else:
      continue