"""
Band class for 'my_band'
"""
from prac_09.musician import Musician


class Band:
    """Band Class"""
    def __init__(self, name=''):
        """Setup Band Class"""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Print band name and musician details (reference Musician class for musician object str)"""
        return f"{self.name} {self.musicians}"

    def add(self, musician):
        """Append a musician to musicians list."""
        self.musicians.append(musician)

    def play(self):
        for musician in self.musicians:
            print(musician)
