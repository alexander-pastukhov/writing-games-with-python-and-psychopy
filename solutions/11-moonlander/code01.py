"""
Moonlander game.
"""

import json

from psychopy import visual, event

# getting settings
with open('settings.json') as json_file:
    settings = json.load(json_file)

# opening window
win = visual.Window(settings["Window"]["Size [pix]"])

# waiting for any key press
event.waitKeys()

# cleaning up 
win.close()
