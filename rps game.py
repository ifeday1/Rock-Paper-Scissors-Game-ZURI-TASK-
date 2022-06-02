import random
from tkinter.messagebox import YES
import xxlimited 

while True:
    choices = ["R", "P", "S"]

    computer = random.choice(choices)
    player=None

    while player not in choices:
        player  = input("R, P or S?: ")  .lower()

    if player == computer:
        print("Computer: ", computer)
        print("Player: ", player)
        print("Tie!")
    elif player == "rock":
        if computer ==  "paper":
             print("Computer: ", computer)
             print("Player: ", player)
             print("You lose!")
        if computer ==  "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win!")
         
    elif player == "scissors":
        if computer ==  "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You lose!")
        if computer ==  "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win!")

    elif player == "paper":
        if computer ==  "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You lose!")
        if computer ==  "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win!")

    play_again= input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break
print("Bye!")