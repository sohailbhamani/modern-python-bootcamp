# This is a guessing game using a while loop

from random import randint

random_num = randint(1, 10)

while True:
    guess = int(input("Guess a number from 1 - 10: "))
    if guess > random_num:
        print("Too high")
    elif guess < random_num:
        print("Too Low")
    else:
        print("You guessed it, you win!")
        play_again = input("Do you want to play again? (y/n) ")
        if play_again == "y":
            random_num = randint(1, 10)
            guess = None
        else:
            print("Thank you for playing")
            break
