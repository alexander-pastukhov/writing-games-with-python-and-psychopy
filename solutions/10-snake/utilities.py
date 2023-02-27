"""
Utility functions for the snake game.

Functions
---------
compute_new_direction(direction, turn)
    Compute new direction based on turn direction.
"""

DIRECTION =  ["left", "up", "right", "down"]
TURN_INCREMENT = {"left": -1, "right" : 1}

def compute_new_direction(direction, turn):
    """
    Compute new direction based on turn direction.

    Parameters
    ----------
    direction : str
        "left", "up", "right", "down"
    turn : str
        "left" (counterclockwise) or "right" (clockwise)

    Returns
    ----------
    str
    """
    icurrent = DIRECTION.index(direction)
    inew = (icurrent + TURN_INCREMENT[turn]) % len(DIRECTION)
    return DIRECTION[inew]
