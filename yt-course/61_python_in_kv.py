# https://www.youtube.com/watch?v=83C4tl8scoY&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=59
from kivy.lang import Builder
from kivymd.app import MDApp

 

class MainApp(MDApp):
    some_text= "hello"
    our_list = ["John", "teddy", "Tina"]
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        
        return Builder.load_file('61_python_in_kv.kv')


MainApp().run()
