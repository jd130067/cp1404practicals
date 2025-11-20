"""
CP1404 - Practical 08
Program to dynamically create labels based on a string.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
import random


class DynamicLabels(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ['oliver', 'bob', 'dylan', 'james', 'peach', 'mario', 'bowser']

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Creates a label with a random colour and based on the list of names."""
        for name in self.names:
            temp_label = Label(text=name)
            temp_label.color = (random.random(),random.random(),random.random(),1)
            self.root.ids.label_list.add_widget(temp_label)


DynamicLabels().run()

