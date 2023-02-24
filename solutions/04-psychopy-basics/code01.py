"""
PsychoPy basic code.
"""

from psychopy import event, visual

# creating a 800 x 600 window
win = visual.Window(size=(800, 600))

# waiting for any key press
event.waitKeys()

# closing the window
win.close()
