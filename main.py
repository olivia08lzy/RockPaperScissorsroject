"""
Main file to run the rock, paper scissors game
"""
import random
from enum import IntEnum


class Action(IntEnum):
    """
    This enum class describes what you can choose as options in the game.
    """
    ROCK=0
    PAPER=1
    SCISSORS=2

# matchups, the key beats the value
matchups = {
    Action.PAPER : Action.ROCK,
    Action.ROCK: Action.SCISSORS,
    Action.SCISSORS: Action.PAPER
}
winner_moves = {
    Action.PAPER : "covers",
    Action.ROCK: "smashes",
    Action.SCISSORS: "cuts"
}
action_names = {
    Action.ROCK: "Rock",
    Action.PAPER: "Paper",
    Action.SCISSORS: "Scissors"
}

def choose_winner(player1, player2):
    """
    Compare two actions and choose a winner.
    """
    if player1==player2:
        print("Both players selected "+ action_names[player1].lower() +". It's a tie!")
    elif matchups[player1] == player2:
        print(action_names[player1]
              + " "
              + winner_moves[player1]
              + " " + action_names[player2].lower()
              + ". You win!")
    else:
        print(action_names[player2]
              + " "
              + winner_moves[player2]
              + " "
              + action_names[player1].lower()
              + ". You lose.")

while True:
    print("Make your throw")
    try:
        user_input=int(input("Enter a choice (rock[0], paper[1], scissors[2]): "))
        computer_input=random.randint(0, len(Action)-1)
        print("You threw "
              + action_names[Action(user_input)].lower()
              + ", the computer threw "
              + action_names[Action(computer_input)].lower()
              + ".")
    except ValueError:
        print ("Invalid selection. Enter a value in range [0,2].")
        continue

    choose_winner(user_input, computer_input)

    again=input("Want some more? (y/n): ")
    if again.lower()=="n":
        break

print("Goodbye!")
