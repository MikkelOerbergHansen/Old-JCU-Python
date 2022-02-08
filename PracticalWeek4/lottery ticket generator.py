"""
“Quick Pick” Lottery Ticket Generator
Write a program that asks the user how many “quick picks” they wish to generate.
The program then generates that many lines of output.
Each line consists of 6 random numbers between 1 and 45.
These values should be stored as CONSTANTS.
Each line should not contain any repeated number.
Make sure your numbers are unique.
Each line of numbers should be displayed in sorted (ascending) order.
Note: Python's random function has a sample method, which returns a selection from a list.
This is a nice way to solve this problem... but it's too easy :)
Do not use it for this program.
"""

import random


quick_picks = int(input("how many quick picks would you like: "))

for y in range(1, quick_picks+1):
    quick_pick = []
    for x in range(1, 6+1):
        quick_pick.append(random.randrange(1, 45+1, 1))
    while len(quick_pick) > len(set(quick_pick)):
        quick_pick = []
        for z in range(1, 6 + 1):
            quick_pick.append(random.randrange(1, 45 + 1, 1))

    quick_pick = sorted(quick_pick, key=int)
    print(" {:2d} {:2d} {:2d} {:2d} {:2d} {:2d}".format(quick_pick[0], quick_pick[1], quick_pick[2], quick_pick[3],
                                                        quick_pick[4], quick_pick[5]))
