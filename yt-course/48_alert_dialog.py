#https://www.youtube.com/watch?v=tToJBfDgCsc&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=48

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton


class MainApp(MDApp):
    dialog = None


    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title = "Pretty Neat, Right?",
                text = "This is just a text",
                buttons = [
                    MDFlatButton(
                        text="Cancel",
                        text_color= self.theme_cls.primary_color,
                        on_release = self.close_dialog),
                    MDRectangleFlatButton(
                        text = "Yes It's Neat!",
                        text_color= self.theme_cls.primary_color,
                        on_release= self.neat_dialog)
                ]
            )
        self.dialog.open()

    #Click canel button
    def close_dialog(self, obj):
        self.dialog.dismiss()

    #Click neat button
    def neat_dialog(self, obj):
        self.dialog.dismiss()
        #Change label text
        self.root.ids.my_label.text = "Yes It's Neat"

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('48_alert_dialog.kv')



MainApp().run()
