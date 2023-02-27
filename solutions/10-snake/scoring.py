"""Score class.
"""

from re import L
from psychopy import visual

class Score(visual.TextStim):
    """
    Score class.
    
    Properties
    ----------
    score : int

    Methods
    ----------
    plus_one() : Increase the score by one.
    """

    def __init__(self, win):
        """
        Parameters
        ----------
        win : psychopy.visual.Window
        """
        self.score = 0
        super().__init__(win, text="Score: %d"%(self.score), pos=(0, 0.9))

    def plus_one(self):
        """Increase the score by one.
        """
        self.score += 1
        self.text = "Score: %d"%(self.score)
