"""
Obstacle class.
"""

import random

from psychopy import clock, visual

class Obstacle:
    """
    Obstacle class.
    """

    def __init__(self, win, settings):
        """
        Parameters
        ----------
        win : psychopy.visual.Window
        setttings : dict
        """
        self.settings = settings

        # timing
        self.frame_timer = clock.Clock()

        # deciding on a location
        x = 1 - settings["Width"] / 2

        # figuring out opening size
        opening_size = random.uniform(settings["Minimal size"], settings["Maximal size"])

        # find remaining space and place opening within it
        available_space = 2 - (settings["Lower margin"] + settings["Upper margin"]) - opening_size
        opening_y = -1 + settings["Lower margin"] + opening_size /2 + available_space * random.random()
        opening_lower_edge = opening_y - opening_size / 2
        opening_upper_edge = opening_y + opening_size / 2

        # creating lower rectangle
        lower_rect_height = opening_lower_edge - (-1) # lower screen edge is -1
        self.lower_rect = visual.Rect(win,
                                      width=settings["Width"],
                                      height=lower_rect_height,
                                      pos=(x, -1 + lower_rect_height / 2.0),
                                      lineColor=settings["Color"],
                                      fillColor=settings["Color"])

        # creating upper rectangle
        upper_rect_height = 1 - opening_upper_edge
        self.upper_rect = visual.Rect(win,
                                      width=settings["Width"],
                                      height=upper_rect_height,
                                      pos=(x, 1 - upper_rect_height / 2.0),
                                      lineColor=settings["Color"],
                                      fillColor=settings["Color"])

    def update(self):
        """Update obstacle position.
        """
        # get the time and reset the timer
        elapsed_time = self.frame_timer.getTime()
        self.frame_timer.reset()

        # move rectangles
        self.lower_rect.pos = (self.lower_rect.pos[0] - self.settings["Speed"] * elapsed_time, self.lower_rect.pos[1])
        self.upper_rect.pos = (self.upper_rect.pos[0] - self.settings["Speed"] * elapsed_time, self.upper_rect.pos[1])

    def draw(self):
        """Draw obstacle.
        """
        self.lower_rect.draw()
        self.upper_rect.draw()

    def check_if_hit(self, bird):
        """
        Check if bird hit one of the rectangles.

        Parameters
        ----------
        bird : FlappyBird

        Returns
        ----------
        logical
        """
        return self.lower_rect.overlaps(bird) or self.upper_rect.overlaps(bird)

class ObstaclesManager:
    """
    Manager for obstacles.
    """

    def __init__(self, win, settings):
        """
        Parameters
        ----------
        win : psychopy.visual.Window
        setttings : dict
        """
        self.win = win
        self.settings = settings
        self.spawn_timer = clock.Clock()

        self.obstacles = [Obstacle(win, self.settings)]

    def draw(self):
        """Draw all obstacles.
        """
        for obstacle in self.obstacles:
            obstacle.draw()

    def update(self):
        """Update location of all obstacles.
        """
        for obstacle in self.obstacles:
            obstacle.update()

    def check_if_hit(self, bird):
        """Check if bird hit any obstacle.
        """
        for obstacle in self.obstacles:
            if obstacle.check_if_hit(bird):
                return True

        # we can be here only, if none of the obstacles were hit
        return False            

        