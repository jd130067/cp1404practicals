"""CP1404/CP5632 Practical06 - Programming Languages Class."""
from docutils.parsers.rst.directives.misc import Class


class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}: Typing: {self.typing}, Reflection: {self.reflection}, Year: {self.year}"

    def is_dynamic(self):
        return self.typing == "Dynamic"
