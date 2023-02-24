"""
Memory game.
"""

from psychopy import event, visual

from utilities import position_from_index

# creating a 240 * 2 x 400 * 2 window
win = visual.Window(size=(240 * 4, 400 * 2))

# visuals
chicken = visual.ImageStim(win, "Images/l01.png", pos=position_from_index(6))

# main loop
show_must_go_on = True
while show_must_go_on:
    # visuals
    chicken.draw()
    win.flip()

    # waiting for any key press
    show_must_go_on = len(event.getKeys(keyList=['escape'])) == 0

# closing the window
win.close()
