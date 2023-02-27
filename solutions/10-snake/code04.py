"""
Snake game.
"""

import json

from psychopy import visual, event

from gridwindow import GridWindow


# getting settings
with open('settings.json') as json_file:
    settings = json.load(json_file)

# creating a window
win = GridWindow(settings["Window"]["grid size [in squares]"], 
                 settings["Window"]["square size [in pixels]"])


# creating a square and drawing it
square = visual.Rect(win, size=win.square_size, pos=win.grid_to_win((0, 19)), fillColor="green")
square.draw()
win.flip()

# waiting for any key press
event.waitKeys()

# cleaning up 
win.close()
