"""
Whack-a-mole game.
"""

import random

from psychopy import event, visual

MOLE_POS = [-0.3, 0, 0.3]
MOLE_COLOR = ["red", "yellow", "blue"]

# creating a 800 x 600 window
win = visual.Window(size=(800, 600), units="height")

# visuals
imole = random.randrange(len(MOLE_POS))
mole = visual.Circle(win, radius=0.1, pos=(MOLE_POS[imole], 0), fillColor=MOLE_COLOR[imole])

# main loop
show_must_go_on = True
while show_must_go_on:
    # visuals
    mole.draw()
    win.flip()

    # waiting for any key press
    show_must_go_on = len(event.getKeys(keyList=['escape'])) == 0

# closing the window
win.close()
