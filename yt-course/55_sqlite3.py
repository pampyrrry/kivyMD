# https://www.youtube.com/watch?v=X2MkC1ru3cQ&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=55

from kivy.lang import Builder
from kivymd.app import MDApp
import sqlite3

class MainApp(MDApp):

    def build(self):

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        # Create Database Or Connect To One
        connect = sqlite3.connect('first_db.db')

        # Create A Coursor
        cursor = connect.cursor()

        # Create A Table
        cursor.execute("""CREATE TABLE if not exists customers (
        name text) """)

        # Commit our changes
        connect.commit()

        # Close our connection
        connect.close()

        return Builder.load_file('55_sqlite3.kv')

    def submit(self):
        # Create Database Or Connect To One
        connect = sqlite3.connect('first_db.db')

        # Create A Coursor
        cursor = connect.cursor()

        # Add a record
        cursor.execute("INSERT INTO customers VALUES (:first)",
                       {
                           'first': self.root.ids.word_input.text,
                       })
        # Add a little message
        self.root.ids.word_label.text = f"{self.root.ids.word_input.text} added"

        # Clear input box
        self.root.ids.word_input.text = ""

        # Commit our changes
        connect.commit()

        # Close our connection
        connect.close()

    def show_records(self):
        # Create Database Or Connect To One
        connect = sqlite3.connect('first_db.db')

        # Create A Coursor
        cursor = connect.cursor()

        # Grab records  from database
        cursor.execute("SELECT * FROM customers")
        records = cursor.fetchall()

        word = ""

        # Loop thru records
        for record in records:
            word = f"{word}\n{record[0]}"
            self.root.ids.word_label.text = f"{word}"
        # Commit our changes
        connect.commit()

        # Close our connection
        connect.close()

MainApp().run()
