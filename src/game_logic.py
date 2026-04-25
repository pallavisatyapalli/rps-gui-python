# src/game_logic.py

import random

options = ['Rock', 'Paper', 'Scissors']
emojis = {'Rock': '✊', 'Paper': '🖐', 'Scissors': '✌'}

def get_computer_choice():
    """Return a random choice for the computer."""
    return random.choice(options)

def determine_winner(user, computer):
    """Determine the winner between the user and computer."""
    if user == computer:
        return "Draw"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissors" and computer == "Paper"):
        return "User"
    else:
        return "Computer"
