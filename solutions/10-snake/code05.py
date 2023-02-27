"""
Snake game.
"""

import json

from psychopy import visual, event

from gridwindow import GridWindow
from snaking import SnakeSegment


# getting settings
with open('settings.json') as json_file:
    settings = json.load(json_file)

# creating a window
win = GridWindow(settings["Window"]["grid size [in squares]"], 
                 settings["Window"]["square size [in pixels]"])


# creating a snake segment and drawing it
snake_segment = SnakeSegment(win, (0, 19), settings["Snake"]["color"])
snake_segment.draw()
win.flip()

# waiting for any key press
event.waitKeys()

# cleaning up 
win.close()
