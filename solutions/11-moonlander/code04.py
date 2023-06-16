"""
Moonlander game.
"""

from psychopy import event, visual

from contexts import GameContext, GameAbort
from moonlander import MoonLander


with GameContext("settings.json") as context:
    # game objects
    ship = MoonLander(context.win, context.settings["Ship"])

    # main loop
    while True:
        # visuals
        ship.draw()
        context.win.flip()

        # waiting for escape
        if event.getKeys(keyList=["escape"]):
            raise GameAbort
