# https://www.youtube.com/watch?v=CJ18PcYFozA&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=66

from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    title = "Simple List"
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('66_lists.kv')

    def presser(self, pressed, list_id):
        pressed.text = f"You pressed {list_id}"
        pressed.secondary_text = f"You pressed scondary {list_id}"
        pressed.tertiary_text = f"You pressed tertiary {list_id}"
MainApp().run()
