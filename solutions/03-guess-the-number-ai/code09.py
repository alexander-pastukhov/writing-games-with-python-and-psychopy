"""
Guess-the-number game. Human player picks a number, computer guesses it.
"""

from utils import player_feedback, split_interval


fewest_attempts = 100
want_to_play = True
while want_to_play:

    # ----- Single game -----
    # initial lack of knowledge
    lower_limit = 1
    upper_limit = 11
    attempts = 0
    feedback = None
    while feedback != "=":

        # guess in the middle
        attempts += 1
        guess = split_interval(lower_limit, upper_limit)

        # get feedback and adjust, if needed
        feedback = player_feedback(guess)
        if feedback == "<":
            # player's number is smaller
            upper_limit = guess
        elif feedback == ">":
            # player's number is larger
            lower_limit = guess
    if attempts < fewest_attempts:
        fewest_attempts = attempts
    print("Nailed it in just %d attempts! Best so far is %d."%(attempts, fewest_attempts))

    # ----- Check if player wants to play again  -----
    play_again = input("Want to play again? Y/N ")
    want_to_play = play_again == "Y" or play_again == "y"

print("Thank you for playing the game!")
