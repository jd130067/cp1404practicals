"""
CP1404 Practical - 06
Guitar Class
Estimate Time: 1hr (including guitar test and 'playing the guitar')
"""


class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name}: year - {self.year}, cost - {self.cost}"

    def get_age(self):
        age = 2025 - self.year
        return age

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        return False
