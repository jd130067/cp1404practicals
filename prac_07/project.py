"""
CP1404 - Practical 07
Class for project_management
"""

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"Project - {self.name} ({self.start_date}) is {self.completion_percentage}% done costs ~${self.cost_estimate:.2f} Priority: {self.priority}"

    def __lt__(self, object):
        return self.priority < object.priority

    def is_complete(self):
        return self.completion_percentage >= 100