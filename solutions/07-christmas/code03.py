"""
Christmas special.
"""
from psychopy import clock, visual, event

BALL_POS = [(0, 0), (-0.08, 0.17), (-0.12, -0.12), (0.1, 0.1), (-0.1, 0.08), (0.1, -0.1)]
BALL_SIZE = [0.01, 0.015, 0.015, 0.02, 0.02, 0.025]
BALL_COLOR = ["red", "red", "blue", "blue", "yellow", "yellow"]
COLORS = ["red", "blue", "yellow"]
TWINKLE_DURATION = 0.5

win = visual.Window(size=(800, 600), units="height")

# create visuals
tree = visual.ImageStim(win, image="pine-tree.png")
balls = [visual.Circle(win, pos=pos, fillColor=color, lineColor=color, radius=size)
         for pos, color, size in zip(BALL_POS, BALL_COLOR, BALL_SIZE)]

# initial twinkle
icolor = 0
for iball in range(len(balls)):
    if BALL_COLOR[iball] == COLORS[icolor]:
        balls[iball].fillColor = COLORS[icolor]
    else:
        balls[iball].fillColor = "white"

show_must_go_on = True
twinkle_timer = clock.Clock()
while show_must_go_on:
    # twinkle balls
    if twinkle_timer.getTime() > TWINKLE_DURATION:
        icolor = (icolor + 1) % len(COLORS) # this wraps the counter to 0
        for iball in range(len(balls)):
            if BALL_COLOR[iball] == COLORS[icolor]:
                balls[iball].fillColor = COLORS[icolor]
            else:
                balls[iball].fillColor = "white"
        twinkle_timer.reset()

    # draw visuals
    tree.draw()
    for ball in balls:
        ball.draw()
    win.flip()

    # check for a key press
    show_must_go_on = len(event.getKeys(keyList=["escape"])) == 0

# clean up
win.close()