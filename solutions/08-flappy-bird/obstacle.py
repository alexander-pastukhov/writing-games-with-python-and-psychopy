"""
Obstacle class.
"""

import random

from psychopy import clock, visual

class Obstacle:
    """
    Obstacle class.

    Properties
    ----------
    settings : dict
    score : logical
        whether obstacle clearing was accounted for.
    x : float
        Horizontal position.
    frame_timer : psychopy.clock.Clock
    lower_rect : psychopy.visual.Rect
    upper_rect : psychopy.visual.Rect

    Methods
    ----------
    update() : Update obstacle position.
    draw() : Draw obstacle.
    check_if_hit(bird) : Check if bird hit one of the rectangles.
    score() : Score a point if obstacle cleared mid-line the first time.
    """

    def __init__(self, win, settings):
        """
        Parameters
        ----------
        win : psychopy.visual.Window
        setttings : dict
        """
        self.settings = settings

        # whether obstacle clearing was accounted for
        self.scored = False

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

    @property
    def x(self):
        """Horizontal position.
        """
        return self.lower_rect.pos[0]

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
    
    def score(self):
        """Score a point if obstacle cleared mid-line the first time.
        """
        if not self.scored and self.x < 0:
            self.scored = True
            return 1

        return 0

class ObstaclesManager:
    """
    Manager for obstacles.

    Properties
    ----------
    win : psychopy.visual.Window
    settings : dict
    total_score : int
        Total number of obstacles cleared.
    spawn_timer : clock.CountdownTimer
    obstacles : list

    Methods
    ----------
    draw() : Draw all obstacles.
    update() : Update location of all obstacles, spawn new ones, remove ones off the screen.
    check_if_hit(bird) : Check if bird hit any obstacle.
    score() : Score all obstacles, adds one for every cleared obstacle.
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

        # total number of obstacles cleared
        self.total_score = 0

        # time till next obstacle
        self.spawn_timer = clock.CountdownTimer(random.uniform(self.settings["Spawn time"][0], self.settings["Spawn time"][1]))

        # individual obstacles
        self.obstacles = [Obstacle(win, self.settings)]

    def draw(self):
        """Draw all obstacles.
        """
        for obstacle in self.obstacles:
            obstacle.draw()

    def update(self):
        """
        Update location of all obstacles, spawn new ones,
        remove ones off the screen.
        """
        # remove left-most (first) obstacle if it is off the screen
        if self.obstacles[0].x < -1:
            self.obstacles.pop(0)

        # update individual obstacles
        for obstacle in self.obstacles:
            obstacle.update()

        # spawn new obstacle and reset timer
        if self.spawn_timer.getTime() <= 0:
            self.obstacles.append(Obstacle(self.win, self.settings))
            self.spawn_timer = clock.CountdownTimer(random.uniform(self.settings["Spawn time"][0], self.settings["Spawn time"][1]))

    def check_if_hit(self, bird):
        """Check if bird hit any obstacle.
        """
        for obstacle in self.obstacles:
            if obstacle.check_if_hit(bird):
                return True

        # we can be here only, if none of the obstacles were hit
        return False

    def score(self):
        """
        Score all obstacles, adds one for every cleared obstacle.

        Returns
        ----------
        int
        """
        for obstacle in self.obstacles:
            self.total_score += obstacle.score()
        return self.total_score
        