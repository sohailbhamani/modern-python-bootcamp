# This is Rock Paper Scissors v1 coding exercise from
# The Modern Python3 Bootcamp from Udemy
#
# In this incarnation, it only handles blank entries from either player
# and not if they enter the wrong strings altogether


# Function to print a certain number of lines hiding player1s answer
def printLines(num):
    '''Print the line num number of times'''
    while num > 0:
        print("***No Cheating***")
        num -= 1


# Display the choices
print("Your Choices (no dots)")
print("...rock...")
print("...paper...")
print("...scissors...")

# Gather player 1 input
player1 = input("(enter Player 1's choice): ")
player1 = player1.lower()

# If player 1 not blank
if player1:
    # Scroll player1's choice out of the view hopefully
    printLines(50)
    player2 = input("(enter Player 2's choice): ")
    player2 = player2.lower()
    # if player 2 not blank
    if player2:
        print("SHOOT!")

        # Determine winner
        if player1 == player2:
            print("Its a tie!")
        elif player1 == "rock" and player2 == "scissors":
            print("player 1 wins")
        elif player1 == "paper" and player2 == "rock":
            print("player 1 wins")
        elif player1 == "scissors" and player2 == "paper":
            print("player 1 wins")
        else:
            print("player2 wins")
    else:
        # Player 2 entered a blank input
        print("Player2, you must enter rock, papers or scissors!")
else:
    # Player 1 entered a blank input
    print("Player1, you must enter rock, papers or scissors!")
