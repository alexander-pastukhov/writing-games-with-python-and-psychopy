"""
Moonlander game.
"""

from psychopy import event

from contexts import GameContext


with GameContext("settings.json") as context:
    # waiting for any key press
    event.waitKeys()
