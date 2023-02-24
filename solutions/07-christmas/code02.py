"""
Christmas special.
"""
from psychopy import visual, event

BALL_POS = [(0, 0), (-0.08, 0.17), (-0.12, -0.12), (0.1, 0.1), (-0.1, 0.08), (0.1, -0.1)]
BALL_SIZE = [0.01, 0.015, 0.015, 0.02, 0.02, 0.025]
BALL_COLOR = ["red", "red", "blue", "blue", "yellow", "yellow"]


win = visual.Window(size=(800, 600), units="height")

# create visuals
tree = visual.ImageStim(win, image="pine-tree.png")
balls = [visual.Circle(win, pos=pos, fillColor=color, lineColor=color, radius=size)
         for pos, color, size in zip(BALL_POS, BALL_COLOR, BALL_SIZE)]

# draw visuals
tree.draw()
for ball in balls:
    ball.draw()
win.flip()

# wait for a key press
event.waitKeys()

# clean up
win.close()