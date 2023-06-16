"""
Moonlander game.
"""

from psychopy import event, visual

from contexts import GameContext, GameAbort


with GameContext("settings.json") as context:
    # visuals
    text = visual.TextStim(context.win, "Press ESCAPE")

    # main loop
    while True:
        # visuals
        text.draw()
        context.win.flip()

        # waiting for escape
        if event.getKeys(keyList=["escape"]):
            raise GameAbort
