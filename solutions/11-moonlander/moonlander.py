"""
Moonlander ship class.
"""

from psychopy import visual
import pyglet
import random

GRAVITY = 0.0001
VERTICAL_ACC = GRAVITY * 2
HORIZONTAL_ACC = 0.0002
FULL_TANK = 100


class MoonLander:
    """
    Moonlander ship.

    Properties
    -----------
    bottom : float
        Bottom edge of moon lander
    left: float
        Left edge of moon lander
    right : float
        Right edge of moon lander
    fuel : int
        Amount of fuel left
    pos : tuple
        Position of moon lander
    speed : tuple
        list of horizontal and vertical speed
    visuals : object
        Visuals of moon lander
    """
    def __init__(self, win, settings):
        """
        Creates visuals of the moon lander.

        Parameters
        ----------
        win : psychopy.visual.Window
        settings : dict
        """
        self.settings = settings

        self.fuel = None
        self.pos = None
        self.speed = (0, 0)
        self.fuel_bar = visual.Rect(win, width=0.1, lineColor="black")
        self.visuals = visual.ImageStim(win, image=settings["Image"])
        self.reset()

        # setting up keyboard monitoring
        self.key = pyglet.window.key
        self.keyboard = self.key.KeyStateHandler()
        win.winHandle.push_handlers(self.keyboard)

    def reset(self):
        """
        Randomizes position of moon lander for new round.
        """
        self.visuals.pos = (random.uniform(-0.5, 0.5), random.uniform(0.8, 0.9))
        self.speed = (0, 0)
        self.fuel = FULL_TANK

    def update(self):
        """
        Updates position of moon lander according to speed and thrusters and
        reduced fuel when a key is pressed.
        """
        if self.fuel > 0:
            if self.keyboard[self.key.DOWN]:
                self.speed = (self.speed[0], self.speed[1] - GRAVITY + VERTICAL_ACC)
                self.fuel -= 1
            elif self.keyboard[self.key.LEFT]:
                self.speed = (self.speed[0] + HORIZONTAL_ACC, self.speed[1] - GRAVITY)
                self.fuel -= 1
            elif self.keyboard[self.key.RIGHT]:
                self.speed = (self.speed[0] - HORIZONTAL_ACC, self.speed[1] - GRAVITY)
                self.fuel -= 1
            else:
                self.speed = (self.speed[0], self.speed[1] - GRAVITY)
        else:
            self.speed = (self.speed[0], self.speed[1] - GRAVITY)

        self.visuals.pos = self.visuals.pos + self.speed

        self.fuel_bar.height = self.fuel/100
        self.fuel_bar.pos = (-0.95, self.fuel_bar.height/2)
        if self.fuel > 66:
            self.fuel_bar.fillColor = "green"
        elif self.fuel < 66 and self.fuel > 33:
            self.fuel_bar.fillColor = "orange"
        else:
            self.fuel_bar.fillColor = "red"

    def draw(self):
        """
        Draws moon lander.
        """
        self.visuals.draw()
        self.fuel_bar.draw()

    @property
    def bottom(self):
        """
        Computes and returns coordinate of bottom edge of the lander.

        """
        self.__bottom = self.visuals.pos[1] - self.visuals.size[1]/2
        return self.__bottom

    @property
    def left(self):
        """
        Computes and returns coordinate of left edge of the lander.

        """
        self.__left = self.visuals.pos[0] - self.visuals.size[0]/2
        return self.__left

    @property
    def right(self):
        """
        Computes and returns coordinate of right edge of the lander.

        """
        self.__right = self.visuals.pos[0] + self.visuals.size[0]/2
        return self.__right
