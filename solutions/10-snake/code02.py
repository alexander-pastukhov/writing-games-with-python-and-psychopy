"""
Snake game.
"""

import json

from psychopy import visual, event

# getting settings
with open('settings.json') as json_file:
    settings = json.load(json_file)

# computing window size
window_size = [grid_dim * settings["Window"]["square size [in pixels]"]
              for grid_dim in settings["Window"]["grid size [in squares]"]]
win = visual.Window(window_size, units="norm")

# waiting for any key press
event.waitKeys()

# cleaning up 
win.close()
