while True:
    player1 = input("Enter your choice player 1: ")
    player2 = input("Enter your choice player 2: ")

    valid_inputs = ["rock","paper","scissors"]
    if player1 not in valid_inputs or player2 not in valid_inputs:
        print("Wrong input")
        continue
    
    if player1 == player2:
        print("Its a tie")
    elif(player1 == "rock" and player2 == "scissors") or (player1 == "scissors" and player2 == "paper") or (player1 == "paper" and player2 == "rock"):
        print("Player 1 wins") 
    else:
        print("Player 2 wins")

    play_again=input("If you want to play again enter yes/no: ")
    if play_again.lower() != "yes":
        break

print("End of the game")    
