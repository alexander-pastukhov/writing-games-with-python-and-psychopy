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
while show_must_go_on and bird.is_airborne:
    # move game objects around
    bird.update()

    # visuals
    bird.draw()
    win.flip()

    # inputs check
    keys = event.getKeys(keyList=["escape", "space"])
    if keys:
        if keys[0] == "escape":
            # user pressed abort button
            show_must_go_on = False
        else:
            # flap wings
            bird.flap()

win.close()
