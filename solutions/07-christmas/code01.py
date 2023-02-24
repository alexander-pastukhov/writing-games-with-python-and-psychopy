"""
Christmas special.
"""

from psychopy import visual, event

win = visual.Window(size=(800, 600))

# create visuals
tree = visual.ImageStim(win, image="pine-tree.png")

# draw visuals
tree.draw()
win.flip()

# wait for a key press
event.waitKeys()

# clean up
win.close()