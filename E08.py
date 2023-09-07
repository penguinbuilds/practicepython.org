init = 0

while init == 0:
    player1 = int(
        input("Player 1; enter 0 for Rock, 1 for Paper, 2 for Scissors: "))
    player2 = int(
        input("Player 2; enter 0 for Rock, 1 for Paper, 2 for Scissors: "))

    if player1 == player2:
        print("Draw.")
    elif player1 == 0:
        if player2 == 1:
            print("Player 2 wins.")
        else:
            print("Player 1 wins.")
    elif player1 == 1:
        if player2 == 2:
            print("Player 2 wins.")
        else:
            print("Player 1 wins.")
    elif player1 == 2:
        if player2 == 0:
            print("Player 2 wins.")
        else:
            print("Player 1 wins.")

    init = int(input("Enter 0 to play again, 1 to stop playing: "))
