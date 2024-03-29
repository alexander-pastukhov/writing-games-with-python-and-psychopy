# Gettings started with PsychoPy {#psychopy-basics}

Before we program our first game using [PsychoPy](https://psychopy.org/), we need to spend some time figuring out its basics. It is not the most suitable library for writing games, for that you might want to use [Python Arcade](https://arcade.academy/) or [PyGame](https://www.pygame.org/). However, it is currently the best Python library for developing psychophysical experiments (and this is what we are after).

## Chapter concepts

* Understanding how to use [classes and objects](#classes-and-objects).
* Using [named parameters](#arguments-by-position-or-name) in functions.
* Understanding PsychoPy [units system](#psychopy-units).
* Using basic Psycho [visual stimuli](#adding-text-message) and handling [user inputs](#make-the-square-jump-on-your-command).

## Minimal PsychoPy code {#minimal-psychopy}
Copy-paste the following code into `code01.py` file (you did remember to create a new folder for the chapter?):
```python
"""
A minimal PsychoPy code.
"""

# this imports two modules from psychopy
# visual has all the visual stimuli, including the Window class
# that we need to create a program window
# event has function for working with mouse and keyboard
from psychopy import visual, event

# creating a 800 x 600 window
win = visual.Window(size=(800, 600))

# waiting for any key press
event.waitKeys()

# closing the window
win.close()
```

Run it to check that PsychoPy work. If you get an error saying that `psychopy` library is not found, check the [active Python interpreter](#install-vs-code). You should get a gray window with _PsychoPy_ title. Press any key (click on the window, if you switched to another one, so that it registers a key press) and it should close. Not very exciting but does show that everything works as it should.

::: {.program}
Put your code into _code01.py_.
:::

The code is simple but packs quite a few novel bits. First line is easy, we simply import [visual](https://psychopy.org/api/visual/index.html) and [event](https://psychopy.org/api/event.html) modules from _psychopy_ library (a library can be itself organized into sublibraries to make things even more modular). Then, we create an _object_ `win` using a _class_ [Window](https://psychopy.org/api/visual/window.html#psychopy.visual.Window) with custom size. Third line uses function [waitKeys()](https://psychopy.org/api/event.html#psychopy.event.waitKeys) from _event_ module to wait for a key press. The last one closes the window by calling its `close` _method_. You should have little trouble with lines #1 and #3 but you need to learn about object-oriented programming to understand #2 and #4.

## Classes and objects
The PsychoPy library is a collection of _classes_ that you use to create _objects_, an approach called _object-oriented programming_. The core idea is in the name: Instead of keeping variables (data) separate from functions (actions), you combine them in an object that has attributes^[Also called properties] (its own variables) and methods (its own functions). This approach utilizes our natural tendency to perceive the world as a collection of interacting objects.

First, you need to understand an important distinction between _classes_ and _objects_. A _class_ is a "blueprint" that describes properties and behavior of _all_ objects of that class. This "blueprint" is used  to create an _instance_ of that class, which is called an _object_. For example, Homo sapiens is a _class_ that describes species that have certain properties, such as height, and can do certain things, such as running. However, Homo sapiens as a class has only a _concept_ of height but no specific height itself. E.g., you cannot ask "What is height of Homo sapiens?" only what is an average (mean, median, etc.) height of individuals of that class. Similarly, you cannot say "Run, Homo sapiens! Run!" as abstract concepts have trouble performing real actions like that. Instead, it is Alexander Pastukhov who is an _instance_ of Homo sapiens class with a specific (average) height and a specific (below average) ability to run. Other instances of Homo sapiens (other people) have different height and a different (typically better) ability to run. Thus, a class describes all common properties and methods that all _instances_ of the class (all objects) will have. But an individual object will behave differently because of different values of their properties. This means that whenever you meet a Homo sapien, you could be sure that they have height per se but will need to look at an individual _instance_ to figure what height they have. 

`Window` is a class that describes properties that a PsychoPy window must have and actions it can perform (you can see the complete list in [the manual](https://psychopy.org/api/visual/window.html#psychopy.visual.Window)). To create an object, we use its class definition and store the result in a variable. In the code above we call `Window` class^[Technically, we call a class constructor method called `__init__` but this is not important for now.] while passing custom parameters to it (`size=(800, 600)`) and store an object that it returns in variable `win`.

Attributes are, essentially, variables that belong to the class and, therefore, variables that each object will possess. For example, a `Window` class has [size](https://psychopy.org/api/visual/window.html#psychopy.visual.Window.size) attribute that determines its on-screen size in pixels. It also has (background) [color](https://psychopy.org/api/visual/window.html#psychopy.visual.Window.color), an attribute that determines whether it should be shown in [full screen mode](https://psychopy.org/api/visual/window.html#psychopy.visual.Window.fullscr), etc. Thus, a `win` object will have all these attributes and they will have specific values.

To understand both properties and class/object distinction better, put a breakpoint on the third line of code (`event.waitKeys()`) and fire up the debugger via **F5**. Once the window is created, the execution will pause and you will find a `win` object in _Variables/Locals_. Click on it and it will expand to show all attributes and its values, including `size` (check that it is `[800, 600]`). Note that you will not see `Window` itself in the same list. This is because it is a class, an abstract concept, whereas as `win` is its instance and object of that class.

Methods, such as `Window.close()` are, essentially, functions that belong to the class/object and perform certain actions on the object. For example, method [close()](https://psychopy.org/api/visual/window.html#psychopy.visual.Window.close) closes the window, [flip()](https://psychopy.org/api/visual/window.html#psychopy.visual.Window.flip) updates it after we finished drawing in it, etc. What is important is to remember is that each method will act only on the object _it belongs to_ and not on other instances of the same class. This means that you can create two windows (`win1` and `win2`) and calling `win1.close()` will close the first but not the second window (try this out!). Same goes for attributes, changing them in one object will not affect any other objects of the same class, just like changing a value in one variable will not affect the other ones.

Although we barely scratched the surface of object-oriented programming, it will be enough for us to be able to use classes defined for us in PsychoPy library.

## Function parameters: default values, passing by position or by name{#arguments-by-position-or-name}
There are a few more curious bits in the `visual.Window(size=(800, 600))` call above that we need to discuss. These curiosities are related to functions (and, therefore, methods that are functions that belong to a class) not classes per se. First, constructor method of the Window class has [a lot of arguments](https://psychopy.org/api/visual/window.html#psychopy.visual.Window) (when we construct an object, we call a constructor _method_ of the class, which is why we are talking about functions). And yet, we only passed one of them. This is because you can specify [default values](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values) for individual parameters. In this case, if a parameter is omitted, a default value is used instead

```python
def divide(x1, x2=2):
  """
  Divides numbers, uses 2 as a second value if a second term is omitted.
  
  Parameters:
  ----------
  x1 : number
  x2 : number, defaults to 2
  
  Returns:
  ----------
  number
  """
  return x1 / x2
print(divide(2))
#> 1.0
print(divide(2, 4))
#> 0.5
```
If you look at [documentation](https://psychopy.org/api/visual/window.html#psychopy.visual.Window), you will see that for the Window class constructor _all_ parameters have a default value. This is a part of PsychoPy's philosophy of combining rich customization (just look at the sheer number of parameters!) with simplicity of use through sensible defaults (specify nothing and the window will still work).

Second, we did not just pass the value but specified which parameter this value is for via `size=(800, 600)`. This notation is called [keyword arguments](https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments). The advantage is in making it more explicit which parameter you are passing a value through. Plus, it allows you to put parameters any order, if that is more relevant given the context^[However, stick to original order for consistency otherwise.]. If you do not use names, the values are assigned to individual parameters based on their _position_ (a.k.a. positional parameters). You can even mix the two, but positional parameters must come first, see [documentation](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions) if you want to know more.

```python
# using positional parameters
print(divide(2, 4))
#> 0.5
```


```python
# using keyword arguments
print(divide(x2=4, x1=2))
#> 0.5
```


```python
# mixing positional and keyword arguments
print(divide(2, x2=4))
#> 0.5
```


```python
print(divide(2, x1=4))
#> divide() got multiple values for argument 'x1'
```

## Adding main loop
Currently, not much is happening in our program. One thing we need to add is a loop in which we can repeatedly draw in a window (and update it via its [flip()](https://psychopy.org/api/visual/window.html#psychopy.visual.Window.flip) method), check user input, and perform any other necessary actions.

First, let us add the loop and handling of user inputs (the fun drawing part will be next). The loop goes between opening and closing the window:
```python
importing libraries
opening the window

--> our main loop <--

closing the window
```

The loop should be repeated until the user presses an _escape_ key and, therefore, you will need a variable that signals this. My approach is to create a variable `gameover` initializing it to `False` and repeat the loop as long as the game not over. Then, in the loop, use function [event.getKeys()](https://psychopy.org/api/event.html#psychopy.event.getKeys) to check whether _escape_ button was pressed (for this, you need to pass `keyList=['escape']`). The function returns a _list_ of keys, if any of them were pressed in the meantime or an empty list, if no keys from the `keyList` were pressed. Store that returned value in a temporary variable (I tend to call it `keys`). You will learn about lists only in the _next_ chapter, so for now use a ready-made: `len(keys) > 0` is a comparison that is `True` if list is not empty. If the list is indeed not empty, that means that the user pressed _escape_ (as that is the only key that we specified in the function call) and the game should be over. Think how can you do it _without_ an `if` statement, computing the logical value directly?

::: {.program}
Put your code into _code02.py_.
:::

## Adding text message
Although we are now running a nice game loop, we still have only a boring gray window to look at. Let us create a text stimulus, which would say "Press escape to exit" and display it during the loop. For this we will use [visual.TextStim](https://psychopy.org/api/visual/textstim.html) class from PsychoPy library.

First, you need to create the `press_escape_text` object (instance of the [TextStim](https://psychopy.org/api/visual/textstim.html class)) before the main loop. There are quite a few parameters that you can play with but minimally, you need to pass the window the text should be displayed in (our `win` variable) and the actual text you want to display (`text="Press escape to exit"`). For all other settings PsychoPy will use its [defaults](#arguments-by-position-or-name) (default font family, color and size, placed right at the windows' center).
```python
press_escape_text = visual.TextStim(win, "Press escape to exit")
```

To show the visuals in PsychoPy, you first _draw_ each element by calling its [draw()](https://psychopy.org/api/visual/textstim.html#psychopy.visual.TextStim.draw) method and then update the window by _flipping_^[This is called flipping because a window has two buffers: one that is currently displayed on the screen and the other one in which you can draw your stimuli. Once you are done with drawing, you "flip" the buffers so that they exchange their places. Now the one you drew in gets displayed and you have the other buffer to draw in.] it. Note that you call [flip()](https://psychopy.org/api/visual/window.html#psychopy.visual.Window.flip) only _once_ after _all_ stimuli are drawn. I typically organize this code into a separate chunk and prepend it with a comment line `# drawing stimuli`.

The `# drawing stimuli` chunk goes inside the main loop either before or after the keyboard check^[My personal preference is to draw first but in most cases it makes no difference.]. Organize the latter also as a separate code chunk with its own brief comment.

::: {.program}
Put your code into _code03.py_.
:::

Now, you should have a nice, although static, message positioned at the window's center that tells you how you can exit the game. Check out the manual page for [visual.TextStim](https://psychopy.org/api/visual/textstim.html) and try changing it by passing additional parameters to the class call. For example you can change its `color`,  whether text is `bold` and/or `italic`, how it is aligned, etc. However, if you want to change _where_ the text is displayed, read on below.

## Adding a square and placing it _not_ at the center of the window
Now, let us figure out how create and move visuals to an arbitrary location on the screen. In principle, this is very straightforward as every visual stimulus (including [TextStim](https://psychopy.org/api/visual/textstim.html#psychopy.visual.TextStim) we just used) has [pos](https://psychopy.org/api/visual/textstim.html#psychopy.visual.TextStim.pos) property that specifies (you guessed it!) its position within a window. However, to make your life easier, PsychoPy first complicates it by having [**five** (5!) different position units systems](https://psychopy.org/general/units.html).

Before we start exploring the units, let us create a simple white square. The visual class we need is [visual.Rect](https://psychopy.org/api/visual/rect.html). Just like the [TextStim](https://psychopy.org/api/visual/textstim.html#psychopy.visual.TextStim) above, it requires `win` variable (so it knows which window it belongs to), `width` (defaults to 0.5 of those mysterious units), `height` (also defaults to 0.5), `pos` (defaults to (0,0)), `lineColor` (defaults to `white`) and `fillColor` (defaults to `None`). Thus, to get a "standard" white outline square with size of `(0.5, 0.5)` units at `(0, 0)` location you only need pass the `win` variable: `white_square = visual.Rect(win)`. However, on _some_ computers a curious bug prevents PsychoPy from drawing the outline correctly. If you end up staring at an empty screen^[This sometimes was an issue with Intel graphic cards.], add `fillColor="white"` to the call and you should see a filled white square.

You draw the square just like you drew the text stimulus, via its [draw()](https://psychopy.org/api/visual/rect.html#psychopy.visual.rect.Rect.draw) method (and, again, you first draw all the stimuli and then flip the window _once_). Create the code (either keep the text and draw both, or drop the text), run it to see a very white square.

::: {.program}
Put your code into _code04.py_.
:::

What? Your square is not really a square? Well, I've warned you: [Five unit systems](https://psychopy.org/general/units.html#units)!

## Five unit systems {#psychopy-units}

### Height units {#psychopy-units-height}
With [height units](https://psychopy.org/general/units.html#height-units) everything is specified in the units of window height. The center of the window is at `(0,0)` and the window goes vertically from `-0.5` to `0.5`. However, horizontal limits depend on the aspect ratio. For our 800×600 window (4:3 aspect ratio), it will go from -0.666 to 0.666 (the window is 1.3333 window heights wide). For a 600×800 window (3:4 aspect ratio) from -0.375 to 0.375 (the window is 0.75 window heights wide), for a square window 600×600 (aspect ratio 1:1) from -0.5 to 0.5 (again, in all these cases it goes from -0.5 to 0.5 vertically). This means that the actual on-screen distance for the units is the same for both axes. So that a square of `size=(0.5, 0.5)` is actually a square (it spans the same distance vertically and horizontally). Thus, height units make _sizing_ objects easier but _placing them on horizontal axis correctly_ harder (as you need to know the aspect ratio).

Modify your code by specifying the unit system when you create the window: `win = visual.Window(..., units="height")`. Play with your code by specifying position of the square when you create it. You just need to pass an extra parameter `pos=(<x>, <y>)`.

::: {.program}
Put your code into _code05.py_.
:::

By the way, which way is up when y is below or above zero? Unfortunately, unlike x-axis, the y-axis can go both ways. For PsychoPy y-axis points up (so negative values move the square down and positive up). However, if you would use an Eyelink eye tracker to record where participants looked _on the screen_, it assumes that y-axis starts at the top of the screen and points down^[This could be very confusing, if you forget about this when overlaying gaze data on an image you used in the study and wondering what on Earth the participants were doing.].

Now, modify the size of the square (and turn it into a non-square rectangle) by passing `width=<some-width-value>` and `height=<some-height-value>`.

::: {.program}
Put your code into _code06.py_.
:::

### Normalized units {#psychopy-units-norm}
[Normalized units](https://psychopy.org/general/units.html#normalised-units) are default units and assume that the window goes from -1 to 1 both along x- and x-axis. Again, (0,0) is the center of the screen but the bottom-left corner is (-1, -1) whereas the top-right is (1, 1). This makes _placing_ your objects easier but _sizing_ them harder (you need to know the aspect ratio to ensure that a square is a square).

Modify your code, so that it uses `"norm"` units when you create the window and size your white square stimulus, so it does look like a square.

::: {.program}
Put your code into _code07.py_.
:::

### Pixels on screen
For [pixels on screen](https://psychopy.org/general/units.html#pixels-on-screen) units, the window center is still at `(0,0)` but it goes from `-<width-in-pixels>/2` to `<width-in-pixels>/2` horizontally (from -400 to 400 in our case) and `-<height-in-pixels>/2` to `<height-in-pixels>/2` vertically (from -300 to 300). These units could be more intuitive when you are working with a fixed sized window, as the span is the same along the both axes (like for the height units). However, they spell trouble if your window size has changed or you are using a full screen window on a monitor with an unknown resolution. In short, you should use them only if they dramatically simplify your code.

Modify your code to use `"pix"` units and briefly test sizing and placing your square within the window.

::: {.program}
Put your code into _code08.py_.
:::

### Degrees of visual angle
Unlike the three units above, using [degrees of visual angle](https://psychopy.org/general/units.html#degrees-of-visual-angle) requires you knowing a physical size of the screen, its resolution, and viewing distance (how far your eyes are away from the screen). They are _the_ measurement units used in visual psychophysics as they describe stimulus size as it appears on the retina (see [Wikipedia](https://en.wikipedia.org/wiki/Visual_angle) for details). Thus, these are the units you want to use when running an actual experiment in the lab.

### Centimeters on screen
Here, you would need know the physical size of your screen and its resolution. These are fairly exotic units for very specific usage cases^[So specific that I cannot think of one, to be honest.].

## Make your square jump
So far, we fixed the location of the square when we created it. However, you can move it at any time by assigning a new `(<x>, <y>)` coordinates to its `pos` property. _E.g._, `white_square.pos = (-0.1, 0.2)`. Let us experiment by moving the square to a random location on every iteration of the loop (this could cause a lot of flashing, so if you have a photosensitive epilepsy that can be triggered by flashing lights, you probably should do it just once before the loop). Use the units of your choice and generate a new position using [random.uniform(a, b)](https://docs.python.org/3/library/random.html#random.uniform) function, that generates a random value within _a..b_ range^[You need to import the random library for this, of course.]. Generate two values (one for x, one for y). If you use `"norm"` units, your range is the same (from -1 to 1) for the two dimensions. However, if you used `"height"` units, you need to take into account the aspect ratio of your window (4:3 if you are using 800×600 pix window).

::: {.program}
Put your code into _code09.py_.
:::

## Make the square jump on your command
This was very flashy, so let us make the square jump only when you press **space** button. For this, we need to expand the code that processes keyboard input. So far, we restricted it to just **escape** button and checked whether any (hence, **escape**) button was pressed.

You will learn about lists and indexes in the next chapter, so here is another ready-made. First, add `"space"` to the `keyList` parameter. Next, use conditional [if statement](#{#if-statement) to check whether [event.getKeys()](https://psychopy.org/api/event.html#psychopy.event.getKeys) returned a key press. If it did  (`len(keys) > 0`), you can now check whether `keys[0]` is equal to `"space"` or `"escape"`^[You can use `if..else`, because we only have two options but I would recommend to go for a more general solution `if..elif` ]. If it was the latter, the game is over as before. If it was `"space"` then move the square to a new random position (and do not move it on every frame!)

Hint, if you are debugging, put you breakpoint inside the `if` statement, so that the program pauses only once you pressed a key (what happens if you put it on the `win.flip()` line?)

::: {.program}
Put your code into _code10.py_.
:::

## Basics covered
There is plenty more to learn about PsychoPy but we've got the basics covered. Submit your files and get ready to [Whack a Mole](#whack-a-mole)!
