"""
Guitar hero game.
"""

import json

from psychopy import event, visual

from timed_response import TimedResponseTask

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
    show_must_go_on = len(event.getKeys(keyList=["escape"])) == 0

win.close()
