"""
Guitar hero game.
"""

import json

from psychopy import event, visual

from timed_response import TimedResponseTask

RESPONSE_KEYS = ["left", "down", "right"]

# getting settings
with open('settings.json') as json_file:
    settings = json.load(json_file)

win = visual.Window(size=settings['Window']['Size'])

# visuals
timed_task = TimedResponseTask(win, settings["Target"])

# main loop
show_must_go_on = True
while show_must_go_on:
    # move game objects
    timed_task.update()

    # visuals
    timed_task.draw()
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
            timed_task.check(ipos)


win.close()
