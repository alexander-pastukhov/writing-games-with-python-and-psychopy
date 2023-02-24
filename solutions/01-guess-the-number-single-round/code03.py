"""One-armed bandit.
A single round edition.
"""

import random

# generate three random numbers, one per slot
slot1 = random.randint(1, 5)
slot2 = random.randint(1, 5)
slot3 = random.randint(1, 5)

print("%d - %d - %d"%(slot1, slot2, slot3))

if slot1 == slot2 == slot3:
    print("Three of a kind!")
elif slot1 == slot2 or slot1 == slot3 or slot2 == slot3:
    print("Pair!")
