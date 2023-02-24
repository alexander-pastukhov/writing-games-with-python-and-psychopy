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


# test interval splitting
print(split_interval(2, 8))

