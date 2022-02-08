from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class ListOfNames(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.list_of_names = ("Luke Skywalker", "Darth Vader", "C3PO", "Han Solo", "R2D2", "Princess Leia")

    def build(self):
        self.title = "List of Names"
        self.root = Builder.load_file('List_of_Names.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.list_of_names:
            temp_label = Label(text=name, id=name)
            self.root.ids.entries_box.add_widget(temp_label)


ListOfNames().run()
