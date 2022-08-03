# This is Rock Paper Scissors v4 expansion of the coding exercise from
# The Modern Python3 Bootcamp from Udemy
#
# CHANGELOG
#
# v4 - Added a loop to play first to winning_score variable
#    - Added a running scoreboard
#    - Added ability to use shorter inputs r, p, s
#    - Updated rpsWinner() to handle short inputs and refactored code
#    - Added ability to quit with quit or q
#    - Added rpsConvert() to change short inputs to long and refactored
#
# v3 - Added computer oppponent utilizng randint for selection in a
#      function rpsOpponent()
#    - Refactored code
#
# v2 - Created rpsWinner() function to determine winner
#    - Created rpsValidate() function for validation and adjusted code
#    - Added try, except blocks to handle Value errors
#
# v1 - initial version based on the exercise on Udemy

# Import needed modules
from random import randint


def rpsWinner(player, computer):
    """Determine the winner of rock paper scissors where
       the 2 inputs, player and computer are compared.
       These will be "rock" "paper" or "scissors"""
    if player == computer:
        return ("draw")
    elif player == "rock" and computer == "scissors":
        return ("player")
    elif player == "paper" and computer == "rock":
        return ("player")
    elif player == "scissors" and computer == "paper":
        return ("player")
    else:
        return ("computer")


def rpsValidate(choice):
    """Ensure the response given is rock paper or scissors and return
       True or False"""
    if choice == 'rock' or choice == 'paper' or choice == 'scissors':
        return True
    elif choice == 'r' or choice == 'p' or choice == 's':
        return True
    return False


def rpsOpponent():
    """Uses a random integer from 0-2 to return 'rock' 'paper' or
       'scissors' acting as an ai for a computer opponent"""
    selection = randint(0, 2)
    if selection == 1:
        return 'rock'
    elif selection == 2:
        return 'paper'
    else:
        return 'scissors'

def rpsConvert(choice):
    """Convert short input to regular"""
    if choice == "r":
        choice = 'rock'
    elif choice == 'p':
        choice = 'paper'
    elif choice == "s":
        choice = 'scissors'
    return choice


try:
    computer_wins = 0
    player_wins = 0
    winning_score = 3

    print("Welcome to a simple RPS game against a pseudo ai")
    print(f"First to {winning_score} wins takes the crown\n")

    while computer_wins < winning_score and player_wins < winning_score:
        # Display the score
        print(f"Player: {player_wins} vs Computer: {computer_wins}\n\n")
        # Display the choices
        print("Your Choices (no dots)")
        print("...rock or r...")
        print("...paper or p...")
        print("...scissors or s...")
        print("...quit or q...")

        # Gather player 1 input
        player = input("player, enter your move: ").lower()

        # Give the user a chance to quit
        if player == "quit" or player == "q":
            break

        # Validate and continue or raise error
        if rpsValidate(player):
            computer = rpsOpponent()
            print(f"computer opponent plays: {computer}\n")

            # Determine winner
            if rpsWinner(rpsConvert(player), computer) == "player":
                print("You win!!")
                player_wins += 1
            elif rpsWinner(rpsConvert(player), computer) == "computer":
                print("Computer wins!!")
                computer_wins += 1
            else:
                print("Its a draw!!")
        else:
            raise ValueError
    # Display the score
    print(f"Final Score: Player: {player_wins} Computer: {computer_wins}\n\n")
    if player_wins > computer_wins:
        print("Congrats, you have beat a dumb ai!")
    elif computer_wins > player_wins:
        print("You lost to an idiot ai!")
    elif computer_wins == player_wins:
        print("Its a Draw!!")
except ValueError:
    print("Invalid Entry: You must use 'rock' or 'r', 'paper' or 'p', or 'scissors' or 's'")
