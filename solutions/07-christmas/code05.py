"""
Christmas special.
"""
import json

from psychopy import clock, visual, event
from psychopy.sound import Sound


with open('settings.json') as json_file:
    settings = json.load(json_file)

COLORS = ["red", "blue", "yellow"]

win = visual.Window(size=(800, 600), units="height")

# create visuals
tree = visual.ImageStim(win, image=settings["Tree"])
balls = [visual.Circle(win, pos=pos, fillColor=color, lineColor=color, radius=size)
         for pos, color, size in zip(settings['Balls']['position'], settings['Balls']['color'], settings['Balls']['size'])]

# initial twinkle
icolor = 0
for iball in range(len(balls)):
    if settings['Balls']['color'][iball] == COLORS[icolor]:
        balls[iball].fillColor = COLORS[icolor]
    else:
        balls[iball].fillColor = "white"

show_must_go_on = True
twinkle_timer = clock.Clock()
Sound(settings["Song"]).play()
while show_must_go_on:
    # twinkle balls
    if twinkle_timer.getTime() > settings['Twinkle duration [sec]']:
        icolor = (icolor + 1) % len(COLORS) # this wraps the counter to 0
        for iball in range(len(balls)):
            if settings['Balls']['color'][iball] == COLORS[icolor]:
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