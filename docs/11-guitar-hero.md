# Guitar Hero: staircase and iterator functions {#seminar-02-06}

## Chapter concepts

* Staircase
* Iterator / Generator functions
* Special class methods


## Getting the difficulty just right: Staircase procedure
In game design, one of the hardest things to get right is difficulty. Make your game too easy and it will be boring. Make it too hard and only hardcore fans will play and only for [an achievement](https://www.imdb.com/title/tt4975856/). Thus, you would like to make your game hard enough to push a player to the limit but not much harder than that, so not to frustrate them. One way to solve this conundrum is to create different preset difficulty levels. An alternative way is to make a game that adapts its difficulty to the player.

The same is true for psychophysical experiments. You want to test ability of your participants to perform a certain task at their limit for one simple reason: At this _threshold_ point influence of any additional factor, whether positive or negative, is most pronounced. For example, use an unusual stimulus configuration or increase attentional load and performance will probably drop. Allow to preallocate attention via cuing or use a prime that is congruent with a target and performance is likely to improve. Of course, these manipulations will have the same overall effect also when the task is particularly easy or maddeningly hard but it will much more difficult to _measure_ this effect. It is one thing if performance drops from 75% to 65% than if it goes from 98% to 95% or from 53% to 52%^[Here, I assume that 50% is chance level performance.] or vice versa. The silliest thing you can do is to _hope_ that performance will allow you too see the effect of the factors that you manipulated. In things like these, knowledge and careful design is definitely superior to hope.

Thus, you want performance of your participants to be approximately in the middle between the ceiling (100% performance, fastest response times, super easy) and the floor (chance level performance, slowest response times, super hard or even impossible). But how do you know where this magic point for a _particular_ person is? Particularly, if the task is novel so you have little information to guide you^[It is the usual paradox that in order to optimally measure a threshold condition for a particular task, you should measure at or around the threshold. But if you already know where to measure, you don't need to measure.]. The solution is to adjust the difficulty on-the-fly based on participant's responses. For example, if you have a two-alternatives-forced-choice task, you can use a two-up-one-down staircase (difficulty increases after two correct responses and decreases after one mistake) that targets 70.7% performance threshold. There are different methods and even different ways to use the same core method (e.g., does the step stays constant or changes, what is the run termination criteria, etc.), so it is always a good idea to refresh your memory and read about [adaptive procedures](https://doi.org/10.3758/BF03194543) when designing your next experiment.

In our game, we will use a very simple 3-up-1-down staircase: get the three responses correct on a row and things get faster, make a mistake and the game slows down. We'll see how fast you can go! First, you will implement it by hand and then we will use its [PsychoPy implementation](https://psychopy.org/api/data.html#stairhandler). 

## Guitar Hero
Today, we will program Guitar Hero game. In the original game, you must play notes on a guitar-shaped controller pressing buttons at the right time, just like when you actually play music on a guitar. On the one hand, it is a straightforward and repetitive motor task. On the other hand, take a fast and complicated music piece and it'll take many minutes or even hours of practice to get it right. It is a lot of fun, as music cues and primes your responses. The same idea of music-synchronized-actions was used in _Raymon Legends_ music levels where jumps and hits are timed to drums or bass. It is a bizarrely cool dance-like sequence and a very satisfying experience, also when watching pros to do it (I happened to have couple in my household).

We will program this game (sans Guitar and Hero) and you can see it in the video below. The player must press a correct key (_left_, _down_, or _right_) whenever the target crosses the line. Pressing it to early or too late counts as a mistake. Of course, the faster the targets go, the harder it is to respond on time and with a correct key. As I wrote above, we will use the 3-up-1-down staircase procedure to control for that. 



As per usual, we will take a gradual approach:

* Boilerplate code
* Create a class for individual moving targets
* Create a timed-response task class that will create them (using cool generators), dispose of them, check the response, and adjust staircase.
* Add bells-and-whistles like score and time limited runs.

## Boilerplate
Create our usual boilerplate code in _code01.py_:

* Create file with basic settings (e.g., window size, I've picked 640×480 but choose whatever looks good on your screen) to which you can add later on. 
* Import what is needed from PsychoPy.
* Create a window. 
* Create our usual main game loop with `gamover` variable, flipping the window, and checking for _escape_ button press.

::: {.rmdnote .program}
Put your boilerplate code into _code01.py_.
:::

## Target and TimedResponseTask classes
Our main work horse will be `TimedResponseTask` class. It will spawn a new random `Target` at random intervals (which will depend on speed), pass speed information to moving targets, and remove targets, once they disappear below the screen. The `Target` class will inherit from  [visual.rect.Rect](https://psychopy.org/api/visual/rect.html#psychopy.visual.rect.Rect) class with some extra bells and whistles to make it appear at the right location, move at the right speed, change its line color (indicating a correct response), compute whether it is already off the screen, etc. We will start with a single target first.

## Target class: a static target
First, create a `Target` class: a colored rectangle in one of the three positions that starts at the top of the window and moves down at a specific speed. Its constructor should take PsychoPy window as a parameter (you will need it to create the rectangle as an attribute), position index (`ipos`, from 0 to 2), speed (`speed`, in `"norm"` units _per second_), and common settings (`settings`, a dictionary with target-specific settings from our settings file) . The only thing we need to do right now in the constructor is use the constructor of the ancestor `Rect()` class via `super().__init__(...)` call, similar to how you initialized an the `FlappyBird` class. Think of which parameters you need to pass, as you need to think about rectangle's position, size, and color. Store both `ipos` and `speed` as attributes for later use. In addition, define a `score` attribute and set it to `None`. This will hold the score the participant got for this target and `None` means that it has not been responded upon yet.

The second parameter --- position index --- determines the horizontal position of the target and its color (to make targets more fun and distinct). For my code, I have decided to make rectangle 0.4 norm units wide and 0.1 norm units high. The leftmost _red_ rectangle (for `ipos` 0), is centered at -0.5, the middle _green_ one is dead center, and the rightmost _blue_ rectangle is centered at 0.5. I've defined all these in my `settings.json` file under `Target` group. Think about how you can compute both color and position for a target from `ipos` and `settings` without using if-else statements. Also, think about the y-position of the rectangle, so it appears right at the top of the window.

Test it by creating a target at one of the position (or three targets at all three positions) and drawing them in the main loop. You should get nice looking but static rectangle(s).

::: {.rmdnote .program}
Put updated code in `code02.py`  and create the class `Target` in a separate file.
:::

## Target class: a moving target
Our targets fall down at speed defined by their `speed` attribute. Later on, we will change that attribute dynamically to speed up or slow down their fall.

For the actual falling down, implement a new method, call it `fall()`, that will update target's position on every frame. The speed is in `norm units per second`, thus, to compute the change in vertical position you also need to know the how much time  _in seconds_ has elapsed since last position update. The simplest way to do this is by using a [Clock](https://psychopy.org/api/clock.html#psychopy.clock.Clock) class. You create it as an attribute in the constructor and then, in the `fall()` method you use its current time to compute and apply a change in vertical position of the rectangle. Don't forget to reset the clock after that! (Same logic as for the Flappy Bird you already programmed.)

Include `fall()` method call in the main loop and see how the target falls. Experiment with falling speed!

::: {.rmdnote .program}
Put updated code in `code03.py`  and update the class `Target`.
:::

## Iterator/Generator functions
In the next section, we will create a `TimedResponseTask` class that will generate targets at a random location and after a random interval. We can, of course, do it directly in the class but where's fun in that?! Instead, we will use this as an opportunity to learn about iterator/generator functions. An iterator is a _function_ that uses `yield` instead of `return` statement to, well,  _yield_ a value. It _yields_ it, because the function itself _returns_ an iterator object that you can iterate over in a for loop or via `next()` function. Importantly, `yield` "freezes" execution of the function and the next time you call the function _it continues from that point_ rather than from the start of the function. Once you reach the end of the function, it automatically raises `StopIteration()` exception, so you don't need to worry about how to communicate that you ran out of items. It may sound confusing but it is really simple. Here an example to illustrate this:


```python
def iterator_fun():
    yield 3
    yield 1
    yield "wow!"
  
# function returns an iterator, not a value!
print(iterator_fun())
#> <generator object iterator_fun at 0x000001B32C3176F0>

# iterating via for loop
for elem in iterator_fun():
    print(elem)
#> 3
#> 1
#> wow!
    
# iterating via next(), note you use an iterator object 
# that function returned, not the function itself!
an_iterator = iterator_fun()  

# now you can use an_iterator to get a next item from it
print(next(an_iterator))
#> 3
print(next(an_iterator))
#> 1
print(next(an_iterator))
#> wow!
```


```python
# next call will raise an exception StopIteration()
print(next(iterator_var))
#> name 'iterator_var' is not defined
```

This format makes writing iterators very easy, just `yield` whatever you want in an order you want and Python will take care of the rest. You can also `yield` in a loop, inside an if-else statement, etc. Look at the code below and figure out what will be printed out before running it.
```python
def iterator_fun():
  for e in range(4):
    if e % 2 == 1:
      yield e

for item in iterator_fun():
  print(item)
```

For our `TimedResponseTask` class, we will need two _generators_. They are _generators_ rather than _iterators_ because both will be endless (iterators iterate over finite set of items). One that generates a random delay until the next target and one that generates a random target position (0, 1, or 2). Implement both in a separate file (I called it _generators.py_).

The `time_to_next_target_generator()` function should take a tuple of two float values, which define shortest and longest allowed delays, as a parameter and _yield_ a [random number](https://docs.python.org/3/library/random.html#random.uniform) within this range in an _endless_ loop. We need the endless loop (`while True:` will do) because we do not know how many values we will need, so we just generate as many as needed on demand.

The `next_target_generator()` will be a bit more interesting. It can just return a [random.choice](https://docs.python.org/3/library/random.html#random.choice) from 0, 1, and 2 but where is fun in that? Instead, we will make it a bit more complicated to ensure that all three targets appear equal number of times within _3N_ trials, where _N_ will be a parameter of the generator function. This would ensure random, reasonably unpredictable but balanced targets in the short run. Remember, in the long run random choice will always give us a balanced uniform distribution but there is not such guarantee for the shorter runs of a few trials. First, you should create a list where each target appears N times (think how you can do it using [range()](https://docs.python.org/3/library/functions.html#func-range), [list()](https://docs.python.org/3/library/functions.html#func-list) and [*](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)). Then, create an endless loop (again, we don't know how many values we will need) in which you 1) shuffle elements of the list, 2) yield one element at a time via for loop. Once you run out of elements, you shuffle them again and yield one by one again. Then repeat. And again, and again. Endless loop!

I would suggest creating and testing both function in a Jupyter notebook first and then putting them in a separate file (e.g., _generators.py_). Be careful if you decide to use a for loop instead of `next()` for testing. Remember, both a generators and will never run out of items to yield for a for loop!

::: {.rmdnote .program}
Put both generators into _generators.py_.
:::

## TimedResponseTask class
Now we are ready to create the `TimedResponseTask` class. For our first take, it will create targets at a random location (`next_target_generator()`) after a random interval (`time_to_next_target_generator()`) plus take care of moving and drawing all of them. More bells and whistles (disposing of targets that went past the screen, changing the speed, checking response validity, etc.) will come later.

**For the constructor**, we definitely need PsychoPy window as a parameter, because we need it every time we create a new target. In addition, we need to pass a dictionary with settings for the task (initial speed, a tuple with range for time intervals between targets for `time_to_next_target_generator()`, and number of target repetitions for the `next_target_generator()`) and a dictionary with settings for the `Target` class (we need it every time we create a new target). We will use these parameters beyond the constructor, so save them as attributes. Plus, create an attribute `targets` and initialize it to an empty list (we will store `Target` objects in it), and create attributes for both generator objects using the appropriate parameters. Also create a `speed_factor` attribute and set it to 1. We will use it later to control both the speed of motion and how frequently the targets are generated. The higher is the factor, the faster targets move and the shorter is the interval to the target and vice versa. Finally, we need a [Clock](https://psychopy.org/api/clock.html#psychopy.clock.Clock) that will count the time to the moment when we need to generate a new target (`new_target_timer`) and an attribute that will hold that time (`time_till_next_target`). Initialize the latter to the `next()` item from time-to-next-target generator (remember, you need to use the attribute, which is a generator object that function returned, not the function itself).

Now we need to add three methods `draw`, `update`, and `add_next_target`. The first one is easy, it simply draws all `targets` in a for loop. The second is also easy, it makes all targets `fall` plus, after the loop, it should call `add_next_target` method. The `add_next_target` method should check whether the elapsed time for `new_target_timer` **times the `speed_factor`** (as the speed increases, the time to the next target goes faster) has exceeded the `time_till_next_target` (this modulation of elapsed time due to speed is why we can't easily use a [CountdownTimer](https://psychopy.org/api/clock.html#psychopy.clock.CountdownTimer) instead). If that is indeed the case, create a new random target (get the `next()` position from the position generator and remember to pass `speed` _times_ `speed_factor`!), add it to the list of targets, reset the timer and get new `time_till_next_target` using `next()` item from the time generator.

In the main file, create `TimedResponsTask` object (use a name you like) and call its `draw` and `update` methods in the main loop. You should see targets appearing at random and falling down consistently.

::: {.rmdnote .program}
Put updated code in _code04.py_  and create the class `TimedResponseTask`.
:::

## Disposing of targets
Currently, our targets keep falling down even when they are below the screen. This will not affect the performance _immediately_ but it will be taxing both memory and CPU, so we should dispose of them. In the `Target` class, create a new read-only (computed) `@property` called `is_below_the_screen` that returns `True` if the upper edge of the target is below the lower edge of the screen, `False` otherwise, of course, and you definitely do not need if-else!

Next, in the `update` method of `TimedResponseTask`, add a second loop (or modify the existing loop) where you delete any object that `is_below_the_screen`.

For debugging, run the main code, wait until at least one target falls below the screen, put a break point and check `targets` attribute. Its length should match the number of visible targets, not of the total generated targets.

::: {.rmdnote .program}
Update classes `Target` and `TimedResponseTask`.
:::

## Finishing line
Add a new visual attribute to the `TimedResponseTask` that is a horizontal [line](https://psychopy.org/api/visual/line.html#psychopy.visual.Line). The task of the player will be to press a corresponding key whenever a target crosses (overlaps with) the line. For now, create it as an attribute in the constructor (pick the vertical location you like) and draw it inside the `draw()` method.

::: {.rmdnote .program}
Update class `TimedResponseTask`.
:::

## Response
Now the real fun begins! We will allow a player to press keys and check whether a corresponding target is on the line. For this, we need new methods for both `Target` and `TimedResponseTask` classes. For the `Target`, implement a new method class `overlaps()` that will take a vertical position (of the finishing line) as the only float number parameter. In the method, first you check that the `score` attribute is `None`. If it _not_ `None` that means that the player already responded on to the target and they are not allowed to respond to it twice. If it is `None`, compute a score using the following formula:
$$score = int \left(10 - 10 \cdot \frac{|y_{target} - y_{line}|}{h_{target} / 2} \right)$$
where $y_{target}$ is the vertical center of the target, $y_{line}$ is the vertical position of the line (you get it as a function parameter), $h_{target}$ is height of the target, $|x|$ means absolute value of $x$ (use [fabs](https://docs.python.org/3/library/math.html#math.fabs) function from _math_ library for that), and `10` is an arbitrary scaling factor (you can use any integer and put it into settings). Study the formula and you will see that score is 10 if the target's center is right on the line but decreases linearly with any displacement for both early (target's center is above the line) or late (target's center is already below the line) responses. Once the target is off the line, the score becomes negative. We convert it to `int`, because we want simple scores (floats look messy for this). Compute the score and store in a _temporary local variable_. If the value is _positive_, that means success, so you should store this value permanently in the `score` attribute, change line color of the rectangle to white (to show the player that they got it right), and return `True` (yes, target does overlap with the line!). For all other outcomes, you return `False`. This means that either the response was already made or the target does not overlap with the line at the time of the key press.

In the `TimerResponseTask` class, we need a new method `check()` that will take position of the target based on the key press (so if a player pressed _left_ key, the position will be $0$, _down_ is $1$, and _right_ is $2$). Loop over targets and if target's position (`ipos` attribute) matches the position of the key press (parameter of the function) _and_ target overlaps with the line (the `overlaps()` method returns `True`), return the `score` attribute of that target. Note that the condition order is important here! You need to check for the overlap _only_ if target position matches the key. If you ran out of targets to check that means that the player pressed a wrong key or at the wrong time, so you should return `0` (means "mistake").

In the main loop, add `"left"`, `"down"`, and `"right"` to the key list of [getKeys()](https://psychopy.org/api/event.html#psychopy.event.getKeys) call. Then, if any of these three keys are pressed, translate that into a position, respectively, 0, 1, and 2 (think how you can do it without if-else via a dictionary), and call the new `check` method of the `TimedResponseClass`. Test the code, targets' edges should turn white, if you time your key press correctly!

::: {.rmdnote .program}
Put updated code in _code05.py_, update `Target` and `TimedResponseTask` classes.
:::

## Score
Playing is more fun when you can see how well you are doing. Let us add a simple score indicator that is updated with response score. You already know how you can do it via [TextStim](https://psychopy.org/api/visual/textstim.html#psychopy.visual.TextStim) stimulus but you also already know how you can inherit from a base class and extend its functionality. This is what we will do here, as the class will record and draw the score (that part is covered by the inheritance).

Create a new class (I have called it `ScoreText`) that inherits from [TextStim](https://psychopy.org/api/visual/textstim.html#psychopy.visual.TextStim). In the constructor, you need to create an integer attribute that will hold current `score` and initialize it 0. Plus, call ancestor's constructor via `super().__init__(...)` to initialize and place the text stimulus (I've picked top left corner). Think about parameters that the constructor and ancestor's constructor need.

Next, we need to update the score (both its numeric form _and_ the text that we draw) every time participant presses a key. We could implement the code _outside_ of the class but that is a fairly bad idea, as it puts class-related code elsewhere. We could also implement a "normal" method, e.g., `add()` that will take care of that. Instead, we will implement a _special_ method [__iadd__](https://docs.python.org/3/reference/datamodel.html#object.__iadd__) that allows to "add to" the object. It takes a single parameter (in addition to the compulsory `self`, of course), performs "adding to the self" operation (whatever that means with respect to your object, can be mathematical addition for an attribute, concatenation of the string, adding to the list, etc.), and **returns back the reference to itself**, i.e., returns `self` not a value of any attribute! Here's how it works:


```python
class AddIt():
    def __init__(self):
        self.number = 0
        
    def __iadd__(self, addendum):
        self.number += addendum
        return self # important!!!


adder = AddIt()
print(adder.number)
#> 0
adder += 10
print(adder.number)
#> 10
```

Implement that special method for your class, so we can do `score_stim +=  timed_task.check(...)`. Remember, you have to update both numeric _and_ visual representations of the score in that method! Add the score to the main code.

::: {.rmdnote .program}
Put updated code in `code06.py`, create `ScoreText` class.
:::

## Staircase
We will implement the staircase as part of the `TimerResponseTask` class, so it can speed up and slow down itself. For this, we will need an attribute that counts number of _consecutive_ correct responses (I, typically, call it `correct_in_a_row` or something like that). Create and initialize it to zero in the constructor.

Next, create a new method `staircase()` that will take a single parameter (beyond `self`) on whether the response was `correct` or not. If it was, increment `correct_in_a_row` by one and check whether it reached 3. If it did, increase the `speed_factor` by _multiplying_ it by some chosen factor (I've picked 1.3) and resetting `correct_in_a_row` to 0. This is equivalent to using a logarithmic step as our `speed_factor` is adjusted as a fraction of its magnitude. Alternatively, if the response was not correct, _divide_ `speed_factor` by the same number (e.g., 1.3, so slowing things down) and again, reset `correct_in_a_row` to 0. After that, loop over all targets and update their speed based on `speed` and `speed_factor` attributes.

You need to call this method inside the `check` method, think then and how.

::: {.rmdnote .program}
Update `TimedTaskResponse` class.
:::

## Limiting time
Let us add a competitive edge by limiting the run time to 20 seconds (you can pick your own duration, of course, and you definitely want to be a setting). Create an additional outer loop, so that the game can be played many times over. Once the round is over, show the latest state (redrawing all game objects) plus the "Round over" sign and wait for the player to press either _escape_ (then you exit the game) or _space_ (to start the next round). Remember to recreate all game objects anew for the next round (or create a `reset` method for all of them).

::: {.rmdnote .program}
Put updated code in `code07.py`.
:::

## Using PsychoPy's StairHandler
Now that you know how to program a very basic staircase, let us use its much more flexible implementation by PsychoPy via [StairHandler](https://psychopy.org/api/data.html#stairhandler) class. We will use it so as to replicate the staircase that we already implemented. However, it is capable of much more and PsychoPy has implementation for other adaptive methods, such as parametric [Psi](https://psychopy.org/api/data.html#psychopy.data.PsiHandler) or [Quest](https://psychopy.org/api/data.html#questhandler) approaches. I strongly recommend consulting the literature to decide which method is best suited for your experiment and then relying on PsychoPy's implementation in your code.

We will need to modify our `TimedResponseTask`, so let us create its a twin `TimedResponseTask2` (or `TimedResponseTaskPsychoPy`, if you find that more intuitive). Simply copy-paste the entire code, modify the name, import and use it in your _code08.py_ code. Make sure everything works just as before (because you did not do anything beyond making a carbon copy).

Now let us make use of the [StairHandler](https://psychopy.org/api/data.html#stairhandler) in `TimedResponseTask2`. Drop `correct_on_a_row` attribute and create a [StairHandler](https://psychopy.org/api/data.html#stairhandler) as `stairhandler` attribute instead. You need to specify `startVal` which is the initial value for the `speed_factor`, thus use whatever value you had previously. [StairHandler](https://psychopy.org/api/data.html#stairhandler) uses `nUp=1` and `nDown=3` by default. This matches our custom staircase, so theoretically you can use defaults by omitting these parameters. However, for the sake of code's readability, do specify these explicitly. Our steps were logarithmic, so use `stepType="log"` and a single fixed `stepSizes=-0.1`. The magnitude of `-0.1` correspond roughly to the step that we used in the custom staircase and we need the negative sign because [StairHandler](https://psychopy.org/api/data.html#stairhandler) _increases_ the staircase level following an incorrect response. In our case, we want an exact opposite, _decreasing_ `speed_factor` to slow targets down. Hence, the negative sign that turns increase into a decrease. Finally, [StairHandler](https://psychopy.org/api/data.html#stairhandler) will terminate after it reaches either desired number of trials (`nTrial`) or reversals (`nReversals`, changes from correct to incorrect responses or vice versa). These are the settings that would typically determine length of a single block/run in the real experiment. However, we limited our rounds by _time_, so we only need to make sure that the [StairHandler](https://psychopy.org/api/data.html#stairhandler) does not run out of trials before the game round is over. Thus, specify some very large number (e.g., 1000) for both these parameters.

Once you created `stairhandler` attribute, it is ready for use via `next(self.stairhandler)`. Call it the first time in the constructor and assign the value it returns to `speed_factor` attribute (should be whatever `startVal` you assigned to it but do put a breakpoint and double-check!) 

Next, we need to modify our `staicase()` method making it much simpler. First, remove the `if correct: ... else: ...` code but leave targets' speed adjustment code intact (we still need it!). Then, let `stairhandler` adjust itself via [addResponse()](https://psychopy.org/api/data.html#psychopy.data.StairHandler.addResponse) method using an information on whether the response was correct (you already have a parameter with exactly that information). Finally, get the next `speed_factor` exactly the same way as in the constructor. Done!

::: {.rmdnote .program}
Put updated code in `code08.py` using `TimedResponseTask2`.
:::

Your program should run very much like before but now you have many more opportunities to make it more flexible at little cost for yourself (look at [StairHandler](https://psychopy.org/api/data.html#stairhandler) settings) and to log it via one of `saveAs` methods.Let us do the latter, save staircase logs via [saveAsText()](https://psychopy.org/api/data.html#psychopy.data.StairHandler.saveAsText) after a run is over. Figure out a way to generate a unique filename for each run, so that the logs will not be overwritten.

::: {.rmdnote .program}
Save staircase logs in `code09.py`.
:::

## This is just a start!
As per usual, think about how you can extend the game. A clock showing the remaining time is definitely missing. Auditory feedback would be nice. More positions? Random colors to confuse a player?
