"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


# DONE: 1. write down what you think the output of this will be,
# DONE: 2. use the debugger to step through and see what's actually happening
print(do_it(5))
# think the output will be 3 since (5 mod 2 = 1, 4 mod 2 = 0, 3 mod 2 = 1, 2 mod 2 = 0, 1 mod 2 = 1)


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n > 0:
        print(n ** 2)
        do_something(n - 1)
    return 0


# DONE: 3. write down what you think the output of this will be,
# DONE: 4. use the debugger to step through and see what's actually happening
do_something(4)
# think the output will be:
# a lot of prints of negative numbers to the power of 2

# Done: 5. fix do_something() so that it works the way it probably should :)


def building_pyramid(n):
    print(pyramid(n))


def pyramid(n):
    if n > 0:
        return n + pyramid(n-1)
    return 0

building_pyramid(6)

