# We will write a rock paper scissors game in class - Complete it in this file
import random


player_choice = "rock"
computer_choice = "paper"

def get_choice():
    options = ["rock", "paper", "scissors"]
    player_choice = "rock"
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

choices = get_choice()
print(choices)