"""
Kivy example for CP1404/CP5632, IT@JCU
Dynamically create buttons based on content of dictionary
Lindsay Ward
Modified from popup_demo, 11/07/2016
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class DynamicWidgetsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """
        Construct main app.
        """
        super().__init__(**kwargs)
        # basic data example - dictionary of names: phone numbers
        # TODO: After running it, add another entry to the dictionary and see how the layout changes
        self.phonebook = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}

    def build(self):
        """
        Build the Kivy GUI.
        :return: reference to the root Kivy widget
        """
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_widgets.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """
        Create buttons from dictionary entries and add them to the GUI
        :return: None
        """
        for name in self.phonebook:
            # create a button for each phonebook entry, specifying the text and id
            # (although text and id are the same in this case, you should see how this works)
            temp_button = Button(text=name) #with button(text=name, id=name) program doesn't run
            temp_button.bind(on_release=self.press_entry)
            # add the button to the "entries_box" using add_widget()
            self.root.ids.entries_box.add_widget(temp_button)

    def press_entry(self, instance):
        """
        Handle pressing entry buttons.
        :param instance: the Kivy button instance
        :return: None
        """
        # get name (dictionary key) from the id of Button we clicked on
        name = instance.text  # or name = instance.text (var oprindeligt name = instance.id)
        # update status text
        self.status_text = "{}'s number is {}".format(name, self.phonebook[name])

    def clear_all(self):
        """
        Clear all of the widgets that are children of the "entries_box" layout widget
        :return:
        """
        self.root.ids.entries_box.clear_widgets()


DynamicWidgetsApp().run()
