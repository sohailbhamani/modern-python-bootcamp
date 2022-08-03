# This is Rock Paper Scissors v3 expansion of the coding exercise from
# The Modern Python3 Bootcamp from Udemy
#
# CHANGELOG
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


def rpsWinner(player1, player2):
    '''Determine the winner of rock paper scissors where
       the 2 inputs, player1 and player2 are compared.
       These will be "rock" "paper" or "scissors'''
    if player1 == player2:
        return ("Its a tie!")
    elif player1 == "rock" and player2 == "scissors":
        return ("You win!!!")
    elif player1 == "paper" and player2 == "rock":
        return ("You win!!!")
    elif player1 == "scissors" and player2 == "paper":
        return ("You win!!!")
    else:
        return ("The computer wins!!!")


def rpsValidate(choice):
    '''Ensure the response given is rock paper or scissors and return
       True or False'''
    if choice == 'rock' or choice == 'paper' or choice == 'scissors':
        return True
    return False


def rpsOpponent():
    selection = randint(0, 2)
    if selection == 1:
        return 'rock'
    elif selection == 2:
        return 'paper'
    else:
        return 'scissors'


# Display the choices
print("Welcome to a simple RPS game against a pseudo ai\n")
print("Your Choices (no dots)")
print("...rock...")
print("...paper...")
print("...scissors...")

try:
    # Gather player 1 input
    player1 = input("player, enter your move: ").lower()

    # Validate and continue or raise error
    if rpsValidate(player1):
        player2 = rpsOpponent()
        print(f"computer opponent plays: {player2}\n")

        # Determine winner
        print(rpsWinner(player1, player2))
    else:
        raise ValueError
except ValueError:
    print("Invalid Entry: You must use 'rock' 'paper' or 'scissors'")
