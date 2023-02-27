"""
Snake game.
"""

import json
import sys

from psychopy import clock, event, gui, sound, visual

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

# difficulty
difficulty_dlg = gui.Dlg(title="Snake")
difficulty_dlg.addField('Difficulty:', choices=["Easy", "Medium", "Hard"])
ok_data = difficulty_dlg.show()
if not difficulty_dlg.OK:
    # user aborted
    sys.exit(0)
# updating snake speed based on difficulty
settings["Snake"]["speed [squares per second]"] = settings["Difficulty"][ok_data[0]]

# creating a window
win = GridWindow(settings["Window"]["grid size [in squares]"], 
                 settings["Window"]["square size [in pixels]"])

# create game objects
snake = Snake(win, settings["Snake"])
apple = Apple(win, snake)
score = Score(win)
hearts = [visual.ImageStim(win, "heart.png", size=win.square_size, pos=win.grid_to_win((ipos, win.grid_size[1]-1)))
          for ipos in range(3)]

# audio
round_over_sound = sound.Sound("game-over-arcade.wav")
game_over_sound = sound.Sound("8-bit-game-over-sound.wav")

# decide on the initial direction of motion
direction = "left"
new_direction = direction

# main loop
user_abort = False
for lives in range(3):
    # pause before the round start
    score.draw()
    snake.draw()
    apple.draw()
    for heart in hearts[:(3-lives)]:
        heart.draw()
    visual.TextStim(win, "Press SPACE to start").draw()
    win.flip()
    keys = event.waitKeys(keyList=["space", "escape"])
    if keys[0] == "escape":
        break

    # next round
    snake.reset()
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
        for heart in hearts[:(3-lives)]:
            heart.draw()
        win.flip()

        # controls
        keys = event.getKeys(keyList=["escape", "left", "right"])
        if len(keys) > 0:
            if keys[0] == "escape":
                user_abort = True
            else:
                new_direction = NEW_DIRECTION[keys[0]][direction]

    # are we here because of the abort?
    if user_abort:
        break

    # play appropriate tune
    if lives < 2:
        round_over_sound.play()
    else:
        game_over_sound.play()

# blinking game over 
if not user_abort:
    game_over_text = visual.TextStim(win, "Game over", color="red")
    text_is_on = True
    text_timer = clock.CountdownTimer(0.5)
    can_continue = False
    while not can_continue:
        # visuals
        score.draw()
        snake.draw()
        apple.draw()
        if text_is_on:
            game_over_text.draw()
        win.flip()

        # blinking
        if text_timer.getTime() <= 0:
            text_is_on = not text_is_on
            text_timer.reset()

        # continue
        can_continue = event.getKeys(keyList=["space"])

# cleaning up 
win.close()
