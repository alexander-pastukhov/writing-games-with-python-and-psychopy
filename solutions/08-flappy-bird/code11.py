"""
Flappy Bird game.
"""

import json

from psychopy import event, visual

from flappy_bird import FlappyBird
from obstacle import ObstaclesManager

# getting settings
with open('settings.json') as json_file:
    settings = json.load(json_file)

win = visual.Window(size=settings['Window']['Size'])

# visuals
bird = FlappyBird(win, settings["Bird"])
obstacles = ObstaclesManager(win, settings["Obstacles"])
score_text = visual.TextStim(win, "0", pos=(-0.9, 0.9))

# main loop
show_must_go_on = True
while show_must_go_on and bird.is_airborne and not obstacles.check_if_hit(bird):
    # move game objects around
    obstacles.update()
    bird.update()

    # keep the score 
    score_text.text = str(obstacles.score())

    # visuals
    score_text.draw()
    obstacles.draw()
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
