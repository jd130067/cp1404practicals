"""
CP1404 - Practical 09
Silver Service Taxi Class
>~< meow
"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Special Taxi with extra charges for fanciness."""

    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        return super().get_fare() + self.flagfall
