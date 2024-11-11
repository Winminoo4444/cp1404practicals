from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Kivy App class for dynamic labels"""

    def __init__(self, **kwargs):
        """Constructing main app with names"""
        super().__init__(**kwargs)
        self.name_list = ["Doggo Brownie", "Ivy Leaf", "Yummy Snacks"]

    def build(self):
        """Function for building the Kivy GUI"""
        self.title = "Dynamic label"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Function for listing the names into app"""
        for name in self.name_list:
            temp_button = Label(text=name)
            self.root.ids.label_box.add_widget(temp_button)


DynamicLabelsApp().run()
