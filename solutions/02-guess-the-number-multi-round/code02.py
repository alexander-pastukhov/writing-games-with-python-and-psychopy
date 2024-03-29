"""
Guess-the-number game. Computer picks a number, player guesses it.
Multiple round edition.
"""

import random


# hard-code computer's pick
number_picked = random.randint(1, 10)

# tell user what the answer is
print("The number I've picked is %d"%(number_picked))

# get a guess from the player
guess = int(input("What is your guess? "))

# attempt's counter
attempts = 1

while guess != number_picked:
    # evaluate the guess
    if number_picked < guess:
        print("My number is lower")
    elif number_picked > guess:
        print("My number is higher")

    # get a guess from the player
    guess = int(input("What is your guess? "))
    attempts += 1

print("Spot on! You needed %d attempts."%(attempts))
