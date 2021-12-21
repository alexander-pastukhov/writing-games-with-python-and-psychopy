# Christmas special

Today we are going to program a Christmas-special. However, this is still an opportunity to learn something new. You will learn about zipping lists and we will start offloading settings into a separate file. Here is how the Christmas tree looks for me:



## Chapter concepts

* Building Christmas spirit
* Zipping over lists
* Loading setting from JSON or YAML file.


## Christmas tree
Let us start our Christmas decoration with a Christmas tree. You can download [the one I've found](material/pine-tree.png) (created by [isaiah658](https://openclipart.org/artist/isaiah658)) or find an image that you like. Create your basic PsychoPy code to create a window (we will be using [Circle](https://psychopy.org/api/visual/circle.html#psychopy.visual.circle.Circle) later, so think about suitable units), an [ImageStim](https://psychopy.org/api/visual/imagestim.html#psychopy.visual.ImageStim) with a tree, draw it and wait for any key press.

::: {.rmdnote .program}
Put your code into `code01.py`.
:::

## Christmas tree decoration
For the decoration, let us use [Circle](https://psychopy.org/api/visual/circle.html#psychopy.visual.circle.Circle) objects of various sizes and color. We could create each one separately with its own custom hard-coded values, but let us instead create three constants that are lists of equal length that describe, respectively position of each ball (`BALL_POS` would be a good name, each entry should be a tuple of `(x, y)`), size (`BALL_SIZE`), and color (`BALL_COLOR`, stick to `"red"`, `"blue"`, and `"yellow"`, this limited selection of specific colors will be important later when we animate them). 

Create a list of balls by iterating over these three lists. You have two choices, you can either use an index variable, building an index via [range()](https://docs.python.org/3/library/functions.html#func-range) using [len()](https://docs.python.org/3/library/functions.html#len) of one of the lists (they should all be of the same length). But let use a cool trick of iterating over a [zip()](https://docs.python.org/3/library/functions.html#zip) of lists. [zip()](https://docs.python.org/3/library/functions.html#zip) gives you a tuple combining one element from each list that you can unpack on the fly as in the example below (note that loop variables will receive values in the  order that you used for lists).

```python
numbers = [1, 2, 3]
letters = ["A", "B", "C"]
for  a_number, a_letter in  zip(numbers, letters):
  print("%d: %s"%(a_number, a_letter))
#> 1: A
#> 2: B
#> 3: C
```

You can zip as many lists as you want. We, obviously, want three. Decide on whether you want to create `balls` as an empty list and then append each newly created [Circle](https://psychopy.org/api/visual/circle.html#psychopy.visual.circle.Circle) to it in the loop or use list comprehension. Do not forget to draw the balls and think about what you should draw first: the tree or the balls. Experiment with position and sizes to makes it look just perfect.

::: {.rmdnote .program}
Put your code into `code02.py`.
:::

## Twinkle, twinkle, little star
Now let us make our Christmas balls twinkle, as in the video. The idea is that only one color is "active" at a time. The balls of that color are "on" and balls of other color are "off" (white or gray, or some other color of your liking). Now our display becomes dynamic, so you need to have a game loop and with an opportunity to exit the program by pressing _escape_.

For this, we need to define a list of colors ("red", "blue", "yellow") that we can cycle through and an variable that hold the index of the currently active color (I've called it `icolor`). Every X seconds (I do it  every 0.5 seconds, define this as a constant, e.g., `TWINKLE_DURATION`), increment this index, so that the next color in the list becomes active. Note that you have an out-of-range problem: When  you initialize `icolor` to 0 and increment it by 1 three times, your index is already too large (3, the length of our `colors` list is 3, so the maximal index is 2). You can either use an `if` to check for that or you can use a remainder operator `%` (think about the remainder if you divide _any_ positive value by the length of the `colors` list).

Once you need to update whether balls are "on" or "off", you need to loop both through the balls and their colors in the original `BALLS_COLOR` list (when you use a string with color name, it gets translated into an RGB value, so we cannot compare it directly). Again, you can use [zip()](https://docs.python.org/3/library/functions.html#zip) to loop simultaneously through Christmas balls and their color. If their color matches the active one, their `fillColor` should be that color. If not, their `fillColor` should be some "neutral" / "off" color (white? gray?).


To keep track of time, you will need a timer variable, use either [Clock](https://psychopy.org/api/clock.html#psychopy.clock.Clock) or [CountdownTimer](https://psychopy.org/api/clock.html#psychopy.clock.CountdownTimer). Once the `TWINKLE_DURATION` elapsed, update the active color, all the balls, and do not forget to reset the timer.


::: {.rmdnote .program}
Put your code into `code03.py`.
:::

## Let's make some noise!
Let add some Christmas music! Download [Deck the Halls version by Kevin MacLeod](material/Deck the Halls B.ogg)^[Deck the Halls B by Kevin MacLeod http://incompetech.com
Creative Commons — Attribution 4.0 International — CC BY 4.0
Free Download / Stream: https://bit.ly/deck-the-halls-b
Music promoted by Audio Library https://youtu.be/RzjZ-WdVeyk]. For this, we will use [sound](https://psychopy.org/api/sound.html) module of PsychoPy library that generate sounds on the fly and also play audio files in various format such as wav or ogg (but not mp3!). Unfortunately, sound it surprisingly tricky, there are many libraries that might be used by PsychoPy (as of end of 2021 PsychoPy lists four backends that it might use), and things sometimes break. Thus, if the music does not play for you, ask me and we will try to set your sound libraries up.

Using sound is very simple. First, you need to import the `Sound` class as suggested in the manual:
```python
from psychopy.sound import Sound
```

Then, you need a new object of `Sound` class supplying the file  name as the first parameter (I called the variable `song`). Right before start the loop, you `.play()` the sound. Note, if you want to play the same sound again, you need to "rewind" it by explicitly calling its `.stop()` method (for some reason, the sound stops at the end but does not gets "rewind", so when you try to play it again and notices that it is already at the end and stops without playing anything).

::: {.rmdnote .program}
Put your code into `code04.py`.
:::

## Settings file formats {#settings-files}
So far, we either hard-coded specific values or defined them as constants (a better of these two approaches). However, this means that if you want to run your game with different settings, you need to modify the program itself. And if you want to have two versions of the game (two experimental conditions), you would need to have two programs with all the problems of maintaining virtually identical code in several places at once.

A better approach is to have separate files with settings, so you can keep the code constant and alter specific parameters by specifying which settings file the program should use. This is helpful even you plan to have a single set of setting as it separates code from constants, puts the latter all in one place and makes it easier to edit and check them. There are multiple formats for settings files: XML, INI, JSON, YAML, etc. Our format of the choice for today will be JSON. However, this is a question of taste. Personally, I like YAML for subjective reasons (fewer curly brackets and quotation marks), but you are free to use any format you like. As you will see, this makes little difference for the actual Python code.

### XML
[XML](https://en.wikipedia.org/wiki/XML) --- an Extensible Markup Language --- looks similar to HTML (HyperText Markup Language). Experiments designed using PsychoPy Builder interface are stored using XML files but with [.psyexp extension](https://www.psychopy.org/psyexp.html). A settings file for our Christmas programin XML could look like this
```XML
<Balls>
  <Ball>
    <Position>
      <x>0.1</x>
      <y>0.2</y>
    </Position>
    <Size>0.01</Size>
    <Color>red</Color>
  </Ball>
  <Ball>
    <Position>
      <x>0.2</x>
      <y>0.1</y>
    </Position>
    <Size>0.02</Size>
    <Color>yellow</Color>
  </Ball>
  ...
</Balls>
<Timing>
  <Twinkle duration>0.5</Twinkle duration>
</Timing>
```

The advantage of XML is that it is very flexible yet structured and you can use [native Python interface](https://docs.python.org/3/library/xml.html) to work with it. However, XML is not easy for humans to read, it is overpowered for our purposes of having a simple set of unique constants and its power means that using it is fairly cumbersome (I use `\` to split a single line into many lines).

```python
from xml.dom import minidom
settings = minidom.parse('settings.xml')
# this will give you string "0.4"
size = settings.getElementsByTagName("Balls")[0]. \
                getElementsByTagName("Ball")[0]. \
                getElementsByTagName("Size")[0].firstChild.data
```

### INI
This is a format with a structure similar to that found in MS Windows INI files.
```ini
[Balls]
    x = 0.1, 0.2
    y = 0.2, 0.1
    size = 0.01, 0.02
    color = red, yellow
[Timing]
    TwinkleDuration = 0.5
```

As you can see it is easier to read and Python has a special [configparser](https://docs.python.org/3/library/configparser.html) library to work with them. The object you get is, effectively, a dictionary with additional methods and attributes. However `ConfigParser` does not try to guess the type of data, so all values are stored as _strings_ and it is your job to convert them to whatever type you need, e.g., integer, list, etc.

```python
import configparser
settings = configparser.ConfigParser()
settings.read('settings.ini')
settings['Balls']['size'] # this will give you a string '0.01, 0.02'
```

### JSON{#json} 
[JSON](https://en.wikipedia.org/wiki/JSON) (JavaScript Object Notation) is a popular format to serialize data for web applications that use it to exchange data between a server and a client. 
```json
{
  "Balls": {
    "position": [[0.1, 0.2], [0.2, 0.1]],
    "size": [0.01, 0.02],
    "color": ["red", "yellow"]
  },
  "Timing": {
    "Twinkle duration" : 0.5
  }
}
```

You can parse any _string_ in JSON format into a dictionary in Python using [json](https://docs.python.org/3/library/json.html) module. Its advantage over INI files is that JSON explicitly specifies data type (i.e., strings are in quotation marks), so it converts it automatically. Note that unlike configparse, json module does not work with files directly, so you need to open it manually (ignore the `with` magic for a moment, you will learn about it in detail when we will talk about context managers).
```python
import json
with open('settings.json') as json_file:
    settings = json.load(json_file)
    
settings["Balls"]["size"] # this will give a list [0.01, 0.02]
```

### YAML{#yaml}
[YAML](https://en.wikipedia.org/wiki/YAML) (YAML Ain't Markup Language, rhymes with camel) is very similar to JSON but its config files are more human-readable. It has fewer special symbols and curly brackets but, as in Python, you must watch the indentations as they determine the hierarchy.
```yaml
Balls:
  position: [[0.1, 0.2], [0.2, 0.1]]
  size: [0.01, 0.02]
  color: ["red", "yellow"]
Timing:
  Twinkle duration : 0.5
```

You will need to install a third-party library [pyyaml](https://pyyaml.org/) to work with YAML files. You get the same dictionary as for the JSON
```python
import yaml
with open("settings.yaml") as yaml_stream:
    settings = yaml.load(yaml_stream)
    
settings["Balls"]["size"] # this will give a list [0.01, 0.02]
```

## Using settings
Look at your _code04.py_ and identify constants and hard-coded values that you should put into a settings file. E.g., definitely constants that describes Christmas balls and twinkle duration but, possibly, also the size of the window, name of the Christmas tree and song files, etc. In general, I put every such value into settings even if it used only once (as with the size of the window) because then I know that _all_ constants are the settings file. This way there is a single, nicely organized place to check and I do not need to search through the code to figure a specific value out.

Once you transferred all your constants into the settings file (use either JSON or YAML), add the code that loads it at the very beginning and use settings dictionary in place of constants.

::: {.rmdnote .program}
Put your code into `code05.py`.
:::


## Merry Christmas and a Happy New Year!


