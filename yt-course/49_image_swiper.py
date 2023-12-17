#https://www.youtube.com/watch?v=gDLjaMF15mk&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=49
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton


class MainApp(MDApp):


    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('49_Image_swiper.kv')



MainApp().run()
