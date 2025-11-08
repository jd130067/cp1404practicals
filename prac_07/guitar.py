"""
CP1404 Practical - 07
Guitar Class
"""


class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name}: year - {self.year}, cost - {self.cost}"

    def __lt__(self, object):
        return self.year < object.year

    def get_age(self):
        age = 2025 - self.year
        return age

    def is_vintage(self):
        return self.get_age() >= 50
