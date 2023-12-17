# https://www.youtube.com/watch?v=LmuhbQnSHLU&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=51
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.pickers import MDTimePicker

class MainApp(MDApp):


    def on_cancel(self, instance, time):
        self.root.ids.time_label.text = "Cancel"

    def get_time(self, instance, time):
        self.root.ids.time_label.text = f"You set {time}"

    def show_time_picker(self):
        from datetime import  datetime

        # Define default time
        default_time = datetime.strptime("4:20:00", '%H:%M:%S').time()
        time_dialog = MDTimePicker()
        # Set default time
        time_dialog.set_time(default_time)
        time_dialog.bind(on_cancel=self.on_cancel, time=self.get_time)
        time_dialog.open()

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('52_time_picker.kv')



MainApp().run()
