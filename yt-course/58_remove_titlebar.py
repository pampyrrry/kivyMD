# https://www.youtube.com/watch?v=zVMwbarvDu8&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=58
from kivy.config import Config
Config.set('graphics', 'position', 'custom')
Config.set('graphics', 'left', -100)
Config.set('graphics', 'top', 200)
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window


class MainApp(MDApp):

    def build(self):
        Window.borderless = True
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('58_remove_titlebar.kv')



MainApp().run()
