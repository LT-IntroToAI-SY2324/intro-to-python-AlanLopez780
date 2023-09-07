# We will write a rock paper scissors game in class - Complete it in this file
import random

player_choice = input("Choose rock, paper, or scissors: ")
computer_choice = random.choice(options)

def get_choice():
    options = ["rock", "paper", "scissors"]
    player_choice = input("Choose rock, paper, or scissors: ")
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

choices = get_choice()
print(choices)
if player_choice == "rock":
    if computer_choice == "rock":
        print("Tie")
    elif computer_choice == "paper":
        print("Computer wins")
    elif computer_choice == "scissors":
        print("You win")
elif player_choice == "paper":
    if computer_choice == "rock":
        print("You win")
    elif computer_choice == "paper":
        print("Tie")
    elif computer_choice == "scissors":
        print("Computer wins")
elif player_choice == "scissors":
    if computer_choice == "rock":
        print("Computer wins")
    elif computer_choice == "paper":
        print("You win")
    elif computer_choice == "scissors":
        print("Tie")
else:
    print("Not a valid input. Please put either rock, paper, or scissors.")