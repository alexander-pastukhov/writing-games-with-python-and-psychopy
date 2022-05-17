# Moon lander

Today we will create a moon lander game. You job is simple: land your ship on the pad but do not crash it! Here is a brief video of my implementation of the game

<div style="text-align:center;"><video controls>
    <source src="videos/moonlander.m4v" type="video/mp4"> 
  </video></div>

Here is the general outline of how we will proceed:

1. Create a basic PsychoPy window and main experimental loop.
2. Define a basic `MoonLander` class with a static image and add its drawing to the main loop.
3. Randomize position of the lander.
4. Add gravity pull.
5. Add vertical thruster that counter-act gravity.
6. Add horizontal thrusters, so you can maneuver around.
7. Define `LandingPad` class.
8. Implement landing / crashing checks.
9. Add more runs.
10. Limit the fuel.

But first you will learn about context management and exceptions.

## Boilerplate
As per usual, we will start with our usual boilerplate code. Create settings file that, for now, defines only the size of the window. Create `code01.py` with the usual boilerplate for loading settings, opening the window (its size determined by the settings), a main game loop (you can add a text message to make it look less plain) with a check for an _"escape"_ button to exit the loop, and closing the window at the end. I am being so specific because next you will learn how to hide this boilerplate in a context manager.

::: {.rmdnote .program}
Put your code into _code01.py_.
:::

## Context manager
On the one hand, context management is a frequently used feature in Python, particularly for file operations (you used it when loading settings from a JSON or YAML file). On the other hand, its full power that relies on a custom class implementation is rarely used. However, it can be very useful whenever the context of your programs is the same or very similar, as in case of the PsychoPy games that we programmed or typical PsychoPy experiments. In both cases, there is a fairly fixed structure of the program:

1. Initialization 
    * get experimental settings by reading them from an [external file](#settings-files)
    * create PsychoPy window, logger for experimental results, mouse (if required)
    * initialize special devices such as response box, eye tracker, etc.
2. Actual experiment
3. Saving and cleaning up
    * save data logs
    * if required, close connection to special devices such as response boxes, eye tracker, etc.
    * close PsychoPy window
  
If you look at your code, you will realized that steps 1 and 3 remain pretty much the same throughout all the games that we programmed. Thus, we will create a context manager class that you can always reuse and which will hide away the boilerplate code.

Here is a reminded of how a context manager is used when working with files. First, how it works _without_ a context manager: 1) you open a file and assign the object to a variable, 2) you work with it, 3) you close it. The latter is important to ensure that information was fully written into it and that you do not lock for file.

```python
file = open("somefile.txt", "r")
# ... do something with the file, such as reading the entire file into a single variable
data = file.read()
close(file)
```

A better way is to use a context manager via a `with ... as ...` statement (again, this should look familiar by now):
```python
with open("somefile.txt", "r") as file:
    file.read()
```

Note that now the `file.read()` is inside of the `with` block and there is no `file.close()` call. The latter is evoked automatically, once you run all the code inside the `with` block and exit it. Although for this example the difference is minimal --- a different way to assign a value to a variable and explicit versus implicit file closing --- the second variant takes care of cleaning up, ensures that you do not forget about it, and allows you to concentrate on the important bits.

Here's how it works behind the scenes. A context manager is a class that implements two special methods `__enter__` and `__exit__`[Spoiler alert! This approach is called [duck typing](duck-typing) and we will learn more about in the next game]. The former creates and returns a context, which is whatever attribute or value you require, wheres the latter performs cleaning up that is necessary before exiting the context. Here is how we would implement a limited file context manager by ourselves:
```python
class FileManager():
    def __init__(self, filename, mode):
        """
        Stores the settings for use in __enter__
        
        Parameters
        ----------
        filename : str
        mode : str
        """
        self.file = None
        self.filename = filename
        self.mode = mode
        
    def __enter__(self):
      """ 
      What we need to do to create context:
        * Open the file and returns the object.
      
      Returns
      ----------
      File object
      """
      self.file = open(self.filename, self.mode)
      return self.file
      
    def __exit__(self, exc_type, exc_value, traceback):
      """
      What we need to do before destroying the context:
        * Close the file before we exit the context.
      """
      close(self.file)
      
# and now we use it!
with FileManager("somefile.txt", "r") as file:
    file.read()
```

Note that `__exit__` method has extra parameters `exc_type`, `exc_value`, and `traceback`. They will be relevant for exception handling later on but you can ignore them for now.

Now is your turn! Create a `GameContext` class (in a separate file, of course) that will load settings (filename should be passed to the constructor), create a PsychoPy Window object of a given size upon entering the context, and [close](https://psychopy.org/api/visual/window.html#psychopy.visual.Window.close) when the code exists the context. For now, you will need one attribute to store settings (call it `settings`) and one attribute for PsychoPy Window itself (use `win` as an attribute name). There will be a small but important difference relative to `FileManager` class in the example above. Here, we have two objects (attributes) that we would like to use inside the context: `settings` and `win`. We could return both as a tuple but this approach does not scale well. Instead, the __enter__ should return the reference to the context object itself (reminder, reference to the current object is always in the `self` parameter of a method). This way you can always access either attribute via `context.settings` or `context.win`.

```python
with GameContext("settings.yaml") as context:
  # your usual code inside but
  # PsychoPy window is context.win
  context.win.flip()
```

::: {.rmdnote .program}
Create `GameContext` class and use it in  _code02.py_.
:::

As you can see, the repetitive part is now hidden in the context class making it easier to concentrate on the main code. But the context manager has another ace up its sleeve: it makes handling exceptions (a.k.a. errors) and safe exiting much simpler.

## Exceptions
When you are running an actual experiment, one of the worries that you have is "what happens to the data I have already logged if the program crashes with an error"? Not collecting a full measurement is bad but not keeping at least partial log is even worse, as you can still use it for analysis or as a guidance for future adjustments. Python, as other languages, has special mechanisms to handle [exceptions](https://docs.python.org/3/tutorial/errors.html) that arise during the code execution.

Whenever an error occurs at a run time, it [raises](https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement) an exception: it creates an object of [a special class](https://docs.python.org/3/library/exceptions.html#concrete-exceptions) that contains information describing the problem. For example, a [ZeroDivisionError](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError) is raised whenever you try to divide by zero, e.g., `1 / 0` (you can try this in a Jupyter notebook). A [KeyError](https://docs.python.org/3/library/exceptions.html#KeyError) is raised, if you using a dictionary with a wrong key, the code below will raise it:

```python
a_dict = {"a_key" : 1}
a_dict["b_key"]
#> Error in py_call_impl(callable, dots$args, dots$keywords): KeyError: 'b_key'
#> 
#> Detailed traceback:
#>   File "<string>", line 1, in <module>
```

Similarly, an [IndexError](https://docs.python.org/3/library/exceptions.html#IndexError) is raised, if you try to use an invalid index for a list, a [NameError](https://docs.python.org/3/library/exceptions.html#NameError), if you are trying to access variable that does not exist, [AttributeError](https://docs.python.org/3/library/exceptions.html#AttributeError) when an object does not have an attribute you are trying to use, etc. 

In Python, you use `try: ... except:...finally:` operators to anticipate and handle exceptions:
```python
try:
    # some code that might generate a runtime error
except:  
    # code that is executed if something bad happens
finally:
    # code that is executed both with and without exception
    
# code that is executed ONLY if there were no exceptions or if an exception was handled
```

In the simplest case, you need just the first two operators: `try` and `except`. Create a Jupyter notebook (that you will submit as part of the assignment) and write the code that generates a division-by-zero error but is handled via `try...except...`. In the `except` simply print out a message, so that you know that it was executed. Create another cell, copy the code and now check that the exception handling code is _not_ executed, if the error is not generated (i.e., divide by some non-zero number).

::: {.rmdnote .program}
Put exception handling code is cell of a Jupyter notebook.
:::

Using `except:` catches _all_ exceptions. However, this is considered a bad style (too general) and a linter will complain. Instead, you can be more specific and handle exceptions based on their class.
```python
try:
    # some code that might generate a runtime error
except KeyError as key_error:
    # code that is executed only if KeyError exception was raised 
    # with exception information stored in the key_error object
except ZeroDivisionError as zero_division_error:  
    # code that is executed only if ZeroDivisionError exception was raised
    # with exception information stored in the zero_division_error object
except:
    # code that is executed if any OTHER exception is raised.
```

Implement handling for `KeyError` and `ZeroDivisionError`, they should print out different messages to check that it works. Test it by generating these runtime errors with your code. 

::: {.rmdnote .program}
Put specific exception handling code is cell of a Jupyter notebook.
:::

So far, you generated exception by causing runtime errors code but you can raise these exceptions yourself via [raise](https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement) operator. For example, instead of dividing by zero, you can `raise ZeroDivisionError()`^[Confusingly, if you do not pass any additional parameters, you can also create the object _without_ round brackets: `raise ZeroDivisionError`. I find this mightily confusing but this is fairly common, so drop brackets if it feels more natural.]. Use it with you previous code, instead of an actual division by zero. Try raising other exceptions and see how your code handles them. Also check what happens if you have the first two specific exception handlers but no general `except:` and raise an [NameError](https://docs.python.org/3/library/exceptions.html#NameError)?

::: {.rmdnote .program}
Use `raise` to test exception handling in a Jupyter notebook.
:::

So far I have talked about exceptions as a way to alert about runtime errors. However, they can be used in a more general way to control the execution flow. We will use that side of exception in the next section when dealing with context.

## Exception within context
`try..except...` operators provide a general mechanism for exceptions handling but what happens if an exception is raised inside a context? You can, of course, put a `try...except...` in the code itself, something you should do, if you are planning to handling _specific_ exceptions. However, if an exception occurs in the code inside the context, Python will first _exit_ the context, i.e., call the `__exit__` method, before handling it explicitly. Moreover, it will kindly put the exception information into the parameters `exc_type` (a class of the exception) and `exc_value` (an object of that class). This way, you can perform a proper clean-up (save data, close window, etc.) and then either handle an exception or leave it alone, so that it propagates further and can be handled by other pieces of your code (or it will stop the execution, if you do not handle it explicitly).

Here, we will use this mechanism not only for safe clean-up but also to make aborting an experiment (or a game) easy. In previous games with many rounds, you had nested loops that made aborting a game via _escape_ key press awkward. You had to check it in the inner loop and then differentiate between a normal end-of-round and a used abort in the outside loop. We can make our life much easier via a combination of a context manager and a custom exception. 

First, create a custom `GameAbort` class, which is a descendant of the `Exception` class. You do not need any code in it, even a constructor does not need to be redefined, so use [pass](https://docs.python.org/3/reference/simple_stmts.html#the-pass-statement) statement for its body (you do need to have at least one line of code in the class). Next, you `raise GameAbort()`, if the player pressed _escape_ key (do not forget to import `GameAbort` class, so you can use it in the main script). Finally, in the __exit__ method of the `GameContext` manager, you should check whether `exc_type is GameAbort` (`exc_type` will be `None`, if no exception occurred) and, **very important(!)**, `return True` in that case:

```python
def GameContext:
    ...
    def __exit__(self, exc_type, exc_value, traceback):
        ...
        if exc_type is GameAbort:
            return True
  
```

That last bit `return True` informs Python that you handled the exception and all is good (not need to propagate it further). However, note that your _return_ `True` meaning that any other code that handles the exit from a context must be _before_ that statement. Now, you can safely abort your experiment from any code location, inside nested loops, functions, etc. In all cases, the exception will be propagated until the `__exit__` method, doing away with awkward extra checks.


::: {.rmdnote .program}
Create `GameAbort` exception class,<br/>update `GameContext` class to handle it,<br/>use this in an updated main script in _code03.py_.
:::

## Create MoonLander class
In _moonlander.py_, create a new `MoonLander` class. It should have an [ImageStim](https://psychopy.org/api/visual/imagestim.html) attribute (I will assume it is called `image`) that will contain the visuals of the ship created using [ufo.png](material/ufo.png) image. However, instead of hardcoding the filename, create a new group `"Lander"` in the settings file and add a new setting `"ship image : ufo.png"` (assuming you use YAML). Pass Lander-specific settings to the constructor and save them in an attribute (we will have more of them later).

Note that we do not want to inherit from the [ImageStim](https://psychopy.org/api/visual/imagestim.html) directly, as we will have more visuals elements later on. Also, implement `draw()` method that should draw all visual elements of the lander (we have one for now, of course).

Create an instance of `MoonLander` class in the main script and draw it in the main game loop. You should see a static picture of the ship at the center of the screen.

::: {.rmdnote .program}
Create `MoonLander` class and use it in the main game loop.<br/>
Put updated code into _code04.py_. 
:::

## Randomize lander's position
Implement a new method `reset()` that resets the lander for the next round. At the moment, the only thing it should do is to randomize position of the image. Use a range of -0.5..0.5 horizontally and 0.8..0.9 vertically (I assume that we are using `"norm"` units). Call it in the constructor and test it in the main loop by calling it every time you press _space_ button (that should make the ship jump).

::: {.rmdnote .program}
Add `reset()` method to `MoonLander` class and use it in the main game loop.<br/>
Put updated code into _code05.py_. 
:::

## Flying (but only down)
For the lander to fly, we must adjust its position or, more specifically, the position of its image (`self.image.pos`) based on its speed. But before that, speed itself must be adjusted based on the forces from gravity and thrusters that act upon the lander. Accordingly, we need 

1. A new setting that defines acceleration due to the gravitational force. Define in the settings file, call it `gravity [norm/sec^2]` (so, it is an acceleration in distance units of `"norm"` rather than in meters of the real world) and set to `0.0001`^[The constant itself does not mean anything, I adjusted it to be reasonable for the image and window size that we are using.]
2. A new attribute `speed` that will contain horizontal and vertical velocity in norm units per second. Initialize to `[0, 0]` in the `reset()` but also assign some value (e.g., also `[0, 0]`) as linters do not like to see attributes that were never mentioned in the constructor.
3. A new attribute with a PsychoPy [clock](https://psychopy.org/api/clock.html#psychopy.clock.Clock) that will measure the time elapsed since the last position adjustment (this way we can compute our speed and acceleration "per second"). Do not forget to reset it in `reset()`.

Now, implement a method that will update lander position (call it, unimaginatively, `update()`). Inside, figure out the time elapsed since the last call (or since the last `reset()`) and do not forget to restart the clock. Once you know how much time has elapsed, you can adjust, first, speed based on acceleration (only vertical speed based on gravity for now, we will worry about the horizontal component once we implement thrusters) and, then, position based on speed. Call it in the main loop and watch your lander fall out of the sky. Once it is off the screen, press space and see it go again. Play with the `gravity` setting to adjust the speed of falling to your liking.

::: {.rmdnote .program}
Update `MoonLander` class for the effect of gravity.<br/>
Use it in the main loop of _code06.py_.
:::

## Vertical thurster
PsychoPy allows you to get key presses or, using [hardware.keyboard](https://www.psychopy.org/api/hardware/keyboard.html) to get both press and release time. Unfortunately, you get both only _after_ the key was released. In our game, the thursters must be active for as long as the player presses the key. Thus, we need to know whether a key is _currently_ pressed, not that it was pressed and released at some time in the past. For this, we will use _pyglet_ library (a backend used by PsychoPy)  directly. First, in your _moonlander.py_ add `import pyglet` and then include the following code inside the constructor of the class.

```python
# setting up keyboard monitoring
self.key = pyglet.window.key
self.keyboard = self.key.KeyStateHandler()
win.winHandle.push_handlers(self.keyboard)
```

This installs a "handler" that monitors the state of the keyboard. Now, you can read out the state of, say, _down arrow_ key as`self.keyboard[self.key.DOWN]` (`True` if pressed, `False` otherwise). We will use `DOWN` for the vertical thruster and `LEFT` and `RIGHT` for the horizontal ones.

Define a `vertical accelartion [norm/sec^2]` to be twice the gravity (but you can use some other number, of course) and update the `update()`^[Pun intended.], so that the total vertical acceleration is $vertical acceleration + gravity$ if the the user is pressing _down_ key (use `self.keyboard` and `self.key` to figure that out) but $gravity$ alone, if not.

Test that the vertical thruster works (do you need to update the main code?)!

::: {.infobox .program}
Update `MoonLander` class with a vertical thruster.
:::

## Horizontal thursters
Now implement the same logic, computing acceleration, speed, and position but for horizontal thrusters (define `horizontal acceleration [norm/sec^2]` setting and decide on its value yourself). Remember, the _right_ thruster pushes the lander to the _left_ and vice versa! Think about what you should do if both _left_ and _right_ keys are pressed at the same time. Test it by flying around!

::: {.infobox .program}
Add horizontal thrusters to `MoonLander`.
:::

## Landing pad: visuals
The purpose of the game is to land on a landing pad. A landing pad is just a rectangle with some additional methods and properties. So it stands to reason to make it a descendant of the `visual.Rect` class, unfortunately, for some technical reason I have not figured out yet, this does not work for shape classes like `Rect` or `Circle`.

Create a new file _landing_pad.py_ and a new class `LandingPad`. In the constructor, create a rectangle and store it in attribute (you pick the name). It should be `0.5` units wide and located at the bottom of the window but at a [random](https://docs.python.org/3/library/random.html) position within the window horizontally. Pick the fill and line colors that you like. The only other method the class needs is `draw()`. 

In the main code, create an object of class `LandingPad` and draw it in the main loop, along with the lander itself.

::: {.infobox .program}
Create `LandingPad` class.<br/> 
Use it in _code07.py_.
:::

## Computing edges of game objects

The aim of the game is a soft touchdown on a landing pad. For this, we need to know where the _top_ of the landing pad is, as well as where the _bottom_ of the lander is and where _left_ and _right_ limits of each object are. Let us think about _bottom_ of the lander first, as the rest are very similar.

We do not have information about it _directly_. We have the vertical position of the lander in `self.image.pos[1]` (I assume here that the visuals attribute is called `image`) and its height in `self.image.size[1]`. From this, it is easy to compute the bottom edge (but remember that position is about the _center_ of the rectangle). Accordingly, you could create a [computed property](#computed-attribute-property)  `bottom`. Create computed attributes for `bottom`, `left`, and `right` of the lander class and for `top`, `left`, and `right` of the landing pad.

::: {.infobox .program}
Implement computed properties for `MoonLander` and `LandingPad` classes.
:::

## Landing
We should check for landing whenever the bottom edge of the lander is at or below the top edge of the landing pad. A successful landing must satisfy several conditions:

* The lander must be within the limits of the lander pad horizontally.
* The vertical speed must be zero or negative (otherwise, the lander flies up) but below a certain threshold that we will define as  `vertical speed threshold [norm/sec]`. I set it to `0.05`.
* The absolute horizontal speed must be below a certain threshold, also defined as `horizontal speed threshold [norm/sec] : 0.05`.

If _any_ of these three conditions are false, the lander has crashed. Either way, the game is over, so you should record the outcome (whether the landing was successful) and exit the main game loop. After the loop, inform the player about the outcome. Draw all game objects plus the message about the outcome (e.g., "You did it!" / "Oh, no!" or something else) and wait for a space key press.

The condition above will be quite long, so fitting it into a single line will make it hard to read. In Python, you can split the line by putting `\` at the end of it. So a multiline if statement will look as follows:
```python
if lander_is_within_horizontal_limits and \
   lander_vertical_speed_is_good and \
   lander_horizontal_speed_is_good:
   ...
else:
  ...
```

::: {.infobox .program}
Implement landing checks in _code08.py_.
:::

## More rounds
Extend the game to have more than one round after the player either landed or crashed. Remember to reset the position of the lander before each new round. You can also add a `reset()` method to the landing pad as well, randomizing it horizontal position.

::: {.infobox .program}
Add `reset()` method to the `LandingPad` class.</br>
Add more rounds in _code09.py_.
:::

## Limited fuel
Let us add a fuel limit to make things more interesting, so that thrursters would work _only_ if there is any fuel left. For this, define a new setting `full tank` (I've picked it to be `100` but you can have more) and add a new attribute `fuel` to the `Lander` class (remember that you need to explicitly define all attributes in the constructor). The `fuel` level should be set to `full tank` whenever you reset the lander.

Every use of a thruster should reduce this by 1 and thrusters should work _only_ if there is fuel. You need to take care of this in the `update()` method. Think about how you would do it for both vertical and horizontal thrusters.

We also need to tell the player how much the fuel is left. I've implemented it as a bar gauge but you can implement it as text stimulus as well. Create the appropriate visual attribute in the constructor of the `Lander` class. Remember to update it every time the level of the fuel changes and to draw it whenever you draw the lander itself. As a nice touch, you can change the color to indicate how much of the fuel is left. I've used _green_ for more than 2/3, _yellow_ for more than 1/3, and _red_ if less than that.

::: {.infobox .program}
Add fuel and fuel gauge to `Lander` class.<br/>
:::

## Add to it!
We already have a functioning game but you can add so much more to it: visuals for the thrusters, sounds, background, etc. Experiment at will!

