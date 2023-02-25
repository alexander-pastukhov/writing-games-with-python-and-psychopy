"""
Flappy bird class.
"""

from psychopy import clock, visual

class FlappyBird(visual.image.ImageStim):
    """
    FlappyBird class based on ImageStim.

    Properties
    ----------
    settings : dict
    vspeed : float
        Vertical speed
    frame_timer : psychopy.clock.Clock
    is_airborne : logical
        Whether bird touches the ground.

    Methods
    ----------
    update() : Update bird vertical position.
    flap() : Flap wings to fly upwards.
    """
    def __init__(self, win, settings):
        """
        Parameters
        ----------
        win : psychopy.visual.Window
        settings : dict
        """
        self.settings = settings
        self.vspeed = settings["Initial vertical speed"]
        self.frame_timer = clock.Clock()

        super().__init__(win, image=settings["Image"], size=settings["Size"])

    def update(self):
        """Update bird vertical position.
        """
        # get the time and reset the timer
        time_elapsed = self.frame_timer.getTime()
        self.frame_timer.reset()

        # adjust speed and position
        self.vspeed += self.settings["Gravity"] * time_elapsed
        self.pos = (self.pos[0], self.pos[1] + self.vspeed * time_elapsed)

    def flap(self):
        """Flap wings to fly upwards.
        """
        self.vspeed = self.settings["Flap speed"]

    @property
    def is_airborne(self):
        """Whether bird touches the ground.
        """
        return self.pos[1] > -1
