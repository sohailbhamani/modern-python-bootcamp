# This is Rock Paper Scissors v2 expansion of the coding exercise from
# The Modern Python3 Bootcamp from Udemy
#
#
# CHANGELOG
#
# v2 - Created rpsWinner() function to determine winner and adjusted code
#    - Created rpsValidate() function for validation and adjusted code
#    - Added try, except blocks to handle Value errors
#
# v1 - initial version based on the exercise on Udemy


def printLines(num, message):
    '''Print the line num number of times'''
    while num > 0:
        print(message)
        num -= 1


def rpsWinner(player1, player2):
    '''Determine the winner of rock paper scissors where
       the 2 inputs, player1 and player2 are compared.
       These will be "rock" "paper" or "scissors'''
    if player1 == player2:
        return ("\nShoot!\n\nIts a tie!")
    elif player1 == "rock" and player2 == "scissors":
        return ("\nShoot!\n\nplayer 1 wins")
    elif player1 == "paper" and player2 == "rock":
        return ("\nShoot!\n\nplayer 1 wins")
    elif player1 == "scissors" and player2 == "paper":
        return ("\nShoot!\n\nplayer 1 wins")
    else:
        return ("\nShoot!\n\nplayer2 wins")


def rpsValidate(choice):
    '''Ensure the response given is rock paper or scissors and return
       True or False'''
    if choice == 'rock' or choice == 'paper' or choice == 'scissors':
        return True
    return False

# Display the choices
print("Your Choices (no dots)")
print("...rock...")
print("...paper...")
print("...scissors...")

# If player 1 not blank
try:
    # Gather player 1 input
    player1 = input("(enter Player 1's choice): ").lower()

    # Validate and continue or raise error
    if rpsValidate(player1):
        #obscure answer from player2
        printLines(50, '***NO CHEATING***')
        player2 = input("(enter Player 2's choice): ").lower()

        # Validate and continue or raise error
        if rpsValidate(player2):
            # Determine winner
            print(rpsWinner(player1, player2))
        else:
            raise ValueError
    else:
        raise ValueError
except ValueError:
    print("Invalid Entry: You must use 'rock' 'paper' or 'scissors'")
