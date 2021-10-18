# Currently unused bits

## Clock Module
The two classes you are primarily interested in are [Clock](https://psychopy.org/api/clock.html#psychopy.clock.Clock) and [CountdownTimer](https://psychopy.org/api/clock.html#psychopy.clock.CountdownTimer). The only difference between the two is that [Clock](https://psychopy.org/api/clock.html#psychopy.clock.Clock) starts at (and [resets](https://psychopy.org/api/clock.html#psychopy.clock.Clock.reset) to) 0 and start counting _elapsed_ time, so its [getTime()](https://psychopy.org/api/clock.html#psychopy.clock.MonotonicClock.getTime) method will return only _positive_ values. In contrast, the [CountdownTimer](https://psychopy.org/api/clock.html#psychopy.clock.CountdownTimer) start with (and resets to) a value you initialized it with and starts counting _remaining_ time down. Importantly, it will not stop once it reaches 0, so you will eventually end up with _negative_ remaning time. Thus, for [Clock](https://psychopy.org/api/clock.html#psychopy.clock.Clock) you check whether the _elapsed_ time is longer than some predefined value (blank and presentation durations that you generated), whereas for  [CountdownTimer](https://psychopy.org/api/clock.html#psychopy.clock.CountdownTimer) you start at these values and check that the _remaining_ time is above zero. Note it is not guaranteed that the remaining time will be exactly zero. If anything, it is extremely unlikely that this will ever happen, so never test for an exact equality with zero^[More generally, never compare float values to exact numbers. They are [tricky](http://www.lahey.com/float.htm), as the underlying representation [does not guarantee](https://docs.python.org/3/tutorial/floatingpoint.html) that the computation will produce _exactly_ the number that it should: `.1 + .1 + .1 == .3` is suprisingly `False`, try it yourself]!