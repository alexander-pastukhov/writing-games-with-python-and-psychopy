"""
Guess-the-number game. Human player picks a number, computer guesses it.
"""

def player_feedback():
    """Get player feedback, prompting until valid input is given.

    Returns
    ----------
    string
    """
    # repeat prompt until we get valid input
    feedback = input("Is your number smaller (<), larger (>), or equal to (=) my guess? ")
    while not (feedback == "<" or feedback == ">" or feedback == "="):
        feedback = input("Is your number smaller (<), larger (>), or equal to (=) my guess? ")

    return feedback


# get feedback
player_feedback()
