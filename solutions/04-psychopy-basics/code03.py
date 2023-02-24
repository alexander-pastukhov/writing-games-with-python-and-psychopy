"""
PsychoPy basic code.
"""

from psychopy import event, visual

# creating a 800 x 600 window
win = visual.Window(size=(800, 600))

# visuals
press_escape_text = visual.TextStim(win, "Press escape to exit")

# main loop
show_must_go_on = True
while show_must_go_on:
    # visuals
    press_escape_text.draw()
    win.flip()

    # waiting for any key press
    show_must_go_on = len(event.getKeys(keyList=['escape'])) == 0

# closing the window
win.close()
