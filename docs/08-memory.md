# Memory game {#memory-game}

Today, you will write a good old _Memory_ game: Eight cards are lying "face down", you can turn any two of them and, if they are identical, they are taken off the table. If they are different, the cards turn "face down" again.



Before we start, create a new folder for the game and create a subfolder _Images_ in it. Then, download [images of chicken](material/chicken.zip)^[The images are courtesy of [Kevin David Pointon](https://openclipart.org/artist/Firkin) and were downloaded
from [OpenClipart](https://openclipart.org/). They are [public domain](https://creativecommons.org/publicdomain/zero/1.0/) and can be used and distributed freely.] that we will use for the game and unzip them into _Images_ subfolder. Also, grab the [exercise notebook](notebooks/Memory game.ipynb)!

## Chapter concepts

* [Mutable](#mutable-objects) vs. [immutable](#variables-as-boxes-immutable-objects) objects
* Showing [images](#imagestim).
* Working with files via [os](#os-library) library.
* Using other [dictionary](#dictionaries) containers.
* [List operations](#list-operations).
* Looping over both index and item via list [enumeration](#enumerate).

## Variables as Boxes (immutable objects)
In this game, you will use [dictionaries](#dictionaries). These are _mutable_, like [lists](#lists) in contrast to "normal" _immutable_ values (integers, floats, strings). You need to learn about this distinction as these two kinds of objects (values) behave very differently under some circumstances, which is both good (power!) and bad (weird unexpected behavior!) news.

You may remember the _variable-as-a-box_ metaphor that I used it to introduce [variables](#variables). In short, a variable can be thought of as a "box" with a variable name written on it and a value being stored "inside". When you use this value or assign it to a different variable, you can assume that Python _makes a copy_ of it^[Not really, but this makes it easier to understand.] and puts that _copy_ into a different variable "box". When you _replace_ value of a variable, you take out the old value, destroy it (by throwing it into a nearest black hole, I assume), create a new one, and put it into the variable "box". When you _change_ a variable based on its current state, the same thing happens. You take out the value, create a new value (by adding to the original one or doing some other operation), destroy the old one, and put the new one back into the variable "box". The important point is that although a _variable_ can have different immutable values (we [changed](#random-mole) `imole` variable on every round), the immutable _value_ itself never changes. It gets _replaced_ with another immutable value but _never changes_^[A metaphor attempt: You can wear different shirts, so your _look_ (variable) changes but each individual shirt (potential values) remains the same (we ignore the wear and tear here) irrespective of whether your are wearing it (value is assigned to a variable) or not.].

The box metaphor explains why the [scopes](#scopes-for-immutable-values) work the way they do. Each scope has its own set of boxes and whenever you pass information between scopes, e.g., from a global script to a function, a copy of a value (from a variable) is created and put into a new box (e.g., a parameter) inside the function. When a function returns a value, it is copied and put in one of the boxes in the global script (variable you assigned the returned value to), etc.

However, this is true only for _immutable_ objects (values) such as numbers, strings, logical values, etc. but also [tuples](https://docs.python.org/3/library/stdtypes.html?highlight=tuple#tuple) (see below for what these are). As you could have guessed from the name, this means that there are other _mutable_ objects and they behave very differently.

## Variables as post-it stickers (mutable objects){#mutable-objects}
Mutable objects are lists, dictionaries^[Coming up shortly!], and classes, i.e., things that can change. The key difference is that _immutable_ objects can be thought as fixed in their size. A number takes up that many bytes to store, same goes for a given string (although a different string would require more or fewer bytes). Still, they do not change, they are created and destroyed when unneeded but never truly updated.

_Mutable_ objects can be changed^[Building on the looks metaphor: You can change your look by using a different (immutable) shirt or by _changing_ your haircut. You hair is mutable, you do not wear a different one on different days to look different, you need to modify it to look different.]. For example, you can add elements to your list, or remove them, or shuffle them. Same goes for [dictionaries](https://docs.python.org/3/tutorial/datastructures.html?highlight=dictionary#dictionaries). Making such object _immutable_ would be computationally inefficient: Every time you add a value a (long) list is destroyed and recreated with just that one additional value. Which is why Python simply _updates_ the original object. For further computation efficiency, these objects are not copied when you assign them to a different variable or use as a parameter value but _passed by reference_. This means that the variable is no longer a "box" but a "sticker" you put on an object (a list, a dictionary). And you can put as many stickers on an object as you want _and it still will be the same object_!

What on Earth do I mean? Keeping in mind that a variable is just a sticker (one of many) for a mutable object, try figuring out what will be the output below:

```python
x = [1, 2, 3]
y = x
y.append(4)
print(x)
```

::: {.rmdnote .practice}
Do exercise #1.
:::

Huh? That is precisely what I meant with "stickers on the same object". First, we create a list and put an `x` sticker on it. Then, we assign _the same list_ to `y`, in other words, we put a `y` sticker on the same list. Since both `x` and `y` are stickers on the _same_ object, they are, effectively, synonyms. In that specific situation, once you set `x = y`, it does not matter which variable name you use to change _the_ object, they are just two stickers hanging side-by-side on the _same_ list. Again, just a reminder, this is _not_ what would happen for _immutable_ values, like numbers, where things would behave the way you expect them to behave.

This variable-as-a-sticker, a.k.a. "passing value by reference", has very important implications for function calls, as it breaks your scope without ever giving you a warning. Look at the code below and try figuring out what the output will be.

```python 
def change_it(y):
    y.append(4)

x = [1, 2, 3]
change_it(x)
print(x)
```
::: {.rmdnote .practice}
Do exercise #2.
:::

How did we manage to modify a _global_ variable from inside the function? Didn't we change the _local_ parameter of the function? Yep, that is exactly the problem with passing by reference. Your function parameter is yet another sticker on the _same_ object, so even though it _looks_ like you do not need to worry about global variables (that's why you wrote the function and learned about scopes!), you still do. If you are perplexed by this, you are in a good company. This is one of the most unexpected and confusing bits in Python that routinely catches people^[Well, at least me!] by surprise. Let us do a few more exercises, before I show you how to solve the scope problem for mutable objects.

::: {.rmdnote .practice}
Do exercise #3.
:::

## Tuple: a frozen list {#tuple}
The wise people who created Python were acutely aware of the problem that the _variable-as-a-sticker_ creates. Which is why, they added an **immutable** version of a list, called a [tuple](https://docs.python.org/3/library/stdtypes.html?highlight=tuple#tuple). It is a "frozen" list of values, which you can loop over, access its items by index, or figure out how many items it has, but you _cannot modify it_. No appending, removing, replacing values, etc. For you this means that a variable with a frozen list is a box rather than a sticker and that it behaves just like any other "normal" **immutable** object. You can create a `tuple` by using round brackets.
```python
i_am_a_tuple = (1, 2, 3)
```
You can loop over it, e.g.,

```python
i_am_a_tuple = (1, 2, 3)
for number in i_am_a_tuple:
    print(number)
#> 1
#> 2
#> 3
```

but, as I said, appending will throw a mistake (try this code in a Jupyter Notebook)

```python
i_am_a_tuple = (1, 2, 3)

# throws AttributeError: 'tuple' object has no attribute 'append'
i_am_a_tuple.append(4)
#> Error in py_call_impl(callable, dots$args, dots$keywords): AttributeError: 'tuple' object has no attribute 'append'
```

Same goes for trying to change it

```python
i_am_a_tuple = (1, 2, 3)

# throws TypeError: 'tuple' object does not support item assignment
i_am_a_tuple[1] = 1 
#> Error in py_call_impl(callable, dots$args, dots$keywords): TypeError: 'tuple' object does not support item assignment
```

This means that when you need to pass a list of values to a function and you want them to have no link to the original variable, you should instead pass _a tuple of values_ to the function. The function still has a list of values but the link to the original list object is now broken. You can turn a list into a tuple using `tuple()`. Keeping in mind that `tuple()` creates a frozen copy of the list, what will happen below?
```python
x = [1, 2, 3]
y = tuple(x)
x.append(4)
print(y)
```
::: {.rmdnote .practice}
Do exercise #4.
:::

As you probably figured out, when `y = tuple(x)`, Python creates **a copy** of the list values, freezes them (they are immutable now), and puts them into the "y" box. Hence, whatever you do to the original list, has no effect on the immutable "y".

Conversely, you "unfreeze" a tuple by turning it into a list via `list()`. Please note that it creates **a new list**, which has no relation to any other existing list, even if values are the same or were originally taken from any of them!

::: {.rmdnote .practice}
Do exercise #5.
:::

Remember I just said that `list()` creates a new list? This means that you can use it to create a copy of a list directly, without an intermediate tuple step. This way you can two _different_ lists with _identical_ values. You can also achieve the same results by slicing an entire list, e.g. `list(x)`, is the same as `x[:]`.

::: {.rmdnote .practice}
Do exercise #6.
:::

Here, `y = list(x)` created a new list (which was a carbon copy of the one with the "x" sticker on it) and the "y" sticker was put on that new list, while the "x" remained hanging on the original.

Confusing? You bet! If you feel overwhelmed by this whole immutable/mutable, tuple/list, copy/reference confusion, you are just being a normal human being. I understand the (computational) reasons for doing things this way, I am aware of this difference and how useful this can be but it still catches me by surprise from time to time!

## Minimal code
Enough of theory, let us get busy writing the game. As usual, let us start with a minimal code (try doing it from scratch instead of copy-pasting from the last game):
```python
importing psychopy modules that we need
 
creating a window of a useful size and useful units

waiting for a key press

closing the window
```

The first thing you need to decide on is the window size _in pixels_ and which units would sizing and placing cards easier. Each chicken image is 240×400 pixels and, for the game, we need place for _exactly_ 4×2 images, i.e. our window must be 4 cards wide and 2 cards high. Do not forget to document the file!

::: {.rmdnote .program}
Put your code into `code01.py`.
:::

## Drawing an image{#imagestim}
We used (abstract and boring) circles to represent moles but today we will use actual images of chicken (see instructions above on downloading them). Using an [image stimulus](https://psychopy.org/api/visual/imagestim.html) in PsychoPy is very straightforward because it behaves very much like other visual stimuli you already know. First, you need to create an new object by calling `visual.ImageStim(...)`. You can find the complete list of parameters in the [documentation]((https://psychopy.org/api/visual/imagestim.html)) but for our initial intents and purposes, we only need to pass three of them:

* our window variable: `win`.
* image file name:  `image="Images/r01.png"` (images are in a subfolder and therefore we need to use a relative path).
* size: `size=(???, ???)`. That is one for you to compute. If you picked [norm](#psychopy-units-norm) units, as I did, then window is 2 units wide and 2 units high but for [height](#psychopy-units-height) it is 1 units height and _aspect-ratio_ units wide. We want to have a 4×2 images, what is the size (both width and height) of each image in the units of your choice?

Draw chicken image (it should appear at the center of the screen).

::: {.rmdnote .program}
Put your code into `code02.py`.
:::

## Placing an image (index to position)
By default, our image is placed at the center of the screen, which is a surprisingly useful default for a typical psychophysical experiment that shows stimuli at fixation (which is also, typically, at the center of the screen). However, we will need to draw eight images, each at its designated location. You need to create a function that takes an image index (it goes 0 to 7) and returns a list with pair of values with its location on the screen. Below is a sketch of how index correspond to the location. Note that image location ([pos](https://psychopy.org/api/visual/imagestim.html#psychopy.visual.ImageStim.pos attribute) corresponds to the _center_ of the image.

![Card location index](images/memory-location-index.png){ width=100% }

Name the function `position_from_index`. It should take one argument (`index`) and return a list with `(<x>, <y>)` coordinates in the PsychoPy units (from now on I assume that these are [norm](#psychopy-units-norm)). You can then use this value for the [pos](https://psychopy.org/api/visual/imagestim.html#psychopy.visual.ImageStim.pos) argument of the [ImageStim()](https://psychopy.org/api/visual/imagestim.html#imagestim).

The computation might look complicated, so let me get you started. How can you compute _x_ coordinate for the _top_ row? Concentrating on the top row alone makes things simpler because here the _column index_ is the same as the overall index: The left-most column is 0, the next one is 1, etc. You need a simple algebra of $x = a_x + b_x \cdot column$. You can easily deduce out both $a_x$ and $b_x$ if you figure out locations of the first and second cards by hand. Same goes for the _y_ coordinate. Assuming that you know the _row_, which is either 0 (top row) or 1 (bottom row), you can compute $y = a_y + b_y \cdot row$.

But, I hear you say, you do not have row and column indexes, only the overall index! To compute those you only need to keep in mind that each row has _four_ cards. Then, you can make use of two special division operators: [floor division operator `//`](https://python-reference.readthedocs.io/en/latest/docs/operators/floor_division.html) and [modulos, divison remainder `%`](https://python-reference.readthedocs.io/en/latest/docs/operators/modulus.html) operators. The former returns only the integer part of the division, so that `4 // 3` is `1` (because 4/3 is 1.33333) and `1 // 4` is `0` (because 1/4 is 0.25). The latter returns the remaining integers, so that `4 % 3` is `1` and `1 % 4` is `0`.

My suggestion would be first to play with individual formulas in Jupyter Notebook, which makes it easier to try out (dividing) things and seeing the result, putting various values into formulas, etc. Once you are confident that the code is working, turn it into a function, document it, and put into a separate file (_utilities.py_, do not forget to put a comment at the top of the file as well!). You can then import it in the main script and use it to place the card. Try out different indexes and make sure that the card appears where it should. Remember, put a breakpoint and step through the program while watching variables, if things do not work as you expected.

::: {.rmdnote .program}
Put `position_from_index` into `utilities.py`.<br/>
Put update code into `code03.py`
:::

## Backside of the card
A chicken image is a card _face_ but the game starts with the cards face down, so the player should see their backs. We will use a plain [rectangle](https://psychopy.org/api/visual/rect.html) as a backside. Pick a nice looking combination of `fillColor` (inside) and `lineColor` (contour) colors. Modify your code, to draw image (face of the card) and rectangle (back of the card) side-by-side (_e.g._, if face is at position with index 0, rectangle should be at position 1 or 4). This way you can check that sizes match and that they are positioned correctly.

::: {.rmdnote .program}
Put your code into `code04.py`.
:::

## Dictionaries {#dictionaries}
Each card that we use has plenty of properties: A front (image), a back (rectangle), and will have other properties such as which side should be shown or whether card is already taken off the screen. This calls for a container, so we could put all these relevant bits into a single variable. We _could_ put these values into a list and use numerical indexes to access individual elements (e.g., `card[0]` would be front image but `card[2]` would indicate the active side) but indexes do not have meaning per se, so figuring out how `card[0]` is different from `card[2]` would be tricky. Python has a solution for cases like this: [dictionaries](https://docs.python.org/3/library/stdtypes.html#dict).

A dictionary is a container that stores information using _key : value_ pairs. This is similar to how you look up a meaning or a translation (value) of a word (key) in a real dictionary, hence the name. To create a dictionary, you use _curly_ brackets `{<key1> : <value1>}, {<key2> : <value2>, ...}` or create it via `dict(<key1>=<value1>, <key2>=<value2>, ...)`.
```python
book = {"Author" : "Walter Moers",
        "Title": "Die 13½ Leben des Käpt'n Blaubär"}
```
Once you created a dictionary, you can access or modify each field using its key, _e.g._ `print(book["Author"])` or `book["Author"] = "Moers, W."`. You can also add new fields by assigning values to them, e.g., `book["Publication year"] = 1999`. In short, you can use a combination of `<dictionary-variable>[<key>]` just like you would use a normal variable. This is similar to using the `list[index]` combination, the only difference is that `index` must be an integer, whereas `key` can be any hashable^[Immutable values are [hashable](https://docs.python.org/3/glossary.html#term-hashable), whereas mutable ones, like dictionaries and lists, are not. This is because mutable objects can _change_ while the program is running and therefore are unusable as a key. I.e., it is hard to match by a key, if the key can be different by the time you need to access the dictionary.] value.

## Using a dictionary to represent a card
Our card has the following properties, so these will be key-value entries in a dictionary

1. `"front"`: front side (image of a chicken).
2. `"back"`: back side (rectangle).
3. `"filename"`: identity on the card that we will use later to check whether the player opened two identical cards (their filenames match) or two different ones.
4. `"side"`: can be either `"front"` or `"back"`, information about which side is up (drawn on the screen). Set it to `"back"` because, initially, all cards are face down. However, you can always set it temporarily to `"front"` to see how the cards are distributed.
5. `"show"`: a logical value, set it to `True`. We will use it later to mark out cards that are off the table and are, therefore, not shown. Initially, all cards are shown, so all cards should be created with `"show"` being equal to `True`. 

Create a dictionary variable (name it `card`) and fill it with relevant values (use either `"front"` and "`back"` for `"side"` key) and stimuli (you can put PsychoPy stimuli into a dictionary just like we put them into a list earlier). Modify your code so that it draws the correct image based on the value of the `"side"` entry. Note that you **do not need an if-statement for this**! Think about a key you need to access these two sides and the value that you have in for the `"side"` key.

::: {.rmdnote .program}
Put your code into `code05.py`.
:::

## Card factory
You have the code to create one card but we need eight of them. This definitely calls for a function. Write a function (put it into `utilities.py` to declutter the main file) that takes three parameters

1. a window variable (you need it to create PsychoPy stimuli),
2. a filename,
3. card position index,

and returns a dictionary, just like the one you created. You very much have the code, you only need to wrap it into a function and document it. Call function `create_card` and use it in the main script to create `card` dictionary. Think about libraries you will now need to import in _utilities.py_.

::: {.rmdnote .program}
Put `create_card` into `utilities.py`. <br/>
Put code into `code06.py`.
:::

## Getting a list of files
For a single card, we simply hard-coded the name of an image file, as well as its location. However, for a real game (or an experiment) we would like to be more flexible and automatically determine which files we have in the _Images_ folder. This is covered by [os](https://docs.python.org/3/library/os.html) library that contains various utilities for working with your operating system and, in particular, with files and directories. Specifically, [os.listdir(path=".")](https://docs.python.org/3/library/os.html#os.listdir) returns a list with filenames of _all_ the files in a folder specified by path. By default, it is a current path (`path="."`). However, you can use either a relative path - `os.listdir("Images")`, assuming that _Images_ is a subfolder in your current directory - or an absolute path `os.listdir("E:/Teaching/Python/MemoryGame/Images")` (in my case)^[Use absolute path only if it is the only option, as it will almost certainly will break your code on another machine.].

Try this out in a Jupyter Notebook (do not forget to import the [os](https://docs.python.org/3/library/os.html#module-os) library). You should get a list of 8 files that are coded as _[r|l][index].png_, where _r_ or _l_ denote a direction the chicken is looking. However, for our game we need only four images (4 × 2 = 8 cards). Therefore, we need to select a subset of them, e.g., four random cards, chicken looking to the left or to the right only. Here, let us work with chicken looking to the left, meaning that we need to pick only files that start with "l". To make this filtering easier, we will use a cool Python trick called [list comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions).

## List comprehension
List comprehension provides an elegant and easy-to-read way to create, modify and/or filter elements of the list creating a new list. The general structure is
```python
new_list = [<transform-the-item> for item in old_list if <condition-given-the-item>]
```
Let us look at examples to understand how it works. Imagine that you have a list `numbers = [1, 2, 3]` and you need increment each number by 1^[A very arbitrary example!]. You can do it by creating a new list and adding 1 to each item in the <transform-the-item> part:

```python
numbers = [1, 2, 3]
numbers_plus_1 = [item + 1 for item in numbers]
```

Note that this is equivalent to
```python
numbers = [1, 2, 3]
numbers_plus_1 = []
for item in numbers:
    numbers_plus_1.append(item + 1)
```

Or, imagine that you need to convert each item to a string. You can do it simply as
```python
numbers = [1, 2, 3]
numbers_as_strings = [str(item) for item in numbers]
```
What would be an equivalent form using a normal for loop? Write both versions of code in Jupiter cells and check that the results are the same.

::: {.rmdnote .practice}
Do exercise #7 in Jupyter notebook.
:::

Now, implement the code below using list comprehension. Check that results match.
```python
strings = ['1', '2', '3']
numbers = []
for astring in strings:
    numbers.append(int(astring) + 10)
```

::: {.rmdnote .practice}
Do exercise #8 in Jupyter notebook.
:::

As noted above, you can also use a conditional statement to filter which items are passed to the new list. In our numbers example, we can retain numbers that are greater than 1
```python
numbers = [1, 2, 3]
numbers_greater_than_1 = [item for item in numbers if item > 1]
```

Sometimes, the same statement is written in three lines, instead of one, to make reading easier:
```python
numbers = [1, 2, 3]
numbers_greater_than_1 = [item 
                          for item in numbers
                          if item > 1]
```

You can of course combine the transformation and filtering in a single statement. Create code that filters out all items below 2 and adds 4 to them.

::: {.rmdnote .practice}
Do exercise #9 in Jupyter notebook.
:::

## Getting list of relevant files
Use list comprehension to create a list of files of chicken looking left, _i.e._ with filenames that start with "l". Use [<your-string>.startswith()](https://docs.python.org/3/library/stdtypes.html#str.startswith) to check whether it starts with "l", store the list in `filenames` variable. Test your code in a Jupyter Notebook. You should get a list of four files.

## List operations {#list-operations}
Our list consists of four unique filenames but in the game each card should appear twice. There are several ways of duplicating lists. Here, We will use this as a opportunity to learn about list operations. Python lists implement two operations:

* Adding two lists together: `<list1> + <list2>`.

```python
a = [1, 2, 3]
b = [4, 5, 6]
a + b
#> [1, 2, 3, 4, 5, 6]
```

Note that this produces a _new_ list and, therefore, that this is not equivalent to [extend](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) method `a.extend(b)`! The `+` creates a _new_ list, `.extend()` extends the original list `a`.^[You will learn about practical implications of this later. For now, keep in mind that seemingly identical output might be fundamentally different underneath.]

* List replication:: `<list> * <integer-value>` creates a _new_ list by replicating the original one `<integer-value>` times. For example: 

```python
a = [1, 2, 3]
b = 4
a * b
#> [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
```

Use either operation or `.extend()` method to create the list where each filename is repeated twice. Hint, you can apply list multiplication directly to the filenames list you created via list comprehension (so, replicate it in that same line). Try this code out in a Jupyter Notebook.

## Looping over both index and item via  list enumeration  {#enumerate}
Now that we have a list of filenames, we can create a list of cards out of it. Our dictionary function requires both index and filename. The latter is the _item_ of the list, the former is the _index_ of that item. You could build the index using [range()](#range) function but Python has a better solution for this: a [enumerate()](https://docs.python.org/3/library/functions.html#enumerate) function! If, instead of iterating over a list, you iterate over [enumerate(<list>)](https://docs.python.org/3/library/functions.html#enumerate), you get a tuple with both `(index, value)`. Here is an example:

```python
letters = ['a', 'b', 'c']
for index, letter in enumerate(letters):
    print('%d: %s'%(index, letter))
#> 0: a
#> 1: b
#> 2: c
```

And here is how you can use [enumerate()](https://docs.python.org/3/library/functions.html#enumerate) for list comprehension.

```python
letters = ['a', 'b', 'c']
["%d: %s"%(index, letter) for index, letter in enumerate(letters)]
#> ['0: a', '1: b', '2: c']
```

## Computing path{#os-library}
Originally, we specified image file name as `"Images/r01.png"`. This did the job but now we have many filenames that we need to join with the folder name to form a path string. On top of that, major operating systems disagree with Windows on where `/` (forward slash) or `\` (backslash) should be used for paths. To make your code platform-independent and, therefore, more robust, you need to construct a filename string using [join](https://docs.python.org/3/library/os.path.html#os.path.join) function in [path](https://docs.python.org/3/library/os.path.html) submodule. Thus, you can import _os_ library and call it as `os.path.join(...)` (my personal preference). Or, you can use the same approach as for PsychoPy modules and import `path` from _os_, shortening the code. Or, of course, you can even import _join_ directly but I find that lack of library information during use makes things harder to understand (even though the code is even shorter).

[join](https://docs.python.org/3/library/os.path.html#os.path.join) takes path components as parameters and joins them to match the OS format. E.g., `os.path.join("Python seminar", "Memory game", "memory01.py")` on Windows will return `'Python seminar\\Memory game\\memory01.py'`. As we need to load multiple files, the _filename_ part will vary. However, the _folder_ where the images are located will be the same and, as per usual, it would a good idea to turn it into a formally declared [CONSTANT](#constants). 

Modify the `create_card` function so that it assumes that the `filename` parameter is just the filename with the folder name and, therefore, build the path by [join](https://docs.python.org/3/library/os.path.html#os.path.join) it with the folder name (defined as a constant in the this module!). You now need to drop the `"Images/"` in the value that you pass to it. Test that the code works as before!

::: {.rmdnote .program}
Update `create_card` in `utilities.py`<br/>
Put updated code into `code07.py`.
:::

## A deck of cards
Let us put together all the code we need for figuring out cards' filenames, duplicating them, and creating the cards using filename and index. 

Copy the code for building a duplicated list of filenames that you tested in Jupyter notebook to your main script (that'll be `code09.py`). Then, use enumerate and list comprehension over enumerated duplicate filenames to create `cards` (plural, replacing your singular `card` variable) via `create_card` function you wrote earlier. Update your drawing code to loop over and draw all cards. If your default is `"side"` is `"back"`, things will look pretty boring. Change that to '"front"` for all cards to see their faces.

::: {.rmdnote .program}
Put your code into `code08.py`.
:::

## Shuffling cards {#shuffle}
When you draw cards faces, you will notice that duplicating filenames list produces a very orderly sequence that makes playing the game easy (and boring). We need to [shuffle()](https://docs.python.org/3/library/random.html#random.shuffle) the filename list _before_ we create `cards`. Note that [shuffle()](https://docs.python.org/3/library/random.html#random.shuffle) shuffles list item _in place_ using the fact that the list is [mutable](#mutable-objects). That means you simply call the function and pass the list as an argument. The list gets modified, nothing is returned and nothing need to be assigned back of `filenames` variable.

::: {.rmdnote .program}
Put your code into `code09.py`.
:::

## Let's have a break!
We covered a lot of ground, so it might be a good point to take a break and submit your code for my review.

---

## Adding main game loop
At this point, we have a shuffle deck of cards that we show until a player presses a key. Modify the code to have the main presentation loop, similar to one we had when we experimented with [PsychoPy](#psychopy-basics) stimuli. Previously, we used a logical `gameover` variable to control the [while](##while-loop) loop. Here, we will have two reasons to exit the loop: the player pressed an **escape** key or they won the game. Therefore, let us use a _string_ `game_state` variable that is initialized to `"running"`. Repeat the loop while the `game_state` is equal to `"running"` but change it `"abort"` if a player pressed **escape**. You also need to replace [waitKeys()](https://psychopy.org/api/event.html#psychopy.event.waitKeys) with  [getKeys()](https://psychopy.org/api/event.html#psychopy.event.getKeys).

::: {.rmdnote .program}
Put your code into `code10.py`.
:::

## Detecting a mouse click {#psychopy-mouse}
In the game, the player will click on individual cards to turn them over. Before you can use a [mouse](https://psychopy.org/api/event.html#psychopy.event.Mouse) in PsychoPy, you must create it via `mouse = event.Mouse(visible=True, win=win)` call, where `win` is the PsychoPy window you already created. This code should appear immediately below the line where you create the window itself.

Now, you can check whether the left button was pressed using [mouse.getPressed()](https://psychopy.org/api/event.html#psychopy.event.Mouse.getPressed) method. It returns a three-item tuple with `True`/`False` values indicating whether each of the three buttons are _currently being pressed_. Use it the main loop, so that if the player presses _left_ button (its index in the returned list is 0), you change `"side"` of the first card (so, the card with index 0 in the list) to `"front"`. This assumes that you initialized card with their `"back"` shown, of course. If you run the code and click _anywhere_, this should flip the first card.

Put the mouse-click-processing code _before_ drawing cards. At the moment, it makes no difference but will be useful later on, as it will allow us to draw the latest state of the card (i.e., right after it was flipped by a player).

::: {.rmdnote .program}
Put your code into `code11.py`.
:::

## Position to index
Currently, the first card is flipped if you click _anywhere_. But the card you flip should be the card the player clicked on. For this we need to implement a function `index_from_position` that is an inverse of `position_from_index`. It should take an argument `pos`, which is a tuple of `(<x>, <y>)` values (a mouse position within the window), and return an _integer card index_. You have float values (with decimal points) in the `pos` argument (because it ranges from -1 to 1 for [norm](#psychopy-units-norm) units) and by default the values you compute from them will also be float. However, an index _must_ be integer, so you will need to wrap it in [int()](https://docs.python.org/3/library/functions.html#int) function call, before returning it.

Going backwards --- from position to index --- is (IMHO) easier. First, you need to think how you can convert an _x_ coordinate (goes from -1 to 1) to a column index (goes from 0 to 3) given that you have 4 columns (draw a sketch on paper as it will make figuring out math simpler). Similarly, you translate _y_ (from -1 to 1) into row index given that there are only two rows. Once you know row and column index, you can compute the index itself, keeping in mind that there are four card in a row. As with `position_from_index`, I think it is easier to first play with formulas in a Jupyter Notebook, before turning the code into a function, documenting it, and putting it into `utilities.py`.

::: {.rmdnote .program}
Put `index_from_position` into `utilities.py`.
:::

## Flip a selected card on click
Now that you have function that returns an index from position (don't forget to import it), you can flip the card that the player clicked on. For this, you need to extend the card-flipping code inside the _if left-mouse button was pressed_ code. Get the position of the mouse within the window by calling [mouse.getPos()](https://psychopy.org/api/event.html#psychopy.event.Mouse.getPos). This will return a pair of `(x, y)` values, which you can pass to your `index_from_position()` function. This, in turn will return the index of the card the player click on. Change the `"side"` of a card with that index to `"front"`. Test the code by turning different cards over, make sure that it is the card that you clicked on that gets turned. And a usual reminder, do not hesitate to put a breakpoint inside the if-statement to check the actual mouse position values and how they are translated into index, if things do not work.

::: {.rmdnote .program}
Put your code into `code12.py`.
:::

## Keeping track of open cards
In the actual game, a player is allowed to flip only _two_ cards at a time. If they match, they are removed. If not, they are flipped to their backs again. This means we need to keep track of which and how many cards are face up. We can always figure this out by doing a list comprehension scanning for cards that have their `"side"` as `"face"`. But, mutable nature of dictionaries presents us with a simpler solution. We create a new list (let us call it `face_up`) and add cards to it. Mutable dictionary will not be copied but rather a reference to it will be present in both lists (same card dictionary will have two stickers on it, one from the `cards` list, one from `face_up` list). This way we know _which_ cards are face up (those that are in the list) and we know how many (length of the `face_up` list). 

However, you need to be careful not do add a card more than once (this will mess up our "how many cards are face up" number). There are several ways to do this. Assuming that `icard` is the index of the card, which you computed via `position_to_index()` from mouse position, you can simply check whether this card `"side"` is `"front"`. Alternatively, you can check whether this card is already [in](https://docs.python.org/3/reference/expressions.html?highlight=list%20dictionary#in) the `face_up` list. Either way will tell you whether the card is face up. If it is not, you should set its `"side"` to `"front"` and add it to `face_up` list. Finally, you can store the cards in a [set](https://docs.python.org/3/tutorial/datastructures.html#sets), which is an unordered collection that does not allow duplicate items. This means that you can add the card multiple times but it will appear only once in the set.

Implement this code, open a few cards. Then, use a breakpoint to pause the program and check that `face_up` list (or set) contains exactly these (this many) cards. If it has _more_ then your face-up checks do not work. Put a breakpoint on them and step through the code to see what happens.

::: {.rmdnote .program}
Put your code into `code13.py`.
:::

## Opening only two cards
Now we need to check whether a player opened exactly two cards. In your code, mouse checks should be _before_ the drawing code. This means that cards are drawn face up immediately after a click. Once they are drawn, check the length of `face_up`, if it equal to 2:

* pause the program for ~0.5 s^[Pick the timing you like!] via [wait](https://psychopy.org/api/clock.html#psychopy.clock.wait), so that the player can see both cards.
* flip both cards back (i.e., set their `"side"` to `"back"`).
* remove them from `face_up` list (see [.clear()](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) method).

::: {.rmdnote .program}
Put your code into `code14.py`.
:::

## Taking a matching pair off the table
Our code turns cards back even you found a matching pair but we need to take them off the table. Once you have two cards in the `face_up` list (if you have a set, you can convert it to the list via `list()`), you need to check whether they have the same chicken on them, i.e., their filenames are the same. If they are, you set `"show"` field to `False`. If not, you set their `"side"` to `"back"` (what your code is already doing). Either way, you still need to pause the program to allow the player to see them and to clear `face_up` list/set (they are either off the table or face down, definitely not face up).

We also need to modify our code to handle `"show"` field correctly. First, modify your drawing code to draw only the cards that should be shown. Second, when handling mouse click, you need to check both that the card is not face up and that it is shown (otherwise you can "open" invisible cards).

::: {.rmdnote .program}
Put your code into `code15.py`.
:::

## Game over once all the cards are off the table
When your code works correctly, you can take all the card off the table, so that only the gray screen remains. However, that should be the point when the game finishes and congratulates you on your success. Write a function `remaining_cards` that will take the list with cards (i.e., our `cards` list) and will return how many cards are still shown (their `"show"` field is `True`). You definitely need a [for](#for-loop) for this but implementation can be very different. You could use an extra counter variable that you initialize to 0 and then increment by one (see [+=](https://docs.python.org/3/reference/simple_stmts.html#augmented-assignment-statements) for a shortcut). Alternatively, you can use [list comprehensions](l#list-comprehension) to filter out all cards that are not shown and return the length of that list (a single line solution). Implement this function in _utilities.py_ and exit the loop by setting `game_state` to `"victory"`. After the loop, you can check the `game_state` variable and if the player was victorious, show a congratulatory message ([TextStim](https://psychopy.org/api/visual/textstim.html#psychopy.visual.TextStim), note that you don't even need to create a variable for it, you can create an object and call `.draw()` on it, i.e., `visual.TextStim(...).draw()`) and wait for a key press before you close the window.

::: {.rmdnote .program}
Put your code into `code16.py`.
:::

## Do it fast!
There are different ways on how you can quantify speed in this game. You could look at the number of pairs the player had to open until clearing them up (the fewer, the better). Or, you could measure how fast the player did it in seconds. Or use a combination of these two measures. Let us use the second option --- total time taken --- as an opportunity to learn about using PsychoPy [clocks](https://psychopy.org/api/clock.html).

The two classes you will be primarily interested in are [Clock](https://psychopy.org/api/clock.html#psychopy.clock.Clock) and [CountdownTimer](https://psychopy.org/api/clock.html#psychopy.clock.CountdownTimer). The only difference between the two is that [Clock](https://psychopy.org/api/clock.html#psychopy.clock.Clock) starts at (and [resets](https://psychopy.org/api/clock.html#psychopy.clock.Clock.reset) to) 0 and start counting _elapsed_ time, so its [getTime()](https://psychopy.org/api/clock.html#psychopy.clock.MonotonicClock.getTime) method will return only _positive_ values. In contrast, the [CountdownTimer](https://psychopy.org/api/clock.html#psychopy.clock.CountdownTimer) start with (and resets to) a value you initialized it with and starts counting _remaining_ time down. Importantly, it will not stop once it reaches 0, so you will eventually end up with _negative_ remaining time. Thus, for [Clock](https://psychopy.org/api/clock.html#psychopy.clock.Clock) you check whether the _elapsed_ time is longer than some predefined value, whereas for  [CountdownTimer](https://psychopy.org/api/clock.html#psychopy.clock.CountdownTimer) you start at a predefined value and check that the _remaining_ time is above zero. Note it is not guaranteed that the remaining time will be exactly zero. If anything, it is extremely unlikely that this will ever happen, so never test for an exact equality with zero^[More generally, never compare float values to exact numbers. They are [tricky](http://www.lahey.com/float.htm), as the underlying representation [does not guarantee](https://docs.python.org/3/tutorial/floatingpoint.html) that the computation will produce _exactly_ the number that it should: `.1 + .1 + .1 == .3` is surprisingly `False`, try it yourself]!

Here, we are interested in the _elapsed_ time, so [Clock](https://psychopy.org/api/clock.html#psychopy.clock.Clock) is the obvious choice. Create a clock before the game loop and use the elapsed time in the congratulatory message.

::: {.rmdnote .program}
Put your code into `code17.py`.
:::

## How can you improve it?
Excellent game but you can always improve it: highscore, multiple round, etc. The sky is the limit!
