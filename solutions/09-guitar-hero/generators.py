"""
Generators for timed response task.

time_to_next_target_generator(time_range)
    Generate random time till next target.
next_target_generator(n)
    Generate next target, ensure equal occurence within n*3 trials.
"""

import random

def time_to_next_target_generator(time_range):
    """
    Generate random time till next target.

    Parameters
    ----------
    time_range : tuple
        Min and max time.

    Yields
    ----------
    float
    """
    while True:
        yield random.uniform(time_range[0], time_range[1])

def next_target_generator(n):
    """
    Generate next target, ensure equal occurence within n*3 trials.
    
    Parameters
    ----------
    n : int 
        Number of repetitions.

    Yields
    ----------
    int : in 0..2 range.        
    """
    targets_list = list(range(3)) * n
    
    while True:
        # next batch
        random.shuffle(targets_list)
        for target in targets_list:
            yield target
