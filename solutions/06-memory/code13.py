"""
Memory game.
"""

import os, random

from psychopy import event, visual

from utilities import create_card, index_from_position

IMAGE_FOLDER = "Images"

# creating a 240 * 2 x 400 * 2 window
win = visual.Window(size=(240 * 4, 400 * 2))
mouse = event.Mouse()

# visuals
filenames = [filename
             for filename in os.listdir(IMAGE_FOLDER)
             if filename.startswith("l")] * 2
# randomize card order
random.shuffle(filenames)
cards = [create_card(win, os.path.join(IMAGE_FOLDER, filename), index) 
         for index, filename in enumerate(filenames)]

# main loop
face_up = []
show_must_go_on = True
while show_must_go_on:
    # processing mouse inputs
    if mouse.getPressed()[0]:
        icard = index_from_position(mouse.getPos())
        if cards[icard]['side'] != "front":
            cards[icard]['side'] = "front"
            face_up.append(cards[icard])
            # debug output
            print("%d cards are open"%(len(face_up)))

    # visuals
    for card in cards:
        card[card['side']].draw()
    win.flip()

    # waiting for any key press
    show_must_go_on = len(event.getKeys(keyList=['escape'])) == 0

# closing the window
win.close()
