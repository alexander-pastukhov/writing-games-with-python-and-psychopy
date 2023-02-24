"""
Memory game.
"""

import os, random

from psychopy import clock, event, visual

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

    # visuals
    for card in cards:
        if card["show"]:
            card[card['side']].draw()
    win.flip()

    # checking if we have enough cards open
    if len(face_up) == 2:
        clock.wait(0.5)

        # check if we got a pair
        if face_up[0]['filename'] == face_up[1]['filename']:
            # take cards off the table
            for card in face_up:
                card['show'] = False
        else:
            # flip them back
            for card in face_up:
                card['side'] = "back"
        face_up.clear()

    # waiting for any key press
    show_must_go_on = len(event.getKeys(keyList=['escape'])) == 0

# closing the window
win.close()
