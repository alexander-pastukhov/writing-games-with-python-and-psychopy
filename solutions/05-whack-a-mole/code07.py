"""
Whack-a-mole game.
"""

import random

from psychopy import clock, visual

MOLE_POS = [-0.3, 0, 0.3]
MOLE_COLOR = ["red", "yellow", "blue"]
BLANK_RANGE_S = [0.5, 0.75]
PRESENTATION_RANGE_S = [0.75, 1.5]
TRIALS_N = 10

# creating a 800 x 600 window
win = visual.Window(size=(800, 600), units="height")

for itrial in range(TRIALS_N):
    # visuals
    imole = random.randrange(len(MOLE_POS))
    mole = visual.Circle(win, radius=0.1, pos=(MOLE_POS[imole], 0), fillColor=MOLE_COLOR[imole])

    # presentation schedule
    blank = random.uniform(BLANK_RANGE_S[0], BLANK_RANGE_S[1])
    presentation = random.uniform(PRESENTATION_RANGE_S[0], PRESENTATION_RANGE_S[1])

    # blank
    win.flip()
    clock.wait(blank)

    # presentation
    mole.draw()
    win.flip()
    clock.wait(presentation)

# closing the window
win.close()
