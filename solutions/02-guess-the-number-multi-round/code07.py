"""
Guess-the-number game. Computer pick a number, player guesses it.
Multiple round edition.
"""

import random


MAX_ATTEMPTS = 3

want_to_play = True
while want_to_play:
    # ----- Single game -----
    # hard-code computer's pick
    number_picked = random.randint(1, 10)

    # tell user what the answer is
    print("The number I've picked is %d"%(number_picked))


    # attempt's counter
    attempts = 1

    # get an initial guess from the player
    guess = int(input("Please enter the guess, you have %d attempts remaining: "%(MAX_ATTEMPTS - attempts + 1)))

    # limiting number of attemps that we allow the player to make
    while guess != number_picked and attempts < MAX_ATTEMPTS:
        # evaluate the guess
        if number_picked < guess:
            print("My number is lower")
        elif number_picked > guess:
            print("My number is higher")

        # get a guess from the player
        attempts += 1
        guess = int(input("Please enter the guess, you have %d attempts remaining: "%(MAX_ATTEMPTS - attempts + 1)))

    if guess == number_picked:
        print("Spot on! You needed %d attempts."%(attempts))
    else:
        print("Better luck next time!")

    # ----- Check if player wants to play again  -----
    play_again = input("Want to play again? Y/N ")
    want_to_play = play_again == "Y" or play_again == "y"

print("Thank you for playing the game!")
