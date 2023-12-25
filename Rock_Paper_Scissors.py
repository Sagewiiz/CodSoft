import tkinter as tk
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(user_choice):
    computer_choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(computer_choices)
    
    result = determine_winner(user_choice, computer_choice)
    
    result_label.config(text=f"Computer chose {computer_choice}. {result}")

def on_choice_click(choice):
    play_game(choice)

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

instruction_label = tk.Label(root, text="Choose rock, paper, or scissors:")
instruction_label.pack()

choices_frame = tk.Frame(root)
choices_frame.pack()

rock_button = tk.Button(choices_frame, text="Rock", command=lambda: on_choice_click('rock'))
rock_button.pack(side=tk.LEFT)

paper_button = tk.Button(choices_frame, text="Paper", command=lambda: on_choice_click('paper'))
paper_button.pack(side=tk.LEFT)

scissors_button = tk.Button(choices_frame, text="Scissors", command=lambda: on_choice_click('scissors'))
scissors_button.pack(side=tk.LEFT)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
