# https://www.youtube.com/watch?v=f3FL_tfqhyg&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=60

#from kivy.lang import Builder
from kivymd.app import MDApp
from kivy_garden.mapview import MapView


class MainApp(MDApp):

    def build(self):
        mapview = MapView(zoom=10, lat=36, lon=-115 )
        return mapview


MainApp().run()
