"""
intermediate exercise
"""

from car import Car
from random import randint


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        rand = randint(0, 100)
        if self.reliability > rand:
            super().drive(distance)
        else:
            return 0


