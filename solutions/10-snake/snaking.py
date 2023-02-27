"""
Snake-related classes.

* SnakeSegment
* Snake
"""

import random

from psychopy import clock, visual

class SnakeSegment:
    """
    A single snake segment.

    Properties
    ----------
        ipos : tuple
            (gridx, gridy) location on the grid
        visuals = visual.Rect

    Methods
    ----------
        draw() : Draw visuals.
    """

    def __init__(self, win, ipos, color):
        """
        Parameters
        ----------
        win : GridWindow
        ipos : tuple
            (gridx, gridy) location on the grid
        color : psychopy color
        """
        self.ipos = ipos
        self.visuals = visual.Rect(win, size=win.square_size, pos=win.grid_to_win(ipos), fillColor=color, lineColor="white")

    def draw(self):
        """Draw visuals.
        """
        self.visuals.draw()


class Snake:
    """
    Snake class.

    Properties
    ----------
    win : GridWindow
    settings : dict
            Setting for the snake.
    segments : list
        SnakeSegment
    movement_clock : clock.CountdownTimer
        Timer till moving to the next square.
    can_move : bool
        Whether it is time to move the snake.
    hit_the_wall : bool
        Whether a snake hit the wall.
    bit_itself : bool
        Whether snake bit itself.
    Methods
    ----------
    reset_clock() : Reset movement timer.
    reset() : Initialize the snake: single segment at the center of the screen.
    draw() : Draw all segments.
    is_inside(ipos) : Check whether grid position is inside the snake.
    grow(dxy) : Grow snake by a single segment in dxy direction.
    trim() : Trim the last segment of the snake.
    """

    def __init__(self, win, settings):
        """
        Parameters
        ----------
        win : GridWindow
        settings : dict
            Setting for the snake
        """
        self.win = win
        self.settings = settings
        self.segments = [SnakeSegment(self.win, 
                                      (self.win.grid_size[0]//2, self.win.grid_size[1]//2),
                                      self.settings["color"])]

        step_duration = 1 / self.settings["speed [squares per second]"]
        self.movement_clock = clock.CountdownTimer(step_duration)

    def reset_clock(self):
        """Reset movement timer.
        """
        self.movement_clock.reset()

    @property
    def can_move(self):
        """logical: Whether it is time to move the snake.
        """
        ready_to_move = self.movement_clock.getTime() <= 0
        if ready_to_move:
            self.reset_clock()
        return ready_to_move

    def reset(self):
        """Initialize the snake: single segment at the center of the screen.
        """
        self.segments.clear()
        self.segments = [SnakeSegment(self.win, 
                                      (self.win.grid_size[0]//2, self.win.grid_size[1]//2),
                                      self.settings["color"])]
        self.reset_clock()

    def draw(self):
        """Draw all segments.
        """
        for segment in self.segments:
            segment.draw()

    def grow(self, dxy):
        """
        Grow snake by a single segment in dxy direction.

        Parameters
        -----------
        dxy : tuple
            (dx, dy) direction of motion
        """
        self.segments.insert(0,
                             SnakeSegment(self.win,
                                          [xy + change for xy, change in zip(self.segments[0].ipos, dxy)],
                                          self.settings["color"]))

    def trim(self):
        """Trim the last segment of the snake.
        """
        self.segments.pop()

    @property
    def hit_the_wall(self):
        """bool: whether a snake hit the wall.
        """
        return self.segments[0].ipos[0] == -1 or \
               self.segments[0].ipos[1] == -1 or \
               self.segments[0].ipos[0] == self.win.grid_size[0] or \
               self.segments[0].ipos[1] == self.win.grid_size[1]

    def is_inside(self, ipos):
        """
        Check whether grid position is inside the snake.
            
        Parameters
        ----------
        ipos : tuple
            (x, y) position on the grid

        Returns
        ----------
        bool
        """
        for segment in self.segments:
            if segment.ipos[0] == ipos[0] and segment.ipos[1] == ipos[1]:
                return True
        return False

    @property
    def bit_itself(self):
        """bool : Whether snake bit itself.
        """
        for segment in self.segments[1:]:
            if segment.ipos[0] == self.segments[0].ipos[0] and \
               segment.ipos[1] == self.segments[0].ipos[1]:
                return True
        return False
