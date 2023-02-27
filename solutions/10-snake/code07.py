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

# grow and trim the snake, should end up with three segments.
snake.grow((0, 1))
snake.grow((0, 1))
snake.grow((1, 0))
snake.trim()

# draw snake
snake.draw()
win.flip()

# waiting for any key press
event.waitKeys()

# cleaning up 
win.close()
