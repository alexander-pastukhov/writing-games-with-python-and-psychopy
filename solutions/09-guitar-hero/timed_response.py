"""
Timer response task classes.

Target
TimedResponseTask
TimedResponseTaskPsychoPy
"""

import time 

from psychopy import clock, data, visual

from generators import next_target_generator, time_to_next_target_generator

class Target:
    """
    Moving target class.

    Properties
    ----------
    score : None / int 
        Whether target was score (None, not scored yet) and what was the score.
    ipos : int
        Position index.
    settings : dict
    speed : float
        Vertical speed in norm units per second.
    frame_timer : clock.Clock
    rect : psychopy.visual.Rect
    is_below_the_screen : logical
        Upper edge is below the screen.

    Methods
    ----------
    draw() : Draw target.
    fall() : Move the target downwards.
    overlaps(yline) : Check whether target overlaps with the line and compute the score.
    """

    def __init__(self, win, settings, speed, ipos):
        """
        Parameters
        ----------
        win : psychopy.visual.Window
        settings : dict
        speed : float
             Vertical speed in norm units per second.
        ipos : int
            Position index.
        """
        self.score = None
        self.ipos = ipos
        self.settings = settings
        self.speed = speed
        self.frame_timer = clock.Clock()
        self.rect = visual.Rect(win,
                                size=(settings["Width"], settings["Height"]),
                                pos=(settings["Position"][ipos], 1 - settings["Height"] / 2),
                                fillColor = settings["Color"][ipos],
                                lineColor = settings["Color"][ipos])
        
    def draw(self):
        """Draw target.
        """
        self.rect.draw()

    def fall(self):
        """Move the target downwards.
        """
        self.rect.pos = (self.rect.pos[0], self.rect.pos[1] - self.speed * self.frame_timer.getTime())
        self.frame_timer.reset()

    @property
    def is_below_the_screen(self):
        """Upper edge is below the screen.
        """
        return self.rect.pos[1] + self.rect.size[1] < -1
    
    def overlaps(self, yline):
        """Check whether target overlaps with the line and compute the score.

        Parameters
        ----------
        yline : float
            Location of the finish line.

        Returns
        ----------
        logical
        """
        if self.score is None:
            score = int(10 - 10 * abs(self.rect.pos[1] - yline) / (self.rect.size[1] / 2))
            if score > 0:
                self.score = score
                self.rect.lineColor = "white"
                return True
            
        return False


class TimedResponseTask:
    """
    Timed response task.

    Properties
    ----------
    win : psychopy.visual.Window
    setttings : dict
    speed_factor : float
        Difficulty.
    time_to_next_target : time_to_next_target_generator
    next_target_pos : next_target_generator
    new_target_timer : clock.CountdownTimer
    self.targets : list
    self.finish_line : visual.Line
    correct_in_a_row : int
        Staircase counter.

    Methods
    ----------
    draw() : Draw all targets and the finish line.
    update() : Update all targets, make them fall.
    add_next_target() : Add next target, if the time is right.
    check(ipos) : Check whether response was for a target.
    staircase(correct) : Adjust speed via 3-up-1-down staircase.
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

        # difficulty
        self.speed_factor = 1
        self.correct_in_a_row = 0

        # timing
        self.time_to_next_target = time_to_next_target_generator(settings["Spawn time"])
        self.next_target_pos = next_target_generator(settings["Shuffle repetitions"])
        self.new_target_timer = clock.CountdownTimer(next(self.time_to_next_target))

        # targets
        self.targets = []

        # finishing line
        self.finish_line = visual.Line(win, start=(-1, settings["Finish line Y"]), end=(1, settings["Finish line Y"]), lineColor="yellow")

    def draw(self):
        """Draw all targets and the finish line.
        """
        for target in self.targets:
            target.draw()
        self.finish_line.draw()

    def update(self):
        """Update all targets, make them fall.
        """
        # make all targets fall
        for target in self.targets:
            target.fall()

        # dispose of targets below the screen
        if self.targets:
            while self.targets[0].is_below_the_screen:
                self.targets.pop(0)

        # see if we can add more
        self.add_next_target()

    def add_next_target(self):
        """Add next target, if the time is right.
        """
        if self.new_target_timer.getTime() <= 0:
            self.targets.append(Target(self.win, self.settings, self.settings["Speed"] * self.speed_factor, next(self.next_target_pos)))
            self.new_target_timer = clock.CountdownTimer(next(self.time_to_next_target))

    def check(self, ipos):
        """
        Check whether response was for a target.

        Parameters
        ----------
        ipos : int
            Response location.

        Returns
        ----------
        int : Score.
        """
        for target in self.targets:
            if target.ipos == ipos and target.overlaps(self.settings["Finish line Y"]):
                self.staircase(True)
                return target.score
        
        # no valid target at the finish line
        self.staircase(False)
        return 0

    def staircase(self, correct):
        """
        Adjust speed via 3-up-1-down staircase.

        Parameters
        ----------
        correct : logical
        """
        if correct:
            # up
            self.correct_in_a_row += 1
            if self.correct_in_a_row == 3:
                self.speed_factor *= self.settings["Staircase multuplier"]
                self.correct_in_a_row = 0
        else:
            # down
            self.speed_factor /= self.settings["Staircase multuplier"]
            self.correct_in_a_row = 0
        
        # distribute speed factor among targets
        for target in self.targets:
            target.speed = self.settings["Speed"] * self.speed_factor


class TimedResponseTaskPsychoPy:
    """
    Timed response task with PsychoPy staircase.
    
    Properties
    ----------
    win : psychopy.visual.Window
    setttings : dict
    speed_factor : float
        Difficulty.
    time_to_next_target : time_to_next_target_generator
    next_target_pos : next_target_generator
    new_target_timer : clock.CountdownTimer
    self.targets : list
    self.finish_line : visual.Line
    stairhandler : data.StairHandler
        Staircase.

    Methods
    ----------
    draw() : Draw all targets and the finish line.
    update() : Update all targets, make them fall.
    add_next_target() : Add next target, if the time is right.
    check(ipos) : Check whether response was for a target.
    staircase(correct) : Adjust speed via 3-up-1-down staircase.
    save() : Save logs under unique timestamp name.
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

        # difficulty
        self.stairhandler = data.StairHandler(startVal=1, nUp=1, nDown=3, stepType="log", stepSizes=-0.1, nTrial=1000, nReversals=1000)
        self.speed_factor = next(self.stairhandler)

        # timing
        self.time_to_next_target = time_to_next_target_generator(settings["Spawn time"])
        self.next_target_pos = next_target_generator(settings["Shuffle repetitions"])
        self.new_target_timer = clock.CountdownTimer(next(self.time_to_next_target))

        # targets
        self.targets = []

        # finishing line
        self.finish_line = visual.Line(win, start=(-1, settings["Finish line Y"]), end=(1, settings["Finish line Y"]), lineColor="yellow")

    def draw(self):
        """Draw all targets and the finish line.
        """
        for target in self.targets:
            target.draw()
        self.finish_line.draw()

    def update(self):
        """Update all targets, make them fall.
        """
        # make all targets fall
        for target in self.targets:
            target.fall()

        # dispose of targets below the screen
        if self.targets:
            while self.targets[0].is_below_the_screen:
                self.targets.pop(0)

        # see if we can add more
        self.add_next_target()

    def add_next_target(self):
        """Add next target, if the time is right.
        """
        if self.new_target_timer.getTime() <= 0:
            self.targets.append(Target(self.win, self.settings, self.settings["Speed"] * self.speed_factor, next(self.next_target_pos)))
            self.new_target_timer = clock.CountdownTimer(next(self.time_to_next_target))

    def check(self, ipos):
        """
        Check whether response was for a target.

        Parameters
        ----------
        ipos : int
            Response location.

        Returns
        ----------
        int : Score.
        """
        for target in self.targets:
            if target.ipos == ipos and target.overlaps(self.settings["Finish line Y"]):
                self.staircase(True)
                return target.score
        
        # no valid target at the finish line
        self.staircase(False)
        return 0

    def staircase(self, correct):
        """
        Adjust speed via 3-up-1-down staircase.

        Parameters
        ----------
        correct : logical
        """
        self.stairhandler.addResponse(correct)
        self.speed_factor = next(self.stairhandler)
        
        # distribute speed factor among targets
        for target in self.targets:
            target.speed = self.settings["Speed"] * self.speed_factor

    def save(self):
        """Save logs under unique timestamp name.
        """
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        self.stairhandler.saveAsText(timestamp + ".txt)
