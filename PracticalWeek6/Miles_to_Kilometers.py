"""
convert miles to kilometers
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class MilesToKilometers(App):

    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('Miles_to_Kilometers.kv')
        Window.size = (400, 200)
        return self.root

    def calculation(self):
        value = self.error_check_input()
        result = value * 1.60934
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, increment):
        value = self.error_check_input() + increment
        self.root.ids.input_number.text = str(value)
        self.calculation()

    def error_check_input(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


MilesToKilometers().run()
