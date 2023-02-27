"""
Snake game.
"""

import json

from psychopy import visual, event

from gridwindow import GridWindow
from snaking import Snake


# getting settings
with open('settings.json') as json_file:
    settings = json.load(json_file)

# creating a window
win = GridWindow(settings["Window"]["grid size [in squares]"], 
                 settings["Window"]["square size [in pixels]"])

# create a snake
snake = Snake(win, settings["Snake"])

# main loop
user_abort = False
snake.reset_clock()
while not user_abort:
    # move snake
    if snake.can_move:
        snake.grow((0, 1))
        snake.trim()

    # visuals
    snake.draw()
    win.flip()

    # controls
    keys = event.getKeys(keyList=["space", "escape"])
    if len(keys) > 0:
        if keys[0] == "escape":
            user_abort = True

# cleaning up 
win.close()
