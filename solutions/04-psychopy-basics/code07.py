"""
PsychoPy basic code.
"""

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
    show_must_go_on = len(event.getKeys(keyList=['escape'])) == 0

# closing the window
win.close()
