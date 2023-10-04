# Python basics {#python-basics}
Hopefully, you already [created a special folder](#files-folder) for this book. Download the [exercise notebook](notebooks/Basics.ipynb) (Alt+Click should download rather than open it), put it in a chapter's folder, and open it, see [relevant instructions](#jupyter-notebooks). You will need to switch between explanations here and the exercises in the notebook, so keep them both open.

## Chapter concepts

* [Variables](#variables).
* [Constants](#constants).
* Basic [value types](#value-types).
* [Printing](#print) things out.
* Putting values [into strings](#string-formatting).

## Variables {#variables}
The first fundamental concept that we need to be acquainted with is **variable**. Variables are used to store information and you can think of it as a box with a name tag, so that you can put something into it. The name tag on that box is the name of the variable and its value what you store in it. For example, we can create a variable that stores the number of legs that a game character has. We begin with a number typical for a human being.

<img src="images/variable-as-box.png" width="50%" style="display: block; margin: auto;" />

In Python, you would write

```python
number_of_legs = 2
```

The **assignment statement** above has very simple structure:

```python
<variable-name> = <value>
```
Variable name (name tag on the box) should be meaningful, it can start with letters or _ and can contain letters, numbers, and _ symbol but not spaces, tabs, special characters, etc. Python recommends^[Well, actually, [insists](https://www.python.org/dev/peps/pep-0008/).] that you use **snake_case** (all lower-case, underscore for spaces) to format your variable names. The `<value>` on the right side is a more complex story, as it can be hard-coded (as in example above), computed using other variables or the same variable, returned by a function, etc.

Using variables means that you can concentrate what corresponding values **mean** rather than worrying about what these values are. For example, the next time you need to compute something based on number of character's legs (e.g., how many pairs of shoes does a character need), you can compute it based on current value of `number_of_legs` variable rather than assume that it is `1`. 

```python
# BAD: why 1? Is it because the character has two legs or
# because we issue one pair of shoes per character irrespective of
# their actual number of legs?
pairs_of_shoes = 1

# BETTER (but what if our character has only one leg?)
pairs_of_shoes = number_of_legs / 2
```

Variables also give you flexibility. Their values can change during the program run: player's score is increasing, number of lives decreasing, number of spells it can cast grows or falls depending on their use, etc. Yet, you can always use the value in the variable to perform necessary computations. For example, here is a slightly extended `number_of_shoes` example.

```python
number_of_legs = 2

# ...
# something happens and our character is turned into an octopus
number_of_legs = 8
# ...

# the same code still works and we still can compute the correct number of pairs of shoes
pairs_of_shoes = number_of_legs / 2
```

As noted above, you can think about a variable as a labeled box you can store something in. That means that you can always "throw away" the old value and put something new. In case of variables, the "throwing away" part happens automatically, as a new value overwrites the old one. Check yourself, what will be final value of the variable in the code below?

```python
number_of_legs = 2
number_of_legs = 5
number_of_legs = 1
number_of_legs
```

::: {.rmdnote .practice}
Do exercise #1.
:::

Note that a variable ("a box with a name tag") exists only after you assign something to it. So, the following code will generate a `NameError`, a Python's way to tell that you it never heard of variable `number_of_hands`.

```python
number_of_legs = 2
number_of_gloves = number_of_hands / 2
```

However, you can create a variable the does not hold any _specific_ value by assigning `None` to it. `None` was added to the language specifically to mean _no value_ or _nothing_.

```python
number_of_hands = None # variable exists now, but holds no particular value.
```

As you have already seen, you can _compute_ a value instead of specifying it. What would be the answer here? 

```python
number_of_legs = 2 * 2
number_of_legs = 7 - 2
number_of_legs
```

::: {.rmdnote .practice}
Do exercise #2.
:::

## Assignments are not equations!

**Very important**: although assignments _look_ like mathematical equations, they are **not equations!** They follow a **very important** rule that you must keep in mind when understanding assignments: the right side of an expression is evaluated _first_ until the final value is computed, then and only then that final value is assigned to the variable specified on the left side (put into the box). What this means is that you can use the same variable on _both_ sides! Let's take a look at this code:

```python
x = 2
y = 5
x = x + y - 4
```

What happens when computer evaluates the last line? First, it takes _current_ values of all variables (`2` for `x` and `5` for `y`) and puts them into the expression. After that internal step, the expression looks like

```python
x = 2 + 5 - 4
```

Then, it computes the expression on the right side and, **once the computation is completed**, stores that new value in `x`

```python
x = 3
```

::: {.rmdnote .practice}
Do exercise #3 to make sure you understand this.
:::

## Constants {#constants}
Although the real power of variables is that you can change their value, you should use them even if the value remains constant throughout the program. There are no true constants in Python, rather an agreement that their names should be all `UPPER_CASE`. Accordingly, when you see `SUCH_A_VARIABLE` you know that you should not change its value. Technically, this is just a recommendation, as no one can stop you from modifying value of a `CONSTANT`. However, much of Python's ease-of-use comes from such agreements (such as a `snake_case` convention above). We will encounter more of such agreements later, for example, when learning about objects.

Taking all this into account, if number of legs stays constant throughout the game, you should highlight that constancy and write

```python
NUMBER_OF_LEGS = 2
```

I strongly recommend using constants and avoid hardcoding values. First, if you have several identical values that mean different things (2 legs, 2 eyes, 2 ears, 2 vehicles per character, etc.), seeing a `2` in the code will not tell you what does this `2` mean (the legs? the ears? the score multiplier?). You can, of course, figure it out based on the code that uses this number but you could spare yourself that extra effort and use a properly named constant instead. Then, you just read its name and the meaning of the value becomes apparent and it is the meaning not the actual value that you are mostly interested in. Second, if you decide to permanently _change_ that value (say, our main character is now a tripod), when using a constant means you have only one place to worry about, the rest of the code stays as is. If you hard-coded that number, you are in for an exciting^[not really] and definitely long search-and-replace throughout the entire code.

::: {.rmdnote .practice}
Do exercise #4.
:::

## Value types {#value-types}
So far, we only used integer numeric values (1, 2, 5, 1000...). Although, Python supports [many different value types](https://docs.python.org/3/library/stdtypes.html), at first we will concentrate on a small subset of them:

* integer numbers, we already used, e.g. `-1`, `100000`, `42`.
* float numbers that can take any real value, e.g. `42.0`, `3.14159265359`, `2.71828`.
* strings that can store text. The text is enclosed between either paired quotes `"some text"` or apostrophes `'some text'`. This means that you can use quotes or apostrophes inside the string, as long as its is enclosed by the alternative. E.g., `"students' homework"` (enclosed in `"`, apostrophe `'` inside) or `'"All generalizations are false, including this one." Mark Twain'` (quotation enclosed by apostrophes). There is much much more to strings and we will cover that material throughout the course.
* logical / Boolean values that are either `True` or `False`.

When using a variable it is important that you know what type of value it stores and this is mostly on you. In some cases, Python will raise an error, if you try doing a computation using incompatible value types. In other cases, Python will automatically convert values between certain types, e.g. any integer value is also a real value, so conversion from `1` to `1.0` is mostly trivial and automatic. However, in other cases you may need to use explicit conversion. Go to exercise #5 and try guessing which code will run and which will throw an error due to incompatible types? 

```python
5 + 2.0
'5' + 2
'5' + '2'
'5' + True
5 + True
```

::: {.rmdnote .practice}
Do exercise #5.
:::

Surprised by the last one? This is because internally, `True` is also `1` and `False` is `0`!

You can explicitly convert from one type to another using special functions. For example, to turn a number or a logical value into a string, you simply write [str(\<value\>)](https://docs.python.org/3/library/functions.html#func-str). In examples below, what would be the result?

```python
str(10 / 2)
str(2.5 + True)
str(True)
```

::: {.rmdnote .practice}
Do exercise #6.
:::

Similarly, you can convert to a logical/Boolean variable using [bool(\<value\>)](https://docs.python.org/3/library/functions.html#bool) function. The rules are simple, for numeric values `0` is `False`, any other non-zero value is converted to `True`. For string, an empty string `''` is evaluated to `False` and non-empty string is converted to `True`. What would be the output in the examples below?


```python
bool(-10)
bool(0.0)

secret_message = ''
bool(secret_message)

bool('False')
```

::: {.rmdnote .practice}
Do exercise #7.
:::

Converting to integer or float numbers using, respectively, [int(\<value\>)](https://docs.python.org/3/library/functions.html#int) and [float(\<value\>)](https://docs.python.org/3/library/functions.html#float) is trickier. The simplest case is from logical to integer/float, as `True` gives you `int(True)` is `1` and `float(True)` is `1.0` and `False` gives you `0`/`0.0`. When converting from float to integer, Python simply drops the fractional part (it does not do proper rounding!). When converting a string, it must be a valid number of the corresponding type or the error is generated. E.g., you can convert a string like `"123"` to an integer or a float but this won't work for `"a123"`. Moreover, you can convert `"123.4"` to floating-point number but not to an integer, as it has fractional part in it. Given all this, which cells would work and what output would they produce?


```python
float(False)
int(-3.3)
float("67.8")
int("123+3")
```

::: {.rmdnote .practice}
Do exercise #8.
:::

## Printing output{#print}
To print the value, you need to use [print()](https://docs.python.org/3/library/functions.html#print) function (we will talk about functions in general later). In the simplest case, you pass the value and it will be printed out.

```python
print(5)
#> 5
```

or 

```python
print("five")
#> five
```

Of course, you already know about the variables, so rather than putting a value directly, you can pass a variable instead and its _value_ will be printed out.

```python
number_of_pancakes = 10
print(number_of_pancakes)
#> 10
```

or

```python
breakfast = "pancakes"
print(breakfast)
#> pancakes
```

You can also pass more than one value/variable to the print function and all values will be printed one after another. For example, if we want to tell the user what did I had for breakfast, we can do

```python
breakfast = "pancakes"
number_of_items = 10
print(breakfast, number_of_items)
#> pancakes 10
```

What will be printed by the code below?

```python
dinner = "steak"
count = 4
desert = "cupcakes"

print(count, dinner, count, desert)
```

::: {.rmdnote .practice}
Do exercise #9.
:::

However, you probably would want to be more explicit, when you print out the information. For example, imagine you have these three variables:

```python
meal = "breakfast"
dish = "pancakes"
count = 10
```
You could, of course do `print(meal, dish, count)` but it would be nicer to print "_I had **10 pancakes** for **breakfast**_", where items in bold would be the inserted variables' values. For this, we need to use string formatting. Please note that the string formatting is not specific to printing, you can create a new string value via formatting and store it in a variable without printing it out or print it out without storing it.

## String formatting {#string-formatting}
A great resource on string formatting in Python is [pyformat.info](https://pyformat.info/). As Python constantly evolves, it now has more than one way to format strings. Below, I will introduce the "old" format that is based on classic string formatting used in `sprintf` function in C, Matlab, R, and many other programming languages. It is somewhat less flexible than newer ones but for simple tasks the difference is negligible. Knowing the old format is useful because of its generality. If you want to learn alternatives, read at the link above.

The general call is `"a string with formatting"%(tuple of values to be used during formatting)`. You will learn about tuples later. For now, assume that it is just a comma-separated list of values enclosed in round brackets: `(1, 2, 3)`.

In `"a string with formatting"`, you specify where you want to put the value via `%` symbol that is followed by an _optional_ formatting info and the _required_ symbol that defines the **type** of the value. The type symbols are

* `s` for string
* `d` for an integer
* `f` for a float value
* `g` for an "optimally" printed float value, so that scientific notation is used for large values (_e.g._, `10e5` instead of `100000`).

Here is an example of formatting a string using an integer:

```python
print("I had %d pancakes for breakfast"%(10))
#> I had 10 pancakes for breakfast
```

You are not limited to a single value that you can put into a string. You can specify more locations via `%` but you must make sure that you pass the right number of values in the right order. Before running it, can you figure out which call will actually work (and what will be the output) and which will produce an error?


```python
print('I had %d pancakes and either %d  or %d steaks for dinner'%(2))
print('I had %d pancakes and %d steaks for dinner'%(7, 10))
print('I had %d pancakes and %d steaks for dinner'%(1, 7, 10))
```

::: {.rmdnote .practice}
Do exercise #10.
:::

As noted above, in case of real values you have two options: `%f` and `%g`. The latter uses scientific notation (e.g. `1e10` for `10000000000`) to make a representation more compact.

::: {.rmdnote .practice}
Do exercise #11 to get a better feeling for the difference.
:::

These is much more to formatting and you can read about it at [pyformat.info](https://pyformat.info/). However, these basics are sufficient for us to start programming our first game in the next chapter.
