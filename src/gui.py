# src/gui.py

import tkinter as tk
from tkinter import messagebox
from .game_logic import get_computer_choice, determine_winner
from .config import MAX_ROUNDS

# Initialize scores and rounds
user_score = 0
computer_score = 0
rounds = 0

def play(user_choice):
    global user_score, computer_score, rounds

    # Get computer's choice and determine the winner
    comp_choice = get_computer_choice()
    result = determine_winner(user_choice, comp_choice)

    # Update scores based on the result
    if result == "User":
        user_score += 1
    elif result == "Computer":
        computer_score += 1

    rounds += 1

    # Update the GUI with the results
    result_message = f"You: {user_choice}  vs  {comp_choice}:Computer\n{result}!"
    result_label.config(text=result_message)
    score_label.config(text=f"Score — You: {user_score}, Computer: {computer_score}")

    # If we've reached max rounds, end the game
    if rounds >= MAX_ROUNDS:
        end_game()

def end_game():
    """Show the winner and end the game."""
    if user_score > computer_score:
        winner = f"🎉 You won the game!"
    elif user_score < computer_score:
        winner = f"💻 Computer won the game!"
    else:
        winner = "It's a tie!"
    messagebox.showinfo("Game Over", f"{winner}\nFinal Score — You: {user_score}, Computer: {computer_score}")
    reset_game()

def reset_game():
    """Reset the game to start again."""
    global user_score, computer_score, rounds
    user_score = 0
    computer_score = 0
    rounds = 0
    score_label.config(text="Score — You: 0, Computer: 0")
    result_label.config(text="")

def start_game():
    """Create the GUI interface and run the main loop."""
    global result_label, score_label

    # GUI setup
    root = tk.Tk()
    root.title("Rock Paper Scissors ✊🖐✌")
    root.geometry("420x380")
    root.configure(bg="#f0f0f0")

    tk.Label(root, text="Rock 🪨  Paper 📄  Scissors ✂️", font=("Helvetica", 16, "bold"), bg="#f0f0f0").pack(pady=10)

    # Button frame
    btn_frame = tk.Frame(root, bg="#f0f0f0")
    btn_frame.pack()

    # Create buttons for each option
    options = ['Rock', 'Paper', 'Scissors']
    for option in options:
        tk.Button(btn_frame, text=f"{option} {option[0]}", font=("Arial", 12), width=15,
                  bg="#4CAF50", fg="white", activebackground="#388E3C", command=lambda o=option: play(o)).pack(pady=5)

    result_label = tk.Label(root, text="Choose an option!", font=("Arial", 13), bg="#f0f0f0")
    result_label.pack(pady=10)

    score_label = tk.Label(root, text="Score — You: 0, Computer: 0", font=("Arial", 13, "bold"), bg="#f0f0f0")
    score_label.pack(pady=5)

    # Reset button
    tk.Button(root, text="🔄 Reset Game", font=("Arial", 12), bg="#FF5722", fg="white",
              activebackground="#E64A19", command=reset_game).pack(pady=10)

    root.mainloop()
