
from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):

    data = {
        #    Text           Icon
        "Python": "language-python",
        "Ruby": "language-ruby",
        "JS": "language-javascript"
    }

    def callback(self, instance):
        self.root.ids.my_label.text = {instance.icon}

    def open(self):
        self.root.ids.my_label.text = "Open!"

    def close(self):
        self.root.ids.my_label.text = "Close!"

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('47_speed_dial_button.kv')



MainApp().run()
