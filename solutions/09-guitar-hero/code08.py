"""
Guitar hero game.
"""

import json

from psychopy import clock, event, visual

from timed_response import TimedResponseTaskPsychoPy
from scoreboard import ScoreBoard

RESPONSE_KEYS = ["left", "down", "right"]

# getting settings
with open('settings.json') as json_file:
    settings = json.load(json_file)

win = visual.Window(size=settings['Window']['Size'])

# main loop
show_must_go_on = True
while show_must_go_on:

    round_timer = clock.CountdownTimer(settings["Duration [s]"])
    # visuals
    timed_task = TimedResponseTaskPsychoPy(win, settings["Target"])
    scoreboard = ScoreBoard(win)

    # round loop
    while show_must_go_on and round_timer.getTime() > 0:
        # move game objects
        timed_task.update()

        # visuals
        timed_task.draw()
        scoreboard.draw()
        win.flip()

        # inputs check
        keys = event.getKeys(keyList=["escape"] + RESPONSE_KEYS)
        if keys:
            if keys[0] == "escape":
                # abort
                show_must_go_on = False
            else:
                # response
                ipos = RESPONSE_KEYS.index(keys[0])
                scoreboard += timed_task.check(ipos)

    if show_must_go_on: # we are out of time, not aborted via escape
        # visuals
        timed_task.draw()
        scoreboard.draw()
        visual.TextStim(win, "Round over").draw()
        win.flip()

        # reponse on whether to play again (space) or exit (escape)
        keys = event.waitKeys(keyList=["escape", "space"])
        show_must_go_on = keys[0] == "space"


win.close()
