"""
Guitar hero game.
"""

import json

from psychopy import event, visual

# getting settings
with open('settings.json') as json_file:
    settings = json.load(json_file)

win = visual.Window(size=settings['Window']['Size'])

# main loop
show_must_go_on = True
while show_must_go_on:
    # visuals
    win.flip()

    # inputs check
    show_must_go_on = len(event.getKeys(keyList=["escape"])) == 0

win.close()
