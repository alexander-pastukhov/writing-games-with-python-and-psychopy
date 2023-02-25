"""
Timer response task classes.
"""

import random

from psychopy import clock, visual

class Target:
    """
    Moving target class.
    """

    def __init__(self, win, settings, ipos):
        """
        Parameters
        ----------
        win : psychopy.visual.Window
        setttings : dict
        ipos : int
            Position index.
        """
        self.settings = settings
        self.speed = settings["Speed"]
        self.frame_timer = clock.Clock()
        self.rect = visual.Rect(win,
                                size=(settings["Width"], settings["Height"]),
                                pos=(settings["Position"][ipos], 1 - settings["Height"] / 2),
                                fillColor = settings["Color"][ipos],
                                lineColor = settings["Color"][ipos])
        
    def draw(self):
        """Draw target.
        """
        self.rect.draw()

    def fall(self):
        """Move the target downwards.
        """
        self.rect.pos = (self.rect.pos[0], self.rect.pos[1] - self.speed * self.frame_timer.getTime())
        self.frame_timer.reset()


