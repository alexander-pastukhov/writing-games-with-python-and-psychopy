"""
Memory game.
"""

from psychopy import event, visual

# creating a 240 * 2 x 400 * 2 window
win = visual.Window(size=(240 * 4, 400 * 2))

# main loop
show_must_go_on = True
while show_must_go_on:
    # visuals
    win.flip()

    # waiting for any key press
    show_must_go_on = len(event.getKeys(keyList=['escape'])) == 0

# closing the window
win.close()
