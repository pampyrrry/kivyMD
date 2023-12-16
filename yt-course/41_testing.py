from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivy.uix.slider import Slider
# Designate our *.kv design file
Builder.load_file('41_testing.kv') #split

class MyLayout(Widget):
    pass

class AwsomeApp(MDApp):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    AwsomeApp().run()
