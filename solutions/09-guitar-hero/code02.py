"""
Guitar hero game.
"""

import json

from psychopy import event, visual

from timed_response import Target

# getting settings
with open('settings.json') as json_file:
    settings = json.load(json_file)

win = visual.Window(size=settings['Window']['Size'])

# visuals
target = Target(win, settings["Target"], 0)

# main loop
show_must_go_on = True
while show_must_go_on:
    # visuals
    target.draw()
    win.flip()

    # inputs check
    show_must_go_on = len(event.getKeys(keyList=["escape"])) == 0

win.close()
