
from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('44_login.kv')
    def logger(self):
        self.root.ids.welcome_label.text = f'Sub {self.root.ids.user.text} !'

    def clear(self):
        self.root.ids.welcome_label.text = "WELCOME"
        self.root.ids.user.text = ""
        self.root.ids.password.text = ""
    def look (self):
        self.root.ids.password.password = False
    def dlook (self):
        self.root.ids.password.password = True
MainApp().run()
