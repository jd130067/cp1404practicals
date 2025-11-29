"""
Unreliable car class
Inherits from Car class
"""

from car import Car
import random


class UnreliableCar(Car):
    """Special version of car that sometimes doesn't drive."""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        distance_driven = 0
        if random.random()*100 < self.reliability:
            distance_driven = super().drive(distance)
        return distance_driven
