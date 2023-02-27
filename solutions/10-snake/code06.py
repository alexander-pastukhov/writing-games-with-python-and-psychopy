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


# creating a (single segment) snake and drawing it
snake = Snake(win, settings["Snake"])
snake.draw()
win.flip()

# waiting for any key press
event.waitKeys()

# cleaning up 
win.close()
