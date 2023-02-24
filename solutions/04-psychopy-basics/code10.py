"""
PsychoPy basic code.
"""

import random

from psychopy import event, visual

# creating a 800 x 600 window
win = visual.Window(size=(800, 600), units="norm")
aspect_ratio = win.size[0] / win.size[1]

# visuals
square = visual.Rect(win, size=(0.2, 0.2 * aspect_ratio))

# main loop
show_must_go_on = True
while show_must_go_on:
    # visuals
    square.draw()
    win.flip()

    # waiting for any key press
    pressed_keys = event.getKeys(keyList=['escape', 'space'])
    if len(pressed_keys) > 0:
        if pressed_keys[0] == "space":
            # move the square to a random position
            square.pos = (random.uniform(-1, 1), random.uniform(-1, 1))
        else:
            # user pressed abort
            show_must_go_on = False

# closing the window
win.close()
