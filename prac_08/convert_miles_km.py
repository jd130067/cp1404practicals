"""
CP1404 - Practical 08
Program to convert miles to kilometres using a KIVY based GUI.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMilesKilometresApp(App):
    def build(self):
        Window.size = (600, 400)
        self.title = "Miles to Kilometres Converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


ConvertMilesKilometresApp().run()
