# https://www.youtube.com/watch?v=LmuhbQnSHLU&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=51
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.pickers import MDDatePicker

class MainApp(MDApp):

    # Click ok
    def on_save(self, instance, value, date_range):
        #print(instance, value, date_range)
        #self.root.ids.date_label.text = f"You choose {value}"
        self.root.ids.date_label.text = str(date_range[0]) + " - " + str(date_range[-1])
    #Click cancel
    def on_cancel(self, instance, value):
        #print(instance, value)
        self.root.ids.date_label.text = "You clicked cancel"

    def show_data_picker(self):
        #date_dialog = MDDatePicker(year=2001, month=3, day=2)
        date_dialog = MDDatePicker(mode='range')
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('51_date_picker.kv')



MainApp().run()
