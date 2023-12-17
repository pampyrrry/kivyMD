# https://www.youtube.com/watch?v=MpCUGq9aM5k&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=50&pp=iAQB


class MainApp(MDApp):

    def on_swipe_left(self):
        self.root.ids.toolbar.title = "You swipe left"
        #print("you swipe left")

    def on_swipe_right(self):
        self.root.ids.toolbar.title = "You swipe right"
        #print("you swipe right")

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('50_image_swiper_tips&tricks.kv')



MainApp().run()
