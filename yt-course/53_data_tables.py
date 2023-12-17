# https://www.youtube.com/watch?v=LmuhbQnSHLU&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=51
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp  # pixles
# Display pixels

class MainApp(MDApp):

    def build(self):
        # Define screen
        screen = Screen()
        # Define table
        table = MDDataTable(
            pos_hint = {"center_x": .5, "center_y": .5},
            size_hint = (0.9, 0.6),
            check = True,
            column_data = [
                ("First Name", dp(30)),
                ("Last Name", dp(30)),
                ("Email Adress", dp(30)),
                ("Phone Number", dp(30))
            ],
            row_data = [
                ("John", "Elder", "je@com.com","(123)321321"),
                ("Dan", "Miel", "dm@com.com","(123)321321"),
            ]
        )

        #Bind table
        table.bind(on_check_press=self.checked)
        table.bind(on_row_press=self.row_checked)

        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        #return Builder.load_file('53_data_tables.kv')
        # Add table widget to screen
        screen.add_widget(table)
        return screen
    #Function for Check presses
    def checked(self, instance_table, current_row):
        print(instance_table, current_row)
    # Function for row presses
    def row_checked (self, instance_table, instance_row):
        print(instance_table, instance_row)



MainApp().run()
