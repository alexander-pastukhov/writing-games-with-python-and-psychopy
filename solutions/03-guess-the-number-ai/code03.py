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


# get feedback
player_feedback(2)

