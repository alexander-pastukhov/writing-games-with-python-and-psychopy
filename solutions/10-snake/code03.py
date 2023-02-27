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

# waiting for any key press
event.waitKeys()

# cleaning up 
win.close()
