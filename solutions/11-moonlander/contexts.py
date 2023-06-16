"""
Game context classes.

GameAbort
GameContext
"""
import json

from psychopy import visual, event

class GameAbort(Exception):
    """Game abort by user exception.
    """
    pass


class GameContext:
    """
    Game context.

    Properties
    ----------
    win : psychopy.visual.Window
    settings : dict
    filename : str
        Settings filename
    """

    def __init__(self, filename):
        """
        Parameters
        ----------
        filename : str
        """
        self.filename = filename
        self.win = None
        self.settings = None

    def __enter__(self):
        """Enter context.
        """
        # getting settings
        with open(self.filename) as json_file:
            self.settings = json.load(json_file)

        # opening window
        self.win = visual.Window(self.settings["Window"]["Size [pix]"])

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """ Exit context.
         """
        self.win.close()

        # is this abort or something more sinister?
        if exc_type is GameAbort:
            return True
