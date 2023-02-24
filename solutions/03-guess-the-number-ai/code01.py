"""
Guess-the-number game. Human player picks a number, computer guesses it.
"""

# repeat prompt until we get valid input
feedback = input("Is your number smaller (<), larger (>), or equal to (=) my guess? ")
while not (feedback == "<" or feedback == ">" or feedback == "="):
    feedback = input("Is your number smaller (<), larger (>), or equal to (=) my guess? ")
