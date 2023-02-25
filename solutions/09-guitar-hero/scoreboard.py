"""
Class for keeping and showing the score.
"""

from psychopy.visual import TextStim

class ScoreBoard(TextStim):
    """
    Class for keeping and showing the score.

    Properties
    ----------
    score : int
        Current score

    Methods
    ----------
    __iadd__(additional_score) : Add to the score.
    """

    def __init__(self, win):
        """
        Parameters
        ----------
        win : psychopy.visual.Window
        """
        self.score = 0
        super().__init__(win, "0", pos=(-0.95, 0.95))

    def __iadd__(self, additional_score):
        """
        Add to the score.

        Parameters
        ----------
        additional_score : int
        """
        self.score += additional_score
        self.text = str(self.score)
        return self
