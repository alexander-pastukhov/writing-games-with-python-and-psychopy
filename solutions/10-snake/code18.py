"""
Snake game.
"""

import json

from psychopy import visual, event

from gridwindow import GridWindow
from snaking import Snake
from apples import Apple
from scoring import Score

DIRECTION_TO_DXY = {"up" : (0, 1), "right": (1, 0), "left": (-1, 0), "down": (0, -1)}
NEW_DIRECTION = {"right" : {"up" : "right", "right" : "down", "down" : "left", "left" : "up"},
                 "left" : {"up" : "left", "right" : "up", "down" : "right", "left" : "down"}}

# getting settings
with open('settings.json') as json_file:
    settings = json.load(json_file)

# creating a window
win = GridWindow(settings["Window"]["grid size [in squares]"], 
                 settings["Window"]["square size [in pixels]"])

# create game objects
snake = Snake(win, settings["Snake"])
apple = Apple(win, snake)
score = Score(win)

# decide on the initial direction of motion
direction = "left"
new_direction = direction

# main loop
user_abort = False
snake.reset_clock()
while not user_abort and not snake.hit_the_wall and not snake.bit_itself:
    # move snake
    if snake.can_move:
        direction = new_direction
        snake.grow(DIRECTION_TO_DXY[direction])
        if snake.is_inside(apple.ipos):
            # ate an apple! 
            score.plus_one()

            # recreate apple elsewhere
            apple = Apple(win, snake)
        else:
            # keep moving
            snake.trim()

    # visuals
    apple.draw()
    snake.draw()
    score.draw()
    win.flip()

# controls
    keys = event.getKeys(keyList=["escape", "left", "right"])
    if len(keys) > 0:
        if keys[0] == "escape":
            user_abort = True
        else:
            new_direction = NEW_DIRECTION[keys[0]][direction]

# cleaning up 
win.close()
