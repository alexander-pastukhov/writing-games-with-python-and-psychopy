"""
Whack-a-mole game.
"""

from psychopy import event, visual

# creating a 800 x 600 window
win = visual.Window(size=(800, 600), units="height")

# visuals
moles = [visual.Circle(win, radius=0.1, pos=(-0.3, 0), fillColor="red"),
         visual.Circle(win, radius=0.1, pos=(0, 0), fillColor="yellow"),
         visual.Circle(win, radius=0.1, pos=(0.3, 0), fillColor="blue")]

# main loop
show_must_go_on = True
while show_must_go_on:
    # visuals
    moles[0].draw()
    moles[1].draw()
    moles[2].draw()
    win.flip()

    # waiting for any key press
    show_must_go_on = len(event.getKeys(keyList=['escape'])) == 0

# closing the window
win.close()
