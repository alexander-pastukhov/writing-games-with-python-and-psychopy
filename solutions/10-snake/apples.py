"""Apple class.
"""

from psychopy import visual
import random


class Apple(visual.ImageStim):
    """
    Apple class.

    Properties
    ----------
    ipos : tuple
        (ix, iy) Location on the grid.
    """

    def __init__(self, win, snake):
        """
        Parameters
        ----------
        win : GridWindow
        snake : Snake
        """
        # find a random location
        self.ipos = [random.randrange(limit) for limit in win.grid_size]
        while snake.is_inside(self.ipos):
            self.ipos = [random.randrange(limit) for limit in win.grid_size]

        # create visuals
        super().__init__(win, image="apple.png", size=win.square_size, pos=win.grid_to_win(self.ipos))
