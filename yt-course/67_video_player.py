# https://www.youtube.com/watch?v=jGY7haFtIPY&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=67

# from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.videoplayer import VideoPlayer


class MainApp(MDApp):
    title = "Simple Video"

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        # Create video player instance
        player = VideoPlayer(source="video/1.mp4")

        # Assign Video Player State
        player.state = 'play'

        # set options
        player.options = {'eos': 'loop'}  # {} <- dictionary

        player.allow_stretch = True

        # Return player
        return player


MainApp().run()
