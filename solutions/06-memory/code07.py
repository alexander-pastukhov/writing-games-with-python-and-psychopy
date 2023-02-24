"""
Memory game.
"""

import os

from psychopy import event, visual

from utilities import position_from_index, create_card


IMAGE_FOLDER = "Images"


# creating a 240 * 2 x 400 * 2 window
win = visual.Window(size=(240 * 4, 400 * 2))

# visuals
card = create_card(win, os.path.join(IMAGE_FOLDER, "l01.png"), 1)

# main loop
show_must_go_on = True
while show_must_go_on:
    # visuals
    card[card['side']].draw()
    win.flip()

    # waiting for any key press
    show_must_go_on = len(event.getKeys(keyList=['escape'])) == 0

# closing the window
win.close()
