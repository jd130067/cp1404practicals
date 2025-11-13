"""
CP1404 - Practical 08
Program to convert miles to kilometres using a KIVY based GUI.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

CONVERSION_FACTOR = 1.60934

class ConvertMilesKilometresApp(App):
    def build(self):
        Window.size = (600, 400)
        self.title = "Miles to Kilometres Converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self, miles):
        try:
            km = float(miles)*CONVERSION_FACTOR
            self.root.ids.output_label.text = str(km)
        except ValueError:
            self.root.ids.output_label.text = '0.0'

    def handle_incrementing(self, difference, miles):
        try:
            new_miles = float(miles) + difference
            self.root.ids.input_value.text = str(new_miles)
        except ValueError:
            self.root.ids.input_value.text = str(difference)


ConvertMilesKilometresApp().run()
