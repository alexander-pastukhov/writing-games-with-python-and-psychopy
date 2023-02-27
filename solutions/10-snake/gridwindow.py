"""
Grid window, inherits from PsychoPy window and adds grid attributes and functions.
"""

from psychopy.visual import Window


class GridWindow(Window):
    """
    Grid window, inherits from PsychoPy window and adds grid attributes and functions.

    Properties
    ----------
    grid_size : tuple
        Size of the grid
    square_size_pix : integer
        size of a single square in pixels        

    Methods
    ----------
    grid_to_win(ipos) : Convert grid coordinates to window coordinates in height units.
    """

    def __init__(self, grid_size, square_size_pix):
        """
        Parameters
        ----------
        grid_size : tuple
            Size of the grid
        square_size_pix : integer
            size of a single square in pixels
       """
        self.grid_size = grid_size
        self.square_size = tuple([2 / s for s in self.grid_size])

        # calling constructor of the ancestor
        super().__init__(size=(self.grid_size[0] * square_size_pix, self.grid_size[1] * square_size_pix), units="norm", screen=1)

    def grid_to_win(self, ipos):
        """
        Convert grid coordinates to window coordinates in height units.

        Parameters
        -----------
        ipos : tuple
            (x, y) coordiantes on the grid

        Returns
        -----------
        tuple : (norm_x, norm_y) coordinates in the window
        """
        return [-1 + self.square_size[i] / 2.0 + ipos[i] * self.square_size[i]
                for i in range(2)]
