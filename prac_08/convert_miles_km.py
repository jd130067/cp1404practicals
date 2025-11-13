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

    def handle_conversion(self, miles):
        try:
            km = float(miles)*1.60934
            self.root.ids.output_label.text = str(km)
        except ValueError:
            pass

    def handle_incrementing(self, miles, difference):
        new_miles = float(miles) + difference
        self.root.ids.input_value.text = str(new_miles)



ConvertMilesKilometresApp().run()
