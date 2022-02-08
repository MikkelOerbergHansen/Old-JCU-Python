"""
practical 07 - do from scratch exercise
"""

from Guitars import Guitar


def guitar_test(guitar, expected):
    got = [guitar.get_age(), guitar.is_vintage()]

    print("{} get_age() - expected {}. got {}".format(guitar.name, expected[0], got[0]))
    print("{} is_vintage() - expected {}. got {}".format(guitar.name, expected[1], got[1]))


first_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar_test(first_guitar, [95, "True"])

another_guitar = Guitar("Another Guitar", 2012, 999.99)
guitar_test(another_guitar, [5, "False"])
