"""
Memory game.
"""

import os, random

from psychopy import event, visual

from utilities import position_from_index, create_card

IMAGE_FOLDER = "Images"

# creating a 240 * 2 x 400 * 2 window
win = visual.Window(size=(240 * 4, 400 * 2))

# visuals
filenames = [filename
             for filename in os.listdir(IMAGE_FOLDER)
             if filename.startswith("l")] * 2
# randomize card order
random.shuffle(filenames)
cards = [create_card(win, os.path.join(IMAGE_FOLDER, filename), index) 
         for index, filename in enumerate(filenames)]

# turn cards front side up for demo purposes
for card in cards:
    card['side'] = "front"

# main loop
show_must_go_on = True
while show_must_go_on:
    # visuals
    for card in cards:
        card[card['side']].draw()
    win.flip()

    # waiting for any key press
    show_must_go_on = len(event.getKeys(keyList=['escape'])) == 0

# closing the window
win.close()
