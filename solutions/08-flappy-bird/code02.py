"""
Flappy Bird game.
"""

import json

from psychopy import event, visual

from flappy_bird import FlappyBird

# getting settings
with open('settings.json') as json_file:
    settings = json.load(json_file)

win = visual.Window(size=settings['Window']['Size'])

# visuals
bird = FlappyBird(win, settings["Bird"])

# main loop
show_must_go_on = True
while show_must_go_on:
    # visuals
    bird.draw()
    win.flip()

    # inputs check
    show_must_go_on = len(event.getKeys(keyList=["escape"])) == 0

win.close()
