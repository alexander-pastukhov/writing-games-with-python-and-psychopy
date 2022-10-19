# Guess the Number: a multi round edition {#guess-the-number-multi-round}

In previous chapter, you programmed a single-attempt-only "Guess the Number" game. Now, we will expand to allow multiple attempts and will add other bells-and-whistles to make it more fun. Create a new subfolder and download the [exercise notebook](notebooks/Guess the number - multi round.ipynb) before we start!

## Chapter concepts

* Repeating code using [while](#while-loop) loop.
* Making in [emergency exit](#break) from a loop.

## While loop {#while-loop}
If you want to repeat something, you need to use loops. There are two types of loops: [while](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement) loop, which is repeated _while_ a condition is true, and [for](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement) loop that iterates over items (we will use it later).

The basic structure of a _while_ loop is

```python
# statements before the loop

while <condition>:
    # statements inside are executed
    # repeatedly for as long as
    # the condition is True
    
# statements after the loop
```

The `<condition>` here is any expression that is evaluated to be either `True` or `False`, just like in an `if...elif...else` [conditional statement](#comparisons). Also, the same [indentations rules](#indentation) determine which code is inside the loop and which outside.

::: {.rmdnote .practice}
Do exercise #1.
:::

Let us use _while_ loop to allow the player to keep guessing until they finally get it right. You can copy-paste the code you programmed during the last seminar or could redo it from scratch (I would strongly recommend you doing the latter!). The overall program structure should be the following

```python
# import random library so you can use randint function

# generated a random number and store in number_picked variable
# get player input, convert it to an integer, and store in guess variable

# while players guess is not equal to the value the computer picked:
    # print out "my number is smaller" or "my number is larger" using if-else statement
    # get player input, convert it to an integer, and store in guess variable
    
# print "Spot on!" 
# (because if we got here that means guess is equal to the computer's pick)
```

::: {.rmdnote .program}
Put your code into `code01.py`.
:::

Do not forget to document the file and use breakpoints and step overs to explore the program flow.

## Counting attempts
Now let us add a variable that will count a total number of attempts by the player. For this, create a new variable (call it `attempts` or something similar) _before the loop_ and initialize it `1`. Add `1` to it every time the player enters a guess. After the loop, expand the `"Spot on!"` message by adding information about the number of attempts. Use [string formatting](##string-formatting) to make things look nice, e.g., `"Spot on, and you needed just 5 attempts!"`. Check that the number of attempts your required _matches_ the number of attempts reported by the program!

::: {.rmdnote .program}
Put your code into `code02.py`.
:::

## Breaking (and exiting){#break}
Code inside the _while_ loop is executed repeatedly while the condition is `True` and, importantly, all of code the inside is executed before the condition is evaluated again. However, sometimes you may need to abort sooner without executing the remaining code. For this, Python  has a [break](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops) statement that causes the program to exit the loop immediately without executing the rest of the code inside the loop, so that the program continues with the code _after_ the loop.


```python
# this code runs before the loop

while <somecondition>:
  # this code runs on every iteration
  
    if <someothercondition>:
        break
  
  # this code runs on every iteration but not when you break out of the loop

# this code runs after the loop
```


::: {.rmdnote .practice}
Do exercise #2 to build your intuition.
:::

## Limiting number of attempts via break
Let's put the player under some pressure! Decide on maximal number of attempts you allow and stores it as a [CONSTANT](#constants). Pick an appropriate name (e.g. `MAX_ATTEMPTS`) and REMEMBER, ALL CAPITAL LETTERS for a constant name! Now, use `break` to quit the `while` loop, if the current attempt number is greater than `MAX_ATTEMPTS`. Think about when (within the code inside the loop) you should check this.

::: {.rmdnote .program}
Put your code into `code03.py`.
:::

## Correct end-of-game message
Let us update the final message. Currently it says "Spot on..." because we assumed that program exited the loop only if the player gave a correct answer. With limited attempts that is not necessarily the case. Now there are two reasons why it exited the while loop:

1. The player answered correctly
2. The player ran out of attempts.

Use `if-else` conditional statement to print out an appropriate message. E.g., print `"Better luck next time!`, if the player lost (ran out of attempts).

::: {.rmdnote .program}
Put your code into `code04.py`.
:::

## Limiting number of attempts without a break
Although it was my idea to add the `break` statement, you should use it sparingly. Without `break` there is a _single_ place in the code that you need to check to understand when the program will exit the loop: the condition. However, if you add a `break`, you now have _two_ places that need to be examined. And every additional `break` keeps adding to that. This does not mean that you should avoid them at all costs! You _should_ use them, if this makes the code easier to understand. But always check if a modified condition could also do the trick.

Let us try exactly that. Modify your code to work _without_ the `break` statement. You need a more complicated condition for your while loop. so that it repeats while player's guess is incorrect and the number of attempts is still less than the maximally allowed. Test that your code works both when you win and when you lose. 

::: {.rmdnote .program}
Put your code into `code05.py`.
:::

## Show remaining attempts
It is all about a user interface! Modify the `input` prompt message to include a number of _remaining_ attempts. E.g. `"Please enter the guess, you have X attempts remaining"`.

::: {.rmdnote .program}
Put your code into `code06.py`.
:::

## Repeating the game {#guess-the-number-repeat-game}
Let us give an option for the player to play again. This means putting _all_ the current code inside of another `while` loop (this is called _nested loops_) that is repeated for as long as the player wants to keep playing. The code should look following:

```python
# import random library so you can use randint function

# define MAX_ATTEMPTS

# define a variable called "want_to_play" and set to True
# while the player still wants to play
  
  # your current working game code goes here
  
  # ask user whether via input function. E.g. "Want to play again? Y/N"
  # want_to_play should be True if user input is equal to "Y" or "y"
  
# very final message, e.g. "Thank you for playing the game!"
```

**Pay extra attention to indentations to group the code properly!**

::: {.rmdnote .program}
Put your code into `code07.py`.
:::

## You do not need a comparison, if you already have the value
In your updated code, you have `want_to_play` variable that is either `True` or `False`. It is used in the loop that repeats while its value is `True`. Sometimes, people write `want_to_play == True` to express that. While it is technically correct and will certaintly work correctly, it is also redundant. Since `want_to_play` can only be `True` or `False` this comparison turns into `True == True` (which is of course `True`) or `False == True` (which is `False`). So comparing either value to `True` produces exactly the same value. Thus, you can just write `while want_to_play:` and use the logical value directly. 

## Best score
A "proper" game typically keeps the track of players' performance. Let us record a fewest number of attempts that the player needed to guess the number. For this, create a new variable `fewest_attempts` and set it to `MAX_ATTEMPTS` (this is as bad as the player can be). Think, where do you need to create it. You should update it after each game round. Add the information about "Best so far" into the round-over message.

::: {.rmdnote .program}
Put your code into `code08.py`.
:::

## Counting game rounds
Let us count how many rounds the player played. The idea and implementation is the same as with counting the attempts. Create a new variable, initialize it to 0, increment by 1 whenever a new round starts. Include the total number of rounds into the very final message, e.g. "Thank you for playing the game _X_ times!"

::: {.rmdnote .program}
Put your code into `code09.py`.
:::

## Wrap up
Most excellent, you now have a proper working computer game with game rounds, limited attempts, best score, and what not! Zip the folder and submit.
