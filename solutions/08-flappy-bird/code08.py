"""
Flappy Bird game.
"""

import json

from psychopy import event, visual

from flappy_bird import FlappyBird
from obstacle import Obstacle

# getting settings
with open('settings.json') as json_file:
    settings = json.load(json_file)

win = visual.Window(size=settings['Window']['Size'])

# visuals
bird = FlappyBird(win, settings["Bird"])
obstacle = Obstacle(win, settings["Obstacles"])

# main loop
show_must_go_on = True
while show_must_go_on and bird.is_airborne:
    # move game objects around
    obstacle.update()
    bird.update()

    # visuals
    obstacle.draw()
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
