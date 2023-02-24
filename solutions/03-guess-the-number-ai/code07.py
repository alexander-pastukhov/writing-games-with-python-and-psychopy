"""
Guess-the-number game. Human player picks a number, computer guesses it.
"""

def player_feedback(guess):
    """Get player feedback, prompting until valid input is given.

    Parameters
    ----------
    guess : int

    Returns
    ----------
    string
    """
    # repeat prompt until we get valid input
    feedback = input("Is your number smaller (<), larger (>), or equal to (=) my guess: %d? "%(guess))
    while not (feedback == "<" or feedback == ">" or feedback == "="):
        feedback = input("Is your number smaller (<), larger (>), or equal to (=) my guess: %d? "%(guess))

    return feedback

def split_interval(lower_limit, upper_limit):
    """Split the interval (approximatelly) at integer half point.

    Parameters
    ----------
    lower_limit : int
    upper_limit : int

    Returns
    ----------
    int
    """
    return int(round((upper_limit + lower_limit) / 2.0))


want_to_play = True
while want_to_play:

    # ----- Single game -----
    # initial lack of knowledge
    lower_limit = 1
    upper_limit = 11

    feedback = None
    while feedback != "=":

        # guess in the middle
        guess = split_interval(lower_limit, upper_limit)

        # get feedback and adjust, if needed
        feedback = player_feedback(guess)
        if feedback == "<":
            # player's number is smaller
            upper_limit = guess
        elif feedback == ">":
            # player's number is larger
            lower_limit = guess
    print("Nailed it!")

    # ----- Check if player wants to play again  -----
    play_again = input("Want to play again? Y/N ")
    want_to_play = play_again == "Y" or play_again == "y"

print("Thank you for playing the game!")
